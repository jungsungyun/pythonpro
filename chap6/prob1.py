inventory = ("sword","armor","shield","healing potion")
invenlist = list(inventory)
print("your item:")
for item in inventory:
    print(item)
print("\n")
print("Press the enter key to continue.\n")
print("You have ",len(invenlist),"items in your possession.\n")
print("\n")
print("Press the enter key to continue.")
if "healing potion" in inventory:
    print("You will live to fight anoter day.\n")
indexnum = int(input("Enter the index number for an item in inventory:"))
print("At index",indexnum,"is",invenlist[indexnum])
print("\n")
slc1 = int(input("Enter the index number to begin a slice:"))
slc2 = int(input("Enter the index number to end the slice:"))
print("invenlist[",slc1,":",slc2,"]                    ",invenlist[slc1:slc2])
print("\n")
print("Press the enter key to continue,")
print("You find a chest. It contains :")
chest = ("gold", "gems")
chestlist = list(chest)
print(chestlist)
print("You add the contents of the chest to your inventory.")
invenlist += chest
print("Your inventory is now:")
print(invenlist)
print("\n\n")
inventory2 = ("crossbow","armor","shield","healing potion","gold","gems")
invenlist2 = list(inventory2)
print("Press the enter key to continue.")
print("You trade your sword for a crossbow.")
print("Your inventory is now:")
print(invenlist2)
print("\n")
print("Press the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.")
del invenlist2[4:6]
invenlist2.append("orb of future telling")
print(invenlist2)
print("\n")
print("Press the enter key to continue.")
print("In a great battle, your shield is destroyed.")
print("Your inventory is now:")
del invenlist2[2]
print(invenlist2)
print("\n")
print("Press the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.")
print("Your inventory is now:")
del invenlist2[0:2]
print(invenlist2)
print("\n\n")
print("Press the enter key to exit.")







