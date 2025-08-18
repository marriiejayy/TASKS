# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# **Task2**
# Federal Government Scholarship Key Eligibility Requirements:
Name = input("Enter your name: ").title()
Citizenship = input("Enter your Citizenship: ").title()
Enrollment = (input("Specify (with Yes or No) if you registered full time student at a registered University: ")).title()
Other_scholarship = (input("Specify (with Yes or No) if you are recieving any other scholarship: ")).title()
Academic_qualification = (input("Specify (with Yes or No) if you have five distinctions in your WASSCE exams\nN.B Including English and Mathematics:")).title()

Citizenship_0 = "Nigerian"
Enrollment_0 = "Yes"
Other_scholarship_0 = "No"
Academic_qualification_0 = "Yes"

Key_eligibility_requirement = (Citizenship == Citizenship_0) and (Enrollment == Enrollment_0) and (Other_scholarship == Other_scholarship_0) and (Academic_qualification == Academic_qualification_0)
print(f"Candidate: {Name}\nCitizenship: {Citizenship}\nEnrollment: {Enrollment}\nOther scholarship: {Other_scholarship}\nAcademic qualification: {Academic_qualification}\nEligible: {Key_eligibility_requirement}\nN.B If you are eligibile, it will print true.")