import os
import random as r

os.system("clear")

def get_input_of_user():
    """Returns the input of word lower case with method isalpha"""
    while True:
        user_word = input("Enter your guess: ").lower()
        
        if user_word.isalpha():
            return user_word

        print("your input is not correct. please try again!")

def get_word_of_user(list_words):
    """This function returns a list of words with input user"""
    print("Hello !\nEnter your personalization words and use the (done) to exit the words entry")
    while True:
        word_user = input("Enter your word: ").lower()
        
        if word_user == "done":
            break
        else:
            if word_user.isalpha():
                list_words.append(word_user)   
            else:
                print("your input word invalid")
                continue

def get_input_from_words(words):
    """This is function for getting input from words -> list_words
    and if user_guess not in words or list_words infinit loop
    """
    user_guess = get_input_of_user()

    while user_guess not in words:
        print('your gussed is wrong and not of specified words')
        print('Please Enter correct word !!')

        user_guess = get_input_of_user()
    
    return user_guess


def print_info_game():
    """This function prints info and introduction game and show the user"""
    print("*" * 25)
    print("hey, welcome to the game guess")
    print(f"All words: {list_words}")
    print("please start gusses")
    print("*" * 25)


def settings_game(number_of_rounds, words):
    """This is the function for game settings:
    
    run print_info_game function ,, Deadline settings for the user
    
    Implement conditions
    """
    print_info_game()
    
    print(f"number of gusses: {number_of_rounds}")
    
    correct_word = r.choice(words)

    for i in range(number_of_rounds):

        user_guess = get_input_from_words(words)

        if user_guess == correct_word:
            print("YOU WON!")
            return
        else:
            print(f"your guess wrong\nnumber of round left : {number_of_rounds-1 - i}")

    print(f"YOU LOST!\ncorrect word: {correct_word}")

list_words = []

get_word_of_user(list_words)

settings_game(5, list_words)