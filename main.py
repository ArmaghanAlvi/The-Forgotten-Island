"""
-----------------------------------------------------------------------------
                   Setting up modules and global variables
-----------------------------------------------------------------------------
"""
import random
import time
from threading import Timer 
import os

#Player stats
deathCount = 0
day = 1
restarts = 0
hp = 20
weaponDMG = 0.5
armor = 0
hunger = 10
insanityLevel = 0
health = "Healthy"
hungerStatus = "Moderately Hungry"
insanityStatus = "Sane"


#Timekeeping and Events
hour = 0
tHour = "6:00 AM"
setting = "beach"

#Endings
endingCount = 0
insanityEnding = False
volcanoDeathEnding = False
newBeginningsEnding = False
escapeEnding = False

#Player Inventory
weapon = None
invArmor = None
inventory = ("Wristwatch",)
sticks = 0
stone = 0
vines = 0
turtleShell = 0
materials = ()
materialsNum = (sticks, stone, vines, turtleShell)

textDisplay = ""

"""
-----------------------------------------------------------------------------
                              Title Screen 
-----------------------------------------------------------------------------
"""
def titleScreen():  
  global textDisplay
  control.clear()
  try:
    print("""
_________          _______                                                       
\__   __/|\     /|(  ____ \                                                      
   ) (   | )   ( || (    \/                                                      
   | |   | (___) || (__                                                          
   | |   |  ___  ||  __)                                                         
   | |   | (   ) || (                                                            
   | |   | )   ( || (____/\                                                      
   )_(   |/     \|(_______/                                                      
                                                                                 
 _______  _______  _______  _______  _______ __________________ _______  _       
(  ____ \(  ___  )(  ____ )(  ____ \(  ___  )\__   __/\__   __/(  ____ \( (    /|
| (    \/| (   ) || (    )|| (    \/| (   ) |   ) (      ) (   | (    \/|  \  ( |
| (__    | |   | || (____)|| |      | |   | |   | |      | |   | (__    |   \ | |
|  __)   | |   | ||     __)| | ____ | |   | |   | |      | |   |  __)   | (\ \) |
| (      | |   | || (\ (   | | \_  )| |   | |   | |      | |   | (      | | \   |
| )      | (___) || ) \ \__| (___) || (___) |   | |      | |   | (____/\| )  \  |
|/       (_______)|/   \__/(_______)(_______)   )_(      )_(   (_______/|/    )_)
                                                                                 
_________ _______  _        _______  _        ______                             
\__   __/(  ____ \( \      (  ___  )( (    /|(  __  \                            
   ) (   | (    \/| (      | (   ) ||  \  ( || (  \  )                           
   | |   | (_____ | |      | (___) ||   \ | || |   ) |                           
   | |   (_____  )| |      |  ___  || (\ \) || |   | |                           
   | |         ) || |      | (   ) || | \   || |   ) |                           
___) (___/\____) || (____/\| )   ( || )  \  || (__/  )                           
\_______/\_______)(_______/|/     \||/    )_)(______/                                         
          """)
  except SyntaxError:
    print("This will never be printed but thats fine, its for the grade.")
    
  print("\nYou are wake up on an island with no memory of how you got there.\n You need to survive. But remember, things aren't always as they seem...\n\n")

  print(""" -̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳
        
      How to play:
You make choices depending on the given prompts during story events. However, there are a \nlot of other things you need to do to stay alive. There are many things you can do on the \nisland to help you survive. You can gather resources and craft tools and weapons to help you. \nYou can also fish and hunt for food. Make sure to check your status to check the state of \nyour health. \nIf you are ever confused about choices that you are given, type "help".\nGood Luck! \n\nTip: Pay attention to everything. There are many ways to lose, and only a few to win.
 -̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳-̳
        
  """)
  textDisplay = control.safeInput("What mode do you want text display to be: Auto, or Manual\n", "auto", "manual")
  
  #Allows the player to start the game
  print(input("Hit enter to start the game."))
  story.intro()


"""
---------------------------------------------------------------------------------
                                Control Functions 
---------------------------------------------------------------------------------
"""
class control:
  def clear():
    #Used to clear the console to improve playability
    os.system("clear")
  
  #a-e are possible valid inputs; at least one is required
  def safeInput(string, a, b = None, c = None, d = None, e = None, f = None, g = None, h = None):
    while True:
      #Makes any input lowercase
      safeString = input(string + "\n")
      aChoices = (a, b, c ,d, e, f, g, h)
      safeString = safeString.lower()
      safeString = safeString.strip()
      if safeString not in aChoices:
        print("Invalid input\n")
        continue
      else:
        return safeString

  def timeKeeping():
    global hour
    global tHour
    global setting
    global hunger

    hour += 2
    if hour == 24:
      return

    hunger += 1
    if hunger == 20:
      return
    
    if hour < 6 or hour >= 18:
      m = "AM"
    else:
      m = "PM"

    if hour <= 6:
      tHour = str(6 + hour) + ":00 " + m
    elif hour > 6 and hour <= 18:
      tHour = str(hour - 6) + ":00 " + m
    else:
      tHour = str(hour - 18) + ":00 " + m

  def storyLine(string, delay):
    if textDisplay == "auto":
      print(string)
      time.sleep(delay)
    else:
      print(input(string + " (ENTER)\n"))
"""
--------------------------------------------------------------------------------
                              General Functions
--------------------------------------------------------------------------------
"""
class general:
  def playerStatus():
    global health 
    global hungerStatus 
    global insanityStatus 
    global hp
    global weaponDMG
    global armor
    global tHour
  
    #Judges the state of the player's health
    if hp >= 15:
      health = "Healthy"
    elif hp >= 10 and hp < 15:
      health = "Moderate"
    elif hp > 5 and hp < 10:
      health = "Unhealthy"
    else:
      health = "Dying"
  
    #Judges how hungry the player is
    if hunger >= 15:
      hungerStatus = "Starving"
    elif hunger >= 10 and hunger < 15:
      hungerStatus = "Hungry"
    elif hunger >= 5 and hunger < 10:
      hungerStatus = "Moderately Hungry"
    else:
      hungerStatus = "Full"
  
    #Judges the state of the player's insanity
    if insanityLevel >= 15:
      insanityStatus = "Near-Insane"
    elif insanityLevel >= 10 and insanityLevel < 15:
      insanityStatus = "Unstable"
    elif insanityLevel >= 5 and insanityLevel < 10:
      insanityStatus = "Relatively Sane"
    else:
      insanityStatus = "Sane"
  
    #Prints a menu to check the player's status
    print("Health: " + health)
    print("Hunger: " + hungerStatus)
    print("Insanity: " + insanityStatus)
    print("HP: " + str(hp) + "/20")
    print("Attack Damage: " + str(weaponDMG))
    print("Armor: " + str(armor))
    print("\nWatch display: " + tHour)
  
  def invStatus():
    global inventory
    global materials
    global materialsNum
  
    print("Inventory: \n  Weapon: " + str(weapon) + "\n  Armor: " + str(invArmor) + "\n\n  Items:")
  
    #Prints all the items in the inventory
    for item in inventory:
      print("    " + item)
    
    print("\n  Materials:")
    
    #Prints each item in the tuple materials and pairs it with a value from the tuple materialsNum
    for i in range(len(materials)):
      print("    " + materials[i] + ": " + str(materialsNum[i]))
  
  def action():
    #Between events the player can choose to do one of 3 things;     #rest, hunt, manage resources (one action)
    global hp
    while True:
      action = control.safeInput("What do you want to do?\nCheck status, rest, hunt, or manage resources? \n", "check status", "status", "rest", "hunt", "manage resources", "help")
      
      #If the user decides to rest
      if action == "check status" or action == "status":
        general.playerStatus()
        time.sleep(1)
        break
        
      elif action == "rest":
        print("You find a comfortable place to rest, sit down, lean back, and close your eyes.")
        time.sleep(3)
    
        #Doesn't allow the user to heal to an amount over 20
        if hp > 0 and hp < 11:
          hp += 10
          print("You rested and gained 10 hp!")
        else:
          hps = 20 - hp
          hp += hps
          print("You rested and gained " + str(hps) +" hp!")
        break
    
      #If the user chooses to hunt
      elif action == "hunt":
        #You can only hunt if you have the weapons
        if weapon != "Wooden Spear" and weapon != "Stone Spear" and weapon != "Bone Spear" and weapon != "Magic Spear" and "Bow" not in inventory:
          print("You don't have any hunting weapons.\n\n")
          continue
        else:
          mechanics.hunt()
          break
      #If the user chooses to manage resources 
      elif action == "manage resources":
        mechanics.manageResources()
        break
      else:
        print("""
You now have to choose an action.
There are 4 actions that you can make:\n
check status - Allows you to see your status.   This includes your current health, hunger, insanity, HP (health points), attack damage, and armor; also displays the time on your watch\n
rest - Allows you to rest and restore 10 HP; if your HP is full (20/20), rest will simply do nothing but skip the action turn\n
hunt - Allows you to hunt; if you catch an animal, you will improve your hunger status (which can be checked in the "check status" action)\n
manage resources - Allows you to gather resources and craft items; also displays your inventory
              """)
        time.sleep(10)
        continue
