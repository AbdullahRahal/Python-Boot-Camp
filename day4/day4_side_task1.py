line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
position = position.lower()
if position[0] == "a":
  if position[1] == "1":
    map[0][0] = "X"
  elif position[1] == "2":
    map[1][0] = "X"
  elif position[1] == "3":
    map[2][0] = "X"
  else:
    print("Out of map range!")
elif position[0] == "b":
  if position[1] == "1":
    map[0][1] = "X"
  elif position[1] == "2":
    map[1][1] = "X"
  elif position[1] == "3":
    map[2][1] = "X"
  else:
    print("Out of map range!")
elif position[0] == "c":
  if position[1] == "1":
    map[0][2] = "X"
  elif position[1] == "2":
    map[1][2] = "X"
  elif position[1] == "3":
    map[2][2] = "X"
  else:
    print("Out of map range!")
else:
  print("Out of map range")
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")