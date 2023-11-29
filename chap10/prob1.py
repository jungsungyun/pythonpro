class Player:
  def blast(self, enemy):
    print("The player blasts an enemy.\n")
    print("The alien gasps and says, 'oh, this is it. This is the big one.")
    print("Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...")
    enemy.die()
class Alien():
  def die (self):
    print("Good-bye, cruel universe.'")

print("           Death of an Alien\n")
hero = Player()
invader = Alien()
hero.blast(invader)

print("\nPress the enter key to exit.")

