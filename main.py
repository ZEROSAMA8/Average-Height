# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total_height=0
for height in student_heights:
  total_height=total_height+height

number=0
for numbers in student_heights:
  number= number+1
print(f"The avarage height is {round(total_height/number)}") 


