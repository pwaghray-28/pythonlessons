class Student(object):
    def __init__(self,gender,grades,name):
        self.name = name
        self.gender = gender
        self.grades = grades or {}
    def setgrade(self,course,grade):
        self.grade[course] = grade
    def getgrade(self,course):
        return self.grades[course]
    def getgpa(self):
        return sum(self.grades.values())/len(self.grades)
pradhi = Student("female",{"math":3.7,"science":3.8},"pradhi")
print(pradhi.getgpa())
