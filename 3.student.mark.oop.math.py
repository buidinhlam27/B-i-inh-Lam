import math
import numpy as np

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
    def __init__(self):
        self.Students = []
        self.Courses = []
    def getInfo(self):
        y = int(input("Enter the amount of students: "))
        for i in range(y):
            name = input("Enter student name: ")
            id = input("Enter student id: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.Students.append(student)
            print()

    def getInfoCourse(self):
        t = int(input("Enter the amount of courses: "))
        for i in range(t):
            name = input("Enter the course name: ")
            courseId = input("Enter the course id: ")
            etc = int(input("Enter the amount of etcs: "))
            course = Course(courseId, name, etc)
            self.Courses.append(course)
            print()

    def addMarks(self):
        amount = int(input("Enter the amount of time you want to enter a mark: "))
        for i in range(amount):
            studentid = input("Enter student ID: ")
            courseid = input("Enter the course ID: ")
            mark = float(input("Enter the mark for the course: "))
            for student in self.Students:
                if student.student_id == studentid:
                    for course_id in self.Courses:
                        if course_id.course_id == courseid:
                            student.transcript[course_id.course_id] = mark
                            print("Mark added successfully.")
                            break
                    else:
                        print("Course not found.")
                    break
            else:
                print("Student not found.")
    def printStuff(self):
        for student in self.Students:
            print(f"Student id: {student.student_id}")
            print(f"Student name: {student.name}")
            print(f"Student dob: {student.dob}")
            for course in student.transcript.keys():
                print(f"Student mark for course {course}: {student.transcript[course]}")
            print(f"Student's gpa: {student.gpa}")
            print()

    def getGpa(self):
        for student in self.Students:
            a = 0
            totalamount = 0
            couretcs = 0
            for course in student.transcript.keys():
                for cour in self.Courses:
                    if course == cour.course_id:
                        couretcs = cour.credit
                        break
                a += (student.transcript[course] * couretcs)
                totalamount += couretcs
            student.gpa = math.floor((a / totalamount))
    def conversion(self):
        self.Students = np.array(self.Students)
        self.Courses = np.array(self.Courses)
    
    def insertion_sort(self):
        for i in range(1, len(self.Students)):
            key_item = self.Students[i].gpa
            j = i - 1
            while j >= 0 and self.Students[j].gpa < key_item:
                self.Students[j + 1] = self.Students[j]
                j -= 1
            self.Students[j + 1].gpa = key_item


s = addStuffs()
s.getInfo()
s.getInfoCourse()
s.addMarks()
s.getGpa()
s.printStuff()

#Since adding items to numpy to array is quite complicated i used the python array first then convert it to numpy array
s.conversion()
s.insertion_sort()
s.printStuff()