import time
times = time.strftime('%H:%M:%S')
print("Current time is :",times)
hour = int(time.strftime('%H'))
if(0 <= hour <= 12):
    print("Good morning")
elif(12 <= hour <=17):
    print("Good afternoon")
else:
    print("Good Evening")





# 2nd code for time display
print("Enter your current time \n")
a = int(input("Hour : "))
b = input("Minutes : ")
c = input("Seconds : ")
print(a, ":", b, ":", c)
if(0 <= a <= 12):
    print("Good morning")
elif(12 <= a <=17):
    print("Good afternoon")
else:
    print("Good Evening")
