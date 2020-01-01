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
from networkx.algorithms.flow import *
from networkx.algorithms.bipartite import hopcroft_karp_matching
from Team import *

students = read_students_new('data/input/Test_data/student_data.csv')
projects = read_projects('data/input/Test_data/projects.csv')

G = create_graph(students, projects)
print(nx.is_bipartite(G))

teams = match_students(G,students,projects)
print_result(teams)




#nx.draw(G,with_labels = True)
#plt.show()


"""
Testing the writing Projects log 
source = 'sample projects log'
semester = '2019-08-Fall-CAP'
destination = 'projects-API'
get_projects_semester(source,destination,semester)
"""

