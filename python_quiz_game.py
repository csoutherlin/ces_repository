# Define quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "correct_answer": "A"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. William Shakespeare", "B. Jane Austen", "C. Charles Dickens", "D. Mark Twain"],
        "correct_answer": "A"
    }
]

# Initialize score and lists to store correct and incorrect answers
score = 0
correct_answers = []
incorrect_answers = []

# Display and process each question
for idx, question in enumerate(questions, 1):
    print(f"\nQuestion {idx}: {question['question']}")
    for option in question['options']:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    # Check answer and update score and lists
    if user_answer == question['correct_answer']:
        print("Correct!")
        score += 1
        correct_answers.append(question['question'])
    else:
        print("Incorrect!")
        incorrect_answers.append(question['question'])

# Display final results
print("\nQuiz Complete!")
print(f"\nTotal Score: {score}/{len(questions)}")

print("\nCorrect Answers:")
for answer in correct_answers:
    print(answer)

print("\nIncorrect Answers:")
for answer in incorrect_answers:
    print(answer)

# Provide correct answers for the questions the user got wrong
print("\nCorrect Answers for Incorrectly Answered Questions:")
for question in questions:
    if question['question'] in incorrect_answers:
        print(f"{question['question']}: {question['correct_answer']}")
