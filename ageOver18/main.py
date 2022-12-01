while True:
    inp=input('Age: ')
    try:
        age = int(inp)
        if(age<0 or age>120) :
            raise Exception('Age must be between 0 and 120!')
    except ValueError as err:
        print('Age must be an integer number!')
    except Exception as err:
        print(err)



