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
# person1.printInfo()
# person2.printInfo()

class Student(Person):
    def __init__(self, firstName, lastName, age, nationality,university,yearOfGraduation):
       super().__init__(firstName,lastName,age,nationality)
       self.university=university
       self.yearOfGraduation=yearOfGraduation

    def printInfo(self):
        print("I am", self.firstName, self.lastName, "and I am a",self.nationality,"student from",self.university,"and I will graduate in", str(self.yearOfGraduation))

student1=Student("Maria", "Petrova", 22, "Bulgarian","TU Sofia",2028)
#student1.printInfo()

class Lecturer(Person):
    def __init__(self, firstName, lastName, age, nationality,university,experience):
       super().__init__(firstName,lastName,age,nationality)
       self.university=university
       self.experience=experience

    def printInfo(self):
        print("I am", self.firstName, self.lastName, "and I am a", self.nationality, "lecturer from", self.university,
              "and I have", str(self.experience),"years of experience")

lecturer1=Lecturer("Doan", "Pavlov", 43, "Indian","TU Sofia",6)
# lecturer1.printInfo()

lecturers=[]
for x in range(5):
    print('Lecturer ',x+1)
    newLecturer=Lecturer(input("First name: "),input("Second name: "),
                         input("University: "),int(input("Age: ")),int(input("Years of experience:")))
    lecturers.append(newLecturer)
for x in lecturers:
     x.printInfo()