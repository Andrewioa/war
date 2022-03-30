def hangman(word:str):
    '''
    Play the game hangman!
    :param word: the word you need the player to find.
    '''
    print('Welcome to hangman!')
    name = input('Enter your name: ')
    print(f'Good luck {name}! '
          f'Find the hidden word!')
    empty_word = ['_'] *len(word)
    print(empty_word)
    loses = 0
    words_not = []
    while True:


        print('Letters used{}'.format(words_not))
        letter=input('Choose a letter: ')
        if letter in word:
            print('{0} is in the word!!'.format(letter))
            x=word.index(letter)
            empty_word[x] = letter
            print(empty_word)
        else:
            print(f'{letter} is not in the word')
            print(empty_word)
            print(f'You have {5 - loses} more tries!')
            words_not.append(letter)
            loses+=1
        if loses > 5:
            print(f'You lose! The word was {word}!')
            break
        elif '_' not in empty_word:
            print(f'You win! You found the word {word}!')

        else:
            continue





hangman('penis')
