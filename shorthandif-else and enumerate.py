# shorthand if else

a=330
b=30
print("A") if a>b else print("=") if a==b else print("B")
c = 9 if a>b else 0
print(c)

#enumerate function
marks=[23,45,67,98,67,78]

for index,mark in enumerate(marks,start=1):
    print(f"{index} : {mark}")
    if(index==4):
        print("Wow")