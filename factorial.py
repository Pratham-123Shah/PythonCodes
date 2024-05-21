a = int(input("Enter a number for which factorial to be found : "))
b=1

for k in range(a,0,-1):
    b = b * k
print(b)

# by using while loop
while(a>0):
    b=b*a
    a=a-1

print(b)