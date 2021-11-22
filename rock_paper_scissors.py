import os
import random as r
os.system("clear")

user_rounds = int(input("How many rounds do you play? "))

DASHES = "-" * 15

for i in range(user_rounds):
    print(DASHES)
    user_choice = input("Enter rock [r] paper [p] scissors [s]: ")

    choices = ["r", "p", "s"]

    ai_choice = r.choice(choices)

    if user_choice in choices:
        print(DASHES)
        print(f"Your choice: {user_choice}\tAI choice: {ai_choice}")
        
        if user_choice == "r" and ai_choice == "s":
            print("You Win!")
        
        elif user_choice == "s" and ai_choice == "p":
            print("You Win!")

        elif user_choice == "p" and ai_choice == "r":
            print("You Win!")

        elif user_choice == ai_choice:
            print("Tie")

        else:
            print("You Lose")

    else:

        user_rounds += 1

        print(DASHES)
        print(""" Error !!!
        
        your wrong choice
        
        you must choice [r], [p], [s]
        
        """)