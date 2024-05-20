# Write your code here 👇
fizz = "Fizz"
buzz = "Buzz"
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print(fizz + buzz)
        else:
            print(fizz)
    elif number % 5 == 0:
        print(buzz)
    else:
        print(number)
