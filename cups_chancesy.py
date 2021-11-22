import os
import colorama
import random as r
from colorama.initialise import init
os.system("clear")

user_cups = int(input("how many cups: "))
user_chances = int(input("how many chances: "))

ai_chances = r.randint(1, user_cups)

STAR = "*" * 14
NUM = user_chances

for i in range(user_chances):
    print(STAR)
    print(f"your chance: {NUM}")
    user_choice = int(input(f"you can choice cups [1:{user_cups}]: "))
    print(STAR)
    NUM -= 1
    
    if user_choice == ai_chances:
        init()
        print(colorama.Fore.GREEN + "Your choice right")
        break
    
    else:
        init()    
        print(colorama.Fore.RED + "Your choice wrong")
    
print(
    """

THE END !!

""")