from random import choice, sample
import numpy as np
import pandas as pd
Gold=2
HasSword=False
Health=5
break_first=False
HasStaff=False
HasDagger= False
Shop=False
break_fork=False
lucy_break1=False
lucy_break2=False
rested=False
beggar_friend=False
Lucifer_Health=10 
line_break=str("\n==================================================================")
print("⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄"
+ "\n⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠤⠤⠴⢶⣶⡶⠶⠤⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⠁"
+ "\n⠀⠻⣯⡗⢶⣶⣶⣶⣶⢶⣤⣄⣀⣀⡤⠒⠋⠁⠀⠀⠀⠀⠚⢯⠟⠂⠀⠀⠀⠀⠉⠙⠲⣤⣠⡴⠖⣲⣶⡶⣶⣿⡟⢩⡴⠃⠀"
+ "\n⠀⠀⠈⠻⠾⣿⣿⣬⣿⣾⡏⢹⣏⠉⠢⣄⣀⣀⠤⠔⠒⠊⠉⠉⠉⠉⠑⠒⠀⠤⣀⡠⠚⠉⣹⣧⣝⣿⣿⣷⠿⠿⠛⠉⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠈⣹⠟⠛⠿⣿⣤⡀⣸⠿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⣇⢰⣶⣿⠟⠋⠉⠳⡄⠀⠀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⢠⡞⠁⠀⠀⡠⢾⣿⣿⣯⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⢀⣿⣿⣯⢼⠓⢄⠀⢀⡘⣦⡀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⣰⣟⣟⣿⣀⠎⠀⠀⢳⠘⣿⣷⡀⢸⣿⣶⣤⣄⣀⣤⢤⣶⣿⡇⢀⣾⣿⠋⢀⡎⠀⠀⠱⣤⢿⠿⢷⡀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⣰⠋⠀⠘⣡⠃⠀⠀⠀⠈⢇⢹⣿⣿⡾⣿⣻⣖⠛⠉⠁⣠⠏⣿⡿⣿⣿⡏⠀⡼⠀⠀⠀⠀⠘⢆⠀⠀⢹⡄⠀⠀⠀"
+ "\n⠀⠀⠀⢰⠇⠀⠀⣰⠃⠀⠀⣀⣀⣀⣼⢿⣿⡏⡰⠋⠉⢻⠳⣤⠞⡟⠀⠈⢣⡘⣿⡿⠶⡧⠤⠄⣀⣀⠀⠈⢆⠀⠀⢳⠀⠀⠀"
+ "\n⠀⠀⠀⡟⠀⠀⢠⣧⣴⣊⣩⢔⣠⠞⢁⣾⡿⢹⣷⠋⠀⣸⡞⠉⢹⣧⡀⠐⢃⢡⢹⣿⣆⠈⠢⣔⣦⣬⣽⣶⣼⣄⠀⠈⣇⠀⠀"
+ "\n⠀⠀⢸⠃⠀⠘⡿⢿⣿⣿⣿⣛⣳⣶⣿⡟⣵⠸⣿⢠⡾⠥⢿⡤⣼⠶⠿⡶⢺⡟⣸⢹⣿⣿⣾⣯⢭⣽⣿⠿⠛⠏⠀⠀⢹⠀⠀"
+ "\n⠀⠀⢸⠀⠀⠀⡇⠀⠈⠙⠻⠿⣿⣿⣿⣇⣸⣧⣿⣦⡀⠀⣘⣷⠇⠀⠄⣠⣾⣿⣯⣜⣿⣿⡿⠿⠛⠉⠀⠀⠀⢸⠀⠀⢸⡆⠀"
+ "\n⠀⠀⢸⠀⠀⠀⡇⠀⠀⠀⠀⣀⠼⠋⢹⣿⣿⣿⡿⣿⣿⣧⡴⠛⠀⢴⣿⢿⡟⣿⣿⣿⣿⠀⠙⠲⢤⡀⠀⠀⠀⢸⡀⠀⢸⡇⠀"
+ "\n⠀⠀⢸⣀⣷⣾⣇⠀⣠⠴⠋⠁⠀⠀⣿⣿⡛⣿⡇⢻⡿⢟⠁⠀⠀⢸⠿⣼⡃⣿⣿⣿⡿⣇⣀⣀⣀⣉⣓⣦⣀⣸⣿⣿⣼⠁⠀"
+ "\n⠀⠀⠸⡏⠙⠁⢹⠋⠉⠉⠉⠉⠉⠙⢿⣿⣅⠀⢿⡿⠦⠀⠁⠀⢰⡃⠰⠺⣿⠏⢀⣽⣿⡟⠉⠉⠉⠀⠈⠁⢈⡇⠈⠇⣼⠀⠀"
+ "\n⠀⠀⠀⢳⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠈⢿⣿⣷⣌⠧⡀⢲⠄⠀⠀⢴⠃⢠⢋⣴⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⢠⠇⠀⠀"
+ "\n⠀⠀⠀⠈⢧⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣧⠐⠸⡄⢠⠀⢸⠀⢠⣿⣟⡿⠋⠀⠀⠀⠀⠀⠀⠀⡰⠁⠀⢀⡟⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠈⢧⠀⠀⠀⠣⡀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡇⢰⠁⠸⠄⢸⠀⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⢀⡞⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⢨⡷⣜⠀⠀⠀⠘⣆⢻⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⣠⠎⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠑⠦⣀⠀⠀⠀⠀⠈⣷⣿⣦⣤⣤⣾⣿⢾⠀⠀⠀⠀⠀⣀⠴⠋⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢄⡀⢸⣶⣿⡑⠂⠤⣀⡀⠱⣉⠻⣏⣹⠛⣡⠏⢀⣀⠤⠔⢺⡧⣆⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⢽⡁⠀⠀⠀⠀⠈⠉⠙⣿⠿⢿⢿⠍⠉⠀⠀⠀⠀⠉⣻⡯⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠲⠤⣀⣀⡀⠀⠈⣽⡟⣼⠀⣀⣀⣠⠤⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠉⠉⠉⢻⡏⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+ "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("============================================================")
print("Welcome to Hell!")
print(f"\nYou have {Health} health and {Gold} gold remaining")
print("\nYou gaze off into the fiery pits of hell and notice two things"
               +"\n"
               + "\nYou notice a castle off in the distance, and a forest set ablaze."
               +"\n"
               +"\nWhich do you travel to, the 'forest', or the 'castle'?")
#CHEAT, FOREST, OR CASTLE
while True:
    Choice_1= input("\n: ")
    if Choice_1==str("forest"):
        print("\nYou start your journey to the forest.")
        Choice_1=1
        print(line_break)
        break
    if Choice_1==str("castle"):
        print("\nYou make way to the castle")
        print(line_break)
        Choice_1=2
        break
    if Choice_1==str("cheat"):
        cheat_1=input("\n" +"\n: ")
        if cheat_1==str("sword"):
            print("\n" + "\nYOU HAVE OBTAINED THE SWORD")
            print(line_break)
            HasSword=True
            Choice_1=1
            break
        if cheat_1==str("Gold"):
            print("\nHOW MUCH GOLD WOULD YOU LIKE?")
            Gold_Cheat=input("\n" +"\n :  ")
            Gold += int(Gold_Cheat)
            print(f"\nYOU HAVE OBTAINED {Gold_Cheat} GOLD")
            print(line_break)
            Choice_1=1
        else: print("\nYOU DONT KNOW THE CHEATS!!")
        print("\nWould you like to travel to the 'forest' or 'castle'?")
        print(line_break)
        Choice_1=input("\n:  ")
        if Choice_1==str("forest"):
            print("\nYou start your journey to the forest.")
            print(line_break)
            Choice_1=1
            break
        if Choice_1==str("castle"):
            print("\nYou make way to the castle")
            print(line_break)
            Choice_1=2
            break
    else: 
        print("\nInvalid choice, try again!")
#FOREST
if Choice_1==1:
    print("\nYou enter the forest, leaves are set ablaze burning to the ground around you"
          +"\nYou peer into the hellfire that encommpasses you"
          +"\nOn a hill near you, you notice a dark save entrance"
          +"\nIn the forest around you, you notice a pedestal"
        +"\nYou spot a chest on the pedestal."
          +"\n"
          "\nDo you open it, yes or no, or instead travel to the cave?"
          + line_break)
    while True:
        Chest_decision=input("\n: ")
        if Chest_decision==str("yes"):
            print(
                "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀"
                + "\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠀⠀⠀"
                + "\n⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⠀⣉⠑⠀⠠⣤⣤⣤⣤⣤⠀⠀⠚⢉⠀⡀⠀⠀⠀"
                +"\n⠀⠀⣠⣴⣶⣶⠆⢀⣈⡉⠛⠀⠉⠀⠓⠒⠙⠛⠛⠛⠃⠒⠒⠀⠉⠠⠿⠦⠀⠀"
                +"\n⠀⣸⣿⣿⡿⠋⣠⡿⠋⠀⢸⣿⠏⢸⣿⣿⠁⢻⣿⠃⠈⢿⡿⠀⣶⣶⠀⣶⡤⠀"
                +"\n⠀⣿⣿⠟⢁⣼⠟⡁⢾⣧⠀⠋⠀⠈⢿⠇⠀⠀⠃⠀⠀⠘⠁⠀⢸⡟⠀⠙⠁⠀"
                +"\n⠀⠸⠋⣠⡿⠃⣴⡇⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀"
                +"\n⠀⠀⢰⡟⠀⢀⠀⠉⡀⠀⠀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⠀⠀⠀⠀"
                +"\n⠀⠀⠀⠀⠰⣿⡄⣴⣇⠀⣰⣇⠀⣰⣿⡇⠀⣴⡄⠀⢰⣆⠀⢰⣿⡄⢠⣷⡀⠀"
                +"\n⠀⠀⠀⣶⣶⣤⣤⣍⡉⢀⣉⠙⠀⠛⠛⠓⠐⠛⠓⠀⠛⠛⠂⠚⠛⠁⣈⣉⠁⠀"
                +"\n⠀⠀⠀⣿⣿⣿⣿⣿⠁⣼⣿⣿⣿⣿⣿⡇⢸⣿⠟⣿⡇⢸⣿⣿⣿⣿⣿⣿⠀⠀"
                +"\n⠀⠀⠀⠸⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⡇⢸⣿⠄⣿⡇⢸⣿⣿⣿⣿⣿⣿⠀⠀"
                +"\n⠀⠀⠀⠄⠹⣿⡿⠋⠀⠙⢿⣿⣿⣿⣿⡇⢸⣿⣤⣿⡇⢸⣿⣿⣿⣿⣿⠟⠀⠀"
                +"\n⠀⠀⠀⠀⠀⠉⠀⠺⠀⣧⡈⢻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣾⣿⣿⣿⡿⠃⣰⠀⠀"
                +"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀")
            print("\n"
            +"\nYOU HAVE BEEN ATTACKED BY A MIMIC DO YOU 'fight' OR 'run'")
            print(line_break)
            while True:
                Chest_fight_decision=input("\n:  ")
                if Chest_fight_decision==str("fight"):
                    print("\nWould you like to use your staff, sword, or hands?" + line_break)
                    while True: 
                        weaponchoice=input("\n: ")
                        if weaponchoice==str("staff"):
                            if HasStaff== True:
                                        print("\nYou use your staff imbued with power to bring the mimic to its knees. ")
                                        Gold += 5
                                        print("\n"
                                            +"\nPLUS 5 GOLD")
                                        print(f"You have {Gold} gold remaining")
                                        print(line_break)
                                        break_first=True
                                        break
                            elif HasStaff==False:
                                        print("\nYOU HAVE NO STAFF, THE MIMIC TOOK ADVANTAGE OF YOUR STUPIDITY AND DEALT TWO DAMAGE")
                                        Health = Health-2
                                        print(f"\nYou have {Health} health remaining")
                                        print("\nYou scramble out of the forest greatly harmed.")
                                        print(line_break)
                                        break_first=True
                                        break
                        if weaponchoice == str("sword"):
                            if HasSword==True:
                                        print("\nIn one fell swoop you pierce the heart of the mimic, killing it")
                                        Gold += 5
                                        print("\n"
                                            +"\nPLUS 5 GOLD")
                                        print(f"You have {Gold} gold remaining")
                                        print(line_break)
                                        break_first=True
                                        break
                            elif HasSword==False:
                                        print("\nYOU HAVE NO SWORD, THE MIMIC TOOK ADVANTAGE OF YOUR STUPIDITY AND DEALT TWO DAMAGE")
                                        Health = Health-2
                                        print(f"\nYou have {Health} health remaining")
                                        print("\nYou scramble out of the forest greatly harmed.")
                                        print(line_break)
                                        break_first=True
                                        break
                        if weaponchoice == str("hands"):
                            print("\nIt's made of wood, and your hands are made of flesh. "
                                  + "\n¯\_(O_O)_/¯")
                            Health = Health-2
                            print(f"\nYou have {Health} health remaining")
                            print("\nYou scramble out of the forest greatly harmed." + line_break)
                            break_first=True
                            break
                if Chest_fight_decision==str("run"):
                    print("\n"+ "\nSmart choice")
                    print("\n"
                        +"\nAs you run you stumble past a gold coin"
                        +"\n"
                        +"\nPLUS 1 GOLD")
                    print(line_break)
                    Gold+=1
                    break_first=True
                    break
                else: 
                    if break_first==True:
                        break
                    else: print("\nyou have made an invalid choice, try again")
        if Chest_decision== str("no"): 
                    print("\nYou continue along your path and it leads you on the trail to the castle")
                    print(line_break)
                    break
        if Chest_decision==str("cave"):
            print(line_break
                  +"\n ********************************************************************************"
                    +"\n*                    /   \              /'\       _                              *"
                    +"\n*\_..           /'.,/     \_         .,'   \     / \_                            *"
                    +"\n*    \         /            \      _/       \_  /    \     _                     *"
                    +"\n*     \__,.   /              \    /           \/.,   _|  _/ \                    *"
                    +"\n*          \_/                \  /',.,''\      \_ \_/  \/    \                   *"
                    +"\n*                           _  \/   /    ',../',.\    _/      \                  *"
                    +"\n*             /           _/m\  \  /    |         \  /.,/'\   _\                 *"
                    +"\n*           _/           /MMmm\  \_     |          \/      \_/  \                *"
                    +"\n*          /      \     |MMMMmm|   \__   \          \_       \   \_              *"
                    +"\n*                  \   /MMMMMMm|      \   \           \       \    \             *"
                    +"\n*                   \  |MMMMMMmm\      \___            \_      \_   \            *"
                    +"\n*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *"
                    +"\n*                    /'.,___________...,,'   \            \   \        \         *"
                    +"\n*                   /       \          |      \    |__     \   \_       \        *"
                    +"\n*                 _/        |           \      \_     \     \    \       \_      *"
                    +"\n*                /                               \     \     \_   \        \     *"
                    +"\n*                                                 \     \      \   \__      \    *"
                    +"\n*                                                  \     \_     \     \      \   *"
                    +"\n*                                                   |      \     \     \      \  *"
                    +"\n*                                                    \ms          |            \ *"
                    +"\n ********************************************************************************")
            print(line_break+ "\nYou make your way torwards the dark mass in the hillside."
                  +"\n")
            print(line_break)
            print("\nYou notice a pedestal in the center of the cave."
                  + "\nAs you approach you notice a staff floating on the pedestal"
                  +"\nThe staff comes to your grip."
                  +"\n" + "\nYOU HAVE OBTAINED THE STAFF" + line_break)
            HasStaff=True
            print("\nYou return to the entrance of the forest"
                  +"\n"
                  +"\nDo you open the chest?"
                  + line_break)
            continue
        if break_first==True:
            break
        else: print("\nyou have made an invalid choice, try again.")
#CASTLE FORK
print("\nYou make way to the castle")
print("\nAlong your path you encounter a fork in the road"
      +"\n "
      +"\nDo you continue left or right?")
print(line_break)
while True:
    fork=input("\n: ")
    if break_fork==True:
        break
    if fork==str("left"):
        print("\nYou continue left along the path")
        print(line_break)
        print("\nYou encounter a beggar along the path" +"\n"
              +"\nHe begs of thee only one coin.")
        print("\n" +
            "\nWill you give him a coin?" + line_break)
        while True:
            beggar=input(str("\n: "))
            if beggar== str("yes"):
                print("\nThe beggar thanks you for your graciousness.")
                Gold= Gold-1
                print(f"\nYou have {Gold} gold remaining" + line_break)
                beggar_friend=True
                break_fork=True 
                Shop=True
                break
            elif beggar== str("no"):
                print("\nThe beggar looks as you walk away, dissapointed." + line_break)
                Shop=True
                break_fork=True
                break
    if fork==str("right"):
        print("\nYou continue right along the fork")
        print(line_break)
        print("\nYou encounter a demon hoarding goods"
              +"\nHe speaks to you in an ancient language, offering a dagger for only two gold."
              +"\nWould you like to purchase?" +line_break)
        while True:
            dagger_purchase=input("\n: ")
            if dagger_purchase==str("yes"):
                Gold= Gold-2
                print("\nThe demon hands you a dagger" + "\nThe blade glimmers with an unrecognizable metal" 
                      + f"\nYou have {Gold} gold reamining" + line_break)
                HasDagger= True 
                break_fork=True 
                break
            elif dagger_purchase==str("no"):
                print("\nYou walk past the demons shop continuing along your path")
                break_fork=True
                break
            else: print("you have made an invalid choice, try again.")    
    else: 
        if break_fork==True:
            break
        else: print("you have made an invalid choice, try again.")
print("\nYou continue past the fork in the road")
if Shop==True:
    print("\nYou encounter a demon hoarding goods"
              +"\nHe speaks to you in an ancient language, offering a dagger for only two gold."
              +"\nWould you like to purchase?" +line_break)
    while True:
            dagger_purchase=input("\n: ")
            if dagger_purchase==str("yes"):
                Gold= Gold-2
                print("\nThe demon hands you a dagger" + "\nThe blade glimmers with an unrecognizable metal" 
                      + f"\nYou have {Gold} gold reamining" + line_break) 
                HasDagger=True
                break
            elif dagger_purchase==str("no"):
                print("\nYou walk past the demons shop continuing along your path")
                break
            else: print("you have made an invalid choice, try again.")    
print("\n"
+"\n   /\                                                        /|"
+"\n  |  |                                                      |  |"
+"\n /----\                                                    /----|"
+"\n[______]                                                  [______]"
+"\n |    |         _____                        _____         |    |"
+"\n |[]  |        [     ]                      [     ]        |  []|"
+"\n |    |       [_______][ ][ ][ ][][ ][ ][ ][_______]       |    |"
+"\n |    [ ][ ][ ]|     |  ,----------------,  |     |[ ][ ][ ]    |"
+"\n |             |     |/'    ____..____    '\|     |             |"
+"\n  \  []        |     |    /'    ||    '\    |     |        []  /"
+"\n   |      []   |     |   |o     ||     o|   |     |  []       |"
+"\n   |           |  _  |   |     _||_     |   |  _  |           |"
+"\n   |   []      | (_) |   |    (_||_)    |   | (_) |       []  |"
+"\n   |           |     |   |     (||)     |   |     |           |"
+"\n   |           |     |   |      ||      |   |     |           |"
+"\n /''           |     |   |o     ||     o|   |     |           ''|"
+"\n[_____________[_______]--'------''------'--[_______]_____________]")
print(line_break +"\n" +"\nYou come to the doors of the castle.")
print("\nDo you approach?" + line_break)
while True:
    Approach=input("\n: ")
    if Approach==("yes"):
        print("\nYou get closer")
        break
    if Approach==("no"):
        if rested==False:
            print("\nYou take your time to gather yourself, resting at a nearby campsite"
                +"\n"
                "The campfire heals you for 2 health")
            Health=Health+2
            print(f"You have {Health} health remaining")
            rested=True
            continue
        if rested==True:
            print("You are already well rested")
            continue
    else: print("you have made an invalid choice, try again.")
print("\n"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢯⣿⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⣽⢟⣕⢄⠀⠀⠀⠀⠀⠀⣧⠀⡀⠀⠀⠀⠀⢠⢮⡾⣽⡻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣮⣟⡼⡌⡆⠀⠀⠀⠀⡰⡵⠰⡃⠀⠀⠀⢠⢃⡻⣜⢯⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣮⡵⣫⡵⢹⠀⠀⠀⠻⡄⡧⣈⠚⠀⠀⠀⢸⢺⡗⣭⣛⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⡵⢞⣫⡆⡹⠀⠀⠀⢑⠥⡨⡐⠫⣢⠀⠀⢸⢺⣽⢚⡭⣯⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣶⣻⡭⣷⢣⠇⠄⠤⢀⠼⣄⣸⡌⡆⢠⡧⠀⠈⡷⣮⢯⣛⣶⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀"
+"\n⠀⠀⠈⠢⡀⠠⡒⠀⠂⠐⠀⠂⠀⣀⣴⢾⣿⣿⣿⣷⣚⣷⡿⣳⠛⠒⠒⠒⢇⠏⡚⠓⠈⢀⢬⠓⠒⠒⠚⢞⡯⣟⣶⣛⣿⣿⣿⣿⡦⣖⠀⠀⠀⠀⠂⠐⠀⡄⠀⠐⠁⠀⠀⠀"
+"\n⠀⠀⠀⠀⠘⡄⠈⠢⡀⢀⣠⡴⣟⢿⣹⢿⣺⣿⣟⣶⣛⡭⠛⠁⠀⠀⠀⠀⠈⣑⣜⡆⢔⣕⣁⠀⠀⠀⠀⠀⠙⢯⡞⣛⣾⣿⣿⣸⣿⣹⣿⠶⣤⡀⠀⡠⠊⢀⠎⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠈⣦⡴⣾⢯⡽⢾⡹⣾⣝⣾⣟⠫⠞⠋⡁⠤⠀⠒⠀⠉⠁⠀⠀⠀⢈⣷⣁⠀⠀⠀⠀⠉⠁⠐⠂⠤⢈⡙⠛⠯⣻⣾⣷⣏⢾⣻⢫⡽⣻⠶⣤⡂⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⣾⣯⣷⣯⣻⣿⣧⣿⣟⡕⢋⢠⠐⠊⠁⠀⡀⣤⢀⣲⣦⣭⣥⣤⣴⣶⣤⣴⣦⣤⣬⣭⣥⣖⣂⣤⣄⡀⠀⠁⠂⡄⡉⢪⣟⣿⣵⣯⣾⣭⣟⣏⣿⡄⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⢸⢿⣿⣿⣿⣯⣿⣿⢳⣾⠇⠋⢀⢠⠰⠘⢃⣡⣾⣿⣿⢿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣷⣮⣁⠃⠶⡄⡀⠁⠳⢹⣏⣿⣟⣿⣿⣾⣿⣿⣇⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⢸⣟⢟⢿⣝⣟⣻⢻⢿⠁⢀⠜⠋⠀⠀⣠⣿⣿⠏⣿⣧⡇⣸⣿⣟⣯⡿⣽⣻⡿⣽⣿⣏⢈⣼⣿⡟⣧⣝⢧⡀⠀⠁⠃⡄⠀⡏⡿⣻⣻⣻⡽⣫⢻⣿⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⢸⣿⢼⣱⢬⣙⡻⠭⣯⣦⣀⠑⠄⣀⣼⣿⣿⣮⠃⢿⣻⡿⣿⠟⣾⢷⣻⢯⣷⣟⣿⡻⣿⣿⣟⣿⠃⡾⣿⣷⡵⣄⢀⠔⢁⣠⣷⠿⢝⡚⡭⢮⣹⢿⡇⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⢿⣾⣹⢾⡱⣺⠭⣽⣱⢞⡿⣩⢿⣟⣳⣿⢿⣿⣿⣿⡽⡍⢸⣟⣯⣟⣿⢾⡽⣾⡇⠙⣺⣽⣿⣷⣿⣿⣷⢻⣷⣭⢻⣗⢦⣻⡱⣽⢚⣟⣦⣿⣿⠃⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⡸⢿⣿⣟⣧⣷⣹⢥⠷⣞⣱⢏⡾⣱⣎⠧⣽⡱⠯⣟⢿⡡⠈⣿⣳⢿⡾⣿⡽⣷⠃⢄⡧⣟⡝⡧⢿⣲⣙⣧⢳⡞⣧⠺⡭⣖⢿⣸⣏⣷⣿⣿⠏⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⢀⠜⠀⠠⠛⠿⣿⣿⣿⣿⣿⣵⣯⣾⢾⡳⣌⣿⢣⣝⣟⢣⠗⣝⢷⣿⣟⣯⣟⡷⣿⣿⡶⣫⣚⢖⡻⣵⣋⠷⣞⠼⣯⣳⣽⣯⣿⣿⣿⣿⣿⠿⠛⢅⠀⠑⡀⠀⠀⠀⠀"
+"\n⠀⠀⢀⠎⠀⡰⠁⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣷⣿⣋⣮⢷⡹⣌⣧⢿⢫⢵⣻⣟⣾⣽⣻⢷⡿⡽⣜⢻⢮⣕⢫⢷⣽⣎⣿⣿⣿⣿⣿⡿⡟⠉⠉⠀⠀⠀⠀⢢⠀⠘⠄⠀⠀⠀"
+"\n⠀⢀⠊⠀⡐⠀⠀⢀⣀⠀⠀⠀⢸⣿⣾⣿⣿⣿⣿⣿⣾⡷⢻⡹⣜⣣⣿⢫⢧⣿⣟⣾⣽⣿⢻⣞⣧⣏⡳⢯⣛⢾⣶⣿⣿⣿⣿⣿⣿⡇⢻⠀⠀⠀⢀⣀⠀⠀⠡⠀⠈⡄⠀⠀"
+"\n⠀⠌⠀⡰⠀⠀⠀⢸⣿⣷⣤⣀⠘⣿⣿⣿⣿⣿⣿⣽⣷⣿⣿⣿⣭⣷⣼⣟⣾⣻⣿⣯⢿⣏⣿⣿⣶⣾⣽⣻⣟⣿⣻⣿⣽⣿⣿⣿⣿⣇⡏⢀⣤⣴⡿⡝⠀⠀⠀⢣⠀⠘⡀⠀"
+"\n⠐⠀⢠⠁⠀⠀⠀⠀⠙⣷⣿⣻⣷⣿⣿⣿⣻⣟⣿⣯⣿⣿⣽⣯⣟⣭⣷⣿⣾⡿⣯⣿⢿⣿⣷⣿⣿⣼⣹⣿⣻⣿⣿⣽⣿⢿⣻⣽⣿⣿⢳⣿⣟⣟⠟⠀⠀⠀⠀⠀⠆⠀⢡⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣟⣿⣽⣿⣯⣷⣿⡾⣿⣶⣯⣟⠿⣟⣿⣻⣽⢿⣽⣻⣿⣻⣾⣳⢯⣟⣿⣻⣿⣿⣟⣿⣭⣛⣿⣳⣯⣿⣏⣾⣟⣾⣿⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⣿⣿⣟⣿⢿⣯⣟⣷⣻⣾⣽⣻⣾⡿⣷⣿⣻⣾⢿⣷⣿⢿⣻⣿⣻⣿⢿⣻⣾⣽⣾⣽⣻⣽⡿⣿⢷⣽⣿⣿⣿⢹⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣟⣿⣿⣿⣯⣿⣟⣿⣿⣿⣷⣿⣻⣾⣽⢿⣽⣻⢾⡿⣯⢿⣻⣽⢯⡿⣽⡻⣫⣵⣾⣾⣿⣟⣿⣿⢿⡟⣾⣿⣟⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣻⣽⣿⣯⣟⣿⣿⣿⡿⠟⢻⠟⡿⣾⣭⣽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠟⢛⠿⣿⣿⣿⣿⣿⢸⣿⡿⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⢿⣿⣟⣿⣿⣿⣿⠀⠀⢼⠠⠌⠘⣿⣿⣿⣿⡿⣿⣟⢿⣿⣿⣿⡋⠀⠄⡤⠄⠈⣿⣿⣿⣿⣼⢸⣿⣿⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣻⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⢿⣻⣯⣸⣷⣿⣿⣿⣷⣶⣷⣶⣾⣿⣿⣿⣿⢿⣾⣿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⢷⣿⣿⣿⣯⡿⢷⣿⣿⣿⣿⣿⣻⣷⣿⣿⣿⣿⣞⣿⣻⣽⢿⣿⣿⣷⣿⣟⣫⣿⣿⣿⣿⣷⡌⣻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣯⣿⣳⣿⣽⣻⣿⣻⡽⣟⣾⣳⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⣻⢾⣻⣟⡿⣿⡯⢿⣾⣿⣵⣿⡣⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣯⣷⡿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣟⣯⣯⣴⣿⣿⣿⣿⣿⣿⣿⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀"
+"\n⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⣿⣿⣿⣿⣿⣿⣿⡾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠄⠀"
+"\n⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠊⠠⠈⠈⣿⣷⣿⢻⣷⣿⣿⢿⣻⣿⡿⣿⣿⢿⣿⣻⣷⣿⡻⣿⡿⡏⣿⣷⣿⠃⠑⢄⠐⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⡰⠀⠀"
+"\n⠀⠀⢢⠀⠘⡀⠀⠀⠀⠀⠀⠀⡠⠐⢀⠔⠁⠀⠀⢸⣿⣿⣼⠂⢻⠃⣿⢻⣷⣿⣿⣾⣿⡟⣿⡟⢿⠋⣿⠁⣸⣿⣿⣿⠀⠀⠀⠑⠄⠑⢄⠀⠀⠀⠀⠀⠀⢀⠎⠀⡰⠁⠀⠀"
+"\n⠀⠀⠀⠡⡀⠈⢄⠀⢀⡠⠔⠊⠀⠀⠆⠀⠀⠀⠀⢸⣿⣿⣿⣷⣿⠀⣯⠀⡿⢹⠛⣿⠟⣷⣿⠃⣾⡄⠙⣶⣿⣿⣽⣿⠀⠀⠀⠀⠈⡄⠀⠈⠂⠄⣀⠀⢠⠊⠀⡐⠁⠀⠀⠀"
+"\n⠀⠀⠀⠀⠑⡀⠀⠪⡉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠘⣿⣿⢿⣿⢧⡚⣿⣤⡇⡸⠀⢿⠀⢹⣿⣦⣿⡇⣿⣿⣿⣿⣾⠇⠀⠀⠀⡀⠈⠉⠉⠉⠉⠉⠉⡙⠁⢀⠜⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠘⢆⠀⠘⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⢿⣿⣿⣿⣿⣷⣦⣿⣤⣾⣿⣿⣿⣿⡿⡜⣿⣷⡟⠀⠀⣴⣿⣿⣿⣶⡄⠀⠀⣠⠞⠀⣠⠆⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠈⠳⡄⠈⠃⠀⠀⣤⣤⡄⢠⠀⢠⡄⢨⣿⡿⣿⣯⠹⠻⣿⣿⣿⣿⣿⣿⢿⡿⣿⡿⣿⣽⣾⣿⢻⢧⣤⣼⣿⣵⣦⢨⣿⣿⣤⠞⠁⠀⠞⠁⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠐⢌⡉⠐⠢⡀⠀⠀⢰⠹⢿⣻⢿⣸⣄⢹⡻⢿⣿⣿⣿⡿⣿⣜⢿⣞⣿⣿⣳⠏⠉⠀⠀⠙⣿⠟⠀⣹⡇⡇⢀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡀⠈⠂⠄⡀⠑⠄⠘⠴⠉⣿⣟⣿⣧⣼⣧⣸⡆⣼⢀⣿⣿⣟⣧⡻⣿⣿⣷⣦⡰⠀⡠⠊⡠⡶⠈⣾⣿⠗⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠄⡀⠀⠁⠂⠆⠀⢌⠈⣿⣯⢿⡽⣯⣿⢿⡿⣾⣟⣿⣿⢿⣻⣮⣿⣾⡿⣦⣘⠂⠁⠀⣠⣾⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢀⡀⠀⠀⠀⠀⠁⠂⡄⢀⡀⠀⠁⠐⠛⠻⢽⣳⣟⣯⣟⣷⣻⣾⣽⠿⢿⣿⣞⣯⢿⡿⣿⣻⣿⢿⣟⢿⡿⠁⣀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠈⡆⠀⠀⠀⢀⠎⢠⠂⠈⠑⡀⠠⡀⠤⠤⠀⠀⠀⠀⠀⠀⠀⠠⠤⠄⢘⠙⠻⠯⢿⣟⣷⣯⡿⠾⠋⢀⠊⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⢠⠁⠀⢠⠊⠀⠈⠃⠀⠀⢀⠂⡠⠁⠀⠀⠀⠈⢄⠐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠁⡰⠁⠀⠀⠀⢢⠈⢄⠀⠀⠈⠊⠀⠁⠂⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠈⡄⠀⠘⢄⠀⠀⠀⢀⠠⠁⡐⠁⠀⠀⠀⠀⠀⠈⢂⠈⢄⠀⠀⠀⠀⠀⠀⠀⠀⡐⠁⠔⠀⠀⠀⠀⠀⠀⠡⡀⠢⡀⠀⠀⠀⢀⠄⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠐⢄⠀⠀⠉⠐⠂⠁⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠀⠢⠀⠀⠀⠀⠀⢀⠌⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠁⠒⠈⠀⠀⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠠⠄⠐⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠡⡀⠀⠀⢠⠊⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠀⠄⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠄⠐⠄⡠⠁⡠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠈⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
+"\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      ")
print("\nA thunderous boom echos from behind the doors as they swing open"
      +"\n"
      +"\nLucifer throws the doors open standing between you and the castle")
print("\n" + "\nWhat do you do?"
      "\n" + "\n talk, attack, call for friends, or run?" + line_break)
while True: 
    if Health<1:
        print("\nYOU HAVE DIED")
        quit()
    if Lucifer_Health<1:
        print("\nYou have killed the great lucifer")
        lucy_break2=True
        lucy_break1=True
        break
    lucifer_action= input("\n: ")
    if lucifer_action==str("talk"):
        print("\nLucifer does not deign talk to insects.")
        print("\nFor your insolence he blats you with brimfire"
              +"\n" +"\nYOU HAVE TAKEN 1 DAMAGE")
        Health = Health-1
        print(f"\nYou have {Health} health remaining" +line_break
              +"\nWhat do you try now?")
        continue
    if lucifer_action==str("attack"):
        print("\nWould you like to use your staff, sword, dagger,  or hands?" + line_break)
        while True: 
                        if Health<1:
                            print("\nYOU HAVE DIED")
                            quit()
                        if Lucifer_Health<1:
                            print("\nYou have killed the great lucifer")
                            lucy_break2=True
                            lucy_break1=True
                            break
                        weaponchoice=input("\n: ")
                        if weaponchoice==str("staff"):
                            if HasStaff== True:
                                        print("\nYou use your staff imbued with power to attempt to overpower lucifer dealing 3 damage. ")
                                        Lucifer_Health=Lucifer_Health-3
                                        print(f"\nYou have {Health} health remaining")
                                        print(f"\nLucifer has {Lucifer_Health} health remaining ")
                                        print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                                        break
                            elif HasStaff==False:
                                        print("\nYOU HAVE NO STAFF, LUCIFER TOOK ADVANTAGE OF YOUR STUPIDITY AND DEALT TWO DAMAGE")
                                        Health = Health-2
                                        print(f"\nYou have {Health} health remaining")
                                        print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                                        break
                        if weaponchoice == str("sword"):
                            if HasSword==True:
                                        print("\nYou use your sword imbued with power to attempt to overpower lucifer dealing 4 damage. ")
                                        Lucifer_Health=Lucifer_Health-4
                                        print(f"\nYou have {Health} health remaining")
                                        print(f"\nLucifer has {Lucifer_Health} health remaining ")
                                        print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                                        break
                            elif HasSword==False:
                                        print("\nYOU HAVE NO SWORD, LUCIFER TOOK ADVANTAGE OF YOUR STUPIDITY AND DEALT ONE DAMAGE")
                                        Health = Health-1
                                        print(f"\nYou have {Health} health remaining")
                                        print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                                        break
                        if weaponchoice == str("hands"):
                            print("\nYOU ARE FIGHTING SATAN WHAT WILL YOUR HANDS DO? "
                                  + "\nYOU ARE BLASTED WITH THE MIGHT OF HELL"
                                  +"\nYOU TAKE 3 DAMAGE")
                            Health = Health-3
                            print(f"\nYou have {Health} health remaining")
                            print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                            break
                        if weaponchoice==str("dagger"):
                            if HasDagger== True:
                                        print("\nYou use your Dagger imbued with the Crimson Cerulea to stab lucifer.")
                                        print("\n"
                                            +"\nYOU DEAL FIVE DAMAGE")
                                        Lucifer_Health=Lucifer_Health-5
                                        print(f"\nYou have {Health} health remaining")
                                        print(f"\nLucifer has {Lucifer_Health} health remaining ")
                                        print("\n"+ f"\nYour dagger breaks")
                                        print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                                        HasDagger=False
                                        break
                            elif HasDagger==False:
                                        print("\nYOU HAVE NO DAGGER, LUCIFER BLASTS YOU WITH FIRE DEALING THREE DAMAGE")
                                        Health = Health-3
                                        print(f"\nYou have {Health} health remaining")
                                        print("\n" + "\nWhat do you do?" + "\n" + "\ntalk, attack, call for friends, or run?" + line_break)
                                        break
                        else:
                            if lucy_break2==True:
                                break
                            else: print("\nyou have made an invalid choice, try again."+ line_break)
    if lucifer_action==str("call for friends"):
        if beggar_friend==True:
            print("\nThe beggar you took pity on comes to your aid" )
            print("\n" +"\n He uses the last of his strength to blast lucifer with a holy light" + "\nHe deals five damage ") 
            Lucifer_Health=Lucifer_Health-5
            print(f"\nLucifer has {Lucifer_Health} health remaining ")
            continue
        else: 
            print("\nYOU HAVE NO FRIENDS IN THIS HELLSCAPE" + line_break)
            continue
    if lucifer_action==str("run"):
        print("\nLUCIFER DOESN'T TAKE KINDLY TO WIMPS" + "\nLUCIFER DEALS 2 DAMAGE TO YOU")
        Health=Health-2
        print(f"\nYou have {Health} health remaining" + line_break)
        continue
    else: 
        if lucy_break1==True: break
        else: print("you have made an invalid choice, try again.")
print("\n"
+"\n                      _..._"
+"\n                     /MMMMM)"
+"\n                    (I8H#H8I)"
+"\n                    (I8H#H8I)"
+"\n                     \WWWWW/"
+"\n                      I._.I"
+"\n                      I._.I"
+"\n                      I._.I"
+"\n                      I._.I"
+"\n                      I._.I"
+"\n                      I._.I"
+"\n                      I._.I"
+"\n                      I.,.I"
+"\n                     / /#\ )"
+"\n                   .dH# # #Hb."
+"\n               _.~d#XXP I 7XX#b~,_"
+"\n            _.dXV^XP^ Y X Y ^7X^VXb._"
+"\n           /AP^   \PY   Y   Y7/   ^VA)"
+"\n          /8/      \PP  I  77/      \8)"
+"\n         /J/        IV     VI        \L)"
+"\n         L|         |  \ /  |         |J"
+"\n         V          |  | |  |          V"
+"\n                    |  | |  |"
+"\n                    |  | |  |"
+"\n                    |  | |  |"
+"\n                    |  | |  |"
+"\n _                  |  | |  |                  _"
+"\n( \                 |  | |  |                 / )"
+"\n \ \                |  | |  |                / /"
+"\n('\ \               |  | |  |               / /`)"
+"\n \ \ \              |  | |  |              / / /"
+"\n('\ \ \             |  | |  |             / / /`)"
+"\n \ \ \ )            |  | |  |            ( / / /"
+"\n('\ \( )            |  | |  |            ( )/ /`)"
+"\n \ \ ( |            |  | |  |            | ) / /"
+"\n  \ \( |            |  | |  |            | )/ /"
+"\n   \ ( |            |  | |  |            | ) /"
+"\n    \( |            |   Y   |            | )/"
+"\n     | |            |   |   |            | |"
+"\n     J | ___...~~--'|   |   |`--~~...___ | L"
+"\n     >-+<...___     |   |   |     ___...>+-<"
+"\n    /     __   `--~.L___L___J.~--'   __     )"
+"\n    K    /  ` --.     d===b     .-- '  \    H"
+"\n    \_._/        \   // I \\   /        \_._/"
+"\n      `--~.._     \__\\ I //__/     _..~--'"
+"\n             `--~~..____ ____..~~--'"
+"\n                    |   T   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    |   |   |"
+"\n                    I   '   I"
+"\n                     \     /"
+"\n                      \   /"
+"\n                       \ /"
)
print(line_break + "\n"+"\nYOU HAVE KILLED THE MIGHTY LUCIFER AND MAY NOW TAKE THE TITLE AS KING OF HELL")