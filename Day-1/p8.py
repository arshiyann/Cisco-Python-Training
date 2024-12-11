pin = "1234"

i=0
while i<3:
    inpin = input("Enter Your Pin: ")
    if inpin == pin:
        print("transaction Successfull")
        break
    elif i >2 and inpin != pin:
        print("Your Card is Blocked")
    i +=1 
