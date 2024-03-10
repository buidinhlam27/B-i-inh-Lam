class Student:
    def __init__(self, student_id, student_name, dob):
        self.name = student_name
        self.student_id = student_id
        self.dob = dob
        self.transcript = {}
        self.gpa = 0

    def toString(self):
        print(f"Name: {self.name} ID: {self.student_id} Date of birth: {self.dob}")
