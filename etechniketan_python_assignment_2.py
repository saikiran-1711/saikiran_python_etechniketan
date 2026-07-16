#task 33
s1 = "practice is important to perfectly learn python"
indexes = [ i for i,ch in enumerate(s1) if ch == 'p']
print(indexes)

#task 34

words = ["aba", "xyz", "1991", "aa", "madam", "python", "hi"]
count = 0
for w in words:
    if len(w) >=2 and w == w[::-1]:
        count += 1
print("Number of palindromes with length > 2:", count)

#task 35
s1 = "How much wood would a woolchuck chuck if a Woodcutter could chuck wood to build a wooden house to woo for his wife"
words = s1.split()
result = []
for w in words:
    if len(w) >=4 and w.lower().startswith('w'):
        result.append(w)
print(result)

#task 36

s1 = input("Enter a string: ")

char_count = {}

for ch in s1:
    if ch in char_count:
        char_count[ch] += 1   
    else:
        char_count[ch] = 1 
print(char_count)

# task 37

products = {'soap': 50, 'oil': 200, 'laptop': 60000, 'phone': 25000, 'mouse': 500}

costliest = max(products, key=products.get)

print("Costliest product is", costliest)

#task 38

d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New york'}
keys_to_remove = ['name', 'salary']

for key in keys_to_remove:
    if key in d:
        del d[key]

print(d)

#task 39

n = int(input("Enter a number: "))

while n >= 0:
    if n == 0:
        print("Blast!")
    else:
        print(n)
    n -= 1

#task 40
print("Welcome to the grade checker program!")

while True:
    marks = float(input("Enter your marks (0-100): "))
    if 90 <= marks <= 100:
        grade = "A+"
    elif 80 <= marks <= 89:
        grade = "A"
    elif 70 <= marks <= 79:
        grade = "B"
    elif 60 <= marks <= 69:
        grade = "C"
    elif 50 <= marks <= 59:
        grade = "D"
    elif 0 <= marks < 50:
        grade = "Fail"
    else:
        grade = "Invalid marks entered"

    print(f"Your grade is {grade}")
    choice = input("Do you want to check the grade for another marks?: ").strip().lower()
    if choice == "no":
        print("Thank you")
        break

#task 41
a = int(input("Enter a number: "))

if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
elif a % 3 == 0:
    print("Fizz")
elif a % 5 == 0:
    print("Buzz")
else:
    print(a)

#task 42
password = "mypassword"

attempts = 0
while attempts < 3:
    user_input = input("Enter your password: ")
    if user_input == password:
        print("Access granted")
        break
    else:
        attempts += 1
        if attempts == 3:
            print("Access denied")


            
#task 43
import random

print("Welcome to the Simple Coin Toss Game!")

while True:
    guess = input("Guess 'heads' or 'tails': ").strip().lower()
    while guess not in ["heads", "tails"]:
        print("Invalid input. Please enter 'heads' or 'tails'.")
        guess = input("Guess 'heads' or 'tails': ").strip().lower()

    toss = random.choice(["heads", "tails"])
    print("Coin shows:", toss)

    if guess == toss:
        print("You guessed it right!")
    else:
        print("Wrong guess!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "no":
        print("Thanks for playing!")
        break
