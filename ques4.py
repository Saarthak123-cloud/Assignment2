a=input('Enter the number')
b=input('Enter the number')
c=input('Enter the number')
d=0
if (a>b)&(b>c):
    d=a
elif (b>a)&(b>c):
    d=b
elif c>b:
    d=c
print('Greatest number is',d)