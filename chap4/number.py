import random
count = 0
print("             Welcome to 'Guess My Number'!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")
c = random.randrange(1,100)

while(1):
   
    g = int(input("Take a guess: "))    
    count = count + 1
    print(c)
 
    if c < g:
             print("Higher...")
             continue
             
    elif c > g:
             print("Lower...")
             continue
    else:
              print("You guessed it! The number was ",c)
              print("And it only took you",count ," tries!")
              break

       

print("Press the enter key to quit.")
