# Lambda function to find square
print() 

square = lambda x: x * x
print("Square of 252 =", square(252))

print() 

# Lambda function to add two numbers
add = lambda a, b: a + b
print("Addition of 10 and 20 =", add(10, 20))

print() 

# List of numbers
# Using lambda with filter() to get even numbers 

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers =", even_numbers)

print() 

# Student data
# Using lambda with sorted() 
students = [
    ("Ram", 80),
    ("Shyam", 95),
    ("Madhav", 70)
] 

sorted_students = sorted(students, key=lambda x: x[1])

print("Students Sorted by Marks =", sorted_students) 

print() 




