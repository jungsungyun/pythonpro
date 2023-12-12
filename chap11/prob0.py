class Card(object):
  """A playing card."""
  RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
  SUITS = ["c", "d", "h", "s"]
    
  def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit

  def __str__(self):
        reply = self.rank + self.suit
        return reply
class unprintable_Card(Card):
  def __str__(self):
     return "<unprintable>"

class Positionable_Card(Card):
  def __init__(self, rank, suit, face_up = True):
    super().__init__(rank, suit)
    self.is_face_up = face_up
 
  def __str__(self):
    if self.is_face_up:
      reply = super().__str__()
    else:
      reply = "XX"
    return reply

  def flip(self):
    self.is_face_up = not self.is_face_up


card1 = Card("A", "c")
card2 = unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")
print("Printing a Card object:")
print(card1)
print("\nPrinting an Unprintable_Card object:")
print(card2)
print("\nPrinting a Positionable_Card object:")
print(card3)
print("Flipping the Positionable_Card object.")
print("Printing the Positionable_Card object:")
card3.flip()
print(card3)
print("\nPress the enter key to exit.")
