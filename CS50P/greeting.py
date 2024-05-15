def greet(input):
    if "Hello" in input:
        return "Hello, there!"
    else:
        return "I'm not sure what you mean?"
        
        
greeting = greet("Hello comp man")
print("Yo,", greeting)