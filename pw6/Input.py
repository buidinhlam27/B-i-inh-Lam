from domains.Student import Student
from domains.Course import Course
import math
import os
import pickle as pkl

class Input:
    def __init__(self,Students,Courses):
        self.Students = Students
        self.Courses = Courses
    
    def getInfo(self):
        y = int(input("Enter the amount of students: "))
        for i in range(y):
            name = input("Enter student name: ")
            id = input("Enter student id: ")
            dob = input("Enter student date of birth: ")
            student = Student(id, name, dob)
            self.Students.append(student)
            print()
        with open("students.txt","w+") as f:
            for student in self.Students:
                f.write(f"Name: {student.name} \n")
                f.write(f"Student id: {student.student_id} \n")
                f.write(f"Student's DOB: {student.dob} \n")
                f.write("\n")
    
    def getInfoCourse(self):
        t = int(input("Enter the amount of courses: "))
        for i in range(t):
            name = input("Enter the course name: ")
            courseId = input("Enter the course id: ")
            etc = int(input("Enter the amount of etcs: "))
            course = Course(courseId, name, etc)
            self.Courses.append(course)
            print()
            try:
                with open("courses.txt","w") as f:
                    for course in self.Courses:
                        f.write(f"Name: {course.name} \n")
                        f.write(f"Course's id: {course.course_id} \n")
                        f.write(f"Course's etcs: {course.credit} \n")
                        f.write(f"\n")
            except IOError:
                print("0")
                
    def addMarks(self):
        amount = int(input("Enter the amount of time you want to enter a mark: "))
        for i in range(amount):
            studentid = input("Enter student ID: ")
            courseid = input("Enter the course ID: ")
            mark = float(input("Enter the mark for the course: "))
            for student in self.Students:
                if student.student_id == studentid:
                    for course in self.Courses:
                        if course.course_id == courseid:
                            student.transcript[course.course_id] = mark
                            print("Mark added successfully.")
                            break
                    else:
                        print("Course not found.")
                    break
            else:
                print("Student not found.")
    
    def getGpa(self):
        for student in self.Students:
            a = 0
            totalamount = 0
            for course in student.transcript.keys():
                couretcs = 0
                for cour in self.Courses:
                    if course == cour.course_id:
                        couretcs = cour.credit
                        break
                a += (student.transcript[course] * couretcs)
                totalamount += couretcs
            if totalamount == 0:
                student.gpa = 0
            else:
                student.gpa = math.floor((a / totalamount))

    # def conversion(self):
    #     self.Students = np.array(self.Students,dtype = object)
    #     self.Courses = np.array(self.Courses,dtype = object)
    
    def insertion_sort(self):
        for i in range(1, len(self.Students)):
            key_item = self.Students[i].gpa
            j = i - 1
            while j >= 0 and self.Students[j].gpa < key_item:
                self.Students[j + 1] = self.Students[j]
                j -= 1
            self.Students[j + 1].gpa = key_item
    
    # def zipping(self):
    #     try:
    #         with zipfile.ZipFile('students.dat','w') as z:
    #             z.write('Students.pickle')
    #             z.write('"Courses.pickle"')
    #     except Exception as e:
    #         print(str(e))

    def pickling(self):
        with open("Students.pickle","wb") as f:
            pkl.dump(self.Students,f)
        with open("Courses.pickle","wb") as fi:
            pkl.dump(self.Courses,fi)
        
    def depickling(self):
        # if os.path.exists("students.dat"):
        #     try:
        #         with zipfile.ZipFile('students.dat','r') as unz:
        #             unz.extractall()
        #     except Exception as e:
        #         print(str(e))
        #     print("File students.dat does exist")
        # else: 
        #     print("Does not exist")
        with open("Students.pickle","rb") as f:
            self.Students = pkl.load(f)
        with open("Courses.pickle","rb") as fi:
            self.Courses = pkl.load(fi)
