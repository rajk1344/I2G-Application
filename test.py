import csv

from matcher import *
from project import *
from student import *

students_file_name = "roster.csv"
projects_file_name = 'projects.csv'
students = []
projects = []

# read csv files
with open(students_file_name, 'r', encoding='utf-8-sig') as csvfile:
    # create csvread obj
    csvread = csv.reader(csvfile)
    # populate students with Student obj
    for row in csvread:
        temp = []
        # convert string preferances into numericals
        for pref in row[3:]:
            if pref == 'Definitely yes':
                temp.append(5)
            elif pref == 'Probably yes':
                temp.append(4)
            elif pref == 'Maybe':
                temp.append(3)
            elif pref == 'Probably not':
                temp.append(2)
            else:
                temp.append(1)

        students.append(Student(row[0], row[1], row[2], temp))

with open(projects_file_name, 'r', encoding='utf-8-sig') as csvfile:
    # create csvread obj
    csvread = csv.reader(csvfile)
    # populate projects
    for row in csvread:
        # size fixed to 4 for now
        projects.append(Project(row, 4))

# testing

match(students, projects)
