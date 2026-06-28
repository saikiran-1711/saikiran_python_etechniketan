#1
import keyword

keywords = keyword.kwlist

print("Python Keywords")
print("----------------")
for word in keywords:
    print(word)

print("Total Keywords =", len(keywords))


#2
x = 10

print("\nQuestion 2")
print("Value of x =", x)

x_type = type(x)

print("Type of x =", x_type)


#3
numbers = (10, 20, 30, 40)

print("\nQuestion 3")
print("Tuple =", numbers)

second_element = numbers[1]
last_element = numbers[-1]

print("Second Element =", second_element)
print("Last Element =", last_element)


#4
number = "123"

converted_number = int(number)

result = converted_number + 10

print("\nQuestion 4")
print("String =", number)
print("Converted Integer =", converted_number)
print("Result =", result)


#5
float_number = 56.89

integer_number = int(float_number)

print("\nQuestion 5")
print("Float Number =", float_number)
print("Integer Number =", integer_number)


#6
first = "Hello"
second = "World"

space = " "

new_string = first + space + second

string_length = len(new_string)

print("\nQuestion 6")
print("Joined String =", new_string)
print("Length =", string_length)


#7
flag = True

flag_type = type(flag)

print("\nQuestion 7")
print("Flag =", flag)
print("Type =", flag_type)


#8
values = (10, 20, 30, 40, 50)

tuple_length = len(values)

print("\nQuestion 8")
print("Tuple =", values)
print("Length =", tuple_length)


#9
language = "Python"
version = 3.13

version_string = str(version)

result = language + version_string

print("\nQuestion 9")
print("Language =", language)
print("Version =", version)
print("Result =", result)


#10
print("\nQuestion 10")

student_name = input("Enter Student Name : ")
age = int(input("Enter Age : "))
city = input("Enter City : ")
course_name = input("Enter Course Name : ")

subject1 = float(input("Enter Marks in Subject 1 : "))
subject2 = float(input("Enter Marks in Subject 2 : "))
subject3 = float(input("Enter Marks in Subject 3 : "))

total_marks = subject1 + subject2 + subject3
percentage = total_marks / 3

print("\nStudent Details")
print("------------------------")
print("Student Name :", student_name)
print("Age :", age)
print("City :", city)
print("Course :", course_name)
print("Subject 1 Marks :", subject1)
print("Subject 2 Marks :", subject2)
print("Subject 3 Marks :", subject3)
print("Total Marks :", total_marks)
print("Percentage :", percentage)


#11a
subjects = ["Python", "SQL", "Excel", "Tableau"]

print("\nQuestion 11")
print("Original List")

for subject in subjects:
    print(subject)


#11b
first_subject = subjects[0]
last_subject = subjects[-1]

print("\nFirst Subject =", first_subject)
print("Last Subject =", last_subject)


#11c
subjects.insert(1, "Power BI")

print("\nList After Inserting Power BI")

for subject in subjects:
    print(subject)


#11d
subjects.remove("Excel")

print("\nList After Removing Excel")

for subject in subjects:
    print(subject)


#11e
new_subjects = subjects.copy()

print("\nCopied List")

for subject in new_subjects:
    print(subject)


#11f
new_subjects.sort()

print("\nSorted List")

for subject in new_subjects:
    print(subject)


#11g
check = "Excel" in new_subjects

print("\nIs Excel Present?")
print(check)


#12
attendance = True
assignment_submitted = False

print("\nQuestion 12")

print("\na.")
true_result = attendance or assignment_submitted
print("attendance or assignment_submitted =", true_result)

print("\nb.")
false_result = attendance and assignment_submitted
print("attendance and assignment_submitted =", false_result)

print("\nc.")
not_result = not attendance
print("not attendance =", not_result)