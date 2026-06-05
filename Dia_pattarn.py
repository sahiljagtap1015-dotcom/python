

rows = 5

for i in range(rows):
    print(" " * (rows - i - 1) + " 5 " * (i + 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + " 5 " * i)

print()
print() 
print ()

# ex.2 
n = 11

for i in range(1, n + 1):
    print(" " * (n - i) + " *       " * i)

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + " *       " * i) 