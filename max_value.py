# find the maximum value 

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

max = a

if b > max :
    max = b

if c > max :
    max = c

print ("maximum value = ", max )        