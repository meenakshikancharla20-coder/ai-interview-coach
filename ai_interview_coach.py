import random
import json
import os

HISTORY_FILE = "interview_history.json"

questions = {
    "Tell me about yourself.": ["experience", "background", "skills", "passion", "career"],
    "What are your strengths?": ["strength", "good at", "skilled", "excel"],
    "What are your weaknesses?": ["weakness", "improve", "working on", "challenge"],
    "Why should we hire you?": ["hire", "value", "contribute", "unique", "fit"],
    "Where do you see yourself in 5 years?": ["future", "goal", "growth", "career", "plan"],
    "Describe a challenging project you worked on.": ["challenge", "project", "problem", "solved", "learned"],
}

def get_feedback(answer, keywords):
    word_count = len(answer.split())
    feedback = []
    score = 0

    
    if word_count < 15:
        feedback.append("Your answer is quite short. Try to elaborate more with specific examples.")
        score += 1
    elif word_count > 150:
        feedback.append("Your answer is a bit long. Try to be more concise and focused.")
        score += 2
    else:
        feedback.append("Good length for your answer.")
        score += 4


    answer_lower = answer.lower()
    matched = [kw for kw in keywords if kw in answer_lower]

    if matched:
        feedback.append(f"Good, your answer touches on relevant points like: {', '.join(matched)}.")
        score += min(len(matched), 4)
    else:
        feedback.append("Try to include more specific, relevant details related to the question.")

    
    filler_words = ["um", "like", "you know", "maybe", "i guess", "sort of"]
    fillers_found = [f for f in filler_words if f in answer_lower]
    if fillers_found:
        feedback.append(f"Try to avoid filler words like: {', '.join(fillers_found)}. They reduce confidence.")
        score += 0
    else:
        score += 2

    score = min(score, 10)
    return feedback, score

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(session_results):
    history = load_history()
    history.append(session_results)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def mock_interview():
    print("===== AI Interview Coach =====")
    print("Answer each question as if you're in a real interview.\n")

    selected_questions = random.sample(list(questions.keys()), 3)
    total_score = 0
    session_results = []

    for i, q in enumerate(selected_questions, start=1):
        print(f"\nQuestion {i}: {q}")
        answer = input("Your answer: ")

        feedback, score = get_feedback(answer, questions[q])
        total_score += score

        print(f"\n--- Feedback (Score: {score}/10) ---")
        for point in feedback:
            print(f"- {point}")
        print("-" * 40)

        session_results.append({"question": q, "answer": answer, "score": score})

    average_score = round(total_score / len(selected_questions), 1)
    print(f"\nMock interview complete! Your average score: {average_score}/10")

    save_history({"average_score": average_score, "questions": session_results})

    
    history = load_history()
    if len(history) > 1:
        past_avg = [session["average_score"] for session in history[:-1]]
        overall_avg = round(sum(past_avg) / len(past_avg), 1)
        print(f"Your average score across {len(history)-1} previous session(s): {overall_avg}/10")
        if average_score > overall_avg:
            print("You're improving! Keep practicing.")
        else:
            print("Keep practicing to improve your score.")

def main():
    while True:
        print("\n1. Start Mock Interview")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            mock_interview()
        elif choice == "2":
            print("Good luck with your interviews! Goodbye.")
            break
        else:
            print("Invalid choice, try again.")

main()
