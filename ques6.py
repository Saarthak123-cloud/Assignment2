a=int(input("Enter first side"))
b=int(input('Enter seond side'))
c=int(input('Enter third side'))

if ((a>(b+c))|(b>(a+c))|(c>(b+a))):
    print("No")
else:
    print("Yes")
