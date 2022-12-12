class Person:
    def __init__(self,firstName,lastName,age,nationality):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.nationality=nationality

    def printInfo(self):
        print("I am",self.firstName,self.lastName,"and I am",self.nationality)

person1=Person("Ivan", "Ivanov", 22, "Bulgarian")
person2=Person("Petar","Petrov",46,"Canadian")
person1.printInfo()
person2.printInfo()

class Student(Person):
    def __init__(self, firstName, lastName, age, nationality,university,yearOfGraduation):
       super().__init__(firstName,lastName,age,nationality)
       self.university=university
       self.yearOfGraduation=yearOfGraduation

    def printInfo(self):
        print("I am", self.firstName, self.lastName, ",",self.nationality,"student from",self.university,"and I will graduate in", str(self.yearOfGraduation))

student1=Student("Maria", "Petrova", 22, "Bulgarian","TU Sofia",2028)
student1.printInfo()