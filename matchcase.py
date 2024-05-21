
#match case
x=int(input("Enter the number between 0-50"))

match x:
    case _ if 0 <= x < 10:
        print("Number is between 0 to 10")
    case _ if 10 <= x < 20:
        print("Number is between 10 to 20")
    case _ if 20 <= x < 30:
        print("Number is between 20 to 30")
    case _ if 30 <= x < 40:
        print("Number is between 30 to 40")
    case _ if 40 <= x < 50:
        print("Number is between 40 to 50")
    case _ if x==60 or x==90:
        print("number is",x)




