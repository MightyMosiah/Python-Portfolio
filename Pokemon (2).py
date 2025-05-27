#Daniel Brookins
#11/21/24
#Pokemon Simulator

import random
pokemon_level = 0
pokemon_name ="Squirtle"
day = 1
#Int
#Functions⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# Main

def train():
      global pokemon_level
      print("You are training Squirtle")
      pokemon_level= pokemon_level+1
      print(pokemon_level)

def rest():
      global pokemon_level
      print("Squirtle is resting Zzzz")
      print(pokemon_level)

def gym_battle():
      print("Squirtle entered a gym battle!")
      outcome = random.randint(1,2)
      if outcome == 1:
            print(pokemon_name + "Won!")
            pokemon_level= pokemon_level+2
      if outcome == 2:
            print(pokemon_name + "Lost!")


def evolve():
      global pokemon_name
      if pokemon_level >= 10:
            print("Squirtle evolved into Wartorle!")
            pokemon_name ="Wartortle"
      if pokemon_level >= 20:
            print("Wartorle evolved into Blastoise!")
            pokemon_name = "Blastoise"

#Main
while True:
      print("Welcome to Pokemon Evolution,day:" +str(day))
      print("Select an activity for the day")
      print("""1.Train
            2.Gym Battle
            3.Rest(Display info)
            4.Quit""")
      activity = int(input("Activity for the day:"))
      if activity ==1:#Train
            train()
      elif activity == 2:
            rest()

      elif activity== 3:
            gym_battle()

      elif activity== 4:
            break






