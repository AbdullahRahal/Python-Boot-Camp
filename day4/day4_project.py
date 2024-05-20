import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
user = input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors:\n")
cpu = random.randint(0, 2)
user = int(user)
if user <= 2:
    print(f"your choice is {choices[user]}")
else:
    print("Wrong value please read the instructions and start over!")
if user == 0:
    if cpu == 0:
        print(f"Computer choice is {choices[cpu]}")
        print("It's a draw!")
    elif cpu == 1:
        print(f"Computer choice is {choices[cpu]}")
        print("Computer wins...")
    else:
        print(f"Computer choice is {choices[cpu]}")
        print("You Win!")
elif user == "1":
    if cpu == 0:
        print(f"Computer choice is {choices[cpu]}")
        print("You Win!")
    elif cpu == 1:
        print(f"Computer choice is {choices[cpu]}")
        print("It's a draw!")
    else:
        print(f"Computer choice is {choices[cpu]}")
        print("Computer wins...")
else:
    if cpu == 0:
        print(f"Computer choice is {choices[cpu]}")
        print("Computer wins...")
    elif cpu == 1:
        print(f"Computer choice is {choices[cpu]}")
        print("You Win!")
    else:
        print(f"Computer choice is {choices[cpu]}")
        print("It's a draw!")
