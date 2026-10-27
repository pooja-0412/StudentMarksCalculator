
# Student Marks Calculator

print("===== STUDENT MARKS CALCULATOR =====")

# Get student details
name = input("Enter student name: ")

# Get subject marks
tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
maths = int(input("Enter Maths mark: "))
science = int(input("Enter Science mark: "))
social = int(input("Enter Social Science mark: "))

# Calculate total and average
total = tamil + english + maths + science + social
average = total / 5
percentage = (total / 500) * 100

# Calculate grade and result
if min(tamil, english, maths, science, social) < 35:
    grade = "F"
    result = "Fail"
elif average >= 90:
    grade = "A"
    result = "Pass"
elif average >= 75:
    grade = "B"
    result = "Pass"
elif average >= 50:
    grade = "C"
    result = "Pass"
else:
    grade = "D"
    result = "Pass"

# Display results
print("\n===== STUDENT RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)
