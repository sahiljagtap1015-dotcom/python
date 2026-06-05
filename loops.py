# Loops in Python - while & for loop 

# while loop 

count = 0 

while count < 5: #condition 
    print(count)
    count = count + 1

print( )
print ()


# print numbers from 1 to 5 using while loop
count = 1 
while count < 6: #condition 
    print(count)
    # count = count + 1
    count += 1 

print ()
print ()


count = 5 
while count > 0: #condition 
    print(count)
    # count = count + 1
    count -= 1 
else:
    print("while loop ended")

print ()
print ()

# while True:
#     print("again and again!!") 
# check conditions to avoid infinite loop


#for loop 

language = 'Python' # sequence 

for x in language:
    print(x) 

print ()
print ()

# range function
# range(stop)
# range(start, stop)
# range(start, stop, step)

for i in range(5):  # stop argument
    print(i)
print ()
print ("range function ") 
print ()

for i in range(5,10):     # start, stop argument
    print(i)
print ()
print ("range start ")
print ()

for i in range(1,10,3):  # start, stop, step argument
    print(i)

print ()
print ("range stop ")
print ()


for i in range(5):
    print(i)
else:
    print("for loop ended")

print () 
