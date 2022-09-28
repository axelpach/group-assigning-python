import csv
from random import *

#Flags
#To set them write the word minimize or maximize, any other word will be neutral
MINIMIZE_OVERLAP = True
MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP = 'minimize'
MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP = 'minimize'
ITERATIONS = 100

departments = []
levels = []


#We define four functions that we're going to be using throughout the alghoritms
def find_partners(list_to_check, item_to_find, i):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    indices.remove(i)
    return indices

def find_members(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(idx)
    return indices

def find_department_of_members(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(departments[idx])
    return indices

def find_levels_of_members(list_to_check, item_to_find):
    indices = []
    for idx, value in enumerate(list_to_check):
        if value == item_to_find:
            indices.append(levels[idx])
    return indices


#Here we fill two arrays with its values, departments and levels
with open('./people.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        departments.append(row[4])
        levels.append(row[5])
departments.remove('department')
levels.remove('level')


with open('./people.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #The following line counts the number of rows in the csv file
    row_count = sum(1 for row in csv_reader) - 1
    session_1 = []
    session_2 = []    

    #We then get the number of groups we're gonna have
    if row_count % 4 > 0:
        n_groups = int(row_count/4) + 1
    else:
        n_groups = int(row_count/4)


    #We'll start doing a cycle assigning a random group to the employee, 
    # and we'll be checking some conditions are met for optimization
    n_attempts = 0
    for i in range(row_count):
        #Cycle to assign a group to each employee
        while True:
            n_to_append = randint(1,n_groups)            
            #First we make groups of 3 and after they're full we start making groups of 4
            if i < n_groups * 3:
                if session_1.count(n_to_append) < 3:
                    if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'maximize':
                        department_of_members = find_department_of_members(session_1, n_to_append)
                        level_of_members = find_levels_of_members(session_1, n_to_append)
                        n_attempts+=1
                        if len(department_of_members) == 0 or department_of_members.count(departments[i]) > 0 or n_attempts > ITERATIONS:
                            if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            else:
                                session_1.append(n_to_append)
                                n_attempts = 0
                                break
                    elif MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'minimize':
                        department_of_members = find_department_of_members(session_1, n_to_append)
                        level_of_members = find_levels_of_members(session_1, n_to_append)
                        n_attempts+=1
                        if len(department_of_members) == 0 or department_of_members.count(departments[i]) == 0 or n_attempts > ITERATIONS:
                            if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            else:
                                session_1.append(n_to_append)
                                n_attempts = 0
                                break
                    else:
                        level_of_members = find_levels_of_members(session_1, n_to_append)
                        n_attempts+=1
                        if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                            if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or n_attempts > ITERATIONS:
                                session_1.append(n_to_append)
                                n_attempts = 0
                                break
                        elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                            if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or n_attempts > ITERATIONS:
                                session_1.append(n_to_append)
                                n_attempts = 0
                                break
                        else:
                            session_1.append(n_to_append)
                            n_attempts = 0
                            break                        
            else:
                if session_1.count(n_to_append) < 4:
                    if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'maximize':
                        department_of_members = find_department_of_members(session_1, n_to_append)
                        level_of_members = find_levels_of_members(session_1, n_to_append)
                        n_attempts+=1
                        if len(department_of_members) == 0 or department_of_members.count(departments[i]) > 0 or n_attempts > ITERATIONS:
                            if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            else:
                                session_1.append(n_to_append)
                                n_attempts = 0
                                break
                    elif MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'minimize':
                        department_of_members = find_department_of_members(session_1, n_to_append)     
                        level_of_members = find_levels_of_members(session_1, n_to_append)
                        n_attempts+=1
                        if len(department_of_members) == 0 or department_of_members.count(departments[i]) == 0 or n_attempts > ITERATIONS:
                            if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or n_attempts > ITERATIONS:
                                    session_1.append(n_to_append)
                                    n_attempts = 0
                                    break
                            else:
                                session_1.append(n_to_append)
                                n_attempts = 0
                                break
                    else:
                        session_1.append(n_to_append)
                        break

    #We repeat for the second session
    for i in range(row_count):
        #Get partners of last session
        partners = find_partners(session_1, session_1[i], i)
        #Cycle that will run until the two sessions have the same number of groups
        attempts_to_assign = 0
        while len(session_2) < len(session_1) :

            n_to_append = randint(1,n_groups)
            #First we make groups of three
            if i < n_groups * 3:
                if session_2.count(n_to_append) < 3:

                    #Option to minimize overlap within groups
                    if MINIMIZE_OVERLAP is True:
                        if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'maximize':
                            j = 0                            
                            members = find_members(session_2, n_to_append)
                            department_of_members = find_department_of_members(session_2, n_to_append)
                            level_of_members = find_levels_of_members(session_2, n_to_append)
                            attempts_to_assign+=1
                            add = False 
                            #First we check if there are already members of the department in the group
                            # or if the group is empty
                            if len(department_of_members) == 0 or department_of_members.count(departments[i]) > 0 or attempts_to_assign > ITERATIONS:
                                if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                else:
                                    add = True
                            #We find the members that already are in the group to be assigned,
                            #if there is an overlap it doesn't assign.
                            for idx, value in enumerate(partners):
                                if(members.count(partners[idx]) != 0 and attempts_to_assign < ITERATIONS):
                                    attempts_to_assign+=1
                                    add = False
                                    break
                            #If there is no overlap, or there have been to many attempts to assign, 
                            # it assigns this person to the group
                            if add is True:
                                attempts_to_assign = 0
                                session_2.append(n_to_append)
                                break
                        if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'minimize':
                            j = 0
                            #We find the members that already are in the group to be assigned,
                            #if there is an overlap it doesn't assign.
                            members = find_members(session_2, n_to_append)
                            department_of_members = find_department_of_members(session_2, n_to_append)
                            level_of_members = find_levels_of_members(session_2, n_to_append)
                            attempts_to_assign+=1
                            add = False 
                            #First we check if there are already members of the department in the group
                            # or if the group is empty
                            if len(department_of_members) == 0 or department_of_members.count(departments[i]) == 0 or attempts_to_assign > ITERATIONS:
                                if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                else:
                                    add = True

                            for idx, value in enumerate(partners):
                                if(members.count(partners[idx]) != 0 and attempts_to_assign < ITERATIONS):
                                    attempts_to_assign+=1
                                    add = False
                                    break
                            #If there is no overlap, or there have been to many attempts to assign, 
                            # it assigns this person to the group
                            if add is True:
                                attempts_to_assign = 0
                                session_2.append(n_to_append)
                                break
                        else:
                            j = 0
                            #We find the members that already are in the group to be assigned,
                            #if there is an overlap it doesn't assign.
                            level_of_members = find_levels_of_members(session_2, n_to_append)
                            members = find_members(session_2, n_to_append)
                            add = True                           

                            for idx, value in enumerate(partners):
                                if(members.count(partners[idx]) != 0 and attempts_to_assign < ITERATIONS):
                                    attempts_to_assign+=1
                                    add = False
                                    break
                            #If there is no overlap, or there have been to many attempts to assign, 
                            # it assigns this person to the group
                            if add is True:
                                attempts_to_assign = 0
                                session_2.append(n_to_append)
                                break
                    #If there is no need to minimize or maximize overlap between groups
                    else:
                        if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'maximize':
                            department_of_members = find_department_of_members(session_2, n_to_append)
                            level_of_members = find_levels_of_members(session_2, n_to_append)
                            attempts_to_assign+=1
                            if len(department_of_members) == 0 or department_of_members.count(departments[i]) > 0 or attempts_to_assign > ITERATIONS:
                                if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or attempts_to_assign > ITERATIONS:
                                        session_2.append(n_to_append)
                                        attempts_to_assign = 0
                                        break
                                elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or attempts_to_assign > ITERATIONS:
                                        session_2.append(n_to_append)
                                        attempts_to_assign = 0
                                        break
                                else:
                                    session_2.append(n_to_append)
                                    attempts_to_assign = 0
                                    break
                        elif MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'minimize':
                            department_of_members = find_department_of_members(session_2, n_to_append)
                            n_attempts+=1
                            if len(department_of_members) == 0 or department_of_members.count(departments[i]) == 0 or n_attempts > ITERATIONS:
                                session_2.append(n_to_append)
                                n_attempts = 0
                                break
                        else:
                            session_2.append(n_to_append)
                            break
            #Then we make groups of 4
            else:
                if session_2.count(n_to_append) < 4:
                    if MINIMIZE_OVERLAP is True:
                        if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'maximize':
                            j = 0
                            #We find the members that already are in the group to be assigned,
                            #if there is an overlap it doesn't assign.
                            members = find_members(session_2, n_to_append)
                            department_of_members = find_department_of_members(session_2, n_to_append)
                            level_of_members = find_levels_of_members(session_1, n_to_append)
                            attempts_to_assign+=1
                            add = False 
                            #First we check if there are already members of the department in the group
                            # or if the group is empty
                            if len(department_of_members) == 0 or department_of_members.count(departments[i]) > 0 or attempts_to_assign > ITERATIONS:
                                if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                else:
                                    add = True

                            for idx, value in enumerate(partners):
                                if(members.count(partners[idx]) != 0 and attempts_to_assign < ITERATIONS):
                                    attempts_to_assign+=1
                                    add = False
                                    break
                            #If there is no overlap, or there have been to many attempts to assign, 
                            # it assigns this person to the group
                            if add is True:
                                attempts_to_assign = 0
                                session_2.append(n_to_append)
                                break
                        if MINIMIZE_OR_MAXIMIZE_DEPARTMENT_OVERLAP == 'minimize':
                            j = 0
                            #We find the members that already are in the group to be assigned,
                            #if there is an overlap it doesn't assign.
                            members = find_members(session_2, n_to_append)
                            department_of_members = find_department_of_members(session_2, n_to_append)
                            level_of_members = find_levels_of_members(session_1, n_to_append)
                            attempts_to_assign+=1
                            add = False 
                            #First we check if there are already members of the department in the group
                            # or if the group is empty
                            if len(department_of_members) == 0 or department_of_members.count(departments[i]) == 0 or attempts_to_assign > ITERATIONS:
                                if MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'maximize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) > 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                elif MINIMIZE_OR_MAXIMIZE_LEVEL_OVERLAP == 'minimize':
                                    if len(level_of_members) == 0 or level_of_members.count(levels[i]) == 0 or attempts_to_assign > ITERATIONS:
                                        add = True
                                else:
                                    add = True

                            for idx, value in enumerate(partners):
                                if(members.count(partners[idx]) != 0 and attempts_to_assign < ITERATIONS):
                                    attempts_to_assign+=1
                                    add = False
                                    break
                            #If there is no overlap, or there have been to many attempts to assign, 
                            # it assigns this person to the group
                            if add is True:
                                attempts_to_assign = 0
                                session_2.append(n_to_append)
                                break
                        else:
                            j = 0
                            members = find_members(session_2, n_to_append)
                            add = True
                            for idx, value in enumerate(partners):
                                if(members.count(partners[idx]) != 0 and attempts_to_assign < ITERATIONS):
                                    attempts_to_assign+=1
                                    add = False
                                    break
                            if add is True:
                                attempts_to_assign = 0
                                session_2.append(n_to_append)
                                break                    
                    else:
                        session_2.append(n_to_append)
                        break

    # print(session_1)
    # print(session_2)


#This part prints the results in a csv file called groups.csv
data = ["userId", "sessionId for topic 1", "sessionId for topic2"]
with open('groups.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)
    for i in range(row_count):
        writer.writerow([i+1, session_1[i], session_2[i]])

#The following part are tests
#Check overlap
overlaps = 0
for i, value in enumerate(session_1):
    partners = find_partners(session_1, value, i)    
    partners2 = find_partners(session_2, session_2[i], i)
    for j, value in enumerate(partners):
        for k, value in enumerate(partners2):
            if partners[j] == partners2[k]:
                overlaps+=1

#Check overlaps within departments and levels
department_overlaps = 0
department_overlaps2 = 0
levels_overlaps = 0
levels_overlaps2 = 0
for i in range(n_groups):    
    group = find_department_of_members(session_1, i+1)
    group_levels = find_levels_of_members(session_1, i+1)
    group2 = find_department_of_members(session_2, i+1)
    group_levels2 = find_levels_of_members(session_2, i+1)
    for j, value in enumerate(group):
        if group.count(value) > 1:
            department_overlaps+=1
    for k, value in enumerate(group2):
        if group2.count(value) > 1:
            department_overlaps2+=1
    for l, value in enumerate(group_levels):
        if group_levels.count(value) > 1:
            levels_overlaps+=1
    for m, value in enumerate(group_levels2):
        if group_levels2.count(value) > 1:
            levels_overlaps2+=1    
    
print('Overlaps between groups: ' + str(overlaps))
print('Department overlaps session 1: ' + str(department_overlaps/2))
print('Department overlaps session 2: ' + str(department_overlaps2/2))
print('Level overlaps session 1: ' + str(levels_overlaps/2))
print('Level overlaps session 2: ' + str(levels_overlaps2/2))