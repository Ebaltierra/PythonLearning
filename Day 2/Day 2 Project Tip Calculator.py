print("Welcome to the tip calculator.")
print("\nWhat was the total bill?")
bill=int(input("\n"))
print("\nHow many people are splitting the bill?")
people=int(input("\n"))
print("\nWhat tip would you like to provide?"
      +"\n10, 12, 15, 18, or 20?")
tip=int(input("\n"))
bill_2= (bill/people)
tip_2= (1 + tip/100)
total= round(bill_2*tip_2, 2)
print("\nEach person should pay $" + str(total))


