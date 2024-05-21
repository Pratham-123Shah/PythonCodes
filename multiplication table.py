#Multiplication table
a = int(input("Enter a number for which you have to print multiplication table :"))

for k in range(1,11):
 print(a ,"*",k, "=", a*k)



# using while loop
b = int(input("Enter a number for which you have to print multiplication table :"))

i=1
while(i<=10):
    print(b ,"*",i, "=", b*i)
    i=i+1