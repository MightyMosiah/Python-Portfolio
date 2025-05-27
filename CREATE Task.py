
#4/2/25
#CREATETask
#Listsofvideogamegenredatasets
#Thisprogramusedatasetsfromhttps://en.wikipedia.org/wiki/List_of_best-selling_video_games
action=["GrandTheftAutoV(Action/Adventure)","RedDeadRedemption2(Action/Adventure)",
        "TheWitcher3(Action/Adventure/RPG)","TheElderScrollsV:Skyrim(Action/Adventure/RPG)",
        "SuperMarioBros.(Platformer)","NewSuperMarioBros.(Platformer)",
        "NewSuperMarioBros.Wii(Platformer)","TheLegendofZelda:BreathoftheWild(Action/Adventure)",
        "SuperSmash Bros.Ultimate(Fighting)","SuperMarioWorld(Platformer)",
        "SuperMarioBros.3(Platformer)","SonictheHedgehog(Action)","DuckHunt(Shooter)"]
shooter=["PlayerUnknown'sBattlegrounds(BattleRoyale/Shooter)","CallofDuty:ModernWarfare3(First-Person Shooter)","CallofDuty:Black Ops(First-Person Shooter)",
         "CallofDuty:BlackOpsII(First-Person Shooter)","CallofDuty:ModernWarfare2(First-Person Shooter)","CallofDuty:Ghosts(First-Person Shooter)"]
puzzle=["Tetris(EAMobile)(Puzzle)","Tetris(Nintendo)(Puzzle)","Pac-Man(Arcade/Puzzle)","Frogger(Arcade)","Lemmings(Puzzle)","BrainAge(Puzzle/BrainTraining)"]
sports=["WiiSports(Sports)","WiiFitandWiiFitPlus(Fitness/Exercise)","WiiSportsResort(Sports)","FIFA18(Sports)" "MarioKartWii(Racing)","MarioKart8/Deluxe(Racing)","MarioKartDS(Racing)","MarioKart7(Racing)","KinectAdventures!(Party)","WiiPlay(Party)"]
roleplaying=["PokémonRed/Green/Blue/Yellow(RPG)","PokémonGold/Silver/Crystal(RPG)","PokémonSun/Moon/UltraSun/UltraMoon(RPG)","PokémonDiamond/Pearl/Platinum(RPG)","PokémonRuby/Sapphire/Emerald(RPG)","DiabloIII(ActionRPG)","Borderlands2(ActionRPG)"]
platformer=["SuperMarioBros.(Platformer)","SuperMarioLand(Platformer)","SuperMarioWorld(Platformer)","SuperMarioBros.3(Platformer)","NewSuperMarioBros(Platformer)","NewSuperMarioBros.Wii(Platformer)"]

#importsrandomvideogamebasedontheusersinput
import random

#Searchesthroughvideogameslisttofindarandomgametorecommendtotheuserbasedonwhatgenretheyareintrestedin
filtered_list=[]
#Greetstheuserbywelcomingthemtotheprogram
print("Welcome to Best selling video game gere picker!")

#Userinputforbestvideogamegenrestheyareintrestedin
genre=input("What Best selling videogame genres are you intrested in?(Action/Adventure,FPS,Puzzle,Sports,RolePlaying,Platformer)")
print("hmmm let me see what I can find")

def video_games(g):


    if genre=="action":
        for i in range(len(action)):
            filtered_list.append(action[i])
        print(random.choice(filtered_list))

    if genre=="shooter":
        print(random.choice(shooter))
    if genre=="puzzle":
        print(random.choice(puzzle))
    if genre=="sports":
     print(random.choice(sports))
    if genre=="roleplaying":
        print(random.choice(roleplaying))
    if genre=="platformer":
        print(random.choice(platformer))

video_games(genre)









