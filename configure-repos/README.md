
# Configure Repos


This python script is used to setup a classroom GitHub environment with individual student repos and team repos for group work.

## Configuration: 

1.  In */course-specifics* add a folder with your course number e.g. CS5600 
2.  In the new newly created folder create two files: 
    **directorystructure-team.txt** and **directorystructure-individual.txt**
   
    These files will define the directory structure you want each repo to have. One directory name per line. Such as: 
```   
Written Work
Project src
Final Submission
Grades
```

3.  In the same folder create a CSV file with two columns, the first being CCIS_ID and the second being Team assignment 

| CCIS_ID  | TEAM |
| ------------- | ------------- |
| tim  | Fall18-101  |
| alex  | Fall18-102  |
| matt  | Fall18-101  |
| mike  | Fall18-103  |
| jack  | Fall18-101  |
| tom  | Fall18-102  |


4. Edit *config.py* to match the parameters of your github course:

```githuburl = 'github.ccs.neu.edu'
githuborg = 'CS5500'```
5. Execute the python script with:

```python setup-repos.py```

You will be asked to provide username and password of your GitHub account and the course you want to work with (must match the config.py githuborg).
