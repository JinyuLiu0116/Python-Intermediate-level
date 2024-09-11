
class Student:

    classYear = 2024
    numOfStudents = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.numOfStudents +=1
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getNumOfStudents(self):
        return self.numOfStudents
    
s1 = Student("Drop", 30)
print(f"Student: {s1.getName()}")
print(f"Age: {s1.getAge()}")
print(f"The class has {s1.getNumOfStudents()} students")

s2 = Student("Rise", 40)
print(f"Student: {s2.getName()}")
print(f"Age: {s2.getAge()}")
print(f"The class has {s1.getNumOfStudents()} students")
