import csv
from test1 import *
# import fpdf class
from fpdf import FPDF

projectList = []
studentList = []

projects = 'data/input/2019-01-Spring-CAP-MASTER - PROJECTS.csv'
students = 'data/input/2019-01-Spring-CAP-MASTER - STUDENTS.csv'

projectIDLocater = input('Enter project ID: ')
teamNumLocater = input('Enter project team number: ')

count = 0

with open(projects, 'r', encoding='utf-8-sig') as csvProjectFile:
    csvProject = csv.reader(csvProjectFile)
    for i in csvProject:
        client_FirstName = i[4]
        client_LastName = i[5]
        client_Email = i[6]
        client_OrganizationName = i[3]
        project_ID = i[0]
        project_Title = i[17]
        project_TeamNumber = i[1]
        projectList.append(project(client_FirstName, client_LastName, client_Email, client_OrganizationName, project_ID, project_Title, project_TeamNumber))
            # if count > 0:
            #     projectList.append(project(projectInfo))
            # count = count + 1

with open(students, 'r', encoding='utf-8-sig') as csvStudentFile:
        csvStudent = csv.reader(csvStudentFile)
        for n in csvStudent:
            if teamNumLocater == n[7]:
                student_Timestamp = n[0]
                student_FirstName = n[1]
                student_LastName = n[2]
                student_Email = n[3]
                studentList.append(student(student_Timestamp, student_FirstName, student_LastName, student_Email))
printContract(studentList,projectList)
