class Critter:
  def __init__(self, name):
    self.name = name
  def talk(self):
    print("Hi.  I'm", self.name, "\n")
  def __str__(self):
    rep = "Critter object\n"
    rep += "name: " + self.name + "\n"
    return rep
  def init(self):
    print("A new critter has been born!")
    
crit1 = Critter("Poochie")
crit2 = Critter("Randolph")
crit1.init()
crit1.talk()
crit1.init()
crit2.talk()
print("Printing crit1:")
print(crit1)
print("Directly accessing crit1.name:")
print(crit1.name)
print("\nPress the enter key to exit.")