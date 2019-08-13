import csv
from student import *
from project import *
import missing_student

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