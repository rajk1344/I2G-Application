from file_reader import *
from new_student import *
from project import *
import networkx as nx
from networkx.algorithms.flow import *
from networkx.algorithms.bipartite import hopcroft_karp_matching

def create_graph(students, projects):
    G = nx.DiGraph()
    count = 0
    for p in projects:
        for s in students:
            pref = s.preferences
            if pref[count] >= 3 and s.assigned == False:
                G.add_node(s.email,bipartite = 0)
                G.add_node(p.project_title, bipartite = 1.0)
                G.add_edge(s.email, p.project_title, capacity = 1.0)
                G.add_edge('source',s.email,capacity = 1.0)
                G.add_edge(p.project_title,'sink', capacity = 3.0)
        count = count + 1
    return G

def match_students(G):
    flow_value, flow_dict = nx.maximum_flow(G, 'source', 'sink', flow_func=edmonds_karp)
    return flow_value, flow_dict

def find_non_matched_students(R,students):
    stud = []
    for s in students:
        student_exists = R.has_node(s.email)
        if student_exists == False:
            stud.append(s)
    return stud

def find_avaliable_projects(flow_dict,projects):
    proj = []
    for p in projects:
            project_size = flow_dict[p.project_title]['sink']
            if project_size < 3:
                proj.append(p)
    return proj



