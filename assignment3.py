
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



# cgpacalculator

def get_grade(marks):
    """Return grade and grade point based on marks."""

    if marks >= 90:
        return "O", 10
    elif marks >= 80:
        return "A+", 9
    elif marks >= 70:
        return "A", 8
    elif marks >= 60:
        return "B+", 7
    elif marks >= 50:
        return "B", 6
    elif marks >= 40:
        return "D", 4
    else:
        return "E", 0


def calculate_cgpa():
    print("\n" + "=" * 65)
    print("                    CGPACRAFT")
    print("                 CGPA CALCULATOR")
    print("=" * 65)

    # Number of subjects
    while True:
        try:
            number_of_subjects = int(
                input("\nEnter number of courses: ")
            )

            if number_of_subjects > 0:
                break
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    courses = []

    total_credits = 0
    total_weighted_points = 0
    reappear = False

    # details

    for i in range(number_of_subjects):

        print("\n" + "-" * 65)
        print("Course", i + 1)
        print("-" * 65)

        # Course name
        course_name = input("Enter course name: ")

        # Credits
        while True:
            try:
                credits = float(input("Enter credits: "))

                if credits > 0:
                    break
                else:
                    print("Credits must be greater than 0.")

            except ValueError:
                print("Please enter a valid number.")

        # Marks
        while True:
            try:
                marks = float(input("Enter final marks: "))

                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter valid marks.")

        # Get grade
        grade, grade_point = get_grade(marks)

        # Calculate weighted points
        weighted_points = credits * grade_point

        # Check reappear
        if grade == "E":
            reappear = True

        total_credits += credits
        total_weighted_points += weighted_points

        # Store course information
        course = {
            "name": course_name,
            "credits": credits,
            "marks": marks,
            "grade": grade,
            "grade_point": grade_point,
            "weighted_points": weighted_points
        }

        courses.append(course)

        print("\nResult:")
        print("Grade       :", grade)
        print("Grade Point :", grade_point)
        print("Points      :", weighted_points)

        if grade == "E":
            print("⚠ REAPPEAR REQUIRED")

    # cgpa calc

    cgpa = total_weighted_points / total_credits

    # result display

    print("\n\n" + "=" * 75)
    print("                         RESULT")
    print("=" * 75)

    print(
        f"{'Course':<25}"
        f"{'Credits':<10}"
        f"{'Marks':<10}"
        f"{'Grade':<10}"
        f"{'GP':<8}"
        f"{'Points':<10}"
    )

    print("-" * 75)

    for course in courses:

        print(
            f"{course['name'][:24]:<25}"
            f"{course['credits']:<10.1f}"
            f"{course['marks']:<10.1f}"
            f"{course['grade']:<10}"
            f"{course['grade_point']:<8}"
            f"{course['weighted_points']:<10.1f}"
        )

    print("-" * 75)

    print("Total Credits        :", total_credits)
    print("Total Weighted Points:", total_weighted_points)
    print("CGPA                 :", round(cgpa, 2))

    if reappear:
        print("\n⚠ WARNING: One or more courses have grade E.")
        print("   Reappear is required for those courses.")
    else:
        print("\n✓ No reappear required.")

    print("=" * 75)

    # result save

    save_result(
        courses,
        total_credits,
        total_weighted_points,
        cgpa,
        reappear
    )


def save_result(
    courses,
    total_credits,
    total_weighted_points,
    cgpa,
    reappear
):
    """Save the result to a text file."""

    choice = input("\nDo you want to save this result? (y/n): ").lower()

    if choice != "y":
        return

    try:

        with open("cgpa_results.txt", "a") as file:

            file.write("\n")
            file.write("=" * 75 + "\n")
            file.write("                     CGPACRAFT RESULT\n")
            file.write("=" * 75 + "\n")

            for course in courses:

                file.write(
                    "Course: " +
                    course["name"] +
                    "\n"
                )

                file.write(
                    "Credits: " +
                    str(course["credits"]) +
                    "\n"
                )

                file.write(
                    "Marks: " +
                    str(course["marks"]) +
                    "\n"
                )

                file.write(
                    "Grade: " +
                    course["grade"] +
                    "\n"
                )

                file.write(
                    "Grade Point: " +
                    str(course["grade_point"]) +
                    "\n"
                )

                file.write(
                    "Weighted Points: " +
                    str(course["weighted_points"]) +
                    "\n"
                )

                file.write("-" * 40 + "\n")

            file.write(
                "Total Credits: " +
                str(total_credits) +
                "\n"
            )

            file.write(
                "Total Weighted Points: " +
                str(total_weighted_points) +
                "\n"
            )

            file.write(
                "CGPA: " +
                str(round(cgpa, 2)) +
                "\n"
            )

            if reappear:
                file.write("Status: REAPPEAR REQUIRED\n")
            else:
                file.write("Status: PASS\n")

            file.write("=" * 75 + "\n")

        print("✓ Result saved successfully!")
        print("Saved as: cgpa_results.txt")

    except Exception as error:
        print("Could not save result.")
        print("Error:", error)


def view_previous_results():
    """Display previously saved results."""

    print("\n" + "=" * 65)
    print("                 PREVIOUS RESULTS")
    print("=" * 65)

    try:

        with open("cgpa_results.txt", "r") as file:

            results = file.read()

            if results.strip() == "":
                print("No previous results found.")

            else:
                print(results)

    except FileNotFoundError:

        print("No previous results found.")
        print("Calculate and save a result first.")


def show_grading_system():
    """Display the grading system."""

    print("\n" + "=" * 50)
    print("              GRADING SYSTEM")
    print("=" * 50)

    print(f"{'Marks':<15}{'Grade':<15}{'Grade Point'}")
    print("-" * 50)

    print(f"{'90 - 100':<15}{'O':<15}10")
    print(f"{'80 - 89':<15}{'A+':<15}9")
    print(f"{'70 - 79':<15}{'A':<15}8")
    print(f"{'60 - 69':<15}{'B+':<15}7")
    print(f"{'50 - 59':<15}{'B':<15}6")
    print(f"{'40 - 49':<15}{'D':<15}4")
    print(f"{'Below 40':<15}{'E':<15}0")

    print("-" * 50)
    print("E = Reappear")
    print("=" * 50)


# menu

def main():

    while True:

        print("\n")
        print("=" * 65)
        print("                         CGPACRAFT")
        print("                 Academic CGPA Calculator")
        print("=" * 65)

        print("\n1. Calculate CGPA")
        print("2. View Previous Results")
        print("3. View Grading System")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            calculate_cgpa()

        elif choice == "2":

            view_previous_results()

        elif choice == "3":

            show_grading_system()

        elif choice == "4":

            print("\nThank you for using CGPACraft!")
            print("Goodbye!")
            break

        else:

            print("\n❌ Invalid choice.")
            print("Please select 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
