n=int(input("n= "))
isPrime:bool=True
for x in range(2,int(n/2)+1):
    if(int(n%x)==0):
        isPrime=False
        break

if(isPrime):
    print(str(n)+" is a Prime number.")
else:
    print(str(n)+" is not a Prime number.")