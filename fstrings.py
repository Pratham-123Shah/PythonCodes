# String formatting
a=49
b=True
c=49.9789
d="Pratham"
txt="Hi My name is {3} My marks are {2} age is {0}. Is it {1}?"
print(txt.format(a,b,c,d))

#fstrings
pxt=f"Hi My name is {d} My marks are {c: .2f} age is {a}. Is it {b}?"
print(pxt)
print("%.2f"%c)