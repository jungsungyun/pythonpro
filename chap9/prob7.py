class Critter():
  """A Virtual pet"""
  def __init__(self,name,hunger = 0, boredom = 0):
    self.name = name
    self.hunger = hunger
    self.boredom = boredom
  def time(self):
    self.hunger += 1
    self.boredom += 1
  @property
  def setMood(self):
    emotion = self.hunger + self.boredom
    if emotion < 5:
      getMood = "happy"
    elif 5 <= emotion <= 10:
      getMood = "okay"
    elif 11 <= emotion <= 15:
      getMood = "frustrated"
    else:
      getMood = "mad"
    return getMood  
    
  def talk(self):
    print("I'm", self.name, "and I feel", self.setMood,"now\n")
    self.time()
  
  def Feed(self, food = 4):
    print("Thank you.")
    self.hunger -= food
    if self.hunger < 0:
      self.hunger = 0
    self.time()
  
  def play(self,fun =4):
    print("Wheee!")
    self.boredom -= fun
    if self.boredom < 0:
      self.boredom = 0
    self.time()
    
    
crit_name = input("What do you want to name your critter?: ") 
crit = Critter(crit_name)
choice = None
while choice != "0":
  print("""   Critter Caretaker
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - play with your criiter
        """)
  choice = input("Choice:")
  
  if choice == "0":
    break
  elif choice == "1":
    crit.talk()
  elif choice == "2":
    crit.Feed()    
  elif choice == "3":
    crit.play()
  else:
    print("\nInvalid choice.")