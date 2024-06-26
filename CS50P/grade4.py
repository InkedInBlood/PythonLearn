score = int(input("Score: "))

if 89 < score <= 100:
    print("Grade: A")
elif 79 < score < 90:
    print("Grade: B")
elif 69 < score < 80:
    print("Grade: C")
elif 59 < score < 70:
    print("Grade: D")
else:
    print("Grade: F")