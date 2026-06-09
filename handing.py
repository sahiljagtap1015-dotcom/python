# Writing data into file

file = open(r"C:\Users\VS\OneDrive\Desktop\handing\my_ file .txt", "w")

file.write(" Bharat mata ki jay .... \n ")

file.write(" Ram Ram Maharashtra \n ") 

file.close()

# Reading data from file

file = open(r"C:\Users\VS\OneDrive\Desktop\handing\my_ file .txt", "r")

data = file.read()

print("File Content:")
print(data)

file.close()

# Append data 

file = open(r"C:\Users\VS\OneDrive\Desktop\handing\my_ file .txt", "a")

file.write(" 15 - 08 -1947 \n")


file.write(" 01 - 05 - 1960 \n ")

file.write(" sawarkar \n ")

file.write(" 28 - 05 - 1883 \n ")

file.close() 