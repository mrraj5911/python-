class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("hlo",self.name)
        print("your marks are: ", self.marks)
    def grade(self):
        if marks>=70:
            print("you got A grade")
        elif marks>=60:
            print("you got B grade")
        elif marks>=50:
            print("you got C grade")
        else:
            print("your position is low")
a=int(input("enter the total students: "))
for i in range(a):
    name=input("enter hte name: ")
    marks=int(input("enter the marks: "))
    c=Student(name,marks)
    c.display()
    c.grade()
    print()