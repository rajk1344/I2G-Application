import csv
from student import *


def list_missing(catcourse, qualtrics):
    t = 0
    missing_qualtrics = []
    missing_catcourse = []
    for student in catcourse:
        cat_email = student.email
        for stud in qualtrics:
            qual_email = stud.email[0:len(stud.email)-13]
            if qual_email == cat_email:
                t = 1
        if t == 0:
            missing_qualtrics.append(Student(0, student.first_name,
                                   student.last_name, student.email, 0, 0))
        t = 0
    t = 0
    for student in qualtrics:
        qualtrics_email = student.email[0:len(student.email)-13]
        for stud in catcourse:
            cat_email = stud.email
            if qualtrics_email == cat_email:
                t = 1
        if t == 0:
            missing_catcourse.append(Student(0, student.first_name,
                                   student.last_name, student.email, 0, 0))
        t = 0

    return missing_qualtrics,missing_catcourse
