#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))
tip = float(input("What percentage would you like to tip?\nIt should be at least 20 or I will tell on you. "))
people = int(input("How many people are splitting the bill? "))

tip_percent = tip / 100
final_total = total * (tip_percent + 1)
split = round(final_total / people , 2)

print(f"Each person should pay ${split}")