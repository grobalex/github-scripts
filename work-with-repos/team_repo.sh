#!/bin/bash

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

function clone {

if [ -d "$SCRIPTPATH/repos" ] 
then
    cd "$SCRIPTPATH/repos"
else
    mkdir "$SCRIPTPATH/repos"
fi

cd "$SCRIPTPATH/repos"

file="$SCRIPTPATH/teams.txt"
while IFS='' read -r line || [[ -n "$line" ]]; do
    git clone "https://github.ccs.neu.edu/cs4500/$line"
done < "$file"
}

function pull {
while [[ -z "$message" ]]; do
  read -p "Enter Branch name " message
done

echo $PWD
echo $SCRIPTPATH

file="$SCRIPTPATH/teams.txt"

cd "$SCRIPTPATH/repos/"

while IFS='' read -r line || [[ -n "$line" ]]; do 
cd "$SCRIPTPATH/repos/$line" && git pull && git checkout -b "$message" && cd ..
done < "$file"

}

function push {
while [[ -z "$message" ]]; do
  read -p "Enter Commit message " message
done


file="$SCRIPTPATH/teams.txt"


while IFS='' read -r line || [[ -n "$line" ]]; do 
cd "$SCRIPTPATH/repos/$line" && echo $PWD && git checkout "$message" &&  git add . && git commit -m "$message" && git push --set-upstream origin "$message" && cd ..
done < "$file"
}

PS3='Choose an option: '
options=("Initial Cloning of your students repos" "pull the latest changes" "update and commit your comments to all repos" "exit")
select opt in "${options[@]}"
do
     case $opt in
             "Initial Cloning of your students repos")
                       clone 
                               ;;
                               
             "pull the latest changes")
                       pull 
                               ;;
                               
             "update and commit your comments to all repos")
                       push 
                               ;; 
             "exit")
                       exit 
                               ;;  
                               *) echo invalid option;;                    
    esac
	REPLY=
done

