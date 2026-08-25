#Development environment verification: test input-output and branch logic
print("===Environment Check Start===")

#Test 1: input and f-string format
username=input("Please enter your name:")
print(f"Your input name is {username}")

#Test 2: if branch statement
if len(username)>0:
    print("Valid input")
else:
    print("You entered nothing")

print("===Environment Check End===") 