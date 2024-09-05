questions= ("How many elements are in the periodic talbe?: ",
            "Which animal lays the largeest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones in the human body?: ",
            "Which planet in the solar system is the hosttest?: ",)

options= (("A. 116","B. 117","C. 118","D. 119"),
          ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
          ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
          ("A. 206","B. 207","C. 208","D. 209"),
          ("A. Mercury","B. Venus","C. Earth","D. Mars"))

answers= ("C","D","A","A","B")
check = ("A","B","C","D")
guesses = []
score = 100
col= 0

row=1
for question in questions:
    print(f"{row}. {question}")
    for option in options[col]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()
    while not guess in check:
        print("Invalid input")
        guess = input("Please enter again (A, B, C, D): ").upper()
    guesses.append(guess)
    if not guess==answers[col]:
        score-=20
        print("Incorrect")
        print(f"The correct answer is: {answers[col]}")
    else:
        print("Correct")

    col+=1
    row+=1
print(f"Your final score is: {score}")


