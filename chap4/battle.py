import random 

hp = random.randrange(50,100)
mp = random.randrange(50,100)

ha = random.randrange(-10,20)
ma = random.randrange(-10,20) 

    
    

if ha >  0:
    mp = mp - ha
elif ma > 0:
    hp = hp - ma



while hp > 0 and mp >  0:

    if ha >= 1:
        hs = print("sucess")
        
        else
            hs = print("false")
    if ma >= 1:
        ms = print("sucess")
        else
            ms = print("false")



        print("hero(HP:", hp," attack:",ha,") ",hs,"<-> monster(Hp:"),mp," attack:",ma,") ",ms)

print("-----------------------------------------------------------------------------------------")

print("Total phase: ",)
if hp == 0:
    print("Monster win!!!!")
else mp ==0:
    print("Hero win!!!")

