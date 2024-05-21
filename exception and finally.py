'''def func1():
   try:
     l=[1,2,3,4]
     i=int(input("Enter index:"))
     print(l[i])
     return 1
   except:
    print("error")
    return 0

   finally:
    print("Hi")

print(func1())'''

try:
  a= input("Enter a number :")
  if (a=="quit"):
    print("You quited")
  if(int(a)>0 and int(a)<100):
      print("Entered number is between 0 t0 100")
except:
     print("Value error")