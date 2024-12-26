#
while True:

    import random
    options = ["rock","paper","scissors"]
    computer = random.choice(options)

    player= None
    while player not in options:

        player=input("rock,paper or scissors:").lower()
    print("computer:",computer)
    print("player:",player)

    if player == computer:
        print("Tie")

    elif player =="rock":
        if computer=="paper":
            print("You lose!")
        if computer=="scissors":
            print("You win")
    elif player == "paper":
        if computer=="scissors":
            print("You lose")
        if computer=="rock":
            print("You win")
    elif player == "scissors":
        if computer=="rock":
            print("You lose")
        if computer== "paper":
            print("You win ")
    play_again = input("Play Again?:").lower()
    if play_again != "yes":
        break
print("Bye")

#
# class Student :
#     def __init__(self , name , subject):
#         self.name = name
#         self.subject = subject
#
# s1=Student("shoaib","computer")
# s2 = Student("ahmed","mechical enginering")
# s3 =Student("talhaa",'medical')
# print("Name:",s1.name ,"\nSubject:",s1.subject)
# print("Name:",s2.name,"Subject:",s2.subject)
# print("Name:",s3.name,"Subject:",s3.subject)