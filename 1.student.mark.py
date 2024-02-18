students = {}
courses = {}

def add_student():
    amount = int(input("Enter the amount of student that you want to add: "))
    for i in range(amount):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students[student_id] = {"name": name, "dob": dob, "marks": {}}

def add_course():
    amount = int(input("Enter the amount of course that you want to add: "))
    for i in range(amount):
        course_id = input("Enter the course ID: ")
        course_name = input("Enter the name of the course: ")
        courses[course_id] = {"name": course_name}

def add_mark():
    student_id = input("Enter student ID: ")
    course_id = input("Enter the course ID: ")
    mark = int(input("Enter the mark for the course: "))

    if student_id in students:
        if course_id in courses:
            students[student_id]["marks"][course_id] = mark
            print("Mark added successfully.")
        else:
            print("Course not found.")
    else:
        print("Student not found.")

def display_students():
    for student_id, student_info in students.items():
        print(f"ID: {student_id}, Name: {student_info['name']}, DoB: {student_info['dob']}")
        print("Transcript:")
        for course_id, mark in student_info["marks"].items():
            course_info = courses.get(course_id)
            if course_info:
                print(f"Course ID: {course_id}, Name: {course_info['name']}, Mark: {mark}")
        print()

def run():
    st = True
    while st:
        amount = int(input("Enter the amount time that you want to add marks: "))
        for i in range(amount):
            add_mark()
        end = input("Do you want to add more mark(Enter 1 for yes, 0 for no): ")
        if(end == "1"):
            st = True
        if(end == "0"):
            st = False 



add_student()
add_course()
run()   
display_students()