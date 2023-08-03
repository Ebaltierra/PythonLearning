import random 

# random_integer = random.randint(1,10)
# print(random_integer)

# random_float = round(random.random()*5, 5)
# print(random_float)

# love_score=random.randint(1,100)
# print (f"Your love score is {love_score}")

# coin_status = random.randint(1,2)
# if coin_status==1:
#     coin_status="Heads"
# else:
#     coin_status="Tails"
    
# print(coin_status)
# num=1
# states_of_america=['Delaware', 'Pennsylvania']
# print(states_of_america[1])

# states_of_america.insert(1, "texas")

# print(states_of_america)


# Import the random module here
# import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# Name_count=len(names)
# Random_name = names[random.randint(0, Name_count-1)]
# print(f"{Random_name} is going to be paying the bill today!")

# dirty_dozen=["strawberries", 'spinach', 'kale', 'nectarines', ' apples', 
#              'grapes', 'peaches', ' cherries', 'pears', 'tomatoes', 'celery', 'potatoes']

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# first=int(position[0])
# second=int(position[1])
# Column=first-1
# row=second-1
# map[row][Column]='x'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
# print(f"\n\n\n{row1}\n{row2}\n{row3}")





rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

win="\n You win!"
lose = "\n You lose!"
draw="\n It's a draw"
#Write your code below this line 👇
print("What do you choose?"+
      '\nType 0 for Rock, 1 for Paper, or 2 for Scissors')
choice_pic=("Null")
choice = int(input("\n"))
AI_choice = random.randint(0,2)
if choice==0: 
    choice_pic=rock
elif choice==1:
    choice_pic=paper
elif choice==2: 
    choice_pic=scissors
    
if AI_choice==0: 
    AI_choice_pic=rock
elif AI_choice==1:
    AI_choice_pic=paper
elif AI_choice==2: 
    AI_choice_pic=scissors
    
print(f"You choose\n\n\n\n{choice_pic}")
print(f"AI choose\n\n\n\n{AI_choice_pic}")

if choice>=3 or choice<0:
    print("Invalid choice, you lose")
if choice==0:
    if AI_choice==0:
        print(draw)
    if AI_choice==1:
        print(lose)
    if AI_choice==2:
        print(win)
if choice==1:
    if AI_choice==0:
        print(win)
    if AI_choice==1:
        print(draw)
    if AI_choice==2:
        print(lose)
if choice==2:
    if AI_choice==0:
        print(lose)
    if AI_choice==1:
        print(win)
    if AI_choice==2:
        print(draw)