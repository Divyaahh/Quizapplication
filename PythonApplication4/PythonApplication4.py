print("Welcome to the quiz about online safety ! we got several questions to test your knowledge on online safety.")
print("You only got 3 lives in this quiz meaning if you get 3 wrong answers you wont be able to continue, so play carefully!")
lifes = 3
print("What is spam?")
Answer = input()
Answer1  = ("Malicious code that includes virus and worms that can infect computers")
Answer2 = ("Unwanted or unsolicited electronic messages")
Answer3 = ("Software that runs at startup designed to take control of your computer")
Answer4 = ("Security Prevention And Maintenance (S.P.A.M)")
if Answer == "Answer2":
    print("congrats you go it right")
else:
    print("sorry thats not right")
    lifes -= 1 
    print(f"you have {lifes} lifes left")
print("Harassment through the Internet that is rude and/or threatening is")
Answer = input()
Answer5 = ("cyberbullying")
Answer6 = (" feedback")
Answer7 = ("Having fun")
if Answer == "Answer5":
    print("Congrats you got that right")
else:
    print("sorry thats not right")
    lifes -= 1
    print(f"you have {lifes} lifes left")
print("Private conversations on the Internet always remain private.")
Answer = input()
Answer8 = ("True")
Answer9 = ("False")
if Answer == "Answer9":
    print("you are right!")
else:
    print("Sorry thats not right")
    lifes -= 1
    print(f"you have{lifes} lifes left")
if lifes>0:
    print(" What is Cyber Security?")
    Answer = input()
    Answer10 = ("Cyber Security provides security against malware")
    Answer11 =("Cyber Security provides security against cyber-terrorists")
    Answer12 = ("Cyber Security protects a system from cyber attacks")
    Answer13 = (" All of the mentioned")
    if Answer == "Answer13":
        print("You are right")
    else:
        print("sorry thats not right")
        lifes -= 1
        print(f"you have{lifes} lifes left")
if lifes>0:
    print("Which password is the strongest?")
    Answer = input()
    Answer14 = ("Elsa2004")
    Answer15 = ("abc123")
    Answer16 = ("IAmAGr8Guy!$%")
    if Answer == "Answer16":
        print("you are right!")
    else:
        print("sorry that not right")
        lifes -= 1
if lifes>0:
    print("Which of these is classed as personal information?")
    Answer = input()
    Answer17 = ("Gender")
    Answer18 = ("Date of birth")
    Answer19 = ("online nickname")
    if answer == "Answer18":
        print("You are right")
    else:
        print("sorry thats not right")
        lifes -= 1
if lifes>0:
    print("What name would you give to an email attachment that may harm your computer?")
    Answer = input()
    Answer20 =("phishing")
    Answer21 = ("Malware")
    Answer22 = ("spam")
    if Answer == "Answer21":
        print("Thats right!")
    else: ("Sorry thats not right")
    lifes -= 1
if lifes>0:
    print("well done! you completed the quiz.")
else:
    print("you run out of lifes try again")