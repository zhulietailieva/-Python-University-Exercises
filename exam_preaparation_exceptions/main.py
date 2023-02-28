while True:
    try:
        n=int(input('n='))
        k=int(input('k='))
        break
    except ValueError as e:
        print('Invalid n or k! Try again')

list1=[]
list2=[]

for x in range (0,n):
    while True:
        try:
            a =int (input(f'number {x + 1}='))
            break
        except ValueError:
            print('Invalid input! Try again!')
    if(a>k):
        list1.append(a)
    else:
        list2.append(a)

print('List 1: ')
print(list1)

print('Multiplication of numbers with odd indexes:')
p=1
for x in range(0,len(list1)):
    if(x%2!=0):
        p=p*list1[x]

print(p)
print('The index of min element is:')
print(list1.index(min(list1)))

print('List 2: ')
print(list2)
print('Max_value element:')
max_value=max(list2)
print(max_value)
print('Min_value element:')
min_value=min(list2)
print(min_value)
print('Max_value - Min_value =',(max_value-min_value))






