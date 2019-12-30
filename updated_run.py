import csv
from matcher import *
from project import *
from student import *
from missing_student import *
from write import *
from file_reader import *
from new_matcher import *
import networkx as nx
import matplotlib.pyplot as plt

students = read_students_new('data/input/Test_data/student_data.csv')
projects = read_projects('data/input/Test_data/projects.csv')

G = create_graph(students, projects)
print(nx.is_bipartite(G))

"""
Testing the writing Projects log 
source = 'sample projects log'
semester = '2019-08-Fall-CAP'
destination = 'projects-API'
get_projects_semester(source,destination,semester)
"""

