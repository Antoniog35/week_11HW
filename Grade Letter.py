# Ask the user for a score
score = float(input("What is a numeric score (0 to 100)? "))

# Check if the score is valid
if score < 0 or score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
else:
    # Determine the letter grade
    if score >= 89.5:
        grade = 'A'
    elif score >= 79.5:
        grade = 'B'
    elif score >= 69.5:
        grade = 'C'
    elif score >= 59.5:
        grade = 'D'
    else:
        grade = 'F'

    # Display the result
    print(f"The letter grade for score {score} is: {grade}")
