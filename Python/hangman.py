from hangmanwords import words

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']                   
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
def checkguess(word):
    life=6
    empty=['_' ]*len(word)
    word=word.upper()
    end = False
    while not end:
        guess=input("Guess the letter :").upper()
        for i in range(len(word)):
            if(word[i]==guess):
                empty[i]=word[i]
        if guess not in word:
            life-=1
            print(stages[life])
            print(f"try again {life} life left ")
        print(empty)
        if '_' not in empty:
            end=True 
            print("you win")
            break
        elif life==0:
            end=True
             

comp=random.choice(words)
checkguess(comp)
print(f"The word is {comp}")




    
        

