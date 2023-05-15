print("\nWhat is your height in cm?")
height=int(input("\n: "))
print("\nHow old are you?")
age=int(input("\n: "))
if height>=120: 
    if age<12:
        ticket_price=5
    elif age<=18:
        ticket_price=7
    else: 
        ticket_price=12
    wants_photo= input("\nDo you want a photo taken? Y or N")
    if wants_photo==("Y"):
        ticket_price= ticket_price+3
    print(f"Your ticket will be {ticket_price} dollars")
else:
    print("You are too short to ride.")