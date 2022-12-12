class Monthly_Payment:
    def __init__(self,fName,lName,experience,position,hourPayment,workedHours):
       self.fName=fName
       self.lName=lName
       self.experience=experience
       self.position=position
       self.hourPayment=hourPayment
       self.workedHours=workedHours

    def print(self):
        print(f'My name is {self.fName} {self.lName}, I work as a {self.position} and I have {str(self.experience)}'
              f' years of working experience. I get payed {str(self.hourPayment)}lv an hour.')
    def calculate_salary(self):
        return "Salary: "+str(self.workedHours*self.hourPayment)+"lv"

worker1=Monthly_Payment('Ivan','Ivanov',22,'Teacher',10,10)
worker1.print()
print(worker1.calculate_salary())