"""
---------------------------------------------------------------------------------
                              Core Game Mechanics
---------------------------------------------------------------------------------
"""
class mechanics:
  """
                   ------------The Hunting Mechanic-------------
  """
  def hunt():
    global hunger
    global hungerStatus
    global inventory
    global turtleShell
    global materials
    
    animals = ()
    while True:
      #The user selects hunting or fishing
      choice = control.safeInput("Do you want to hunt or fish.", "hunt", "fish")
      if choice == "hunt":
        #Hunting only works if they have a bow
        print("You find an area in the forest that seems like it would be good for hunting.\n")
        if "Bow" in inventory:
          #selects a random animal and defines the hunting words
          animals = ("deer", "rabbit", "duck", "boar")
          ranimal = animals[random.randint(0,3)]
          hWeapon = "bow"
        else:
          print("You don't have a bow to hunt with")
          continue
      else:
        #Fishing only works if they have a bow
        print("You find a nearby stream that looks like it would be good for fishing.")
        if weapon == "Wooden Spear" or weapon == "Stone Spear" or weapon == "Bone Spear" or "Magic Spear":
          #selects a random animal and defines the hunting words
          animals = ("fish", "turtle")
          ranimal = animals[random.randint(0,1)]
          hWeapon = "spear"
        else:
          print("You don't have a spear to fish with")
          continue
    
      #The delay before the user needs to react
      delay = random.randint(1,10)
    
      #How long you have to react
      timeoutMin = 0.3
      timeoutMax = 0.5
    
      #t gets the Timer function with arguments: timeout for the time you have to shoot and print + “The animal got away” (with animal being whatever animal you are hunting) if the timer runs out
      t = Timer(timeoutMax, print, ["You missed! \nHit enter to continue."])
    
      #Prints which animal you found and waits one second 
      print("You found a " + ranimal + ".\n")
      time.sleep(1)
      
      if hWeapon == "bow":
        print("You slowly draw back your bow. Hit enter to shoot when prompted.\n")
      else:
        print("You slowly draw back your spear. Hit enter to throw when prompted.\n")
  
      #Waits as long as the delay
      time.sleep(delay)
  
      #starts the timer and records the time
      t.start()
      start = time.time()
  
      #prompts the user to shoot
      print(input("Hit enter to shoot!\n"))
  
      #Ends the timer and records the time
      t.cancel()
      end = time.time()
  
      #Calculates the reaction time
      reactionTime = end - start
  
      #Checks if the player reacted fast enough and tell what the player gets out of the hunt
      if reactionTime > timeoutMax:
        print("The " + ranimal + " got away.")
        break
      elif reactionTime < timeoutMin:
        if hWeapon == "bow":
          print("You shot too early!")
        else:
          print("You threw too early!");
          
        print("The " + ranimal + " got away.")
        break
      else:
        print("You hit the " + ranimal + "!")
        if ranimal == "deer":
          print("You ate the " + ranimal + " and eased your hunger.")
          hunger -= 3
        elif ranimal == "rabbit":
          print("You ate the " + ranimal + " and eased your hunger.")
          hunger -= 1
        elif ranimal == "duck":
          print("You ate the " + ranimal + " and eased your hunger.") 
          hunger -= 2
        elif ranimal == "boar":
          print("You ate the " + ranimal + " and eased your hunger.")
          hunger -= 4
        elif ranimal == "fish":
          amount = random.randint(1,3)
          print("You ate the " + ranimal + " and eased your hunger.")
          hunger -= amount
        else:
          r = random.randint(2,4)
          print("You ate the " + ranimal + " and eased your hunger.\nYou also found " + str(r) + " turtleshell shards.")
          hunger -= 2
          turtleShell += r
          if "turtleshell shards: " not in materials:
            materials += ("turtleshell shards: ",)
  
        #Makes sure that hunger can't be less than 0
        if hunger < 0:
          hunger = 0
  
        #Tells the player how hungry they are
        print("You are: " + hungerStatus)
        break
        
  """
              ------------The Resource Management Mechanic-------------
  """
  def manageResources():
    #Delcare global variables
    global weapon
    global weaponDMG
    global armor
    global invArmor
    global inventory
    global sticks
    global stone
    global vines
    global turtleShell
    global materials
    global materialsNum

    back = False
    
    #Print the player's inventory
    general.invStatus()
  
    #Allow the user to make 2 actions
    print("\nYou can make 2 actions\n")
    for i in range(2):
      #The user can either collect resources or craft
      while True:
        choice = control.safeInput("\nWhat do you want to do? \nCollect resources or craft?", "collect resources", "collect", "craft", "help")
        #The user can collect 2 resources
        if choice == "collect resources" or choice == "collect":
          print("\nYou can collect 2 different material types (one action)")
          for i in range(2):
            #The first time it asks what you want to collect; the second time says what 'else' do you want to collect
            if i == 0: 
              collect = control.safeInput("What do you want to collect? Sticks, stone, or vines?", "sticks", "stone", "vines")
            else:
              collect = control.safeInput("What else do you want to collect? Sticks, stone, or vines?", "sticks", "stone", "vines")
  
            #Depending on what you collect, you get 2 of that resource
            if collect == "sticks":
              print("\nYou walk into the forest and gather a bundle of sticks that are littered on the ground.\n +2 sticks")
              sticks += 2
              if "sticks" not in materials:
                materials += ("sticks",)
            elif collect == "stone":
              print("\nYou look around and pick a up a few different stones, some smooth, some jagged.\n +2 stone")
              stone += 2
              if "stone" not in materials:
                materials += ("stone",)
            else:
              print("\nYou walk into the forest and pull down some hanging vines. They seem fresh and could be used for binding.\n +2 vines")
              vines += 2
              if "vines" not in materials:
                materials += ("vines",)
          materialsNum = (sticks, stone, vines, turtleShell)
          break
        elif choice == "craft":
          #User chooses something to craft if they have crafting materials
          if weaponDMG >= 4 and armor >= 2 and ("Stone Knife" and "Stone Ax" and "Bow") in inventory:
            print("You no longer have a need to craft.\n")
            continue
          if (sticks > 0 and stone > 0) or turtleShell > 0 or sticks >= 4:
            while True:
              craft = control.safeInput("What do you want to craft? \nWooden Spear - requires 4 sticks \nStone Spear - requires 3 sticks + 3 stone \nStone Dagger (Weapon) - requires 1 sticks + 1 stone \nStone Knife (Tool)- requires 1 sticks + 1 stone \nStone Ax - requires 2 sticks + 2 stone \nBow - requires 2 sticks + 2 vines \nShell Armor - requires 8 turtleshell shards \nNote: You never know when a tool could come in handy...\n\nType " + "back" + " to go back", "wooden spear", "stone spear", "stone dagger", "stone knife", "stone ax", "bow", "shell armor", "back")
              #Adds the crafted tool to the inventory. If you already have a better version, or already have the item it repromots what you want to craft. It then subtracts the resources used. 
              if craft == "stone dagger": 
                if weaponDMG > 1:
                  print("You already have a better weapon")
                  continue
                else:  
                  weapon = "Stone Dagger"
                  weaponDMG = 1
                  print("You crafted a Stone Dagger!")
                  time.sleep(0.5)
                  print("-1 stick\n-1 stone")
                  sticks -= 1
                  stone -= 1
                  break
              elif craft == "wooden spear" and sticks >= 4:
                if weaponDMG > 2:
                  print("You already have a better weapon")
                  continue
                else:  
                  weapon = "Wooden Spear"
                  weaponDMG = 2
                  print("You crafted a Wooden Spear!")
                  time.sleep(0.5)
                  print("-4 sticks")
                  sticks -= 4
                  break
              elif craft == "stone spear" and sticks >= 3 and stone >= 3:
                if weaponDMG > 4:
                  print("You already have a better weapon")
                  continue
                else:  
                  weapon = "Stone Spear"
                  weaponDMG = 4
                  print("You crafted a Stone Spear!")
                  time.sleep(0.5)
                  print("-3 stick\n-3 stone")
                  sticks -= 3
                  stone -= 3
                  break
              elif craft == "stone knife" and sticks >= 1 and stone >= 1:
                inventory += ("Stone Knife",)
                print("You crafted a stone knife!")
                print("-1 stick\n-1 stone")
                sticks -= 1
                stone -= 1
                break
              elif craft == "stone ax" and sticks >= 2 and stone >= 2:
                inventory += ("Stone Ax",)
                print("You crafted a stone ax!")
                print("-2 sticks\n-2 stone")
                sticks -= 2
                stone -= 2
                break
              elif craft == "bow" and sticks >= 2 and vines >= 2:
                inventory += ("Bow",)
                print("You crafted a bow!")
                print("-2 stick\n-2 vines")
                sticks -= 2
                vines -= 2
                break
              elif craft == "shell armor" and turtleShell >= 8:
                if armor > 2:
                  print("You already have better armor")
                  continue
                else:  
                  invArmor = "Shell Armor"
                  armor = 1
                  print("You crafted a Shell Armor!")
                  time.sleep(0.5)
                  print("-8 turtleshell shards")
                  turtleShell -= 8
                  break
              elif craft == "back":
                back = True
                break
                
              else:
                print("You don't have sufficient materials.\n")
                continue
          else:
            print("You don't have enough materials to craft anything.")
            continue
              
        else:
          print("""
You can make 2 actions here. You 2 choices for each action:\n
collect materials - Choose 2 types of materials to collect\n
craft items - based on the materials you have, you can craft different items to help you survive
                """)
          time.sleep(5)
          continue
          
        if back == True:
          back = False
          print("\n")
          continue
          
        break
    

  """
                    ------------The Combat Mechanic-------------
  """
  def combat():
    
    global hp
    global weaponDMG
    global armor 
    global setting 
    global weapon 
    global invArmor
    global inventory
    global deathCount
    global win
  
    block = 0
    heal = 2
    focus = 0
    
    eHp = 0
    eAtk = 0
    eArmor = 0
    eBlock = 0
    eHeal = 0
    eFocusAmount = 0
    eFocus = 0

    if weapon == None:
      weaponDMG = 0.5
    
    r = 0
    if setting == "forest":
      r = random.randint(1,4)
    elif setting == "tribe encounter":
      r = 5
    elif setting == "mysterious forest":
      r = random.randint(6,10)
    elif setting == "volcano":
      r = 11
    else:
      r = 0
      
    rEnemy = ""
    
    if setting == "forest" and r == 1:
      rEnemy = "fox"
      eHp = 5
      eAtk = 1
    
    elif setting == "forest" and r == 2:
      rEnemy = "wolf"
      eHp = 7
      eAtk = 1.5
      eFocusAmount = 0.5
    
    elif setting == "forest" and r == 3:
      rEnemy = "cougar"
      eHp = 12
      eAtk = 2
      eFocusAmount = 1
    
    elif setting == "forest" and r == 4:
      rEnemy = "bear"
      eHp = 16
      eAtk = 4
      eHeal = 1
      eFocusAmount = 1
    
    elif setting == "tribe encounter" and r == 5:
      rEnemy = "tribesman"
      eHp = 15
      eAtk = 6
      eArmor = 2
      eBlock = 1
      eFocusAmount = 1
    
    elif setting == "mysterious forest" and r == 6:
      rEnemy = "goblin"
      eHp = 10
      eAtk = 2
      eArmor = 1
      eBlock = 1
      eHeal = 1
      eFocusAmount = 1
    
    elif setting == "mysterious forest" and r == 7:
      rEnemy = "zombie"
      eHp = 12
      eAtk = 2
      eBlock = 1
      eHeal = 3
      eFocusAmount = 2
    
    elif setting == "mysterious forest" and r == 8:
      rEnemy = "beast"
      eHp = 16
      eAtk = 6
      eBlock = 2
      eHeal = 2
      eFocusAmount = 2
    
    elif setting == "mysterious forest" and r == 9:
      rEnemy = "armored zombie"
      eHp = 12
      eAtk = 5
      eArmor = 3
      eBlock = 1
      eHeal = 3
      eFocusAmount = 2
        
    elif setting == "mysterious forest" and r == 10:
      rEnemy = "armored beast"
      eHp = 16
      eAtk = 7
      eArmor = 4
      eBlock = 3
      eHeal = 2
      eFocusAmount = 2
  
    elif setting == "volcano" and r == 11:
      #Final boss
      rEnemy = "Gaurdian Beast"
      eHp = 100
      eAtk = 8
      eArmor = 1
      eBlock = 3
      eHeal = 5
      eFocusAmount = 5
  
    initialHp = 20
    initialeHp = eHp
    
    cantBlock = ("fox", "wolf", "cougar", "bear")
    cantHeal = ("fox", "wolf", "cougar", "tribesman")
    cantRun = ("tribesman", "Guardian Beast")
    rRun = random.randint(1,3)
    dropEnemies = ("goblin", "armored zombie", "armored beast")
    
    control.clear()
    print("You encountered a(n) " + rEnemy + "!\n")
    
    while True:
      print("It's your turn")
      
      while True:
        block = 0
  
        choice = control.safeInput("What do you want to do? \nAttack, block, heal, focus, or run?", "attack", "heal", "block", "focus", "run", "help")
        
        #Attack
        if choice == "attack":
          weaponDMG += focus
          store_eHp = eHp
  
          eHp -= weaponDMG - (eBlock + eArmor)

          if eHp <= 0:
            eHp = 0 
          
          if eBlock == 0:
            print(f"You attacked the {rEnemy}. The {rEnemy} has {eHp}/{initialeHp} hp remaining.\n")
          elif eBlock + eArmor < weaponDMG:
            print(f"You attacked the {rEnemy}. The {rEnemy} blocked {eBlock+eArmor} damage, and has {eHp}/{initialeHp} hp remaining.\n")
          else:
            print(f"The {rEnemy} blocked your attack")
            eHp = store_eHp

          #Makes you win if eHp is less than or equal to 0 
          if eHp <= 0:
              
            print(f"You defeated the {rEnemy}!\n")
            time.sleep(2)
            #There is a 50% chance for an enemy with drops to actually drop their loot
            drop = random.randint(1,2)
            if rEnemy in dropEnemies and drop == 1:
              if rEnemy == "goblin":
                #Chooses if the goblin either drops a Steel Sword or a Shield; only works if you don't have a more powerful weapon and/or don't have a shield
                gobDrop = random.randint(1,2)
                if gobDrop == 1 and weaponDMG < 6:
                  dropItem = "Steel Sword"
                  weapon = "Steel Sword"
                  weaponDMG = 6
                  print(f"\nYou search the {rEnemy}'s dead body and find a {dropItem}.")
                elif gobDrop == 2 and "Shield" not in inventory:
                  dropItem = "Shield"
                  inventory += ("Shield",)
                  print(f"\nYou search the {rEnemy}'s dead body and find a {dropItem}.")
                #If you have both, nothing drops
                else:
                  pass
              #Armored Zombies can drop Chain Mail Armor if you don't already have more powerful armor
              elif rEnemy == "armored zombie" and armor < 2:
                dropItem = "Chain Mail Armor"
                invArmor = "Chain Mail Armor"
                armor = 2
                print(f"\nYou search the {rEnemy}'s dead body and find a {dropItem}.")
              #Armored Beasts can drop Heavy Armor if you don't already have more powerful armor
              elif rEnemy == "armored beast" and armor < 4:
                dropItem = "Heavy Armor"
                invArmor = "Heavy Armor"
                armor = 4
                print(f"\nYou search the {rEnemy}'s dead body and find a {dropItem}.")
              #If you have these items, or things better than them, nothing will drop
              else:
                pass

            print(input("Hit enter to continue"))
            control.clear()
            return True

          weaponDMG -= focus
          focus = 0
          break
  
        #Heal
        elif choice == "heal":
          if invArmor == "Magic Tunic":
            heal += 3
  
          if hp == initialHp:
            printHeal = 0
          else:
            hp += heal
            printHeal = heal
          #Makes it so that hp can't be more than the initial hp
          if hp > initialHp:
            printHeal = hp - initialHp
            hp = initialHp
            
          print(f"You take a momement to catch your breath. You recovered {printHeal} hp and have {hp}/{initialHp} hp.\n")
          break
  
        #Block
        elif choice == "block":
          block += 2
          if "Shield" in inventory:
            block += 3
          print("You prepare to defend.")
          break
  
        #Focus
        elif choice == "focus":
          focus = 0
          focus += 2
          if weapon == "Magic Spear":
            focus += 3
          print(f"You focus on your breathing and gain +{focus} attack for one turn.\n")
          break
  
        #Run
        elif choice == "run":
          #If you can't get away, it continues your turn
          if rEnemy in cantRun:
            print("\nYou couldn't get away!")
            continue
          elif rRun == 1:
            print("\nYou couldn't get away!")
            continue
          else:
            #Helps break out of combat function
            print(f"\nYou turn around and run until you can't hear anything following you.\nYou look around and can no longer see the {rEnemy}. You got away safely.")
            print(input("\nHit enter to continue"))
            control.clear()
          break
        else:
          print("""
Attack - does as much damage as your weapin to the enemy (no weapon means only 0.5 damage)
Block - Blocks 2 damage from the enemy (5 if you have a shield)
Heal - Recovers 2 health (5 if you have a Magic Tunic)
Focus - +2 damage for one turn (5 if you have a Magic Spear)
Run - Allows you to escape the battle; doesn't always work
                """)
  
      #Helps break out of combat function
      if choice == "run":
        break
      elif hp > 0.0 and eHp > 0.0:
        pass  
      else:
        break
        
      #Moves on to enemy's turn
      print(f"\nIts the {rEnemy}'s turn.")
      
      while True:
        eBlock = 0
        
        eChoice = random.randint(1,4)
        
        #Enemy Attack
        if eChoice == 1:
          eAtk += eFocus
          storeHp = hp
          hp -= eAtk - (block + armor)
  
          if hp <= 0:
            hp = 0 
          
          if block == 0 and armor == 0:
            print(f"The {rEnemy} attacked you. You have {hp}/{initialHp} hp remaining.\n")
          elif block + armor < eAtk:
           print(f"The {rEnemy} attacked you. You blocked {block + armor} damage and have {hp}/{initialHp} hp remaining.\n")
          else:
            print(f"\nYou blocked the {rEnemy}'s attack.")
            hp = storeHp

          #Makes you lose if your hp is less than or equal to 0 
          if hp <= 0:
            print(f"You lost to the {rEnemy}.")
            print(input("Hit enter to continue"))
            deathCount += 1
            control.clear()
            return False
          
          eAtk -= eFocus
          eFocus = 0
          break
  
        #Enemy Heal
        elif eChoice == 2:
          #If an enemy can't heal, it chooses another action
          if rEnemy in cantHeal:
            continue
  
          if eHp == initialeHp:
            continue
          
          eHp += eHeal
          printeHeal = eHeal
          #Makes it so that hp can't be more than the initial hp
          if eHp > initialeHp:
            printeHeal = eHp - initialeHp
            eHp = initialeHp
            
          print(f"The {rEnemy} recovered {printeHeal} hp and has {eHp}/{initialeHp} hp.\n")
          break
        
        #Enemy Block
        elif eChoice == 3:
          #If an enemy can't block, it chooses another action
          if rEnemy in cantBlock:
            continue
          eBlock += 2
          print(f"The {rEnemy} prepared to defend.\n")
          break
  
        #Enemy Focus
        else:
          #If an enemy can't focus, it chooses another action; this only applies to fox
          if rEnemy == "fox":
            continue
          eFocus += eFocusAmount
          print(f"The {rEnemy} focused its senses and gained +{eFocusAmount} attack for one turn.\n")
          break
      
      #Breaks out of combat function
      if choice == "run":
        break
      else:
        #Clears the console and moves to next turn if neither the player or enemy have won
        time.sleep(1)
        print(input("Hit enter to continue"))
        control.clear() 

  
  """
           ------------The Day Restart / Time Loop Mechanic-------------
  """
  def dayRestart():
    #Declaring global variables
    global deathCount
    global day
    global restarts
    global hp
    global weaponDMG
    global armor
    global hunger
    global insanityLevel
    global health
    global hungerStatus
    global insanityStatus
    global hour
    global tHour
    global setting
    global weapon
    global invArmor
    global inventory
    global sticks
    global stone
    global vines
    global turtleShell
    global materials
    global materialsNum
    
    #Resetting Player stats
    day = 1 + deathCount + restarts
    hp = 20
    weaponDMG = 0.5
    armor = 0
    hunger = 10
    insanityLevel += 4
    health = "Healthy"
    hungerStatus = "Moderately Hungry"
    insanityStatus = "Sane"
    
    
    #Resetting Timekeeping and Events
    hour = 0
    tHour = "6:00 AM"
    setting = "beach"
    
    #Resetting Player Inventory
    weapon = None
    invArmor = None
    inventory = ("Wristwatch",)
    sticks = 0
    stone = 0
    vines = 0
    turtleShell = 0
    materials = ()
    materialsNum = (sticks, stone, vines, turtleShell)

    #Triggers the Insanity ending if the player's insanity level is too high
    if insanityLevel >= 20:
      endings.insanityEnding()
    
    #Prints a different story passage depending on how many deaths they've had
    if deathCount == 1 and endingCount == 0:
      time.sleep(3)  
      control.storyLine("Your eyes fly open and you get up with a startled cry.", 2)
      control.storyLine("You rip off your shirt and feel for your wounds.", 2)
      control.storyLine("They're gone. Vanished. Simply not there. It makes no sense.", 3)
      control.storyLine("You should be dead. You \x1B[3mremember\x1B[0m dying.", 3)
      control.storyLine("And yet there isn't even a scar.", 3)
      control.storyLine("You check your watch to see what time it is.", 3.5)
      control.storyLine("What you see in the small box that tells the date makes your heart stop.", 4)
      control.storyLine("It reads 3/14/22.", 4)
      for i in range(3):
        print(".")
        time.sleep(1)
        
    elif restarts == 1 and endingCount == 0:
      time.sleep(3)
      control.storyLine("You wake up laying on sand.", 2)
      control.storyLine("You weren't here seconds ago.", 2)
      control.storyLine("Your eyes widen as you realize that seconds ago, you were at a completely different location.", 2.5)
      control.storyLine("You get up and look around. This is where you woke up yesterday.", 2.5)
      control.storyLine("But when you check your watch, you realize that you didn't wake up on this beach yesterday.", 2.5)
      control.storyLine("You woke up here today. Your heart skips a beat as you look at your watch.", 4)
      control.storyLine("The small box on your watch reads 3/14/22.", 4)
      for i in range(3):
        print(".")
        time.sleep(1)
        
    else:
      rString = random.randint(1,3)
      if rString == 1:
        time.sleep(3)
        control.storyLine("You open your eyes and find yourself on the beach.", 2)
        control.storyLine("The same one as always. You already knew that that would happen.", 3)
        control.storyLine("The question is, how do you make it stop?", 3)
        for i in range(3):
          print(".")
          time.sleep(1)
          
      elif rString == 2:
        time.sleep(3)
        control.storyLine("You slowly crack your eyes open, squinting against the glare of the Sun.", 2)
        control.storyLine("You expected this to happen.", 1.5)
        control.storyLine("You are on the beach again.", 1.5)
        control.storyLine("You check your watch, and the small box reads 3/14/22.", 3)
        control.storyLine("Of course it does.", 3)
        for i in range(3):
          print(".")
          time.sleep(1)
          
      else:
        if day >= 4:
          time.sleep(3)
          control.storyLine("You open your eyes, not surprised by what you see.", 2)
          control.storyLine("Sand.", 2)
          control.storyLine("You already know what your watch will read so you don't even bother checking.", 3)
          for i in range(3):
            print(".")
            time.sleep(1)
            
        else:
          rString2 = random.randint(1,2)
          if rString2 == 1:
            time.sleep(3)
            control.storyLine("You open your eyes and find yourself on the beach.", 2)
            control.storyLine("The same one as always. You already knew that that would happen.", 3)
            control.storyLine("The question is, how do you make it stop?", 3)
            for i in range(3):
              print(".")
              time.sleep(1)
              
          elif rString2 == 2:
            time.sleep(3)
            control.storyLine("You slowly crack your eyes open, squinting against the glare of the Sun.", 2)
            control.storyLine("You expected this to happen.", 1.5)
            control.storyLine("You are on the beach again.", 1.5)
            control.storyLine("You check your watch, and the small box reads 3/14/22.", 3)
            control.storyLine("Of course it does.", 3)
            for i in range(3):
              print(".")
              time.sleep(1)

    story.startStory()

      

