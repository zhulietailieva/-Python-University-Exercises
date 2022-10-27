studentGrade=float(input("Student grade: "))
maxScholarship=float(input("Maximal scholarship: "))

studentScholarship=0.00
if studentGrade>=5.5:
    studentScholarship=maxScholarship
elif studentGrade>=5:
    studentScholarship=0.7*maxScholarship
elif studentGrade>=4.5:
    studentScholarship=0.5*maxScholarship

if studentScholarship==0:
    print("Student does not get scholarship this semester.")
else:
    print("Student scholarship for this semester is: "+str(studentScholarship))