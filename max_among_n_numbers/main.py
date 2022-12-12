import sys
n=int(input("How many numbers? "))
maxNumber=-100
sum=0

for x in range(n):
    a=int((input("number "+str(x+1)+": ")))
    sum+=a
    if a>maxNumber:
        maxNumber=a

#print("The maximal number is: "+str(maxNumber))
print("The sum is "+str(sum))