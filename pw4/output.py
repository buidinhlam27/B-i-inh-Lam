import domains 
class Output:
    def __init__(self,Students):
        self.Students = Students
    def printStuff(self):
        for student in self.Students:
            print(f"Student id: {student.student_id}")
            print(f"Student name: {student.name}")
            print(f"Student dob: {student.dob}")
            for course in student.transcript.keys():
                print(f"Student mark for course {course}: {student.transcript[course]}")
            print(f"Student's gpa: {student.gpa}")
            print()
