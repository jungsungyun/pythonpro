import random
print("Welccome to Word Jumble!")
print("Unscramble the letters to make a word.")
words = ('difficult','banana','apple','python','daegu','catholic','university')
a = random.choice(words)
b = list(a)
random.shuffle(b)


print("Jumbled word",''.join(b))


ip = input("Your guess:")
if ip == a:
    print("correct")
else:
    print("Sorry, that's not correct. The word was:",a)
