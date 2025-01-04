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

# Save the Score to a Leaderboard File
name = input("Enter your name: ")
with open("leaderboard.txt", "a") as file:
    file.write(f"{name}: {score}\n")
print("Your score has been saved to the leaderboard!")

# Function to Display Leaderboard
def display_leaderboard():
    try:
        # Read leaderboard data from the file
        with open("leaderboard.txt", "r") as file:
            scores = []
            for line in file:
                # Parse each line as "name: score"
                try:
                    name, score = line.strip().split(": ")
                    scores.append((name, int(score)))
                except ValueError:
                    print(f"Skipping invalid line in leaderboard file: {line}")

        # Sort scores in descending order
        scores.sort(key=lambda x: x[1], reverse=True)

        # Display the leaderboard
        print("\nLeaderboard:")
        print("-" * 20)
        for rank, (name, score) in enumerate(scores, start=1):
            print(f"{rank}. {name} - {score} points")

    except FileNotFoundError:
        print("Leaderboard file not found. No scores to display.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Display the leaderboard
print("\nWould you like to see the leaderboard? (yes/no)")
show_leaderboard = input("> ").strip().lower()
if show_leaderboard == "yes":
    display_leaderboard()
else:
    print("Thank you for playing!")
