inventory = ("sword","armor","shield","healing potion")
print("your item:")
for item in inventory:
    print(item)
print("\n")
print("Press the enter key to continue.\n")
print("You have ",len(inventory),"items in your possession.\n")
print("\n")
print("Press the enter key to continue.")
if "healing potion" in inventory:
    print("You will live to fight anoter day.\n")
indexnum = int(input("Enter the index number for an item in inventory:"))
print("At index",indexnum,"is",inventory[indexnum])
print("\n")
slc1 = int(input("Enter the index number to begin a slice:"))
slc2 = int(input("Enter the index number to end the slice:"))
print("inventory[",slc1,":",slc2,"]                    ",inventory[slc1:slc2])
print("\n")
print("Press the enter key to continue,")
print("You find a chest. It contains :")
chest = ("gold", "gems")
print("<'gold', 'gems'>")
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
print("\n\n")
print("Press the enter key to exit.")