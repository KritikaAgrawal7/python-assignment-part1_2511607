# ----------------------------------------
# TASK 1: DATA PARSING & PROFILE CLEANING
# ----------------------------------------

print("=== TASK 1: DATA PARSING & PROFILE CLEANING ===\n")

# Raw student data given in the assignment
# This data is "unclean" because:
# - names have extra spaces and inconsistent capitalization
# - roll numbers are stored as strings
# - marks are stored as one comma-separated string instead of a list

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
# Loop through each student dictionary one by one

for student in raw_students:
    # Clean the name:
    # .strip() removes extra spaces at the beginning and end
    # .title() converts the name into proper title case
    clean_name = student["name"].strip().title()
    # Convert roll number from string to integer
    roll_no = int(student["roll"])
    # Split the marks string using comma
    marks_parts = student["marks_str"].split(",")
    # Empty list to store cleaned integer marks
    clean_marks = []
    # Loop through each mark, remove spaces, convert to integer, and store in list
    for mark in marks_parts:
        clean_marks.append(int(mark.strip()))
    # Assume the name is valid first
    valid = True
    # Split the cleaned name into words and check if each word contains only alphabets
    for word in clean_name.split():
        if not word.isalpha():
            valid = False
    # Print a neat profile card for each student
    print("=" * 35)
    print(f"Student : {clean_name}")
    print(f"Roll No : {roll_no}")
    print(f"Marks   : {clean_marks}")
    # Print whether the name is valid or invalid
    if valid:
        print("✔ Valid name")
    else:
        print("✘ Invalid name")
    print("=" * 35)
    # If roll number is 103, print name in uppercase and lowercase
    if roll_no == 103:
        print("Name in ALL CAPS :", clean_name.upper())
        print("Name in lowercase:", clean_name.lower())

# ----------------------------------------
# TASK 2: USING LOOPs and CONDITIONALS
# ----------------------------------------

print("=== TASK 2: MARKS ANALYSIS USING LOOPS & CONDITIONALS ===\n")

# Given student data for Task 2
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

# Print the student name before starting analysis
print(f"Student Name: {student_name}\n")

# Loop through each subject and its corresponding marks
for i in range(len(subjects)):
    mark = marks[i]

    # Assign grade based on marks range
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"

    # Print subject, marks, and grade
    print(f"{subjects[i]}: {mark} -> Grade {grade}")

# Calculate total marks by adding all values in marks list
total_marks = sum(marks)

# Calculate average marks and round it to 2 decimal places
average_marks = round(total_marks / len(marks), 2)

# Find the highest and lowest marks
highest_mark = max(marks)
lowest_mark = min(marks)

# Find the matching subject using index positions
highest_subject = subjects[marks.index(highest_mark)]
lowest_subject = subjects[marks.index(lowest_mark)]

# Print summary of marks analysis
print("\n--- Summary ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Scoring Subject: {highest_subject} ({highest_mark})")
print(f"Lowest Scoring Subject: {lowest_subject} ({lowest_mark})")

# Counter to track how many new subjects were added
new_subject_count = 0

print("\nNow you can add new subjects and marks.")

# Keep asking the user to add new subjects until they type 'done'
while True:

     
    # Ask the user to enter a new subject name
    subject_name = input("\nEnter a new subject name (or type 'done' to stop): ").strip()

    # Stop the loop if user enters 'done'
    if subject_name.lower() == "done":
        break

    # Validate subject name:
    # It should not be empty and should contain only letters/spaces
    if subject_name == "":
        print("Invalid subject name! Subject name cannot be empty.")
        continue

    if not subject_name.replace(" ", "").isalpha():
        print("Invalid subject name! Use only alphabets and spaces.")
        continue

    # Ask for marks of the entered subject
    mark_input = input(f"Enter marks for {subject_name}: ").strip()

    # Try converting entered marks to integer
    try:
        mark = int(mark_input)

        # Check if marks are within valid range
        if 0 <= mark <= 100:
            subjects.append(subject_name.title())
            marks.append(mark)
            new_subject_count += 1
            print(f"{subject_name.title()} added successfully.")
        else:
            print("Do not crash, and do not add invalid entries to the list")

    # If user enters non-numeric value, show error instead of crashing
    except:
        print("Do not crash, and do not add invalid entries to the list")

# Calculate updated average after adding new valid subjects
updated_average = round(sum(marks) / len(marks), 2)

# Print final updated summary
print("\n--- Updated Summary ---")
print(f"New subjects added: {new_subject_count}")
print(f"Updated average across all subjects: {updated_average}")
print()

# ----------------------------------------
# TASK 3: CLASS PERFORMANCE SUMMARY
# ----------------------------------------

print("=== TASK 3: CLASS PERFORMANCE SUMMARY ===\n")

# Class data given in the assignment
# Each tuple contains: (student name, list of marks)

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma", [55, 68, 49, 72, 61]),
    ("Priya Nair", [91, 85, 88, 94, 79]),
    ("Karan Mehta", [40, 55, 38, 62, 50]),
    ("Sneha Pillai", [75, 80, 70, 68, 85])
]

# Variables to track class performance
pass_count = 0
fail_count = 0
all_averages = []

# Variables to track class topper
topper_name = ""
topper_avg = 0

# Print heading for report table
print("Name             | Average | Status")
print("-------------------------------------")

# Loop through each student's name and marks
for name, marks in class_data:

    # Calculate average marks for current student
    avg = round(sum(marks) / len(marks), 2)

    # Decide pass or fail based on average
    if avg >= 60:
        status = "Pass"
        pass_count += 1
    else:
        status = "Fail"
        fail_count += 1

    # Store average in list for class average calculation later
    all_averages.append(avg)

    # Check if current student is topper so far
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # Print each student's performance row
    print(f"{name:<16} | {avg:<7} | {status}")

# Calculate class average
class_average = round(sum(all_averages) / len(all_averages), 2)

# Print overall class summary
print("\n--- Class Summary ---")
print(f"Passed Students: {pass_count}")
print(f"Failed Students: {fail_count}")
print(f"Class Topper: {topper_name} ({topper_avg})")
print(f"Class Average: {class_average}")
print()

# ----------------------------------------
# TASK 4: STRING MANIPULATION UTILITY
# ----------------------------------------

print("=== TASK 4: STRING MANIPULATION UTILITY ===\n")

# Essay given in the assignment
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Remove extra spaces from beginning and end of the essay
clean_essay = essay.strip()

# 1. Print stripped essay
print("1. Stripped Essay:")
print(clean_essay)

# Convert essay into title case
title_essay = clean_essay.title()

# 2. Print title case version
print("\n2. Title Case Essay:")
print(title_essay)

# Count how many times the word 'python' appears
python_count = clean_essay.count("python")

# 3. Print count of 'python'
print("\n3. Count of 'python':")
print(python_count)

# Replace 'python' with 'Python 🐍'
replaced_essay = clean_essay.replace("python", "Python 🐍")

# 4. Print replaced essay
print("\n4. Replaced Essay:")
print(replaced_essay)

# Split the essay into sentences using ". "
sentences = clean_essay.split(". ")

# 5. Print sentence list
print("\n5. Sentence List:")
print(sentences)

# 6. Print each sentence on a new line with numbering
print("\n6. Numbered Sentences:")
for i in range(len(sentences)):
    sentence = sentences[i]

    # Add a full stop if it is missing after splitting
    if not sentence.endswith("."):
        sentence += "."

    print(f"{i + 1}. {sentence}")

print()