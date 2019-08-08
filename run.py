import csv
from matcher import *
from project import *
from student import *
from missing_student import *
from write import *

students_file_name = "data/input/Student_final_roster.csv"
projects_file_name = 'data/input/projects.csv'
catcourse_file_name = "data/input/Catcourse_final_roster.csv"
qualtrics_file_name = "data/input/Student_final_roster_missing.csv"
matched_students = "data/output/student-project.csv"
students = []
students1 = []
projects = []
catcourse = []
students2 = []
projects2 = []
choice = input("1. Match \n2. Find missing students \n3. Generate contracts\n")
# read csv files
with open(students_file_name, 'r', encoding= 'utf-8-sig') as csvfile:
    # create csvread obj
    csvread = csv.reader(csvfile)
    # populate students with Student obj
    for row in csvread:
        temp = []
        # convert string preferances into numericals
        for pref in row[14:]:
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

        students.append(Student(row[0], row[2], row[3], row[4], row[9], temp))
with open(projects_file_name, 'r', encoding='utf-8-sig') as csvfile:
    # create csvread obj
    csvread = csv.reader(csvfile)
    # populate projects
    for row in csvread:
        projects.append(Project(row[0], row[3], row[4], row[5], row[6], row[9]))
with open(catcourse_file_name, 'r', encoding='utf-8-sig') as csvfile:
    # create csvread obj
    csvread = csv.reader(csvfile)
    temp = []
    # populate projects
    for row in csvread:
        catcourse.append(Student(0,row[0], row[1], row[2],0,temp))
with open(qualtrics_file_name, 'r', encoding='utf-8-sig') as csvfile:
    # create csvread obj
    csvread = csv.reader(csvfile)
    # populate students with Student obj
    for row in csvread:
        temp = []
        # convert string preferances into numericals
        for pref in row[14:]:
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

        students1.append(Student(row[0], row[2], row[3], row[4], row[9], temp))
if choice == '1':
    match(students,projects)
if choice == '2':
    export_missing_students(list_missing(catcourse,students1))
"""
if choice == '3':
    with open(matched_students, 'r', encoding='utf-8-sig') as csvfile:
        # create csvread obj
        csvread = csv.reader(csvfile)
        temp = []
        # populate projects
        for row in csvread:
            students2.append(Student(row[0], row[1], row[2],row[3],row[4],0))
            projects2.append(Project(row[5],row[6],row[7],row[8],row[9],row[10]))
    write_project_pdf_contract(students2,projects2)
"""
