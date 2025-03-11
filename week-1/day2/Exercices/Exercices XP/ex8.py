def play_quiz():
    data = [
        {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"
        }
    ]
    
    correct_answers = 0
    wrong_answers = []
    
    print("\nWelcome to the Star Wars Quiz!")
    print("Answer these questions about Star Wars. May the Force be with you!\n")
    
    for question_data in data:
        print(question_data["question"])
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == question_data["answer"].lower():
            correct_answers += 1
            print("Correct!\n")
        else:
            wrong_answers.append({
                "question": question_data["question"],
                "user_answer": user_answer,
                "correct_answer": question_data["answer"]
            })
            print("Wrong!\n")
    
    return correct_answers, wrong_answers

def show_results(correct_answers, wrong_answers):
    total_questions = 6
    print("\n=== Quiz Results ===")
    print(f"Correct answers: {correct_answers}/{total_questions}")
    print(f"Incorrect answers: {len(wrong_answers)}/{total_questions}")
    
    if wrong_answers:
        print("\nQuestions you got wrong:")
        for wrong in wrong_answers:
            print(f"\nQuestion: {wrong['question']}")
            print(f"Your answer: {wrong['user_answer']}")
            print(f"Correct answer: {wrong['correct_answer']}")
    
    if len(wrong_answers) > 3:
        print("\nYou had more than 3 wrong answers. You should try again!")
        if input("\nWould you like to play again? (yes/no): ").lower().startswith('y'):
            main()
    else:
        print("\nWell done! You're a true Star Wars fan!")

def main():
    correct_answers, wrong_answers = play_quiz()
    show_results(correct_answers, wrong_answers)

if __name__ == "__main__":
    main()