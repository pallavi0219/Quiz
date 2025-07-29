print("Welcome to the Easy Quiz!")
name = input("Your name: ")
college = input("Your college: ")
year = input("Your year: ")
score = 0
print("\n1. How many days are there in a week?")
ans1 = input("Answer: ")
if ans1 == "7":
    score += 1
print("\n2. What is your fav color?")
ans2 = input("Answer: ")
if ans2.lower() == "black":
    score += 1
print("\n3. What comes after A in the alphabet?")
ans3 = input("Answer: ")
if ans3.lower() == "b":
    score += 1
print("\n4. Which animal says 'bow'?")
ans4 = input("Answer: ")
if ans4.lower() == "dog":
    score += 1
print(f"\n{name} from {college}, you scored {score} out of 4!")

if score == 4:
    print(" Great job! You got all of them right!")
else:
    print("Good effort!better luck nxt time!")