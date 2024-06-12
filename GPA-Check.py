# M02 Lab - Case Study: if... else and while
# M02-GPA Check
# Brendan Bradfield
# SDEV 220
# 12 June 2024

# This app accepts input of a student's last name, first name, and GPA
# It determines whether the student made the Dean's List or the Honor Roll

# Lists to store student names who qualify for the Dean's List and Honor Roll
honor_roll_students = []
deans_list_students = []

def add_student_to_list(first_name, last_name, gpa):
    if gpa >= 3.5:
        deans_list_students.append((first_name, last_name))
    elif gpa >= 3.25:
        honor_roll_students.append((first_name, last_name))
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or Honor Roll.")

def print_list(title, students_list):
    print(f'{title}:')
    for student in students_list:
        print(student)

while True:
    student_last = input('Please enter student last name (or ZZZ to quit): ')
    if student_last.upper() == 'ZZZ':
        break
    student_first = input('Please enter student first name: ')
    
    try:
        student_gpa = float(input('Please enter student GPA: '))
    except ValueError:
        print("Invalid GPA. Please enter a numeric value.")
        continue
    
    add_student_to_list(student_first, student_last, student_gpa)

# Display the Dean's List and Honor Roll
print_list('Dean\'s List', deans_list_students)
print()
print_list('Honor Roll', honor_roll_students)
