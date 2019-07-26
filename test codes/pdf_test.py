import csv
from fpdf import FPDF
class project (list):
    def __init__(self, client_FirstName, client_LastName, client_Email, client_OrganizationName, project_ID, project_Title, project_TeamNumber):#, studentInfo):
        # parsing both projects and students
        self.client_FirstName = client_FirstName
        self.client_LastName = client_LastName
        self.client_Email = client_Email
        self.client_OrganizationName = client_OrganizationName
        self.project_ID = project_ID
        self.project_Title = project_Title
        self.project_TeamNumber = project_TeamNumber
class student (object): 
    def __init__(self, student_Timestamp, student_FirstName, student_LastName, student_Email):
        self.student_Timestamp = student_Timestamp
        self.student_FirstName = student_FirstName
        self.student_LastName = student_LastName
        self.student_Email = student_Email

def printProject (self):
    print(self.client_FirstName)
    print(self.client_LastName)
    print(self.client_Email)

def printContract (student_list,project_list):
    pdf = FPDF(format = 'letter', unit = 'in')
    pdf.add_page()
    pdf.set_font('Times','',10.0)
    # the contract
    effectivePageWidth = pdf.w - 2*pdf.l_margin
    pdf.multi_cell(effectivePageWidth, 0.15,'Dear')
    pdf.multi_cell(effectivePageWidth, 0.15,'These students digit')
    pdf.ln(0.5)
    pdf.output('contracts.pdf','F')
