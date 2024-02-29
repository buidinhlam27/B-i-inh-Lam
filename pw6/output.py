import domains 
class Output:
    def printStuff(self,Students):
        print()
        for i in range(len(Students)):
            print(f"Student id: {Students[i].student_id}")
            print(f"Student name: {Students[i].name}")
            print(f"Student dob: {Students[i].dob}")
            for course in Students[i].transcript.keys():
                print(f"Student mark for course {course}: {Students[i].transcript[course]}")
            print(f"Student's gpa: {Students[i].gpa}")
            print()
        print(Students[0].name,Students[1].name)
