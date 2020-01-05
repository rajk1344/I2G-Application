from new_student import *
from project import *
import networkx as nx
from networkx.algorithms.flow import *
from networkx.algorithms.bipartite import hopcroft_karp_matching
from Team import *
import matplotlib.pyplot as plt

#this function creates a bipartite graph before matching and assigns necessart capacity to each project

def create_graph(students, projects):
    G = nx.DiGraph()
    current = 0
    for p in projects:
        for s in students:
            pref = s.preferences
            if pref[current] >= 4.0:
                G.add_node(s.email,bipartite = 0)
                G.add_node(p.project_id, bipartite = 1)
                G.add_edge(s.email, p.project_id, capacity = 1.0)
                G.add_edge('source',s.email,capacity = 1.0)
                G.add_edge(p.project_id,'sink', capacity = 3.0)
                s.assigned = True
        current = current + 1
    return G

#This function outputs a team array that consists of matched students and teams
def match_students(students, projects):
    G = create_graph(students, projects)
    teams = []
    flow_value, flow_dict = nx.maximum_flow(G, 'source', 'sink', capacity = 'capacity', flow_func=edmonds_karp)
    R = edmonds_karp(G,'source','sink', capacity='capacity')
    students_left = find_non_matched_students(R, students)
    avaliable_projects = find_avaliable_projects(R, projects)
    team_number = 1
    for p in projects:
        studs = []
        for s in students:
            if s.assigned == True:
                if p.project_id in flow_dict[s.email]:
                    if flow_dict[s.email][p.project_id] == 1.0:
                        studs.append(s)
        teams.append(Team(p,studs,team_number))
        team_number = team_number + 1
    teams = match_remaining_students(teams, G, flow_dict,students_left,avaliable_projects)
    return teams

#This function finds those students that were not matched or were not present in the bipartite graph
def find_non_matched_students(R,students):
    stud = []
    for s in students:
        student_exists = R.has_node(s.email)
        if student_exists == False:
            stud.append(s)
    return stud

#This function finds the projects where non-matched students can go
def find_avaliable_projects(flow_dict,projects):
    proj = []
    for p in projects:
            project_size = flow_dict[p.project_id]['sink']['flow']
            if project_size < 3:
                proj.append(p)
    return proj

#This function matches the remaining students with the remaining projects
def match_remaining_students(teams, G, flow_dict, students, projects):
    for p in projects:
        index = find_team_index(teams, p.project_id)
        studs = teams[index].students
        if len(students) > 0:
            cap = G.get_edge_data(p.project_id, 'sink')
            net_capacity = int(cap['capacity'] - flow_dict[p.project_id]['sink'])
            for i in range(0,net_capacity):
                s = students.pop(0)
                studs.append(s)
            teams[index].students = studs
    return teams

#This function returns the team array's index
def find_team_index(teams, project_id):
    index = 0
    for t in teams:
        p = t.project.project_id
        if p == project_id:
            return index
        index = index + 1
    return -1
