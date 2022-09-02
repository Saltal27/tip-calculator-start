#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people_count = input("How many people to split the bill? ")

paid_tip = float(bill) * (float(tip) / 100)
total_bill = float(bill) + paid_tip
one_person_bill = total_bill / float(people_count)
final_bill = round(one_person_bill, 2)

print(f"Each person should pay: {final_bill} $")