# Fibonacci sequence
def recurse(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return  recurse(n-1) + recurse(n-2)
for k in range(1,11):
    print(recurse(k),end=",")
