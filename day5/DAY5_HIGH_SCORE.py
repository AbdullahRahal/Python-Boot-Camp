# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high = 0
for i in student_scores:
  if i >= high:
    high = i
  if high < student_scores[n]:
    high = student_scores[n]

print(f"The highest score in the class is: {high}")