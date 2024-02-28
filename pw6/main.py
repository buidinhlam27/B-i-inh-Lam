from Input import Input
from output import Output
import domains
Students = []
Courses = []

New_input = Input(Students,Courses)
New_input.getInfo()
New_input.getInfoCourse()
New_input.addMarks()
New_input.getGpa()
New_input.conversion()
New_input.insertion_sort()
New_input.zipping()

toTer = Output(Students)
toTer.printStuff()

