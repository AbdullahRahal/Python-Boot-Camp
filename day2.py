print("Welcome to the tip calculator")
bill = int(input("what was the total of the bill? $"))
tip = input("how much tip would you like to give? 10,12 or 15. ")
ppl = int(input("how many people is the bill to split the bill? "))

# get the tip as in %100
tip = int(tip) / 100
# find the total tip of the bill
bill_tip = float(bill) * tip
# find the total bill after adding the tip
bill += bill_tip
# splitting the bill on the number of people
total = bill / ppl
# print the output
print(f"Each person should pay ${round(total, 2)}")
