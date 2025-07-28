#My completed solution 07/23/2025
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
else:
    print("You are a boomer")

#When we input 1994 nothing prints because we need to have >= and <= as one of our conditions.