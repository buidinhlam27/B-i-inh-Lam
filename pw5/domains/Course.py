class Course:
    def __init__(self, course_id, course_name, etcs):
        self.course_id = course_id
        self.name = course_name
        self.credit = etcs

    def toString(self):
        print(f"Name: {self.name} ID: {self.course_id} Amount of credits: {self.course_id}")