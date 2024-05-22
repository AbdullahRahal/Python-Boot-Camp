# Write your code below this line 👇
def prime_checker(number):
  if number / 1 == number and number / number == 1:
    if number == 3 or number == 2:
      print("It's a prime number.")
    elif number % 3 == 0 and number != 3:
      print("It's not a prime number.")
    elif number % 2 == 0 and number != 2:
      print("It's not a prime number.")
    else:
      print("It's a prime number.")

# Write your code above this line 👆
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
