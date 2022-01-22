import random

import  Hangman_words



gnenrated_word=[]
gnenrated_word[:0]=random.choice(Hangman_words.word_list)
#gnenrated_word=lower(gnenrated_word)

state=[''' 
  +---+
  |   |
      |
      |
      |
      |
=========''',

''' 
  +---+
  |   |
  O   |
      |
      |
      |
=========''',

''' 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',

''' 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',

''' 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',

''' 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',

''' 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''' ]


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''                  

user_word=[]
print(logo)

for letter in gnenrated_word:
    user_word.append('_')

total_attempt=0

print(' '.join(user_word))

print("\nGuess the above Word")
#print(gnenrated_word)

sub=0
while user_word!='_':
    user_input=input("Please enter your letter:")
    mismatch=0

    if user_input in user_word :   
            print("You enter the same letter again")

    
    for i in range(0,len(gnenrated_word)):     
        if user_input==gnenrated_word[i]:
            user_word[i]= user_input       
            print(' '.join(user_word))
            print("\n\n\n")
        else:
            mismatch+=1  
    
    if mismatch==len(gnenrated_word):
        sub+=1
        print(f"Your Guess {user_input} is Wrong")
        print("Total remaining attempts:\t",7-sub)
        print(state[sub-1])
        
        if sub==7:
            print("Game Over...")
            break
        
    elif mismatch==0:
        continue

    hypens=0
    for letter in user_word:
        if letter=='_':
            hypens+=1
    #print(hypens)
    if hypens==0:
        print("You've guessed the word: ")
        print(' '.join(user_word))
        break
    
    else:
        continue


            


