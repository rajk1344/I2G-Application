import csv
from student import *
from new_student import *

def list_missing(catcourse, qualtrics):
    #Checking whether a student has not at all done qualtrics
    missing_student = [] 
    for student in catcourse:
        student_exists = False
        catcourse_email = student.email
        for qualtrics_student in qualtrics:
            if qualtrics_student.email[0:(len(qualtrics_student.email)-13)] == catcourse_email:
                student_exists = True
        if (student_exists == False):
            missing_student.append(student)
    
    # Pre-clean qualtrics data (Differentiating incomplete from complete)
    incomplete_data = []
    clean_data = []
    for student in qualtrics:
        if student.status != str(1):
            duplicate_entry = False
            for dup_student in qualtrics:
                if dup_student.email == student.email and dup_student.status == str(1):
                    duplicate_entry = True
            if duplicate_entry == False:
                incomplete_data.append(student)
        else:
            clean_data.append(student)
    
    # Looking for agreement and non-agreement students
    disagreed_students = []
    for student in qualtrics:
        if student.agreement != "I agree":
            disagreed_students.append(student)

    return missing_student, incomplete_data, clean_data, disagreed_students