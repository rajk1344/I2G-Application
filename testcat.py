import csv

from student_data import*

catcourse_file_name = "cat.csv"
qualtrics_file_name = "qualtrics.csv"
catcourse = []
qualtrics = []

with open(qualtrics_file_name, 'r', encoding='utf-8-sig') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        temp = []
        for data in row:
            temp.append(data)
        qualtrics.append(student_data(temp[0]+''+temp[1],temp[2]))
with open(catcourse_file_name, 'r', encoding='utf-8-sig') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        temp = []
        for data in row:
            temp.append(data)
        catcourse.append(student_data(temp[0],temp[1]))
for data in catcourse:
    print (data.name)
    print (data.email)
