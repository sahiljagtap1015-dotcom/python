# match case example 1 

home = int(input (" Enter home number :  "  ))

match home : 
    case 1 :
        print (" letter delivered to home 1. ")
        
    case 9 :
        print (" letter delivered to home 9 .")  

    case 50 :
        print (" letter delivered to home 50 .")      

    case 101 :
        print (" letter delivered to home 101. ")  

    case 5 :
        print (" letter delivered to home 67. ")   

    case 51 :
        print (" letter delivered to home 51. ")    

    case 150 :
        print (" letter delivered to home 150. ")

    case 199 :
        print (" letter delivered to home 199 .")

    case 2 :
        print (" letter delivered to home 2. ")

    case 200 :
        print (" letter delivered to home 200. ")

print ( ) 

    case _ :
        print ("No Letter ") 

print ( ) 

 # match case example 2  

payment = "Cash"

match payment:

    case "UPI":
        print("Pay using UPI")

    case "Debit Card":
        print("Pay using Debit Card")

    case "Credit Card" : 
        print("Pay using Credit Card")

    case "Cash":
        print("Cash on Delivery")

    case _:
        print("Invalid Option") 

print( ) 
