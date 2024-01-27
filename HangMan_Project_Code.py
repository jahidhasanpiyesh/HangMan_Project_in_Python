import time
name = input("What is Your Name :")
input(f'Hello, {name} Time to play Hangman!')
print("Start This Hangman Game .......")
time.sleep(0.5)

word = "spider"
user_gases = ""
count = 5
while count > 0:
    failed = 0
    for char in word:
        if char in user_gases:
            print(char, end=" ")
        else:
            print("-", end=" ")
            failed += 1

    if failed == 0:
        print(f"\n Congratulations {name} You Win")
        break
    gus = input("You guess a character:")
    Convert_data = gus.lower()
    user_gases += Convert_data

    if Convert_data not in word:
        count -= 1
        print(" You Wrong ")
        print(f'your Chance is {count} Time')
        if count == 0:
            print("You Fail ")
