import csv
import gspread
import xlsxwriter
from oauth2client.service_account import ServiceAccountCredentials
from fpdf import FPDF
import pprint


def write_projects_csv(project_arr, destination):

    with open(destination + '/student_csv.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'First Name', 'Last Name', 'Email', 'Team #', 'Project ID',
                         'Organization Name', 'Client First Name', 'Client Last Name', 'Client Email', 'Project Title'])
        team_number = 1
        for project in project_arr:
            for student in project.students:
                writer.writerow([student.timestamp, student.first_name, student.last_name, student.email, team_number, project.project_id,
                                 project.client_organization_name, project.client_first_name, project.client_last_name, project.client_email, project.project_title])
            team_number = team_number + 1


def write_projects_gsheet(project_arr, destination):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open(destination).sheet1
    sheet.insert_row(['Timestamp', 'First Name', 'Last Name', 'Email', 'Team #', 'Project ID',
                      'Organization Name', 'Client First Name', 'Client Last Name', 'Client Email', 'Project Title'], 1)
    team_number = 1
    index = 3
    for project in project_arr:
        for student in project.students:
            sheet.insert_row([student.timestamp, student.first_name, student.last_name, student.email, team_number, project.project_id,
                              project.client_organization_name, project.client_first_name, project.client_last_name, project.client_email, project.project_title], index)
            index = index + 1
        team_number = team_number + 1


def write_project_information(source, destination):
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'creds.json', scope)
    client = gspread.authorize(creds)
    source_sheet = client.open(source).sheet1
    destination_sheet = client.open(destination).sheet1
    source_row = 2
    source_col = 3
    while source_sheet.cell(source_row, source_col).value != "":
        source_project_id = source_sheet.cell(source_row, source_col).value
        dest_row = 4
        dest_col = 1
        while destination_sheet.cell(dest_row, dest_col).value != source_project_id:
            dest_row = dest_row + 1
        i = 1
        k = 22
        while i <= 4:
            data = source_sheet.cell(source_row, source_col+i).value
            destination_sheet.update_cell(dest_row, dest_col+k, data)
            k = k+1
            i = i+1
        source_row = source_row+1


def export_missing_students(missing_student, incomplete_data, disagreed_students, destination):
    with open(destination + '/missing_student.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        # Writing missing students information
        writer.writerow(['Students who have not finished qualtrics form'])
        writer.writerow(['First Name', 'Last Name', 'Email/UcmNetID'])
        for student in missing_student:
            writer.writerow(
                [student.first_name, student.last_name, student.email])
        writer.writerow('\n')
        # Writing Incomplete registration students information
        writer.writerow(['Students who have incomplete qualtrics data'])
        writer.writerow(['First Name', 'Last Name', 'Email/UcmNetID'])
        for student in incomplete_data:
            writer.writerow(
                [student.first_name, student.last_name, student.email])
        writer.writerow('\n')
        # Writing Disagreed students
        writer.writerow(['Students who have disagreed'])
        writer.writerow(['First Name', 'Last Name', 'Email/UcmNetID'])
        for student in disagreed_students:
            writer.writerow(
                [student.first_name, student.last_name, student.email])


"""
def write_clean_data(clean_data, destination):
    with open(destination + '/missing_student.csv', 'w', encoding='utf-8-sig', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', '''First Name', 'Last Name', 'Email/UcmNetID'])
        for student in qualtrics:
            writer.writerow(
                [student.first_name, student.last_name, student.email])
"""


def write_project_pdf_contract(student_list, project, t, destination):
    # creating the pdf document
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times', '', 10.0)
    effectivePageWidth = pdf.w - 2*pdf.l_margin

    # contract text
    pdf.multi_cell(effectivePageWidth, 0.15,
                   f'Dear {project.client_first_name},')
    pdf.multi_cell(effectivePageWidth, 0.15,
                   'These students digitally signed the IP+NDA agreement "UC Merced Innovate to Grow Program - Student Registration and Agreement" with UC Merced ID credentials:')
    pdf.multi_cell(effectivePageWidth, 0.15, '\n')

    # student information table
    studentTableTitle = ['Timestamp', 'First Name', 'Last Name', 'Email']
    th = pdf.font_size
    columnWidth = effectivePageWidth/4

    for row in studentTableTitle:
        # enters data in columns
        pdf.set_font('Times', 'B', 10.0)
        pdf.cell(columnWidth, th, str(row), border=2)
    pdf.ln(th)

    for student in student_list:
        pdf.set_font('Times', '', 10.0)
        finalList = [student.timestamp, student.first_name,
                     student.last_name, student.email]
        for datum in finalList:
            pdf.cell(columnWidth, th, str(datum), border=2)
        pdf.ln(th)

    # new line
    pdf.multi_cell(effectivePageWidth, 0.15, '\n')

    # project information table
    projectTable = [['Project ID:', project.project_id],
                    ['Project Title:', project.project_title, ],
                    ['Team #:', str(t)],
                    ['Organization:', project.client_organization_name],
                    ['Primary Contact First Name:', project.client_first_name],
                    ['Primary Contact Last Name:', project.client_last_name],
                    ['Primary Conract Email:', project.client_email]]

    for projectData in projectTable:
        for projectInfo in projectData:
            pdf.cell(columnWidth, th, str(projectInfo), border=2)
        pdf.ln(th)

    # contract text cont.
    pdf.multi_cell(effectivePageWidth, 0.15, '\n')
    pdf.multi_cell(effectivePageWidth, 0.15, '''We have a digital record and timestamp of their agreement: the table above includes their credentials and time of acceptance. For your reference this is the language of the agreement that the students digitally signed.
Thank you for your participation in the Innovate to Grow program. Please let us know if you have any questions, or special circumstances to address.

Stefano Foresti
+1-801-971-3680
Stefano.Foresti@UCMerced.edu
University of California Merced, Director of Innovation -> engineering.ucmerced.edu ''')
    pdf.ln(0.5)

    # saves as filename
    pdf.output(destination+'2019-July-Fall-CAP-StudentAgreement-Team'+str(t) +
               '-'+project.client_organization_name+'-'+project.project_id+'.pdf', 'F')


def write_master(project_arr, destination):

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
        projectsheet.write(row1, 3, project.client_organization_name)
        projectsheet.write(row1, 4, project.client_first_name)
        projectsheet.write(row1, 5, project.client_last_name)
        projectsheet.write(row1, 6, project.client_email)
        projectsheet.write(row1, 7, project.project_title)
        row1 = row1 + 1

        for student in project.students:
            studentsheet.write(row2, 0, student.timestamp)
            studentsheet.write(row2, 1, student.first_name)
            studentsheet.write(row2, 2, student.last_name)
            studentsheet.write(row2, 3, student.email)
            row2 = row2 + 1

    workbook.close()