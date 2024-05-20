# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
totalh = 0
runs = 0
for hights in student_heights:
  totalh += hights
  runs +=1
avrage = totalh / runs
print(f"total height = {totalh}")
print(f"number of students = {runs}")
print(f"average height = {round(avrage)}")