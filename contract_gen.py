import csv

class csvProjectInfo(object):
    def __init__(self, client_FirstName, client_LastName, client_Email,client_OrganizationName, project_ID, project_TeamNumber,project_Title):
        self.client_FirstName = client_FirstName
        self.client_LastName = client_LastName
        self.client_Email = client_Email
        self.client_OrganizationName = client_OrganizationName
        self.project_ID = project_ID
        self.project_TeamNumber = project_TeamNumber
        self.project_Title = project_Title

    def printStuff(self):
        # print(self.client_FirstName)
        # print(self.client_LastName)
        # print(self.client_Email)
        # print(self.client_OrganizationName)
        # print(self.project_ID)
        # print(self.project_TeamNumber)
        # print(self.project_Title)
        print(f'Dear {self.client_FirstName},')
        print(f"""These students digitally signed the IP+NDA agreement 'UC Merced Innovate to Grow Program - Student Registration and Agreement' with UC Merced ID credentials:""")
        print('Timestamp\t First Name\tLast Name\tEmail')
        csvStudentInfo().printStuff1()
        print(f"""to participate in your project:
Project ID:	                {self.project_ID}
Project Title:	                {self.project_Title}            
Team #:	                        {self.project_TeamNumber}
Organization:	                {self.client_OrganizationName}
Primary Contact First Name:	{self.client_FirstName}
Primary Contact Last Name:	{self.client_LastName}
Primary Contact Email:	        {self.client_Email}

We have a digital record and timestamp of their agreement: the table above includes their credentials and time of acceptance. For your reference this is the language of the agreement that the students digitally signed.
Thank you for your participation in the Innovate to Grow program. Please let us know if you have any questions, or special circumstances to address.
Stefano Foresti
+1-801-971-3680
Stefano.Foresti@UCMerced.edu
University of California Merced, Director of Innovation -> engineering.ucmerced.edu
    """)

class csvStudentInfo(object):
    def __init__(self,student_Timestamp,student_FirstName,student_LastName,student_Email):
        self.student_Timestamp = student_Timestamp
        self.student_FirstName = student_FirstName
        self.student_LastName = student_LastName
        self.student_Email = student_Email

        

    def printStuff1(self):
        # print(self.student_Timestamp)
        # print(self.student_FirstName)
        # print(self.student_LastName)
        # print(self.student_Email)
        print(f'{self.student_Timestamp} \t {self.student_FirstName} \t {self.student_LastName} \t {self.student_Email}')

def main():

    projectList = []
    studentList = []
    studentArray = []
    
    projectIDLocater = input('Enter the project ID: ')
    TeamNumberLocater = input('Enter the project team number: ')
    
    projects = open('2019-01-Spring-CAP-MASTER - PROJECTS.csv','r',encoding = "utf8")
    students = open('2019-01-Spring-CAP-MASTER - STUDENTS.csv','r',encoding = "utf8")

    # count for creating  projectList
    count = 0

    # parsing the csv file
    with projects as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data = [row for row in csv.reader(csvDataFile)]
            for i in data:
                # if projectIDLocater == i[0]:
                client_FirstName = i[4]
                client_LastName = i[5]
                client_Email = i[6]
                client_OrganizationName = i[3]

                project_ID = i[0]
                project_Title = i[17]
                project_TeamNumber = i[1]
                
                if count > 0:
                    # appending a lists for the respective projectID
                    projectList.append(csvProjectInfo(client_FirstName, client_LastName, client_Email,client_OrganizationName, project_ID, project_TeamNumber,project_Title))
            
                count = count + 1

        with students as csvDataFile1:
            csvReader1 = csv.reader(csvDataFile1)
            for row1 in csvReader1:
                data1 = [row1 for row1 in csvReader1]
            for n in data1:
                if TeamNumberLocater == n[7]:
                    student_Timestamp = n[0]
                    student_FirstName = n[1]
                    student_LastName = n[2]
                    student_Email = n[3]
                    studentArray.append(csvStudentInfo(student_Timestamp,student_FirstName,student_LastName,student_Email))
                    
            for eachStudent in studentArray:
                 # for i in range(4):
                 #     print(eachStudent[i], end = '\t')
                 # print()
                # if TeamNumberLocater == n[7]:
                eachStudent.printStuff1()
                
                            


        # studentArray.printStuff1()

        projectList[12].printStuff()
        
                    
                    
    
main()
