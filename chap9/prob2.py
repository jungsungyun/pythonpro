class Critter:
  """special name"""
  def init1(self):
    print("A new critter has been born!")
  def init2(self):
    print("\nHi. I'm an instance of class Critter.")
inits1 = Critter()
inits2 = Critter()
inits1.init1()
inits1.init1()  
inits2.init2()
inits2.init2()
print("\n\nPress the enter key to exit.")
