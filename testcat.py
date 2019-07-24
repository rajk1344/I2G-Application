import csv

from missing_student import *

catcourse_file_name = "testcat.csv"
qualtrics_file_name = "testqualtrics.csv"
catcourse = []
qualtrics = []

with open(qualtrics_file_name, 'r', encoding='utf-8-sig') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        temp = []
        for data in row:
            temp.append(data)
        qualtrics.append(missing_student(temp[0]+''+temp[1],temp[2]))
with open(catcourse_file_name, 'r', encoding='utf-8-sig') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        temp = []
        for data in row:
            temp.append(data)
        catcourse.append(missing_student(temp[0],temp[1]))


list_missing(catcourse,qualtrics)
