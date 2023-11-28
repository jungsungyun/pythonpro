class food:
  def __init__(self,name, level):
    self.name = name
    self.level = level
  def getLevel(self):
    return self.level
  def setCritterLevel(self,critter):
    critter.level += self.level
  
class Critter:
  def __init__(self, name, level = 0):
    self.name = name
    self.level = level
    
  def feed(self,food):
    food.setCritterLevel(self)
      
crit_name = input("What do you want to name your critter?: ")
crit = Critter(crit_name)

meat = [
  food("1 - 사료", 3),
  food("2 - 고기", 5),
  food("3 - 생선", 7)
]

while True:
  print("""   Critter Caretaker
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        """)

  choice = None
  choice = input("choice: ")
  
  if choice == "0":
    break
  elif choice == "1":
    print("I'm",crit_name,"and I feel",crit.level)
  elif choice == "2":
    print("\nAdd a choice the food")
    for i, food in enumerate(meat, 1):
      print(food.name)
    meat_choice = int(input("choice the food (1-3): "))
    if 1 <= meat_choice <= len(meat):
      crit.feed(meat[meat_choice - 1])  
  else:
    print("Invaild choice")    

  
  

      
      
