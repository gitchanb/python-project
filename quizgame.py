#Show a question with 4 options (A, B, C, D)
#Player types their answer
#Says correct or wrong after each question
#Tracks score out of total questions
#At the end shows final score like "You got 3/5 correct!"
#Ask if they want to play again
quiz = [
    {"question": "Who is prime minister of india?", 
     "options": ["a)modi", "b)godi", "c)rahul", "d)yogi"], 
     "answer": "a"},

    {"question": "Who is president?", 
     "options": ["a)churmu", "b)burme", "c)murmu", "d)bruma"], 
     "answer": "c"},

    {"question": "Where does sun rise from?", 
     "options": ["a)east", "b)west", "c)south", "d)north"], 
     "answer": "a"},
]

score = 0

for question in quiz:
    print(question["question"])
    for option in question["options"]:
        print(option)
    a = input("write the answer: ")
    if a == question["answer"]:
        print("you are right!")
        score = score + 1
    else:
        print(f'wrong! correct answer is {question["answer"]}')

print(f"you got {score}/{len(quiz)} correct!")