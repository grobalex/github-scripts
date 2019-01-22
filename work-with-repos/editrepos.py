from config import *
import os
import requests
import pprint
import getpass
import json
import cmd
import csv

studentteamassignments = []
dir_path = os.path.dirname(os.path.realpath(__file__))


def readinCSV():
    global studentteamassignments
    with open(dir_path + '/course-specifics/' + githuborg + '/student-team.csv') as f:
        reader = csv.reader(f)
        next(reader)
        studentteamassignments = [r for r in reader]


def checkGlobalVar():
    if not studentteamassignments:
        readinCSV()


def returnAllStudents():
    checkGlobalVar()
    temp = []
    for student in studentteamassignments:
        temp.append('Student-' + student[0] + '-F19')
    return temp


def returnAllTeams():
    checkGlobalVar()
    tempset = set()
    for teams in studentteamassignments:
        tempset.add(teams[0])
    return(tempset)


def checkLocalGitLocation():
    print(dir_path)
    os.system("mkdir %s/repos" % (dir_path))
