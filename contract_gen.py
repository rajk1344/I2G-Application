import csv
    
def main ():

    projectInfo = []
    studentArray = []
    timestamps = []
    studentFirstNames = []
    studentLastNames = []
    studentEmails = []

    # teamNumber = [0]

    # User Input
    projectIDLocater = input('Enter the project ID: ')
    
    file = open('2019-01-Spring-CAP-MASTER - PROJECTS.csv','r',encoding="utf8")
    studentRegistrations = open('2019-01-Spring-CAP-MASTER - STUDENTS.csv','r',encoding = "utf8")
            
    with file as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data = [row for row in csv.reader(csvDataFile)]
            for i in data:
                if projectIDLocater == i[0]:
                    projectID = i[0]
                    projectTitle = i[17]
                    teamNumber = i[1]

                    organizationName = i[3]
                    primaryContactFirstName = i[4]
                    primaryContactLastName = i[5]
                    primaryContactEmail = i[6]

        with studentRegistrations as csvDataFile1:
            csvReader1 = csv.reader(csvDataFile1)
            for row1 in csvReader1:
                data1 = [row for row in csvReader1]
          
            for n in data1:
                if teamNumber == n[7]:
                #if projectID == n[13]:
                    studentArray.append(n[0:4])

                    # teamNumber.append(n[7])

            print(f'Dear {primaryContactFirstName},\n')
            print(f"These students digitally signed the IP+NDA agreement 'UC Merced Innovate to Grow Program - Student Registration and Agreement' with UC Merced ID credentials:")
            print('Timestamp\t First Name\tLast Name\tEmail')

            
            for listedInfo in studentArray:
                for i in range(4):
                    print(listedInfo[i], end = '\t\t') 
                print()
                
            

            print(f"""to participate in your project:
Project ID:	                    {projectID}
Project Title:                      {projectTitle}            
Team #:	                            {teamNumber}
Organization:	                    {organizationName}
Primary Contact First Name:	    {primaryContactFirstName}
Primary Contact Last Name:	    {primaryContactLastName}
Primary Contact Email:	            {primaryContactEmail}

We have a digital record and timestamp of their agreement: the table above includes their credentials and time of acceptance. For your reference this is the language of the agreement that the students digitally signed.
Thank you for your participation in the Innovate to Grow program. Please let us know if you have any questions, or special circumstances to address.
Stefano Foresti
+1-801-971-3680
Stefano.Foresti@UCMerced.edu
University of California Merced, Director of Innovation -> engineering.ucmerced.edu
""")

main()