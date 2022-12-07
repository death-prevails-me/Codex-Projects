import math
choice =int(input('''
Please select the type of operation you want to perform:
1.Basic Calculation
2.Constant Values
3.Trigonometry
'''))
def addt(a,b):
    f=a+b
    return f
 
 
def subs(a,b):
    f=a-b
    return f
 
def prod(a,b):
    f=a*b;
    return f 
 
def div(a,b):
    f=a/b;
    return f
 
def divis(a,b):
    f=a%b;
    if f == 0:
        return "Divisible"
    else:
        return "Non Divisible"
 
if choice == 1:
    print("Please Select The Type\n")
    p=int(input('''1.Addition
2.Substraction
3.Multiplication
4.Division
5.Divisibility
6.Exponential'''))
    if p == 1:
        a=float(input("Enter Your Number:"))
        b=float(input("Enter Other Number:"))
        print("Result=",addt(a,b))
 
    elif p == 2:
        a=float(input("Enter Your Number:"))
        b=float(input("Enter Other Number:"))
        print("Result=",subs(a,b))
 
    elif p == 3:
        a=float(input("Enter Your Number:"))
        b=float(input("Enter Other Number:"))
        print("Result=",prod(a,b))   
 
    elif p == 4:
        a=float(input("Enter Your Number:"))
        b=float(input("Enter Other Number:"))
        print("Result=",div(a,b))
 
    elif p == 5:
        a=float(input("Enter Your Number:"))
        b=float(input("Enter Other Number:"))
        print("Result=",divis(a,b))
    elif p == 6:        
        a=float(input("Enter Your Number:"))
        b=float(input("Enter Other Number:"))
        print("Result=",math.pow(a,b))
 
    else:
        print("Error 404 Option Not Found")
 
 
elif choice == 2:
    print("Please Select The Value\n")
    p=int(input('''1.Eulers No.
2.Pi's Value
3.Tau's Value'''))
    if p == 1:
        print("Value Is :",math.e)
    elif p == 2:
        print("VAlue Is :",math.pi)
    elif p == 3:
        print("Value is:",math.tau)
    else:
        print("Error 404 Option Not Found")
 
elif choice == 3:
    print("Please Select The Value\n")
    p=int(input('''1.Degree To Trigonometry
2.Value to Degree\n'''))
    if p == 1:
        z=float(input("Enter Degree: \n"))
        print("Sin:",math.sin(z),"\n")
        print("Cos:",math.cos(z),"\n")
        print("Tan:",math.tan(z),"\n")
 
    elif p == 2:
        z=float(input("Enter Value: \n"))
        print("Sin:",math.asin(z),"\n")
        print("Cos:",math.acos(z),"\n")
        print("Tan:",math.atan(z),"\n")
    else:
        print("Error 404 Option Not Found")
        