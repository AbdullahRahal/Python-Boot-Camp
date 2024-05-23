logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# dectionary to add the names to it
buyers = {}

# print out the logo for the first time
print(logo)

# variables to hold the buyers names and their bet
buyer = ""
paid = 0

# variable to loop the program
run = 1

while run == 1:
    # ask for the required inputs
    buyer = input("what is the name of the buyer?")
    paid = int(input("how much would you like to pay?"))

    # adding the values to the dectionary
    buyers[buyer] = paid

    run = int(input("if there are more people want to join the auction please enter '1', otherwaise enter '0'."))

# a variable to hold the values of the dectionaries
prices = []

# a loop to go throw all the values
for values in buyers:
    prices += str(buyers[values])

# a loop to check and compaier the values with each other
highest = ""
for num in prices:
    for value in buyers:
        if highest == "":
            highest = value
        elif buyers[highest] < buyers[value]:
            highest = value

print(f"The winner is {highest} with bid of ${buyers[highest]}")
