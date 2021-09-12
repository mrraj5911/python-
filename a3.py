class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('hlo',self.name)
        print('your marks are', self.marks)
    def grade(self):
        if self.marks>=70:
            print("you got ist grade")
        elif self.marks>=60:
            print("you got 2nd grade")
        elif self.marks>=50:
            print("you got 3rd position")
        else:
            print("you got last position")
a=int(input("enter the number of student: "))
for i in range(a):
    name=input("enter the student's name: ")
    marks=int(input("enter the student marks: "))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()