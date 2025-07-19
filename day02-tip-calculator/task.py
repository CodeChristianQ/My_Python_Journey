#My completed version 7/9/25
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100

tip_amount_per_person = bill * tip_percent / people
payment_total_per_person = tip_amount_per_person + bill / people
round(payment_total_per_person, 2)
print(f"Each person should pay ${payment_total_per_person}")
