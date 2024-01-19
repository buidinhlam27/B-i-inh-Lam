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
        y = int(input("Enter the amount of student: "))
        for i in range(y):
            name = input("Enter student name: ")
            id = input("Enter student id: ")
            dob = input("Enter student date of birth: ")
            student[id] = Student(id,name,dob)
            print()
    
    def getInfoCourse(self):
        t = int(input("Enter the amount of courses: "))
        for i in range(t):
            name = input("Enter the course name: ")
            courseId = input("Enter the course id: ")
            course[courseId] = Course(id,name)
            print()
    
    def addMarks(self):
        for students in student.keys():
            print(f"Input mark for student id of {students} ")
            for courses in course.keys():
                x = int(input(f"Mark for course's id {courses} "))
                student[students].transcript[courses] = x
            print()
    def printStuff(self):
        for students,student_info in student.items():
            print(f"Student id's {students}")
            print(f"Student name's {student_info.name}")
            print(f"Student dob's {student_info.dob}")
            for courses in course.keys():
                print(f"Student mark for course {student_info.transcript[courses]}")
            print()

s = addStuffs()
s.getInfo()
s.getInfoCourse()
s.addMarks()
s.printStuff()
