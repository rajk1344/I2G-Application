import xlsxwriter







def write_master(project_arr):

    workbook = xlsxwriter.Workbook('demo.xlsx')
    studentsheet = workbook.add_worksheet('STUDENTS')
    projectsheet = workbook.add_worksheet('PROJECTS')

    header_students = ['Timestamp', 'First Name', 'Last Name', 'Email', 'Phone Number',
                       'Major', 'Agreed?', 'Project ID', 'Team #', 'Role', 'Client', 'Alternate Email', 'Notes']

    header_projects = ['Project ID', 'Team (# in class)', 'Time Updated', 'Organization  Name', 'Primary Contact First Name', 'Primary Contact Last Name',
                       'Primary Contact Email Address', 'Primary Contact Phone Number', 'Rules - Accepted', 'Project Title', 'Background', 'Problem', 'Objectives', 'Summary Link']

    for col in header_students:
        studentsheet.write(0, header_students.index(col), col)

    for col in header_projects:
        projectsheet.write(0, header_projects.index(col), col)

    row1 = 1
    row2 = 1

    for project in project_arr:
        projectsheet.write(row1, 0, project.project_id)
        
        
        
        
        
        for student in project.student
        studentsheet.write(row2, 0, student.timestamp)
        studentsheet.write(row2, 1, student.first_name)
        studentsheet.write(row2, 2, student.last_name)
        studentsheet.write(row2, 3, student.email)
        row2 = row2 + 1

    workbook.close()



# Widen the first column to make the text clearer.
#studentsheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})

# Write some simple text.
#studentsheet.write('A1', 'Hello')

# Text with formatting.
#studentsheet.write('A2', 'World', bold)

# Write some numbers, with row/column notation.
#studentsheet.write(2, 0, 123)
#studentsheet.write(3, 0, 123.456)