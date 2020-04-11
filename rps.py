import random

rock = 'R'
paper = 'P'
scissor = 'S'

li = [rock, paper, scissor]


def computer_choice():
    comp_choice = random.choice(li)
    return comp_choice


def user_choice():
    choice = input("Select: \n R -> Rock\n P -> Paper \n S -> Scissor \n")
    try:
        selection = [item for item in li if item == choice.upper()]
        return selection[0]
    except:
        'Please enter the correct value.'


comp = computer_choice()
user = user_choice()


def play_rps():
    game_on = True

    while game_on:
        print(f'Computer chose {comp} and the user chose {user}')
        if comp == user:
            print('Its a draw.')
            game_on = False
        elif comp == rock and user == paper:
            print('User has won.')
            game_on = False
        elif comp == paper and user == scissor:
            print('User has won.')
            game_on = False
        elif comp == scissor and user == rock:
            print('User has won.')
            game_on = False
        else:
            print("The computer has won.")
            game_on = False


play_rps()
