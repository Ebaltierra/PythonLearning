import random
# fruits =["Apple", "Peach", "Pear", "Grapes"]
# for fruit in fruits:
#     print(fruit)
#     print (fruit)
#     print(fruits)

# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# number = -1
# Total_heights=0
# for heights in student_heights:
#     number=number+1
#     Total_heights=Total_heights+(student_heights[number])
# number+=1
# Average_height=round(Total_heights/number)
# print(Average_height)

#Write your code below this row 👇

def strCount():
    string=input(str("Input word here"))
    Letter_count=input(str("What letter are we counting for?"))
    print(str.count(string, Letter_count))
strCount()



