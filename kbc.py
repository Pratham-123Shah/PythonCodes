
Q = ["1) Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?",
     "2) Who, in 1978, became the first person to be born in the continent of Antarctica?",
     "3) Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 18, 1868?",
     "4) Who is the first woman to successfully climb K2, the world’s second highest mountain peak?",
     "5) Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?"]
A = ["A)Solicitor General B)Attorney General C)Cabinet Secretary D)Chief Justice",
     "A)Emilio Palma B)James Weddell C)James Weddell D)Charles Wilkes",
     "A)Belgium B)Italy C)Denmark D)France",
     "A)Junko Tabei B)Wanda Rutkiewicz C)Tamae Watanabe D)Chantal Mauduit",
     "A)Mir Taqi Mir B)Mohammad Ibrahim Zauq C)Zahir Dehlvi D)Abul- Qasim Ferdowsi"]
def kbc(a):
    print(Q[a],"\n")
    print(A[a],"\n")

def answers():
    k=int(input("Enter number '1' for 'A' '2' for 'B' '3' for 'C' '4' for 'D' :  "))
    if (k == 2):
        print("Right Answer. You Won 50,000 rupees")
        print("Second Question for you : \n")
        kbc(1)
        k = int(input("Enter number '1' for 'A' '2' for 'B' '3' for 'C' '4' for 'D' :  "))
        if (k == 1):
            print("Right Answer. You Won 1,00,000 rupees")
            print("Third Question for you : \n")
            kbc(2)
            k = int(input("Enter number '1' for 'A' '2' for 'B' '3' for 'C' '4' for 'D' :  "))
            if (k == 3):
                print("Right Answer. You won 5,00,000 rupees")
                print("Fourth Question for you : \n")
                kbc(3)
                k = int(input("Enter number '1' for 'A' '2' for 'B' '3' for 'C' '4' for 'D' :  "))
                if (k == 2):
                    print("Right Answer. You won 10,00,000 rupees")
                    print("Fifth and last Question for you : \n")
                    kbc(4)
                    k = int(input("Enter number '1' for 'A' '2' for 'B' '3' for 'C' '4' for 'D' :  "))
                    if (k == 3):
                        print("Right Answer. You won 20,00,000 rupees")
                        print("Your total prize money is 36,60,000")
                    else:
                        print("Wrong Answer. Your Total prize money is 16,60,000")
                else:
                    print("Wrong Answer. Your Total prize money is 6,60,000")

            else:
                print("Wrong Answer. Your Total prize money is 1,60,000 ")
        else:
            print("Wrong Answer. Your Total prize money is 60,000 rupees")
    else:
        print("Wrong Answer. Your Total prize money is 10,000 rupees ")


kbc(0)
answers()

