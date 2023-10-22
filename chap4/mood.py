import random 
print(" I sence your energy. Your true emotions are coming across my screen.")
print("You are...\n")
mood = random.randrange(3)
if mood == 0:
    print("--------------------\n")
    print("|                  |\n")
    print("| o           o    |\n")
    print("|                  |\n")
    print("|      <           |\n")
    print("|                  |\n")
    print("|  .           .   |\n")
    print("|   .         .    |\n")   
    print("|       . .        |\n")
    print("--------------------\n")

elif mood == 1:
    print("--------------------\n")
    print("|                  |\n")
    print("| o           o    |\n")
    print("|                  |\n")
    print("|      <           |\n")    
    print("|                  |\n")
    print("|                  |\n")
    print("|  ----------      |\n")
    print("|                  |\n")
    print("--------------------\n") 

elif mood == 2:
    print("--------------------\n")
    print("|                  |\n")
    print("| o           o    |\n")
    print("|                  |\n")
    print("|      <           |\n")
    print("|                  |\n")
    print("|      . .         |\n")
    print("|   .      .       |\n")
    print("|  ,        .      |\n")
    print("-------------------|\n")
else:
    print("Illegal mood value!")

print("...today.")
print("Press the enter key to quit")
