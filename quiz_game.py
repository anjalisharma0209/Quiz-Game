questions = [
    {
    "question":"which keyword is used to define a function in python?",
    "options": ["def", "function","define","fun"],
    "answer": "def"
    },
    {
        "question":"what is the output of 'type(5)' in python?",
        "options": ["int", "str", "float","bool"],
        "answer":"int"
    },
    {
        "question":"what is the correct way to write a comment in python?",
        "options":["// This is a comment", "# This is a comment", "<!-- This is a comment-->", "/* This is a comment */"],
        "answer":"# This is a comment"
    },
    {
        "question": "How do you create an empty list in Python?",
        "options": ["list = {}", "list = []", "list = empty", "list = None"],
        "answer": "list = []"
    },
    {
        "question": "Which operator is used to calculate the remainder of a division?",
        "options": ["//", "%", "/", "**"],
        "answer": "%"
    },
    {
        "question": "Which function is used to get the length of a list in Python?",
        "options": ["size()", "len()", "length()", "count()"],
        "answer": "len()"
    },
    {
        "question": "What will be the output of `bool('False')` in Python?",
        "options": ["False", "None", "True", "Error"],
        "answer": "True"
    },
    {
        "question": "How do you convert a string to an integer in Python?",
        "options": ["toInt()", "int()", "convert()", "strToInt()"],
        "answer": "int()"
    },
    {
        "question": "Which of the following is used to create an infinite loop in Python?",
        "options": ["while(1)", "while True", "for(;;)", "loop()"],
        "answer": "while True"
    }
]

score = 0
def run_quiz():
    global score
    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}:{q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f"{idx}.{option}")

        #User se input lo
        answer = input("Enter your answer (1/2/3/4): ")

        # Input ko check kro
        if answer.isdigit():
            answer=int(answer)
            if 1<=answer<=len(q['options']):     #Valid option check karo
                if q['options'][answer -1] == q['answer']:
                    print("✅ correct!")
                    score +=1
                else:
                    print(f"❌ Wrong! Correct answer: {q['answer']}")
            else:
                print(" ⚠️  Invalid option! Try again.")
        else:
            print(" ⚠️  Please enter a valid number!")

def show_score():
    print("\n🎯 Quiz Completed!")
    print(f"✅ Your final score is: {score}/{len(questions)}")

def main():
    print("🎯 Welcome to the Python Quiz!")
    print("-----------------------------")
    run_quiz()
    show_score()

if __name__ == "__main__":
    main()

