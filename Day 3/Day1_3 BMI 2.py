# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_float= float(height)
weight_float= float(weight)
denom=(height_float**2)
bmi_real=float(weight_float/denom)
bmi = round(weight_float/denom)
if bmi_real<=18.5:
    print(f"Your BMI is {bmi}, " + "you are underweight.")
elif bmi_real<=25:
    print(f"Your BMI is {bmi}, "+"you have a normal weight.")
elif bmi_real<=30:
    print(f"Your BMI is {bmi}, "+"you are slightly overweight.")
elif bmi_real<=35:
    print(f"Your BMI is {bmi}, "+"you are obese.")
elif bmi_real>35:
    print(f"Your BMI is {bmi}, "+"you are clinically obese.")  