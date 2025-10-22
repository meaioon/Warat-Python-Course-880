import random

def test_random():
    random_number = random.randint(1, 100)
    print(random_number)
    
test_random()

# สุ่มเลขระหว่าง 0-9
test_random = random.randint(0, 10)

# รับค่าการทายเลขจากผู้ใช้
guess_number = input("What is your guess number (0 - 9) ? : ")

# condition ==> if-elif-else
if test_random == guess_number:
    print("นปโปะ หม่ำ หม่ำ, หม่ำ หม่ำ กู๊ดบอย, กู๊ดบอย หม่ำ หม่ำ, หม่ำ หม่ำ เก่งมาก, เก่งมาก เก่งมาก!")
elif guess_number < test_random:
    print("น้อยไปหน่อย พยายามเข้านะ!")
elif guess_number > test_random:
    print("มากไปละ อย่าให้มีครั้งที่สอง!")