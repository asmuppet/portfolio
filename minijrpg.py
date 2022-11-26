import random
import math

class Player:
  def __init__(self, equipment = [], base_offense = 0, base_defense = 0, base_speed = 100, base_hp = 100):
    gear_offense = 0
    gear_defense = 0
    gear_weight = 0
    gear_hp = 0

    if len(equipment) > 0:
      for gear in equipment:
        gear_offense += gear[0]
        gear_defense += gear[1]
        gear_weight += gear[2]
        gear_hp += gear[3]

    self.equipment_list = equipment
    self.offense = base_offense + gear_offense 
    self.defense = base_defense + gear_defense
    self.speed = base_speed - gear_weight
    self.maxhp = base_hp + gear_hp
    self.currenthp = self.maxhp
    self.dead = False
    self.defending = False

  def __repr__(self):
    status = 'You are a beginner warrior with {offense} attack power, {defense} defense, {speed} speed, and {hp} life.'.format(offense = self.offense, defense = self.defense, speed = self.speed, hp = self.hp)
    if self.dead == False:
      status += ' You are currently alive and breathing.'
    else:
      status += ' You are currently face down in the dirt, unmoving.'
    return status

  def strike(self, enemy):
    enemy.take_damage(math.floor(self.offense * 3 * random.uniform(.9, 1.1) - enemy.defense))
    

  def damage_dealt(self, enemy):
     return math.floor(self.offense * 3 * random.uniform(.9, 1.1) - enemy.defense)

  def defend(self):
    self.defending = True
    
  def take_damage(self, damage):
    if damage > 0:
      self.currenthp = self.currenthp - damage
    else:
      print('The attack bounced off!')
    if self.currenthp <= 0:
      self.die()
    else:  
      return self.currenthp

  def equip_list(self):
    equips = 'You are currently equipped with: '
    if len(self.equipment_list) == 0:
      equips += 'Nothing'
      print(equips)
    else:
      for equip in self.equipment_list:
        equips += equip[4] + ' '
      print(equips)

  def die(self):
    print('You have been struck down.')
    if self.currenthp != 0:
      self.currenthp = 0
    self.dead = True
    return self.dead

class Enemy:
  def __init__(self, name = 'Slime', attack = 2, defense = 2, speed = 2, hp = 100):
    self.name = name
    self.attack = attack
    self.defense = defense
    self.speed = speed
    self.maxhp = hp
    self.currenthp = hp
    self.dead = False
    self.ischarging = False
    self.approach = 'A slime bogishly and sloshily oozes up to you and seems to exude a combative aura. You ready for battle.'

  def __repr__(self):
    status = 'This is a {name}. This creature has {attack} attack power, {defense} defense, {speed} speed, and {hp} life.'.format(name = self.name, attack = self.attack, defense = self.defense, speed = self.speed, hp = self.hp)
    if not self.dead :
      status += ' The {name} is unfortunately still alive.'.format(name = self.name)
    else:
      status += ' The {name} has been pulverized.'.format(name = self.name)
    return status
    
  def heal(self):
    heal = self.currenthp + random.randint(25, 40)
    self.currenthp = min(heal, self.maxhp)

  def strike(self, player):
    if player.defending != True:
        player.take_damage(math.floor(self.attack * 3  * random.uniform(.6, 1.2) - player.defense))
        
    else:
        player.take_damage(math.floor(self.attack * 3  * random.uniform(.6, 1.2) - player.defense * 2))
        player.defending = False
        

  def charge_powerstrike(self):
    self.ischarging = True


  def power_strike(self, player):
    if player.defending != True:
        player.take_damage(math.floor(self.attack * 10 * random.uniform(.9, 1.1) - player.defense))
        self.ischarging = False
    else:
        player.take_damage(math.floor(self.attack * 4 * random.uniform(.5, .8) - player.defense))
        player.defending = False
        self.ischarging = False
        

  def damage_dealt(self, player):
      if self.ischarging and player.defending:
            return math.floor(self.attack * 4 * random.uniform(.5, .8) - player.defense)

      elif self.ischarging and not(player.defending):
             return math.floor(self.attack * 10 * random.uniform(.9, 1.1) - player.defense)
        
      elif not(self.ischarging) and player.defending:
            return math.floor(self.attack * 3  * random.uniform(.6, 1.2) - player.defense * 2)

      else:
            return math.floor(self.attack * 3  * random.uniform(.6, 1.2) - player.defense)
            

  def take_damage(self, damage):
    if damage > 0:
      self.currenthp = self.currenthp - damage
    else:
      print('The attack bounced off!')
    if self.currenthp <= 0:
      self.die()
    else:  
      return self.currenthp

  def die(self):
    print('You have defeated the {name}!'.format(name = self.name))
    if self.currenthp != 0:
      self.currenthp = 0
    self.dead = True
    return self.dead

#Equipment format: [Attack, Defence, Weight, HP, Name]
basic_clothes = [0, 5, 20, 10, 'Basic Clothes']
iron_armor = [0, 10, 40, 30, 'Iron Armor']
wooden_stick = [10, 0, 10, 0, 'Wooden Stick']
iron_sword = [15, 3, 20, 0, 'Iron Sword']

pchoice = input('Would you like Iron Armor to replace your Basic Clothes, or an Iron Sword to replace your Wooden Stick? Input 1 for the Iron Armor, or 2 for the Iron Sword. You can only choose one.\n')

gear = []

while pchoice != '1' and pchoice != '2':
    pchoice = input('Please input either 1 for the Iron Armor or 2 for the Iron Sword.\n')

if pchoice == '1':
    print('You have chosen the set of Iron Armor.\n')
    gear.append(iron_armor)
    gear.append(wooden_stick)

elif pchoice == '2':
    print('You have chosen the Iron Sword.\n')
    gear.append(basic_clothes)
    gear.append(iron_sword)

player = Player(base_offense = 5, equipment = gear)
enemy = Enemy(attack = 10, hp = 200, defense = 3)

print(enemy.approach)

while player.dead == False and enemy.dead == False:
    action = ''

    action = input('Will you:\n1. Strike\n2. Defend \n')

    while action != '1' and action != '2':
        action = input('Please choose\n1. Strike\n2. Defend\nChoose by inputting 1 or 2.\n')

    if action.lower() == '1':
        print('You render unto the enemy a viscious blow and deal', player.damage_dealt(enemy), 'damage.\n')
        player.strike(enemy)

    elif action.lower() == '2':
        print('You ready a powerful defensive stance.\n')
        player.defend()

    enemyAI = random.randint(1, 3)

    if enemy.ischarging and not(enemy.dead):
        
        print('The {name} unleashes a tidal wave of ooze dealing'.format(name = enemy.name), enemy.damage_dealt(player), 'damage.\n')
        enemy.power_strike(player)

    elif enemyAI == 1 and not(enemy.dead):
        print('The {name} slimes within itself, recovering some HP\n'.format(name = enemy.name))
        enemy.heal()

    elif enemyAI == 2 and not(enemy.dead):
        print('The {name} envelopes your legs in its acidic grasp, dealing'.format(name = enemy.name), enemy.damage_dealt(player), 'damage.\n')
        enemy.strike(player)
    
    elif enemyAI == 3 and not(enemy.dead):
        print('The {name} shrinks into a point and begins vibrating rapidly. You better ready yourself.\n')
        enemy.charge_powerstrike()

if enemy.dead:
    print('The monster lies vanquished and you are victorious.')


















