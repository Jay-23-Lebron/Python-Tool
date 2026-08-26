#dict_demo.py
#Python dictionary practice exercises


# Exercise 1: Create a dictionary storing student name and score
student_dict={
    "Oliver":88,
    "Liam":76,
    "Noah":92
}
print(student_dict)
print(student_dict["Noah"])


# Exercise 2: add, modify, delete, dictionary items
# add new student Ethan with score 85
student_dict["Ethan"]=85
# update Liam's score to 79
student_dict["Liam"]=79
# delete student Oliver
del student_dict["Oliver"]
print(student_dict)


# Exercise 3: loop through dictionary, print name and score
for name, score in student_dict.items():
    print(f"Student:{name}, Score:{score}")


# Exercise 4: simple query system, input name to search score
user_input=input("Please enter student name:")
if user_input in student_dict:
    print(f"Score:{student_dict[user_input]}")
else:
    print("Student not found")