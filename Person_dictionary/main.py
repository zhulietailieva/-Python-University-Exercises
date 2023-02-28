class Person():
    def __init__(self,firstName):
        self.firstName=firstName
        self.characteristics=dict()

    def set_char(self,key,value):
        self.characteristics[key]=value

    def print_info(self):
        print(self.firstName+': ')
        for c in self.characteristics:
            print(c)


person1=Person('Ivan')
person2=Person('Maria')
person3=Person('Yoan')
people=dict()
people[f'{person1.firstName}']=person1.characteristics
people[f'{person2.firstName}']=person2.characteristics
people[f'{person3.firstName}']=person3.characteristics

for p in people:
    hair=input('Choose hair(straight/curly): ')
    eyes=input('Choose eyes(blue/brown): ')
    sex=input('Choose hair(male/female): ')
    height=input('Choose hair(tall/short): ')
    weight=input('Choose hair(slim/overweight): ')
    p.se





person1.print_info()

