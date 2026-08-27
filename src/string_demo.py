# string_demo.py
# Python string operations practice


# Exercise1: basic string transform
message="Hello World"
print(message.upper())
print(message.lower())
print(message.strip())


# Exercise2: check substring exists
text="Programming is fun"
if "fun" in text:
    print("Keyword found")


# Exercise3: split string into list
raw_text="Apple,Banana,Cherry,Mango"
fruit_list=raw_text.split(",")
print(fruit_list)


# Exercise4: loop input, type "quit" to exit
while True:
    user_text=input("Input your text(type quit to exit):")
    if user_text=="quit":
        break
    clean_text=user_text.strip().upper()
    print(f"Processed text: {clean_text}")