from question import Question

#This is a quiz made from strings, Objects used with the question.py file import above.
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple/Blue\n(c) Orange/Yellow\n\n",
    "What color are bananas?\n(a) Green\n(b) Purple\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Red\n(b) Blue\n(c) Orange\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(question):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")
    

run_test(questions)



