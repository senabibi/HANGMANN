#TODO-Randomly choose a word from the word_list and assiggn it to a variable called chosen_word.
#TODO-Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#TODO-Create an empty List called display.
#For each letter in chosen_word,add a "_" to 'display'.
#So if the chosen_word was "apple" display should be 
# ["_","_","_","_","_"] with 5 "_" representing each letter to guess.
#TODO-Ask the user to guess a letter and assign their answer to a variable called guess.Make guess lowercase.
#TODO-Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g.If the user guessed "p" and the chosen word was "apple",then display should be ["_","p","p","_","_"].
#TODO-Print 'display' and you should see the guessed letter in the correct position and every letter replace with "_".
#TODO-Use a while loop to let the user guess again.The loop should only stop oonce the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").Then you can tell the user they've won.
#TODO-Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
#TODO-If the guess is not a letter in the chosen_word,then reduce lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose".
#Join all the elements in the list and turn it into a String.

import random
from hangman_words import word_list 
from  hangman_art import logo

chosen_word=random.choice(word_list)
lives=6
print(logo)
display=[]
word_len=len(chosen_word)
for letter in range(word_len):
    display+="_"
end_of_game=False    
while not end_of_game: 
    guess=input("Guess a letter").lower()
    if guess in display:
        print(f"You 've already guessed {guess}")
    for position in range(word_len):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        print(f"You guessed {guess},that's not in the word.You lose a life.")

        lives-=1
        if lives==0:
            end_of_game=True
            print("LOSER!!!")
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game=True
        print("WINNER!!")
    from hangman_art import stages
    print(stages[lives])    
    
