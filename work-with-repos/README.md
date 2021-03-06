
# Working with Repos

This python script is used to clone, push and pull individual student repos and team repos.

## Configuration: 

1.  In */course-specifics* add a folder with your course number e.g. CS5600 
2.  In the folder from step 1 create a CSV file with two columns, the first being student Individual Number and the second being Team assignment 
3. Edit *config.py* to match the parameters of your github course:

```
githuburl = 'github.ccs.neu.edu'
githuborg = 'CS5500'
localgitlocation = 'repos'
```
4. Execute the python script with:

```python maineditrepo.py```

You will be promted to enter one of the follow four (4) options:
   1. Clone
   2. Pull
   3. Push
   4. Quit 
   
  *Pull and Push will also ask if this is a team or individual request which will allow the script to pull the correct information from the csv file* 

## Extras: 

move_files.sh is a small bash script that moves [name].pdf into their respective folder matching the pdf [name]. 

1. Copy the pdf's and move_file.sh into the the /repo directory
2. Run move_file.sh
3. Any files it cannot find a match will not be moved
