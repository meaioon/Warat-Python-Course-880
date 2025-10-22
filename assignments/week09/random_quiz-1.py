"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random

# สุ่มเลขระหว่าง 0-9
test_random = random.randint(1, 20)

print("--- เกมทายตัวเลข ทายใจคอมพิวเตอร์ ---")
print("--- ทายตัวเลขจำนวนเต็มมาสิตั้งแต่เลข 1 - 20 ---")
print("--- คุณมีโอกาสเพียงแค่ 6 ครั้งเท่านั้น ! ---")

for i in range(6):

    # รับค่าการทายเลขจากผู้ใช้
    print(f"ความพยายามครั้งที่ {i+1}")
    guess_number = int(input("What is your guess number (1 - 20) ? : "))

    # condition ==> if-elif-else
    if test_random == guess_number:
        print("นปโปะ หม่ำ หม่ำ, หม่ำ หม่ำ กู๊ดบอย, กู๊ดบอย หม่ำ หม่ำ, หม่ำ หม่ำ เก่งมาก, เก่งมาก เก่งมาก!")
        break
    elif guess_number < test_random:
        print("น้อยไปหน่อย พยายามเข้านะ!")
    elif guess_number > test_random:
        print("มากไปละ อย่าให้มีครั้งที่สอง!")
