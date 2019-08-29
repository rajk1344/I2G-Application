import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from fpdf import FPDF


def write_projects_csv(project_arr, destination):

    with open(destination + '/student_csv.csv', 'w', encoding='utf-8-sig', newline = '') as f:
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
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scope)
    client = gspread.authorize(creds)
    sheet = client.open(destination).sheet1
    sheet.insert_row(['Timestamp', 'First Name', 'Last Name', 'Email', 'Team #', 'Project ID',
                     'Organization Name', 'Client First Name', 'Client Last Name', 'Client Email', 'Project Title'],1)
    team_number = 1
    index = 3
    for project in project_arr:
        for student in project.students:
            sheet.insert_row([student.timestamp, student.first_name, student.last_name, student.email, team_number, project.project_id,
                             project.client_organization_name, project.client_first_name, project.client_last_name, project.client_email, project.project_title],index)
            index = index + 1
        team_number = team_number + 1

def export_missing_students(qualtrics, catcourse, bad_data, destination):
    with open(destination + '/missing_student.csv', 'w', encoding='utf-8-sig', newline = '') as f:
        writer = csv.writer(f)
        writer.writerow(['Students who have not finished qualtrics form'])
        writer.writerow(['First Name', 'Last Name', 'Email/UcmNetID'])
        for student in qualtrics:
            writer.writerow(
                [student.first_name, student.last_name, student.email])
        writer.writerow('\n')
        writer.writerow(['Students who are not in catcourse roster'])
        writer.writerow(['First Name', 'Last Name', 'Email/UcmNetID'])
        for student in catcourse:
            writer.writerow(
                [student.first_name, student.last_name, student.email])
        writer.writerow('\n')
        writer.writerow(['Bad Data'])
        writer.writerow(['First Name', 'Last Name', 'Email/UcmNetID'])
        for student in bad_data:
            writer.writerow(
                [student.first_name, student.last_name, student.email])

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
