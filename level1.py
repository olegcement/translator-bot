questions = [
    {"question": "Столица Польши?", "answer": "Warsaw"},
    {"question": "2 + 2 = ?", "answer": "4"},
    {"question": "Как по английски 'привет'?", "answer": "hello"}
]

score = 0

for q in questions:
    user_answer = input(q["question"] + " ")
    if user_answer.lower() == q["answer"].lower():
        print("Правильно!")
        score = score + 1
    else:
        print(f"Неправильно. Правильный ответ: {q['answer']}")

print(f"Итого: {score} из {len(questions)}")
if score == 0:
    print(f"У тебя {score}, попробуй еще раз!")
elif score == 1:
    print(f"У тебя {score}, уже лучше")
elif score == 2:
    print(f"У тебя {score}, ты почти у цели!")
elif score == 3:
    print(f"У тебя {score}, ты смог!")
    