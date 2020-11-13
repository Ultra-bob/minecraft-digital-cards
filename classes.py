import random as r

class Card():

  # define basic variable
  name = ""
  health = 0
  maxHealth = 0
  attack = 0
  healHp = 0
  kind = ""
  poisonDamageTaken = 0
  poisonTurnsLeft = 0
  team = ""
  field = None
  
  # define functions
  def __init__(self, name, maxHealth, attack, heal):
    self.name = name
    self.health = maxHealth
    self.maxHealth = maxHealth
    self.attack = attack
    self.heal = heal


  def fight(self, other):
    other.damage(self.attack)
    self.turnActions()

  def healUp(self):
    self.health = max(self.maxHealth, self.health + self.healHp)
    self.turnActions()

  def die(self):
    del self
  
  def damage(self, amount):
    self.health -= amount
    if self.health <= 0: self.die

  def turnActions(self):
    if self.poisonTurnsLeft > 0:
      self.poisonTurnsLeft -= 1
      self.damage(self.poisonDamageTaken)

  def describe(self):
    text = "{}\nHealth: {}\nDamage: {}\nHeal: {}".format(self.name, self.attack, self.health, self.healHp)

    print(text)

class Deck():

  cards = []

  def randomize(self):
    self.cards = r.shuffle(self.cards)

  def draw(self):
    return self.cards.pop()

  def addCard(self, card):
    self.cards.append(card)

  def __init__(self, cards):
    self.cards = cards

class Field():
  # define card spots
  spotA1 = None
  spotA2 = None
  spotB1 = None
  spotB2 = None
  landscape = None

  def enterPlay(self, team, card):
    card.field = self
    if team == "a":
      if self.spotA1 == None: self.spotA1 = card
      elif self.spotA2 == None: self.spotA2 = card
      else: return False
    elif team == "b":
      if self.spotB1 == None: self.spotB1 = card
      elif self.spotB2 == None: self.spotB2 = card
      else: return False
    else: return False

  def getCard(self, team):
    if team == "a": return self.spotA1, self.spotA2
    elif team == "b": return self.spotB1, self.spotB2
    else: return False

#define a dealing function that returns N deck instances with random cards

def deal(decks, deck):
  i = 0
  deck.shuffle()
  returndecks = []
  for i in range(1, decks): returndecks.append(Deck([]))
  k = 0

  while len(deck.cards) > decks:
    for k in range(1,decks):
      returndecks[i].addCard(deck.draw())
  return returndecks
  

    
