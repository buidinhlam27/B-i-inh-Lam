students = {}
courses = {}

def add_student(students):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    students[student_id] = {"name": name, "dob": dob, "transcript": {}}

def add_courses(courses):
    course_id = input("Enter the course ID: ")
    course_name = input("Enter the name of the course: ")
    courses[course_id] = {"course_id": course_id, "course_name": course_name}

def add_mark(students, courses):
    for student_id in students.keys():
        print(f"Enter the transcript for the following courses for student ID {student_id}:")
        for course_id in courses.keys():
            point = int(input(f"Enter the mark for course ID {course_id}: "))
            students[student_id]["transcript"][course_id] = point

def get_info(students):
    x = int(input("How many students: "))
    for _ in range(x):
        add_student(students)

def get_courses(courses):
    y = int(input("How many courses: "))
    for _ in range(y):
        add_courses(courses)

get_courses(courses)
get_info(students)
add_mark(students, courses)
for student_id, student_info in students.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {student_info['name']}")
    print(f"Date of Birth: {student_info['dob']}")
    print("Transcript:")
    for course_id, mark in student_info["transcript"].items():
        print(f"Course ID: {course_id}, Mark: {mark}")
    print()