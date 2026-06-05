percentage = float(input ("enter percentage:"))
 
if percentage >= 0 and percentage <= 34 :
    print("Fail")

elif percentage == 35 :
    print("Pass")

elif percentage >= 36 and percentage <= 50 :
    print("Grade C")   

elif percentage >= 51 and percentage <= 75 :
    print("Grade B")

elif percentage >= 76 and percentage <= 100 :
    print("Grade A") 

else :
     print("invaild")      
