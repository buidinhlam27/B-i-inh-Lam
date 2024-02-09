import math
import numpy as np

Students = []
Courses = []

class Student:
    def __init__(self, student_id, student_name, dob):
        self.name = student_name
        self.student_id = student_id
        self.dob = dob
        self.transcript = {}
        self.gpa = 0

    def toString(self):
        print(f"Name: {self.name} ID: {self.student_id} Date of birth: {self.dob}")

class Course:
    def __init__(self, course_id, course_name, etcs):
        self.course_id = course_id
        self.name = course_name
        self.credit = etcs

    def toString(self):
        print(f"Name: {self.name} ID: {self.course_id} Amount of credits: {self.course_id}")

class addStuffs:
    def getInfo(self):
        y = int(input("Enter the amount of students: "))
        for i in range(y):
            name = input("Enter student name: ")
            id = input("Enter student id: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            Students.append(student)
            print()

    def getInfoCourse(self):
        t = int(input("Enter the amount of courses: "))
        for i in range(t):
            name = input("Enter the course name: ")
            courseId = input("Enter the course id: ")
            etc = int(input("Enter the amount of etcs: "))
            course = Course(courseId, name, etc)
            Courses.append(course)
            print()

    def addMarks(self):
        for student in Students:
            print(f"Input marks for student id {student.student_id}")
            for course in Courses:
                x = int(input(f"Mark for course id {course.course_id}: "))
                student.transcript[course.name] = x
            print()
    def printStuff(self):
        for student in Students:
            print(f"Student id: {student.student_id}")
            print(f"Student name: {student.name}")
            print(f"Student dob: {student.dob}")
            for course in Courses:
                print(f"Student mark for course {course.name}: {student.transcript[course.name]}")
            print(f"Student's gpa: {student.gpa}")
            print()

    def getGpa(self):
        for student in Students:
            a = 0
            totalamount = 0
            for course in Courses:
                a += (student.transcript[course.name] * course.credit)
                totalamount += course.credit
            student.gpa = math.floor((a / totalamount))

def insertion_sort():
    for i in range(1, len(Students)):
        key_item = Students[i].gpa
        j = i - 1
        while j >= 0 and Students[j].gpa < key_item:
            Students[j + 1] = Students[j]
            j -= 1
        Students[j + 1].gpa = key_item

s = addStuffs()
s.getInfo()
s.getInfoCourse()
s.addMarks()
s.getGpa()
s.printStuff()

#Since adding items to numpy to array is quite complicated i used the python array first then convert it to numpy array
Students = np.array(Students)
Courses = np.array(Courses)

insertion_sort()
s.printStuff()