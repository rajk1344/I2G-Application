from file_reader import *
from new_student import *
from project import *
import networkx as nx
from networkx.algorithms.flow import *
from networkx.algorithms.bipartite import hopcroft_karp_matching
from Team import *

def create_graph(students, projects):
    G = nx.DiGraph()
    for p in projects:
        for s in students:
            pref = s.preferences
            for i in pref:
                if i >= 3:
                    G.add_node(s.email,bipartite = 0)
                    G.add_node(p.project_title, bipartite = 1.0)
                    G.add_edge(s.email, p.project_title, capacity = 1.0)
                    G.add_edge('source',s.email,capacity = 1.0)
                    G.add_edge(p.project_title,'sink', capacity = 3.0)
                    s.assigned = True
    return G

def match_students(G, students, projects):
    teams = []
    flow_value, flow_dict = nx.maximum_flow(G, 'source', 'sink', flow_func=edmonds_karp)
    print(flow_value)
    R = edmonds_karp(G,'source','sink')
    students_left = find_non_matched_students(R, students)
    print(len(students_left))
    avaliable_projects = find_avaliable_projects(R, projects)
    for p in projects:
        studs = []
        for s in students:
            if s.assigned == True:
                if p.project_title in flow_dict[s.email]:
                    if flow_dict[s.email][p.project_title] == 1.0:
                        studs.append(s)
        teams.append(Team(p,studs))
    teams = match_remaining_students(teams, G, flow_dict,students_left,avaliable_projects)
    return teams

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
            project_size = flow_dict[p.project_title]['sink']['flow']
            print(project_size)
            if project_size < 3:
                proj.append(p)
    return proj

def match_remaining_students(teams, G, flow_dict, students, projects):
    print(len(students))
    for p in projects:
        studs = []
        if len(students) >= 1:
            print('goes here')
            cap = G.get_edge_data(p.project_title, 'sink')
            net_capacity = int(cap['capacity'] - flow_dict[p.project_title]['sink'])
            for i in range(0,net_capacity):
                s = students.pop(0)
                print(s.email)
                studs.append(s)
            index = find_team_index(teams, p.project_id)
            teams[index].students = studs
            #teams.append(Team(p,studs))
    return teams

def find_team_index(teams, project_id):
    index = 0
    for t in teams:
        p = t.project.project_id
        if p == project_id:
            return index
        index = index + 1
    return -1
def print_result(teams):
    for t in teams:
        project = t.project
        students = t.students
        print(project.project_title)
        for s in students:
            print(s.email)
        print('-----')
