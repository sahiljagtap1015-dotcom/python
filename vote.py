age = int(input("Enter Age: "))
gender = input("Enter Gender (male/female): ")

if age >= 18 and gender == "male":
    print("My age is", age, "I am male. eligible for vote")

elif age >= 18 and gender == "female":
    print("My age is", age,"I am female. eligible for votee")

elif age < 18 and gender == "male":
    print("My age is", age,"I am male. not eligible for vote")

elif age < 18 and gender == "female":
    print("My age is", age,"I am female. not eligible for vote")

else:
    print("Invalid ")  
 
         
        