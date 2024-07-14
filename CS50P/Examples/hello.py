#ask user for name, remove whitespace from str, and capitalize users name (each new word)
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

#say hello to user
print(f"Hello, {name}!")