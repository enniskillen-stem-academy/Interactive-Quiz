# Welcome Message
print("Welcome to the Quiz!")

# Initialize Score
score = 0

# Question 1
print("Question 1: What is the capital of France?")
answer1 = input("Your answer: ")
if answer1.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Oops, the correct answer is Paris.")

# Question 2
print("Question 2: What is 5 + 3?")
answer2 = input("Your answer: ")
if answer2 == "8":
    print("Correct!")
    score += 1
else:
    print("Oops, the correct answer is 8.")

# Final Score
print(f"Your final score is {score} out of 2.")
