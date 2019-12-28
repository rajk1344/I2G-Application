import csv
from matcher import *
from project import *
from student import *
from missing_student import *
from write import *
from file_reader import *

source = 'sample projects log'
semester = '2019-08-Fall-CAP'
destination = 'projects-API'
get_projects_semester(source,destination,semester)

