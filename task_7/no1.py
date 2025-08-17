# Task1: Student Bio Data Storage
Student_bio = {}

# student details
Student_bio["Name"] = input("Enter student name: ")
Student_bio["Age"] =    int(input("Enter student age: "))
Student_bio["Gender"] = input("Enter student gender: ")

# Collect courses as a comma-separated input
courses = input("Enter courses (separate by commas): ")

# Convert input string into a list
Student_bio["Courses"] = [course.strip() for course in courses.split(",")]

# Display the bio-data neatly using escape sequences
print("\n***** Student Bio Data *****")
print(f"Name:\t\t{Student_bio['Name']}")
print(f"Age:\t\t{Student_bio['Age']}")
print(f"Gender:\t\t{Student_bio['Gender']}")
print("Courses:\t", end="")
print(", ".join(Student_bio["Courses"]))
