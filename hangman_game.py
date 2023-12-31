import random
import hangman_stages

word_list=["apple", "beautiful", "potato"]
chosen_word=random.choice(word_list)

print(chosen_word)
display=[]
lives = 6 # lives initialized

for i in range(len(chosen_word)): #1 2 3 4 5
    display += '_'
print(display)

game_over = False
while not game_over:

    guessed_letter = input("Guess a letter:").lower() #x
    for position in range(len(chosen_word)): #0 1 2 3 4
        letter =chosen_word[position]
        if letter == guessed_letter: #p == x
            display[position] = guessed_letter
    print(display)
    
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!!")        

    if '_' not in display:
        game_over = True
        print("You win!!")
        print(hangman_stages.stages[lives])
