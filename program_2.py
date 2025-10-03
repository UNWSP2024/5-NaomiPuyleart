# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
import random

def math_quiz():
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = int(num1 + num2)
    print(num1, "+", num2, "=")
    answer = int(input("What is the answer? "))
    if correct_answer == answer:
        print("Correct!")
    else:
        print("Incorrect! The answer was: ", correct_answer)


input("Press enter to receive a math quiz. ")
math_quiz()