class Person:
    def __init__(self,firstName):
        self.firstName=firstName
        self.characteristics=[self.hair,self.eyes,self.sex,self.weight,self.height]
        # self.eyes=''
        # self.hair=''
        # self.sex=''
        # self.weight=''
        # self.height=''

    def set_hair(self,hair):
        self.hair=hair

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_sex(self, sex):
        self.sex = sex

    def set_height(self, height):
        self.height = height

    def set_weight(self, weight):
        self.weight = weight

    def is_complete(self):
        if(self.hair=='' or self.eyes=='' or self.sex=='' or self.height=='' or self.weight==''):
            return False
        return True

    def print_info(self):
        if(self.hair!=''):
            print(f'This person has {self.hair} hair.')
        if (self.eyes != ''):
            print(f'This person has {self.eyes} eyes.')
        if (self.sex != ''):
            print(f'This person is a {self.sex}.')
        if (self.height != ''):
            print(f'This person is {self.height}.')
        if (self.weight != ''):
            print(f'This person is {self.weight}.')


person=Person('Ivan')
people=dict()
people[f'{person.firstName}']=person.characteristics
print(people)

while not(person.is_complete()):
    num = int(input(f'Choose a number between 1 and 5 for {person.firstName}: '))

    if (num == 1):
        type = input('Choose hair(straight/curly): ')
        if (type == 'straight'):
            person.set_hair('straight')
        elif (type == 'curly'):
            person.set_hair('curly')

    elif (num == 2):
        type = input('Choose eyes(blue/brown): ')
        if (type == 'blue'):
            person.set_eyes('blue')
        elif (type == 'brown'):
            person.set_eyes('brown')

    elif (num == 3):
        type = input('Choose sex(male/female): ')
        if (type == 'male'):
            person.set_sex('male')
        elif (type == 'female'):
            person.set_sex('female')

    elif (num == 4):
        type = input('Choose height(tall/short): ')
        if (type == 'tall'):
            person.set_height('tall')
        elif (type == 'short'):
            person.set_height('short')

    elif (num == 5):
        type = input('Choose weight(slim/overweight): ')
        if (type == 'slim'):
            person.set_weight('slim')
        elif (type == 'overweight'):
            person.set_weight('overweight')

person.print_info()
