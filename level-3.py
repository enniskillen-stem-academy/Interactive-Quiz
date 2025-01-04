# Welcome Message
print("Welcome to the Quiz!")

# Questions and Answers
quiz = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is the largest planet in the solar system?", "answer": "jupiter"}
]

# Initialize Score
score = 0

# Loop Through Questions
for i, q in enumerate(quiz):
    print(f"Question {i+1}: {q['question']}")
    user_answer = input("Your answer: ")
    if user_answer.lower() == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Oops, the correct answer is {q['answer']}.")

# Final Score
print(f"Your final score is {score} out of {len(quiz)}.")

# Stretch: Save the Score to a Leaderboard File
name = input("Enter your name: ")
with open("leaderboard.txt", "a") as file:
    file.write(f"{name}: {score}\n")

print("Your score has been saved to the leaderboard!")
