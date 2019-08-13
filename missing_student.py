import csv
from student import *


def list_missing(catcourse, qualtrics):
    t = 0
    missing = []
    for student in catcourse:
        cat_email = student.email
        for stud in qualtrics:
            qual_email = stud.email
            if qual_email == cat_email:
                t = 1
        if t == 0:
            missing.append(Student(0, student.first_name,
                                   student.last_name, student.email, 0, 0))
        t = 0
    return missing
