import random
print("Guess the Word!!!")
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")
words = ('difficult','banana','apple','python','daegu','catholic','unniversity')
wordlist = list(words)
random_word = random.choice(wordlist)
print("Length of the selected word: ",len(random_word))
count = 3

guess_word = list("_"*len(random_word))

while count >= 0:
    print("Remaining attempts: ",count)

    print("Current Guessd word: "," ".join(guess_word))

    guess = input("Guess a letter: ")
    if guess in random_word:    
        for i in range(len(random_word)):
            if random_word[i] == guess:

                guess_word[i] = guess
        if "".join(guess_word) == random_word:        
            print("Congratulation! You guessed the word: ",random_word)
            break

 
    else:
        print("Incorrect guess.")
        count -= 1
    
    if count == 0:
        print("You've used up all your attempts. The correct word was python.")
        break;
    
