import qualtrics_data_processing
import csv

"""
This functionality does the following:
    1) Remove all the entries where students have disagreed 
    2) Keep the updated responses based on timestamp
"""
def remove_disagreed_students(clean_data):
    new_clean_data = clean_data
    for student in new_clean_data:
        if student.agreement != "I agree":
            new_clean_data.remove(student)
    return new_clean_data

def remove_duplicate_entries(clean_data):
    i = 1
    new_clean_data = clean_data
    for student in new_clean_data:
        for sub_student in range(i,len(new_clean_data)):
            if sub_student.email == student.email:
                new_clean_data.remove(student)
        i = i + 1
    return new_clean_data

def clean_data(qualtrics, clean_data):

    clean_data = remove_disagreed_students(clean_data)
    clean_data = remove_duplicate_entries(clean_data)
    
    return clean_data
