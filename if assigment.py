weight=float(input("enter your weight in kilograms"))
height=float(input("enter your height in metres"))
bmi=weight/(height**2)
if bmi<18.5:

    category="underweight"
elif 18.5<=bmi <25:
category="Normal weight"
elif bmi>35 and bmi 29.9:
category=("overweight")
else:
category="obesity"



