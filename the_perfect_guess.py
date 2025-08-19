import random

# -------------------- BLUE TEAM 🤖 --------------------

n = random.randint(1, 100)

a = -1

blue_guesses = 1

print("🎯 Welcome to the Number Guessing Game!")

print("🤔 I'm thinking of a number between 1 and 100... Can you guess it?")

print("💙 It's now the turn of the Blue Team 🤖")

while a != n:

    try:
        a = int(input("💡 Enter your guess number from 1 to 100: "))

        if a > n:

            print("⬇️ Too high! Try a LOWER number.")

            blue_guesses += 1

        elif a < n:
            print("⬆️ Too low! Try a HIGHER number.")

            blue_guesses += 1

        else:
            print("🎉 Congratulations Blue Team! You guessed the correct number!")

            print(f"🏆 The number was: {n}")

            print(f"🔢 You guessed it in {blue_guesses} attempts!")

            print("🎮 Blue Team's turn has ended....\n")



    except ValueError:
        print("⚠️ Please enter a valid number!")




# -------------------- RED TEAM 😈 --------------------

n = random.randint(1, 100)

a = -1

red_guesses = 1

print("❤️ It's now the turn of the Red Team 😈")

while a != n:
    try:

        a = int(input("💡 Enter your guess number from 1 to 100: "))


        if a > n:

            print("⬇️ Too high! Try a LOWER number.")

            red_guesses += 1


        elif a < n:

            print("⬆️ Too low! Try a HIGHER number.")

            red_guesses += 1

        else:
            print("🎉 Congratulations Red Team! You guessed the correct number!")

            print(f"🏆 The number was: {n}")

            print(f"🔢 You guessed it in {red_guesses} attempts!")

            print("🎮 Red Team's turn has ended....\n")



    except ValueError:

        print("⚠️ Please enter a valid number!")




# -------------------- FINAL RESULT 🏁 --------------------

print("🏁 Final Result:")

if blue_guesses < red_guesses:

    print(f"💙 Blue Team 🤖 WINS with {blue_guesses} attempts! 🏆🎉")



elif red_guesses < blue_guesses:
    print(f"❤️ Red Team 😈 WINS with {red_guesses} attempts! 🏆🔥")
    


else:
    print(f"🤝 It's a TIE! Both teams guessed in {blue_guesses} attempts! 🎯")


print("The game is Ended......")

print("want to play again!!!")

