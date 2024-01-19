student = {} 
course = {}
class Student:
    def __init__(self,student_id,student_name,dob):
        self.name = student_name
        self.student_id = student_id
        self.dob = dob
        self.transcript = {}
    def toString(self):
        print(f"Name: {self.name} ID: {self.student_id} Date of birth: {self.dob}")

class Course:
    def __init__(self,course_id,course_name):
        self.course_id = course_id
        self.name = course_name
    def toString(self):
        print(f"Name: {self.name} ID: {self.course_id}")

class addStuffs:
    def getInfo(self):
        self.student_name = input("Enter student name: ")
        self.id = input("Enter student id: ")
        self.dob = input("Enter student date of birth: ")
    Student[id] = Student(student_id,name,dob)
    
    def getInfo(self):
        self.name = input("Enter the course name: ")
        self.id = input("Enter the course id: ")
    course[self.id] = Course(self.id,self.name)

class addMarks:
    def addMarks(self):
        for student in Student.keys():
            x = int(input(f"Input mark for student id of {student}"))
            for x in range()




        

