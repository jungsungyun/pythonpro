import random 

hp = random.randrange(50,101)
mp = random.randrange(50,101)

count = 0
print("hero HP:",hp,", monster HP: ",mp)

while hp > 0 and mp > 0:
    ha = random.randrange(-10,21)
    ma = random.randrange(-10,21) 

    count = count + 1

    if ha <= 0:
        hs = "false"
    else:
        mp = mp - ha
        hs = "sucees"
    
    if  ma <= 0:
        ms = "false"
    else:
        hp = hp - ma
        ms = "sucess"



    print("hero(HP:", hp," attack:",ha,") ",hs,"<-> monster(Hp:",mp," attack:",ma,") ",ms)
    if hp <= 0 and mp <= 0:
        break
print("\n")
print("-----------------------------------------------------------------------------------------\n")

print("Total phase:",count)
if hp <= 0:
    print("Monster win!!!!")
else:
    print("Hero win!!!")
