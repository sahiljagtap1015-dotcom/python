num1  = 52578
rev = 00

while num1  > 0:
    digit = num1 % 10      
    rev = rev * 10 + digit
    num1 = num1  // 10       

print(rev)  


print ( "Palindrome Number")


num = int(input("Enter number: "))

temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number") 