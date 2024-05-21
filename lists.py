
marks=[34,56,78]
name=["Pratham","Kush","Yash"]

for k in range(0,3):
    print(name[k], "=" ,marks[k] )

# list comprehension
names=["Pratham","Kush","Yash","Parshw"]
name4=[lst+lst for lst in names if "u" in lst]
print(name4)