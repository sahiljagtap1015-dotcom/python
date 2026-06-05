try :
    num = int(input("enter number :"))

    if num > 0:  
        print (1)

    elif num < 0: 
         print (-1)

    else : 
         print (0)

except ValueError : 
    print ("Invalid")  