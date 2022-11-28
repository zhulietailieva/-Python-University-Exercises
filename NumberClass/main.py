class Num:
    def __init__(self,numbers):
        self.numbers=numbers
    def printNumbers(self):
        print(self.numbers)

num1=Num([1,2,3,4])
num2=Num([3])
num1.printNumbers()
num2.printNumbers()

def thirdNumber(num1,num2):
    nums1=num1.numbers
    nums2=num2.numbers

    res=[]
    if(len(nums1)!=len(nums2)):
        difference=abs(len(nums1)-len(nums2))
        print(difference)
        if(len(nums1)>len(nums2)):
            for x in range(len(nums2)):
               res.append(nums1[x]+nums2[x])
            


thirdNumber(num1,num2)