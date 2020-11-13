from classes import *
from subclasses import *

class creeper(explodeCard):
  
  #set stats
  name = "creeper"
  maxHealth = 150
  attack = 20
  healHp = 10
  explosionDamage = 100

class zombie(Card):

  #set stats
  name = "zombie"
  maxHealth = 200
  attack = 40
  healHp = 20

  def useAbility(self, other):
	#if the other card is a zombie then double damage
    a, b = field.getCard(team)
	
	if a.name and b.name == "zombie": other.damage(attack * 2)

	self.turnActions()




class witch(poisonCard):

	#set stats
	name = "witch"
	maxHealth = 300
	attack = 50
	healHp = 30
	poisonDamage = 15
	poisonTurns = 5

class chargedCreeper(explodeCard):
	
	#set stats
	name = "creeper"
	maxHealth = 150
	attack = 20
	healHp = 10
	explosionDamage = 100

class spider(Card):

	#set stats
	name = "spider"
	maxHealth = 100
	attack = 20
	healHp = 15

	def useAbility(self, other):
		#? is this a good idea
		a, b = field.getCard(team)

		if a.name != b.name and a.name or b.name == "skeleton":
			other.damage(self.attack * 4)
		
		self.turnActions()

class skeleton(Card):

	#set stats
	name = "skeleton"
	maxHealth = 200
	attack = 40
	healHp = 5
	dodging  = False

	def damage(self, amount):
		if not dodging: self.health -= amount
		elif dodging: pass


	

	

