from file_reader import *
from new_student import *
from project import *
import networkx as nx

def create_graph(students, projects):
    G = nx.Graph()
    count = 0
    for p in projects:
        for s in students:
            pref = s.preferences
            if pref[count] >= 3 and s.assigned == False:
                G.add_edge(p.project_title, s.email)
        count = count + 1
    return G


