class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Empolyee(Person):
    def __init__(self,name,age,empolyee_ID):
        super().__init__(name,age)
        self.empolyee_ID=empolyee_ID
class Student(Person):
    def __init__(self,name,age,student_ID):
        super().__init__(name,age)
        self.student_ID=student_ID
    def display(self):
        print(f"Name : {self.name}\n, Age: {self.age}\n,Student : {self.student_ID}\n")    
person=Student('Vansh',21,'djdjj')  
person.display()             
            