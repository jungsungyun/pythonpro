scores = [("Moe",1000),("Larry",1500)]

while(1):
    print("     High Scores Keeper\n")
    print("     0 - Quit")
    print("     1 - List Scores")
    print("     2 - Add a Score")

    choice = int(input("Choice: "))
    print("\n")
    if choice == 2:

        name = input("What is the player's name?: ")
        get = int(input("What score did the player get?: "))
        
        entry = (name, get)
        scores.append(entry)
    if choice == 0:
        break
    
    if choice == 1:
        print("High Scores\n")
        print("Name     SCORE")
        sortscore = sorted(scores,key = lambda x: x[1],reverse=True)
        for entry in sortscore:
            name, score = entry
            print(name, "\t",score)
            print("\n")
     
