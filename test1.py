class test1(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(student):
        return student.email

    def test(catcourse, qualtrics):
        t=0
        missing = []
        for student in catcourse:
            cat_email = get_email(student)
            for stud in qualtrics:
                qual_email = get_email(stud)
                if qual_email[0:len(qual_email)-13]==cat_email:
                    t = 1
            if t==0:
                missing.append(missing_students(student.name, student.email))
            t=0
        for data in missing:
            print(data.name+ ';'+ data.email)
            print('------')
