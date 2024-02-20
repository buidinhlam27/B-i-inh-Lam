class Student:
    def __init__(self, student_id, student_name, dob):
        self.name = student_name
        self.student_id = student_id
        self.dob = dob
        self.transcript = {}

    def to_string(self):
        print(f"Name: {self.name} ID: {self.student_id} Date of birth: {self.dob}")


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.name = course_name

    def to_string(self):
        print(f"Name: {self.name} ID: {self.course_id}")


class AddStuffs:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def get_info(self):
        y = int(input("Enter the number of students: "))
        for _ in range(y):
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            dob = input("Enter student date of birth: ")
            self.students[student_id] = Student(student_id, name, dob)
            print()

    def get_info_course(self):
        t = int(input("Enter the number of courses: "))
        for _ in range(t):
            name = input("Enter the course name: ")
            course_id = input("Enter the course ID: ")
            self.courses[course_id] = Course(course_id, name)
            print()

    def add_mark(self):
        amount = int(input("Enter the amount of time you want to enter a mark: "))
        for i in range(amount):
            student_id = input("Enter student ID: ")
            course_id = input("Enter the course ID: ")
            mark = int(input("Enter the mark for the course: "))
            for studentid in self.students.keys():
                if studentid == student_id:
                    for courseid in self.courses.keys():
                        if course_id == courseid:
                            self.students[studentid].transcript[course_id] = mark
                            print("Mark added successfully.")
                            break
                    else:
                        print("Course not found.")
                    break
            else:
                print("Student not found.")

    def print_stuff(self):
        for student_id, student in self.students.items():
            print(f"Student ID: {student_id}")
            print(f"Student Name: {student.name}")
            print(f"Student DoB: {student.dob}")
            for course_id, course in self.courses.items():
                mark = student.transcript.get(course_id)
                if mark is not None:
                    print(f"Student mark for Course ID {course_id}: {mark}")
            print()


s = AddStuffs()
s.get_info()
s.get_info_course()
s.add_mark()
s.print_stuff()