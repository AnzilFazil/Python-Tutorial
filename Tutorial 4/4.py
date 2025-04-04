class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def dataprint(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_no}")

# Creating two instances of Student
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)
s1.dataprint()
s2.dataprint()
