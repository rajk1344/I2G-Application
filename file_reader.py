import csv
from student import *
from project import *
from write import *
from missing_student import *

def read_students(file):
    students = []

    # read csv files
    with open(file, 'r', encoding='utf-8-sig') as csvfile:
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
    
    return students

    
def read_projects(file):
    
    projects = []
    
    with open(file, 'r', encoding='utf-8-sig') as csvfile:
        # create csvread obj
        csvread = csv.reader(csvfile)
        # populate projects
        for row in csvread:
            projects.append(
                Project(row[0], row[3], row[4], row[5], row[6], row[9]))
    
    return projects


def read_catcources(file):
    
    catcourse = []

    with open(file, 'r', encoding='utf-8-sig') as csvfile:
        # create csvread obj
        csvread = csv.reader(csvfile)
        temp = []
        # populate projects
        for row in csvread:
            catcourse.append(Student(0,row[0], row[1], row[2],0,temp))

    return catcourse

#TODO This needs to be fixed
def read_matched_students(file, output):
    with open(file, 'r', encoding='utf-8-sig') as csvfile:
        # create csvread obj

        students2 = []
        projects2 = []

        csvread = csv.reader(csvfile)
        temp = []
        # populate projects
        for row in csvread:
            students2.append(Student(row[0], row[1], row[2],row[3],row[4],0))
            projects2.append(Project(row[5],row[6],row[7],row[8],row[9],row[10]))
        t = 1
        p = 1
        projects2 = list(dict.fromkeys(projects2))
        project_list = []
        while t <= 10:
            student_list = []
            for student in students2:
                if str(t) == student.contract:
                    student_list.append(student)
            write_project_pdf_contract(student_list, projects2[p],t, output)
            t += 1
            p += len(student_list)