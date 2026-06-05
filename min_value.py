# find the minimum value 

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

min = a

if b < min :
    min = b

if c < min :
    min = c

print ("minimum value = ", min )        