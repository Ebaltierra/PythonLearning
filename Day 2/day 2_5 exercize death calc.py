#  I was reading this article by Tim Urban - Your Life in
#  Weeks and realised just how little time we actually have.

#  https://waitbutwhy.com/2014/05/life-weeks.html

#  Create a program using maths and f-Strings that tells 
# us how many days, weeks, months we have left if we live until 90 years old.

#  It will take your current age as the input and output 
# a message with our time left in this format:

#  You have x days, y weeks, and z months left.

#  Where x, y and z are replaced with the actual calculated numbers.

#  Warning your output should match the Example Output format
#  exactly, even the positions of the commas and full stops/


# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆
Days= int(age) * 365
Weeks= int(age) * 52
Months= int(age) * 12
Days_left = ((90*365) - Days)
Weeks_left = ((90*52) - Weeks)
Months_left = ((90*12) - Months)
print(f"You have lived {Days} days, "
      + f"{Weeks} weeks, " 
      + f"and {Months} months.")
print(f"\nYou have {Days_left} days, "
      + f"{Weeks_left} weeks, " 
      + f"and {Months_left} months left till you are 90.")
#Write your code below this line 👇




