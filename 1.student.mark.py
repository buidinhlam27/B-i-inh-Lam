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
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Mark")
        print("4. Display Students")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            add_mark()
        elif choice == '4':
            display_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

run()   
display_students()