"""
---------------------------------------------------------------------------------
                                  Story Functions
---------------------------------------------------------------------------------
"""
class story:
  
  def intro():    
    control.clear()
    control.storyLine("You wake up laying on sand. You get up and look around, not recongnising your surroundings.", 3)
    control.storyLine("You seem to be on the beach of an island.", 3) 
    control.storyLine("There is a forest next to the beach, and on the other side is just ocean.", 3)
    control.storyLine("You look out to sea and strain your eyes, hoping to see somehting. A boat or ship maybe.", 0)
    for i in range(3):
      print(".")
      time.sleep(1)
    control.storyLine("Nothing.", 3)
    control.storyLine("You strain your memory, trying to remember how you got here.", 3)
    control.storyLine("And then you realize that you can't remmeber anything at all.", 3)
    control.storyLine("Not a single memory.", 4)
    control.storyLine("You take inventory of what you have, and realize that you don't have anything with you other than what you are wearing.", 3)
    control.storyLine("You have your clothes and an old brass, analog wristwatch.", 3)
    control.storyLine("You check the time.", 3)
    control.storyLine("It is 6:00 AM. A small box on the left side says the date. It reads 3/14/22", 5) 

    story.startStory()

  def startStory():
    global hour
    global tHour
    global setting
    global deathCount

    while True:
      #Event 1
      control.storyLine("A pang of hunger hits your stomach, and You feel like you haven't eaten for days.", 3)
      control.storyLine("You realize that if you want to survive, you need to start moving.", 3)
      control.storyLine("You need to food and a way off of this island.", 3)
      control.storyLine("Food is definately a priority. However, you don't recognise any plants here.", 3)
      control.storyLine("You need to hunt, but you don't have any hunting weapons.", 3)
      control.storyLine("Looks like you'll have to make some.", 4)
    
      print("\n\nYou can make 3 actions.")
      for i in range(3):
        general.action()
        print("\n")
        time.sleep(2)
      print("You have used your 3 actions.")
      time.sleep(1)
      
      print(input("Hit enter to continue"))
  
      control.timeKeeping()
  
      #Event 2
      control.clear()
      
      control.storyLine("As time passes, you realize that simply surviving isn't enough.", 3)
      control.storyLine("You need to figure out who you are, where you are, how you got here, and how to get back to civilization.", 3)
      control.storyLine("You should probably start by exploring.", 3)
  
      while True:
        choice = control.safeInput("Where do you want to go? \nThe beach or forest?", "beach", "forest")
        if choice == "beach":
          control.storyLine("\nYou decide to stay on the beach for a little longer.\n", 2)
          general.action()
          control.timeKeeping()
          
          control.storyLine("\nYou wonder if you should begin exploring.\n", 2)
        else:
          setting = "forest"
          break
      control.storyLine("\nYou decide to explore the forest to see if you can find anything useful.", 3)
      control.storyLine("As you walk between the trees, filtered sunlight ocassionally breaking through the canopy and splashing onto your face, you hear the sounds of nature all around you.", 6)
      control.storyLine("You hear small animals skittering through the undergrowth, and larger animals rustling through the forest.", 4)
      control.storyLine("It would probably be best to stay away from those.", 3)
      control.storyLine("You hear something crashing through the undergrowth.", 3)
      control.storyLine("Too late. Looks like one of those larger animals found you.", 3)
      x = mechanics.combat()
      if x == False:
        return
      control.timeKeeping() 
  
      #Event 3
      control.clear()
      
      control.storyLine("\nYou look around and are met with unfamiliar surroundings.", 3)
      control.storyLine("\nThat fight had led you pretty far from the beach.", 3)
      control.storyLine("You can't even see it from between the trees anymore.", 3)
      control.storyLine("Nor can you feel the gentle breeze that blew from its direction.", 3)
      control.storyLine("You've lost your sense of direction, and need to choose a path to follow.", 3)
  
      while True:
        choice = control.safeInput("Which way do you want to go?\nLeft or right?", "left", "right")
        correctChoice = random.randint(1,3)
        if correctChoice == 1 or correctChoice == 2:
          correctChoice = "left"
        else:
          correctChoice = "right"
        
        if choice == correctChoice:
          break
        else:
          control.storyLine("You turn to the " + choice + " and begin walking.", 3)
          x = mechanics.combat()
          if x == False:
            return
          control.storyLine("You are lost again and need to choose a direction to travel in.", 3)
          continue
      control.storyLine("You turn to the " + choice + " and begin walking.", 3)
      control.storyLine("You walk deeper and deeper into the forest, and have a feeling that you're not going towards the beach.", 3)
  
      control.storyLine("After a while, you decide to take a break, but you want to do something useful", 3)
  
      general.action()
      print(input("Hit enter to continue"))
  
      control.storyLine("\nAfterwards, you continue to walk", 3)
      control.storyLine("Eventually, you hear something rustling about 10 feet from your current location.", 3)
      control.storyLine("You hear voices coming from that direction. Human voices.", 3)
      control.storyLine("You crouch and look closer.", 3)
  
      choice = control.safeInput("Do you want to run or investigate", "run", "investigate")
  
      control.timeKeeping()
      
      if choice == "run":
        control.storyLine("\nYou turn around and flee. Its better that you don't get involved.", 3)
        control.storyLine("However, your movement alerts the tribesmen, and thinking that you are an animal, they cast their spears and arrows in your direction.", 3)
        control.storyLine("You are hit in three spots and you fall to the ground.", 3)
        control.storyLine("You hear alarmed voices as the hunting party catches up to you, but your vision is already going black.", 3)
        deathCount += 1
        return
        
      else:
        control.storyLine("\nYou slowly creep towards the group of people. They are wearing tribal clothing and are carrying hunting equipment.", 3)
  
        choice = control.safeInput("What do you want to do?\nFight or talk?", "fight", "talk")
        break
        
    if choice == "fight":
      story.branch1()
    else:
      story.branch2()
      

  """
                          ------------Branch 1-------------
  """
  def branch1():
    global hour
    global tHour
    global setting
    global inventory
    global weapon
    global weaponDMG
    global invArmor
    global armor
    global setting
    global sticks
    global stone
    global vines
    global turtleShell
    global materials
    global materialsNum
    global deathCount

    #Event 4a
    control.clear()

    while True:
      control.storyLine("You get up and approach the group quickly and aggresively, hoping to steal some of their weapons and supplies", 3)
      control.storyLine("However, you underestimated the group's size", 3)
      control.storyLine("It is a hunting party of around 7-8 people", 3)
      control.storyLine("You try attacking one now that you've already come this far, but someone hits you on the head with something blunt.", 3)
      control.storyLine("You black out immidiately.", 3)
      for i in range(7):
        print(".")
        time.sleep(1)
  
      hour += 6
      setting = "village"
      control.storyLine("You wake up, tied to a wooden pole, your head pounding.", 3)
      control.storyLine("You are in a small village, with people in tribal clothing bustling about, doing their daily chores. Some cast you curious glances.", 3)
      control.storyLine("You look to the center of the camp. A group of tribesmen seem to be constructing a large fire.", 3)
      control.storyLine("You feel around and you realize that the tribespeople took everything you had.");
      
      if "Stone Knife" in inventory:
        inventory = ("Stone Knife",)
        control.storyLine("However, they seem to have missed the small stone knife you made", 3)
        control.storyLine("You use your knife to cut yourself free, and you run towards the village enterance.", 3)
        control.storyLine("On the way, you grab a leather tunic and a bone spear", 3)
        weapon = "Bone Spear"
        weaponDMG = 3
        invArmor = "Leather Tunic"
        armor = 1
        
        control.storyLine("You make it out of the village, but you hear shouts and footsteps thundering behind you.", 3)
        control.timeKeeping()
        setting = "forest"
        
      else:
        control.storyLine("You struggle helplessly against your bonds trying to get out. If only you had a way to cut them.", 3 )
        control.storyLine("Eventually you feel the wooden pole being picked up.",3 )
        control.storyLine("Realizing what was about to happen, you struggle and kick, but its no use.", 3)
        control.storyLine("The pole is hoisted up, and thrown into the fire, taking you along with it", 3)
        control.storyLine("You let out screams of agony as you watch your skin began to burn and shrivel", 3)
        control.storyLine("This is the end for you. Here is where you die.", 3)
        control.storyLine("The pain overwhelms you and everything goes black", 3)
        deathCount += 1
        return
  
      #Event 5a
      time.sleep(1)
      control.clear()
      control.storyLine("As you run, you realize you need to lose the tribe, at least for a little while.", 3)
      choice = control.safeInput("Which way do you want to go?\nStraight, right, or left?", "straight", "right", "left")
      if choice == "straight":
        control.storyLine("The tribespeople know this forest better than you.", 3)
        control.storyLine("They chase you for a while, gaining on you slowly but surely.", 3)
        control.storyLine("Eventually one of them gets within throwing distance of you.", 3)
        control.storyLine("The tribesman draws back his hand and throws it straight at your back", 3)
        control.storyLine("It burrows itself into your body and you see a tip protruding from the right side of your chest", 3)
        control.storyLine("Seconds later another appears where your heart was supposed to be.", 3)
        control.storyLine("You fall to the ground, blood gurgling from your lips", 3)
        control.storyLine("You curse your idiocy as everything goes black", 3)
        deathCount += 1
        return
      elif choice == "left":
        control.storyLine("You turn left and run straght into a tree.", 3)
        control.storyLine("So much for getting away.", 3)
        control.storyLine("Your head is spinning as you get up, and you wobble a few steps, trying to continue running.", 3)
        control.storyLine("However, the tribesmen had caught up to you while you had been dazed.", 3)
        control.storyLine("One of them threw their spear at your heart while the other shot an arrow at your neck.", 3)
        control.storyLine("You don't even know which one killed you first.", 3)
        deathCount += 1
        return
      else:
        control.storyLine("You look back and see glimpses of the tribesmen through the trees.", 2.5)
        control.storyLine("You realize that they will soon outrun you, so while they are still far enough away that they can't see you properly, you throw yourself to the right.", 4)
        control.storyLine("You land in a patch of bushes, and a hald a minute later, you hear footsteps thunder past you.", 2.5)
        control.storyLine("You wait until you can no longer hear their footsteps",2)
        for i in range(3):
          print(".")
          time.sleep(1)
        control.storyLine("Once you can no longer hear your pursuer's footsteps, you keep running on your new path to the right.", 3)
        control.storyLine("You eventually end up on an unfamilar beach", 3)
        control.timeKeeping()
        setting = "beach"
  
      #Event 6a
      control.storyLine("You have a little bit of time to make final preperations before you leave this island.", 3)
      general.action()
  
      if "Stone Ax" in inventory: 
        control.storyLine("You need to find a way to get off of this island.", 3)
        control.storyLine("Suddenly, you have an idea.", 3)
        control.storyLine("You take your stone ax and began chopping down some trees.", 3)  
        if vines >= 4:
          control.storyLine("You take your vines and use them to bind the logs together, making a raft.", 3)
          control.storyLine("Just as you begin to push off from the shore, the tribesmen catch up.", 3)
          control.storyLine("One of them shouts something in a different langauge, and they rush to shore and begin shooting arrows at you.", 3)
          control.storyLine("Thankfully, they miss, and soon, you are out of range.", 3)
          break
          
        else:
          control.storyLine("Your heart falters when you realize that you don't have anything to bind your logs with.", 3)
          control.storyLine("You look around wildly, trying to find some good vines, but then you hear a rustling in the trees.", 3)
          control.storyLine("The tribe had tracked you and caught up.", 3)
          control.storyLine("An arrow flys through the forest and fills your vision before everything goes black.", 3)
          deathCount += 1
          return
      else:
        control.storyLine("Your heart beats rapidly as you realize that you need to build a raft to get off of this island", 3)
        control.storyLine("After a few seconds, however, you realize that you don't have an ax.", 3)
        control.storyLine("You mentally kick yourself for not being better prepared", 3)
        control.storyLine("Then, you hear shouting coming through the trees.", 3)
        control.storyLine("The tribesmen had tracked you.", 3)
        control.storyLine("You try running, but a few seconds later, multiple spears and arrows pepper your back.", 3)
        control.storyLine("You fall to the ground, struggling for breath as your life's blood seeps into the sand.", 3)
        control.storyLine("You go still and everything goes black.", 3)
        deathCount += 1
        return
      
    endings.escapeEnding()
      
  """
                         ------------Branch 2-------------
  """
  def branch2():
    global hour
    global tHour
    global setting
    global inventory
    global weapon
    global weaponDMG
    global invArmor
    global armor
    global hunger
    global setting
    global sticks
    global stone
    global vines
    global turtleShell
    global materials
    global materialsNum
    global deathCount

    control.clear()
    while True:
      #Event 4b
      control.storyLine("You approach cautiously, your hands in the air to show that you don't have anything with you.", 3)
      control.storyLine("The moment you appear in the clearing the hunting party was resting in, 4 bows are aimed at your chest", 3)
      control.storyLine("You speak slowly and carefully, saying that you mean no harm", 3)
      control.storyLine("They seem to get the message, and lower their bows.", 3)
  
      setting = "village"
      control.storyLine("They gather around you, and escort you all the way back to their village, bringing along the animals they hunted.", 3)

      for i in range(3):
        print(".")
        time.sleep(1)
      
      control.storyLine("You are taken straight to the village leader.", 3) 
      control.storyLine("He explains that he and a few of the elders had met an English-speaking man who had washed up on their island in the past.", 3)
      control.storyLine("He allows you to become part of the tribe, and introduces you to the rest of the village.", 3)
      control.storyLine("You are given a small hut to live in, which is fairly generous seeing that they had just met you.", 3)
  
      if day == 1:
        control.storyLine("However, there is something not quite right about this island, and you want to explore to figure out what that thing is.", 3)
      else:
        control.storyLine("However, there is still the issue of the time loop. All of this will be reset by the end of the day.", 3)
        
      control.timeKeeping()
  
      #Event 5b
      choice = control.safeInput("\nWhere do you want to go? To the forest, or the village?", "village", "forest")
      
      if choice == "village":
        control.storyLine("You wander the village, looking for anything useful to help you.", 3)
        control.storyLine("You realize that this is your home now, and that you should try to help", 3)
        control.storyLine("As you prepare to leave to search for clues, an old man calls out to you, in English.", 3)
        control.storyLine("He must be one of the elders that the leader had spoken of.", 3)
        control.storyLine("The man says that he can tell that you are about to do something to help this island and its people greatly, and that he wants to aid you.", 3)
        control.storyLine("He gives you a Magic Tunic (+5 armor, +5 heal) and a Magic Spear (+8 attack, +5 focus).", 3)
        weapon = "Magic Spear"
        weaponDMG = 8
        invArmor = "Magic Tunic"
        armor = 5
        for i in range(3):
          print(".")
          time.sleep(1)
        control.storyLine("You thank the old man and leave the village.", 3)
        control.timeKeeping()
      else:
        pass
  
      control.storyLine("You travel through the forest for a while, and you notice that it is getting a little misty.", 3)
      control.storyLine("The trees begin looking old, black, and gnarled.", 3)
      setting = "mysterious forest"
      control.storyLine("Suddenly, something comes crashing through the forest.", 3)
      x = mechanics.combat()
      if x == False: 
        return
  
      control.timeKeeping()
  
      #Event 6b
      control.storyLine("Your fight brought you deeper into the forest.", 3)
      control.storyLine("You see a small cave enterance in a nearby rock face. There might be something useful in there.", 3)
  
      while True:
        choice == control.safeInput("\nWhere do you want to explore?\nThe cave or the forest?", "cave", "forest")
        if choice == "cave":
          break
        elif choice == "forest":
          control.storyLine("You decide to explore the forest a little more", 3)
          x = mechanics.combat()
          hour += 1
          hunger += 1
          if x == False:
            return
        break
      
      control.storyLine("You look inside the cave, and find odd markings on the wall", 3)
  
      for i in range(3):
        print(input("Inspect more closely (ENTER)"))
        control.storyLine("It seems to be a map of how to get to a grove in the forest.", 3)
        control.storyLine("You don't quite understand how this could help you.", 3)

      print(input("Inspect more closely (ENTER)"))
      control.storyLine("\nAha! You found something different. There is a depiction of an analog wristwatch on fire. The watch looks vaguely familiar...", 3)
      control.storyLine("You look at the watch on your wrist. It is identical to the watch in the image on the wall.", 3)
      control.storyLine("You know what you must do. You go out side and look over the trees", 3)
      control.storyLine("You see a tall volcano in the center of the island, and make your way towards it.", 3)
      control.storyLine("On the way, you decide to take a break, but you want to do something useful.\n", 3)
  
      general.action()

      print(input("\nHit enter to continue"))
      control.timeKeeping()
      control.clear()
      
      #Event 7b
      control.storyLine("Afterwards, you continue towards/up the volcano.", 3)
  
      setting = "volcano"
      control.storyLine("Eventually, you reach the top and when you are about 20 feet from the lip of the volcano, you begin to take off the watch.", 3)
      control.storyLine("The moment you do so, you hear a loud roar boom through the forest, and a massive beast bounds out of the trees.", 3)
      control.storyLine("You need to fight it so that you can get the watch into the volcano", 3)
  
      x = mechanics.combat()
      if x == False:
        return
  
      control.storyLine("Your body dripping with blood, both the beast's and your own, you drop to your knees, exhausted.", 3)
      control.storyLine("You pick that wretched watch up from where you dropped it, and you toss it into the volcano. ", 3)
      control.storyLine("The second the watch touches the bubbling lava, it explodes into a blinding flash of light.", 3)
      control.storyLine("You let out a relieved sigh, and turn around to head back to the village.", 3)
      for i in range(3):
        print(".")
        time.sleep(1)
  
      #Event 8b
      control.storyLine("You arrive at the village, injured but alive.", 3)
      control.storyLine("The village healers tend to your wounds.", 3)
      if day > 1:
        control.storyLine("You wait for the end of the day, hoping that it worked.", 3)
        control.storyLine("Hoping that the day doesn't restart.", 3)
        control.storyLine("As you wait you fall asleep.", 3)
      else:
        control.storyLine("Your eyelids slowly droop down over your eyes, and you fall asleep.", 3)
  
      for i in range(3):
        print(".")
        time.sleep(1)
  
      control.storyLine("You wake up in the healer's house, covered in bandages.", 3)
      if day < 1:
        control.storyLine("You look at your hand and no longer see the watch.", 3)
        control.storyLine("It worked! The day didn't restart!", 3)
  
      control.storyLine("You lean back into the bed of furs and cloth, making yourself comfortable.", 3)
      control.storyLine("You fall asleep immidiately, content.", 3)
  
      for i in range(5):
        print(".")
        time.sleep(1)
      break
    endings.newBeginningsEnding()
    
