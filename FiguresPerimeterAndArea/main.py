typeOfFigure = input("Chose type of figure (triangle,rectangle or square): ")
P = 0
S = 0
isACorrectFigure: bool = True
if typeOfFigure == "triangle":
    a = float(input("side a: "))
    b = float(input("side b: "))
    c = float(input("side c: "))
    P = a+b+c
    S = (a*b)/2
elif typeOfFigure == "rectangle":
    a = float(input("side a: "))
    b = float(input("side b: "))
    P = 2*(a+b)
    S = a*b
elif typeOfFigure == "square":
    a = float(input("side a: "))
    P = 4*a
    S = a*a
else:
    print("Figure is not correct.")
    isACorrFigure = False

if isACorrectFigure:
    print(f'{typeOfFigure}\nPerimeter: {P}\nArea: {S}')
