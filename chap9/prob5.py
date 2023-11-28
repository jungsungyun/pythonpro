class Critter:
  def __init__(self, name, mood):
    self.name = name
    self.mood = mood
  def talk(self):
    print("A new critter has been born!")
    print("\nI'm",self.name)
    print("Right now I feel", self.mood, "\n")
  def __private_method(self):
    print("This is a private method.")
  def public_method(self):
    print("This is a public method.")
    self.__private_method()
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.public_method()   

print("\nPress the enter key to exit.")