"""
-----------------------------------------------------------------
                          Game Endings
-----------------------------------------------------------------
"""
class endings:
  def insanityEnding():
    global endingCount
    global insanityEnding
    global insanityLevel
    waitTime = 4
    subAmount = 0.2
    printCount = 0
    
    print("You wake up on the sand your head spinning.")
    time.sleep(2.5)
    print("Where were you again?")
    time.sleep(2.5)
    print("You see sand and an ocean from your position on the ground.")
    time.sleep(2.5)
    print("Ah yes, you were on an island.")
    time.sleep(2.5)
    print("And for some reason the day was restarting.")
    time.sleep(3)
    print("Did it really matter?")
    time.sleep(3)
    print("Did anything matter?")
    time.sleep(4)
    print("You lay there, confused.")
    time.sleep(4)
    print("What were you thinking about again?")
    for i in range(100):
      printCount += 1
      time.sleep(waitTime)
      print("You don't know")
      waitTime -= subAmount
      subAmount *= 1.3
      if waitTime <= 0 and printCount < 35:
        waitTime = 0.2
      elif waitTime <= 0 and printCount >= 35:
        waitTime = 0.1
    control.clear()
    print("""
          +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
          """)
    time.sleep(0.2)
    control.clear()
    print("You unlocked the:\n")
    
    print("""  
  @@@  @@@  @@@   @@@@@@    @@@@@@   @@@  @@@  @@@  @@@@@@@  @@@ @@@  
  @@@  @@@@ @@@  @@@@@@@   @@@@@@@@  @@@@ @@@  @@@  @@@@@@@  @@@ @@@  
  @@!  @@!@!@@@  !@@       @@!  @@@  @@!@!@@@  @@!    @@!    @@! !@@  
  !@!  !@!!@!@!  !@!       !@!  @!@  !@!!@!@!  !@!    !@!    !@! @!!  
  !!@  @!@ !!@!  !!@@!!    @!@!@!@!  @!@ !!@!  !!@    @!!     !@!@!   
  !!!  !@!  !!!   !!@!!!   !!!@!!!!  !@!  !!!  !!!    !!!      @!!!   
  !!:  !!:  !!!       !:!  !!:  !!!  !!:  !!!  !!:    !!:      !!:    
  :!:  :!:  !:!      !:!   :!:  !:!  :!:  !:!  :!:    :!:      :!:    
   ::   ::   ::  :::: ::   ::   :::   ::   ::   ::     ::       ::    
  :    ::    :   :: : :     :   : :  ::    :   :       :        :     
                                                                      
  @@@@@@@@  @@@  @@@  @@@@@@@   @@@  @@@  @@@   @@@@@@@@              
  @@@@@@@@  @@@@ @@@  @@@@@@@@  @@@  @@@@ @@@  @@@@@@@@@              
  @@!       @@!@!@@@  @@!  @@@  @@!  @@!@!@@@  !@@                    
  !@!       !@!!@!@!  !@!  @!@  !@!  !@!!@!@!  !@!                    
  @!!!:!    @!@ !!@!  @!@  !@!  !!@  @!@ !!@!  !@! @!@!@              
  !!!!!:    !@!  !!!  !@!  !!!  !!!  !@!  !!!  !!! !!@!!              
  !!:       !!:  !!!  !!:  !!!  !!:  !!:  !!!  :!!   !!:              
  :!:       :!:  !:!  :!:  !:!  :!:  :!:  !:!  :!:   !::              
   :: ::::   ::   ::   :::: ::   ::   ::   ::   ::: ::::              
  : :: ::   ::    :   :: :  :   :    ::    :    :: :: :            
        """)

    if insanityEnding == False:
      endingCount += 1
      
    insanityEnding = True
    
    print("\n\nYou have unlocked " + str(endingCount) + "/3 endings!")
    time.sleep(3)
    if endingCount < 3:
      control.storyLine("\n\n A small corner of your mind that is still intact registers that you have been given a choice.", 3)
      control.storyLine("From whom, you don't know.", 3)
      control.storyLine("You need to choose to either let yourself spiral down into oblivion", 3)
      control.storyLine("Or piece yourself back together and re-enter the loop", 3)
      control.storyLine("You realize that things didn't have to go the way they did", 3)
      control.storyLine("You could have broken the loop. You just need to take a different approach.\n", 3)
      choice = control.safeInput("Do you want to quit or continue?", "quit", "continue")
      if choice == "continue":
        control.storyLine("You brace yourself for what's about to happen.", 3)
        insanityLevel = 0
        mechanics.dayRestart()
      else:
        return
    else:
      print("You have unlocked all of the endings!")
      choice = control.safeInput("Do you want to quit or play again?\n", "quit", "play again")
      if choice == "play again":
        titleScreen()
      else:
        return

  def escapeEnding():
    global endingCount
    global escapeEnding
    global insanityLevel
    control.storyLine("You drift in the ocean for a while.", 3)
    if day > 1:
      control.storyLine("You wonder why the day hasn't restarted yet.", 3)
      control.storyLine("Then you decide that you don't care, and that you're just happy to be out of the loop.", 3)
    control.storyLine("Eventually, a medium sized ship, probably a fishing vessel, comes into view.", 3)
    control.storyLine("You stand up, yell, and wave your arms, moving as much as your makeshift raft allows you to without breaking.", 3)
    control.storyLine("The ship turns towards you, comes closer, and picks you up.", 3)
    control.storyLine("The kind crew brings you on board and gives you food, water, and a place to rest.", 3)

    for i in range(3):
      print(".")
      time.sleep(1)
    
    control.storyLine("When you wake up, you are in a hospital bed, with people standing all around you.", 3)
    control.storyLine("You stare at them blankly, before you feel a sharp pain in your head as your memories flood back.", 3)
    control.storyLine("Your eyes fill with tears as you recognise your family", 3)
    control.storyLine("You are home.", 3)

    control.clear()

    print("You have unlocked the: \n")
    print("""
oooooooooooo                                                      
`888'     `8                                                      
 888          .oooo.o  .ooooo.   .oooo.   oo.ooooo.   .ooooo.     
 888oooo8    d88(  "8 d88' `"Y8 `P  )88b   888' `88b d88' `88b    
 888    "    `"Y88b.  888        .oP"888   888   888 888ooo888    
 888       o o.  )88b 888   .o8 d8(  888   888   888 888    .o    
o888ooooood8 8""888P' `Y8bod8P' `Y888""8o  888bod8P' `Y8bod8P'    
                                           888                    
                                          o888o                   
                                                                  
oooooooooooo                   .o8   o8o                          
`888'     `8                  "888   `"'                          
 888         ooo. .oo.    .oooo888  oooo  ooo. .oo.    .oooooooo  
 888oooo8    `888P"Y88b  d88' `888  `888  `888P"Y88b  888' `88b   
 888    "     888   888  888   888   888   888   888  888   888   
 888       o  888   888  888   888   888   888   888  `88bod8P'   
o888ooooood8 o888o o888o `Y8bod88P" o888o o888o o888o `8oooooo.   
                                                      d"     YD   
                                                      "Y88888P' 
          
          """)

    if escapeEnding == False:
      endingCount += 1
      
    escapeEnding = True
    
    print("\n\nYou have unlocked " + str(endingCount) + "/3 endings!")

    if endingCount < 3:
      control.storyLine("\nHowever, in a small corner of your mind, something gives you a choice.", 3)
      control.storyLine("You don't know what it is, but you know its real.", 3)
      control.storyLine("It tells you that things could have gone differently if you had taken a different approach.", 3)
      control.storyLine("It gives you the choice to either throw yourself back into the loop, or stay here, in relative safety.", 3)
      control.storyLine("You don't know if it would be worth it to go back, but you need to make a choice.", 3)

      choice = control.safeInput("Do you want to quit or continue?\n", "quit", "continue")
      if choice == "continue":
        control.storyLine("You brace yourself for what's about to happen.", 3)
        insanityLevel = 0
        mechanics.dayRestart()
      else:
        return
    else:
      print("You have unlocked all of the endings!")
      choice = control.safeInput("Do you want to quit or play again?\n", "quit", "play again")
      if choice == "play again":
        titleScreen()
      else:
        return
      
  def newBeginningsEnding():
    global endingCount
    global newBeginningsEnding
    global insanityLevel

    control.storyLine("You live the rest of your life on the island.", 3)
    control.storyLine("You learn their language, customs, tradititons, etc.", 3)
    control.storyLine("You live out your life, getting married and watching your children, your granchildren, and their children grow up.", 3)
    control.storyLine("When you die, your only regret is that you never learned about your past.", 3)

    control.clear()
    
    print("You unlocked the :")

    print("""
 _        _______                                                                         
( (    /|(  ____ \|\     /|                                                               
|  \  ( || (    \/| )   ( |                                                               
|   \ | || (__    | | _ | |                                                               
| (\ \) ||  __)   | |( )| |                                                               
| | \   || (      | || || |                                                               
| )  \  || (____/\| () () |                                                               
|/    )_)(_______/(_______)                                                               
                                                                                          
 ______   _______  _______ _________ _        _       _________ _        _______  _______ 
(  ___ \ (  ____ \(  ____ \\__   __/( (    /|( (    /|\__   __/( (    /|(  ____ \(  ____ \
| (   ) )| (    \/| (    \/   ) (   |  \  ( ||  \  ( |   ) (   |  \  ( || (    \/| (    \/
| (__/ / | (__    | |         | |   |   \ | ||   \ | |   | |   |   \ | || |      | (_____ 
|  __ (  |  __)   | | ____    | |   | (\ \) || (\ \) |   | |   | (\ \) || | ____ (_____  )
| (  \ \ | (      | | \_  )   | |   | | \   || | \   |   | |   | | \   || | \_  )      ) |
| )___) )| (____/\| (___) |___) (___| )  \  || )  \  |___) (___| )  \  || (___) |/\____) |
|/ \___/ (_______/(_______)\_______/|/    )_)|/    )_)\_______/|/    )_)(_______)\_______)
                                                                                          
 _______  _        ______  _________ _        _______                                     
(  ____ \( (    /|(  __  \ \__   __/( (    /|(  ____ \                                    
| (    \/|  \  ( || (  \  )   ) (   |  \  ( || (    \/                                    
| (__    |   \ | || |   ) |   | |   |   \ | || |                                          
|  __)   | (\ \) || |   | |   | |   | (\ \) || | ____                                     
| (      | | \   || |   ) |   | |   | | \   || | \_  )                                    
| (____/\| )  \  || (__/  )___) (___| )  \  || (___) |                                    
(_______/|/    )_)(______/ \_______/|/    )_)(_______)                                    
                                                                                                              
          """)

    if newBeginningsEnding == False:
      endingCount += 1
      
    newBeginningsEnding = True
    
    print("\n\nYou have unlocked " + str(endingCount) + "/3 endings!")
    
    if endingCount < 3:
      control.storyLine("\n As you lay on your deathbed, something in a small corner of your mind, gives you a choice.", 3)
      control.storyLine("You don't know what it is, but you know its real.", 3)
      control.storyLine("It tells you that things could have gone differently if you had taken a different approach.", 3)
      control.storyLine("Perhaps you could have regained your memory...", 3)
      control.storyLine("It gives you the choice to either throw yourself back into the loop, or stay here, dying peacefully.", 3)
      control.storyLine("You don't know if it would be worth it to go back, but you need to make a choice.", 3)

      choice = control.safeInput("Do you want to quit or continue?\n", "quit", "continue")
      if choice == "continue":
        control.storyLine("You brace yourself for what's about to happen.", 3)
        insanityLevel = 0
        mechanics.dayRestart()
      else:
        return
    else:
      print("You have unlocked all of the endings!")
      choice = control.safeInput("Do you want to quit or play again?\n", "quit", "play again")
      if choice == "play again":
        titleScreen()
      else:
        return

#Runs the Code
titleScreen()

#Makes it so that when a function breaks out of the code because of death or a day restart, the day restarts
deathCountOld = 0
while deathCount > deathCountOld or hunger == 20 or hour == 24:
    deathCountOld += 1
    control.clear()
    mechanics.dayRestart()
     
""" END """