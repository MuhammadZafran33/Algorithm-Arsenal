questions  = ("How many elements are in the periodic Table?: ",
"which animal lays the eggs?: ",
"what is the most abundant gas on the Earth atmosphare?: ",
"How many bones are in the Human body?: ",
"Which palnet in the solar system is the Hotest?: ")
options = (("A. 116","B. 117", "C. 118", "D. 119"),
("A. whale","B. Crocodile", "C.Elephant", "D. Ostrich"),
("A. Nitrogen","B. Oxygen", "C. Carbon-dioxide", "D. Nitrogen"),
("A. 206","B. 207", "C. 208", "D. 209"),
("A. Murcury","B.Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []
score = 0
question_num = 0
for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)



    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1