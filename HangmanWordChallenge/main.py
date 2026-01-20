import random
from hangman_words import word_list
import hangman_art

chosen_word=random.choice(word_list)
print(hangman_art.logo)
placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
game_over=False
correct_letters=[]
lives=6
display=placeholder
while not game_over:
    print("Word to guess : "+display)
    guess = input("Guess a letter : ").lower()
    if guess in correct_letters:
        print("You've already guessed " + guess)
    display = ""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    if guess not in display:
        print("You guessed "+guess+", that's not in the word. You lose a life.")
        lives-=1
    print(hangman_art.stages[abs(6-lives)])
    if lives!=0:
        print("****************************"+str(lives)+"/6 LIVES LEFT****************************")

    if lives==0:
        game_over=True
        print("****************************IT WAS "+chosen_word+". YOU LOSE.****************************")
    if "_" not in display:
        game_over=True
        print("YOU WIN!")

