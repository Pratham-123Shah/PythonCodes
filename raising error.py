a= input("Enter a number :")
if (a=="quit"):
     print("You quited")
elif(int(a)>6 and int(a)<78):
    print("Entered number is :",int(a))
else:
     raise ValueError("You entered not required number or string")