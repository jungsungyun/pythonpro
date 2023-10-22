import random

hangman = [
    """
    ----------
    :     |  
    :     
    :
    :
    :
    -----------"""
    ,
        """
    ----------
    :     |  
    :     o
    :
    :
    :
    -----------"""
    ,
        """
    ----------
    :     |  
    :     o
    :     |
    :
    :
    -----------"""
    ,
        """
    ----------
    :     |  
    :     o
    :   / |
    :
    :
    -----------"""
    ,
        """
    ----------
    :     |  
    :     o
    :   / | \\
    :
    :
    -----------"""
    ,
        """
    ----------
    :     |  
    :     o
    :   / | \\
    :    /
    :
    -----------"""
    ,
        """
    ----------
    :     |  
    :     o
    :   / | \\
    :    / \\
    :
    -----------"""
    
    ]
          
          
          
          
          

term = ["python","apple","banana"]
random_term = random.choice(term)
guess_word = ['-'] * len(random_term)
temp = 7
attemp = 0
guesslist = []


while attemp < temp:
    guess = input("Enter your guess: ")   
    print(hangman[attemp])  
    guesslist.append(guess)
    if guess in random_term:
        for i in range(len(random_term)):
            if random_term[i] == guess:
                guess_word[i] = guess
        print("Yes!",guess,"is in the word!")
        print("You've used the following letters:\n",(guesslist))
        print("\n")
        print("So far, the word is:")
        print("".join(guess_word))
        print("\n")
        if "-" not in guess_word:
            print("Congratulations! You guessed the word:", random_term)
            break    
    else:
        print("Does not exit.")
    
    
    
        
    attemp += 1
if "-" in guess_word:
    print("You are failed! The word is: ",random_term)
