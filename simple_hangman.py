from random import choice

words = ['car']
is_playing = True
tries = 3


def get_word(word_list):

    random_word = [letter for letter in choice(word_list)]
    secret_word = ['_' for letter in random_word]
    return secret_word, random_word


s_word, r_word = get_word(words)

while is_playing:

    print(s_word)
    user_input = input("Enter a letter: ")

    if user_input in r_word:
        idx = r_word.index(user_input)
        print(idx)
        s_word[idx] = user_input

        if s_word == r_word:
            print("You have guessed the word!")
            is_playing = False

    else:
        tries -= 1
        print(f'Letter not in word, tries left {tries}')

        if tries == 0:
            print("You lost the game!")
            is_playing = False


