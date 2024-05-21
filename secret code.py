print("Welcome to encoding and decoding program")
c=input("Enter  a string you want to encode or decode  :   ")
a=int(input("Enter 1 -> Encoding and Enter 2 -> Decoding\n"))
if(a==1):
    if(len(c)>=3):
      b=c[1:len(c)]
      print(f"adh{b}{c[0]}yut")
    else:
      c=c[::-1]
      print(c)
if(a==2):
    if(len(c)>=3):
        z=c[3:len(c)-3]
        v=z[len(z)-1]
        d=c[3:len(c)-4]
        print(f"{v}{d}")
    else:
        c=c[::-1]
        print(c)





