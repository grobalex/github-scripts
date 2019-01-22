from editrepos import *
import os
import requests
import pprint
import getpass
import json
import cmd
import csv


class main(cmd.Cmd):
    prompt = 'What would you like to: clone, pull or push?'

    def do_clone(self, arg):
        """Clone a GitHub Repository"""
        checkLocalGitLocation()
        teamorindividual = input("Is this a team or individual (t or i):")
        if teamorindividual == 'i':
            for student in returnAllStudents():
                os.system("cd %s && git clone https://github.ccs.neu.edu/%s" %
                          (localgitlocation, 'cs5500/' + student))
        else:
            for team in returnAllTeams():
                os.system("cd %s && git clone https://github.ccs.neu.edu/%s/%s" %
                          (localgitlocation, githuborg, team))

    def do_pull(self, arg):
        """Pull the latest changes from a GitHub Repository"""
        checkLocalGitLocation()
        teamorindividual = input("Is this a team or individual (t or i):")
        if teamorindividual == 'i':
            for student in returnAllStudents():
                os.system("cd %s && git pull https://github.ccs.neu.edu/%s && cd .." %
                          (localgitlocation,  'cs5500/' + student))
        else:
            for team in returnAllTeams():
                os.system("cd %s && git pull https://github.ccs.neu.edu/%s/%s && cd .." %
                          (localgitlocation + '/' + team, githuborg, team))

    def do_push(self, arg):
        """Push the latest changes to a GitHub Repository"""
        checkLocalGitLocation()
        teamorindividual = input("Is this a team or individual (t or i):")
        commitmessage = input("Commit Message:")
        if teamorindividual == 'i':
            for student in returnAllStudents():
                os.system("cd %s && git add . && git commit -m ""%s"" && git push && cd .." %
                          (localgitlocation + '/' + student, commitmessage))
        else:
            for team in returnAllTeams():
                os.system("cd %s && git add . && git commit -m ""%s"" && git push && cd .." %
                          (localgitlocation + '/' + team, commitmessage))

    def do_quit(self, args):
        """Quits the Program"""
        print("Quitting")
        raise SystemExit

main().cmdloop()
