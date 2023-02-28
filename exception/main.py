#list of 5 numbers between 50 100
list=[]
for x in range(0,5):
    while True:
        try:
            n=int(input('Input a number: '))
            if(n<50 or n>100) :
                raise AttributeError
            list.append(n)
            break
        except ValueError:
            print('You must enter an int number!')
        except AttributeError:
            print('Number must be between 50 and 100')
print(list)

