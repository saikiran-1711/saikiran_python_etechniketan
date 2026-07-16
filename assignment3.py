
#MCQ answers 
#1. d
#2. c
#3. D
#4. D
#5. A
#6. C
#7. C




#code of 8
def introduce(name, age=None):
    if age is None:
        print("My name is", name + ".", "My age is secret.")
    else:
        print("My name is", name + ".", "I am", age, "years old.")

introduce("John", 20)
introduce("John")




#9 
def drop_minimum(*args):
    lst = list(args)
    lst.remove(min(lst))
    return lst

print(drop_minimum(5, -2, 8, 4, -5, 7, 10))




#10
def find_max(a, b, c):
    return max(a, b, c)

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    print(find_max(x, y, z))

main()




#11
add = lambda a, b: a + b
print(add(5, 7))




#12
fahrenheit = lambda c: c * 9 / 5 + 32
print(fahrenheit(25))




#13
try:
    with open("student.txt", "x") as f:
        f.write("Python is easy to learn.\n")
        f.write("File handling is important.\n")
        f.write("Practice makes perfect.")
except FileExistsError:
    print("File already exists.")
except Exception as e:
    print("Error:", e)



#14
with open("student.txt", "r") as f:
    print(f.read())

print()

with open("student.txt", "r") as f:
    for i, line in enumerate(f, start=1):
        print(f"Line {i}: {line.strip()}")



#15
with open("student.txt", "r") as f:
    words = f.read().split()

print("Total words:", len(words))



#16
with open("student.txt", "a") as f:
    f.write("\nPython file handling becomes simple with practice.")



#17
numbers = [7, 4, 0, -2, 3]
print(numbers)

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])
except IndexError:
    print("Invalid index.")




#18
#file mame is calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
