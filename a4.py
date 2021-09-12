class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
a=int(input("enter the total students: "))
for i in range(a):
    a=Student()
    name=input("enter the student name: ")
    a.setName(name)
    marks=int(input("enter the marks: "))
    a.setName(marks)
    print("hello",a.getName())
    print("marks are",a.getMarks())
    print()