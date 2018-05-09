from config import *
import os
import requests
import pprint
import getpass
import json
import cmd
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
directorystructureteam = []
directorystructureindividual = []
studentteamassignments = []

user = input("Username:")
passwd = getpass.getpass("Password for " + user + ":")
pp = pprint.PrettyPrinter(indent=4)

# Checks the syntax of the config file
def checkconfig():
	for course in os.listdir(dir_path + '/course-specifics'):
		if course.startswith( 'CS' ) and course == githuborg:
			return(print('Config file syntax OK'))
			break	
	raise NameError('You did not add any course required setup files to the folder: course-specifics for ' + githuborg + ' entered in the config file')		

# 
def readindirconfig():
	global directorystructureteam
	global directorystructureindividual 
	with open(dir_path + '/course-specifics/' + githuborg + '/directorystructure-team.txt') as f:
		directorystructureteam = [r.rstrip('\n') for r in f]
	with open(dir_path + '/course-specifics/' + githuborg + '/directorystructure-individual.txt') as f:
		directorystructureindividual = [r.rstrip('\n') for r in f]

#read in the CSV file
def readinCSV():
	global studentteamassignments
	with open(dir_path + '/course-specifics/' + githuborg + '/student-team.csv') as f:
		reader = csv.reader(f)
		next(reader)
		studentteamassignments = [r for r in reader]
	
# create the repo directory structure as outline in the config files	
def createRepoStructure( repo_name, flag):
	if not directorystructureteam or directorystructureindividual:
		readindirconfig()
	if flag == 'team':	
		createRepoStructureHelper(repo_name, directorystructureteam)	
	else:
		createRepoStructureHelper(repo_name, directorystructureindividual)	
		
def createRepoStructureHelper(repo_name, listofdir):
	for dirs in listofdir:
		data = json.loads('{"message": "'+ dirs +'", "content": "dGVzdA=="}')	
		response = requests.put('https://%s/api/v3/repos/%s/contents/%s/test.txt' % (githuburl, githuborg+'/'+repo_name, dirs), auth=(user, passwd), headers={'Content-Length': '0'}, json = data)		
	try:
		response.raise_for_status()
		print('Created repo dir structure successfully')
	except requests.exceptions.HTTPError as e:
		print ("Error: " + str(e))
	
	
# creates a student repo on student-team.csv
def createstudentrepos(student, description):
	data =  json.loads('{"name": "' + student + '", "description": "' + description +'" ,"auto_init": true,"private": true}')
	sendResponse(requests.post('https://%s/api/v3/orgs/%s/repos' % (githuburl, githuborg), json = data, auth=(user, passwd)))
	createRepoStructure(student, 'INV')
	
# creates a team repo based on student-team.csv
def createteamrepos(repo_name, list_of_collaborator_ccis_id):
	data = json.loads('{"name": "'+ repo_name +'", "description": "team repo for ' + repo_name + '","auto_init": true,"private": true}')
	sendResponse(requests.post('https://%s/api/v3/orgs/%s/repos' % (githuburl, githuborg), json = data, auth=(user, passwd)))
	for ccis_id in list_of_collaborator_ccis_id:
		addstudenttorepo(repo_name, ccis_id)
	createRepoStructure(repo_name, 'team')

def addstudenttorepo(repo_name, collaborator_ccis_id):
	data = json.loads('{}')
	response = requests.put('https://%s/api/v3/repos/%s/collaborators/%s' % (githuburl, githuborg+'/'+repo_name, collaborator_ccis_id), auth=(user, passwd), headers={'Content-Length': '0'}, json = data)
	try:
		response.raise_for_status()
		print('Collaborator added successfully')	
	except requests.exceptions.HTTPError as e:
		print ("Error: " + str(e))
	
def sendResponse(request):
	response = request
	try:
		response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		print ("Error: " + str(e))
	json_obj = response.json()
	print(json_obj)
	
def teamassignments(studentteamassignments):
	tempset = set()
	temp = []
	for teams in studentteamassignments:
		tempset.add(teams[1])
		
	for data in tempset:
		temp.append([data])
				
	for index, teams in enumerate(temp):
		for students in studentteamassignments:
			if students[1] == teams[0]:
				temp[index].append(students[0])
				
	return temp

def createAllIndivudalRepos():
	for student in studentteamassignments:
		createstudentrepos(student[0], 'HW repo for:' + student[0])
		addstudenttorepo(student[0], student[0])

def createAllTeamRepos():
	for team in teamassignments(studentteamassignments):
		temp = []
		for index, teams in enumerate(team):
			if index != 0:
				temp.append(team[index])
		createteamrepos(team[0],temp)		

def mainMethod():
	checkconfig()
	readindirconfig()
	readinCSV()
	createAllIndivudalRepos()
	createAllTeamRepos()

mainMethod()