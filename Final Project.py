#Daniel Brookins
#1/15/25
#Final Project

# Int
import random
clan_loyalty = 0
ninja_skills = 0
ninja_name = "Kai"

#Functions

def loyalty(): # Builds friendship and respect between kai's ninja clan and Ninjao
    global clan_loyalty
    print(" Kai is training hard with his friends in he ninja clan you guys are the best of friends")
    clan_loyalty = clan_loyalty+1
    print("Friendship level:"+ str(clan_loyalty))

def train(): # Unlocks Kai's hidden spinjitzu
    global ninja_skills
    print("Kai has unlocked a part of his potential as a ninja")
    ninja_skills = ninja_skills+1
    print("Awesome ninja aura:"+ str(ninja_skills))

def ninja_battle(): # Defend the ninjago from rival ninja clans
        print("The village is being threatened by a rival clan protect it!")
        outcome= random.randint(1,2)
        if outcome== 1:
            print(ninja_name+"saved Ninjago from danger the village is proud of you and your ninja clan!")
            clan_loyalty+2
        if outcome== 2:
            print(ninja_name+"was knocked out but his  ninja  fiends  helped him save Ninjao")
            clan_loyalty+1

def rest():
     global ninja_skills
     print("Kai is resting being a ninja is hard Zzzzz")
     print("Kai's skill level is:"+ str(ninja_skills))


def Golden_ninja():# Unlocks golden ninja spinjitzu making you stronger"
    global ninja_name
    if ninja_skills >= 10:
        print("Kai unlocked his potential")
        ninja_name = "Unlocked Kai's spinjitzu"
    if  ninja_skills>= 20:
        print("Kai unlocked his full potential and is now  the golden ninja of the village")
        ninja_name = "Golden ninja"

#Main
while True: # Allows player to select activities to play
     print("Weclome to Legend of the Ninjago clan")
     print("Select an activity for the day")
     print(""" 1.Train
               2.Loyalty
               3.Protect the village
               4.Rest)
               5.Quit""")

     activity = int(input("Activity for the day:"))
     if activity == 1: # Train
        train()

     elif activity == 2:
            loyalty()

     elif activity == 3:
            ninja_battle()

     elif activity == 4:
            rest()

     elif activity == 5:
        break







