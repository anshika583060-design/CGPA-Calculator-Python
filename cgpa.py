# Advanced CGPA Calculator

total_semesters = int(input("Enter total number of semesters: "))
total_sgpa = 0

for i in range(1, total_semesters + 1):
    sgpa = float(input(f"Enter SGPA of semester {i}: "))
    total_sgpa += sgpa

cgpa = total_sgpa / total_semesters
percentage = cgpa * 9.5

print("\nYour CGPA is:", round(cgpa, 2))
print("Equivalent Percentage:", round(percentage, 2), "%")
