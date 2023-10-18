geek = {"404": "clueless.","Uninstalled": "being fired."}


while True:
    print("     Geek Translator\n")
    print("     0 - Quit")
    print("     1 - Look Up a Geek Term")
    print("     2 - Add a Geek Term")
    print("     3 - Redefine a Geek Term")
    print("     4 - Delete a Geek Term\n")
    choice = int(input("Choice: "))
    print("\n")
    
    if choice == 0:
        break

    if choice == 1:
        translate = input("What term do you want me to translate?: ")
        if translate in geek:
            print("\n")
            print(translate,"means",geek[translate],"Especially popular during the dot-bomb era.")
            print("\n")
        else:
            print("Does not exist")
    
    if choice == 2:
        addgeek = input("Add a Geek Term: ")
        geek[addgeek] = 0
        if "Dancing Baloney" in geek:
            print("I know what Dancing Baloney is.")
    
        else:
            print("I have no idea what Dancing Baloney is.")

    if choice == 3:
        redeterm = input("What term do you want redefine?: ")
        input(geek.get(redeterm,"what does Redefine mean?"))
        geek["Link Rot"] ="process by wich web page links become absolte."
        if redeterm in geek:
            print("Redefine is complete")
        else:
            print("Redefine is failed")

    if choice == 4:
        delterm = input("what is want to del term?")
        if delterm in geek:
            del geek[delterm]
            print("delete complete")
        else:
            print("delete failed")

