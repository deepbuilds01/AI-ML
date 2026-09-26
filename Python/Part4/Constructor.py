# // constructor

class Student:
    #  constructor
    def __init__ (self):
        print("hello Everyone!")

s1 = Student();




class Student:
    #  constructor
    def __init__ (self, name , ID):
        self.name = name
        self.ID = ID;
        print("hello Everyone!")

s1 = Student("DK",1234)
print(s1.name)

