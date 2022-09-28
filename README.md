To run the program: 
python3 index.py

Conditions: 
- You need to have a file called people.csv in the same level as index.py with the data

Usage: 
There are three flags that can be used:
MINIMIZE_OVERLAP:
    - Possible values: True, False

MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP:
    - Possible values: 'minimize', 'maximize', ''

MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP:
    - Possible values: 'minimize', 'maximize', ''

You can alternate using any flag and it will work.
As a result you will get a csv file called groups.csv with the assign groups for the sessions

Also, you will get the different types of overlaps.
Overlaps between sessions - How many people overlap between sessions
Department overlaps session 1: People with overlapping department within a group in session 1
Department overlaps session 2: People with overlapping department within a group in session 2
Level overlaps session 1: People with overlapping level within a group in session 1
Level overlaps session 2: People with overlapping level within a group in session 2

ALGORITHM EXPLANATION:
Basically, you have a loop that iterates through every employee, checks some conditions 
and assigns him/her to a group.

We do this 2 times, each for each session. 

Within each loop, the algorithm will check first if the MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP is 
for minimizing or maximizing, will do corresponding condition matching and after that it will check for
the other flag. So you can say that the algorithm has a priority over the first one. 

There are a lot of cases you can run here: 
All the combinations between:
True or false
'' , 'minimize', 'maximize'
'' , 'minimize', 'maximize'

So the algorithm goes through each one of those to deliver the best optimized possible option
