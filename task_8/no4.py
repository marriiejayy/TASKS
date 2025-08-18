# Task 4 student record
# Create an empty dictionary called student
Student = {}

#Ask the user to input their name and age,then store them in a dictionary
User_name = (input("Enter your name: ")).title()
user_age = int(input("Enter your age: "))

Student["name"] = User_name
Student["age"] = user_age


#Add a list of scores to the dictionary
Student["scores"] = [76, 69, 90]

# Use comparison operator to check if student passed
average_score = sum(Student["scores"]) / len(Student["scores"])
Student["passed"] = average_score >= 50

# Use logical operator to check if student is a teenager
Student["teenager"] = Student["age"] >= 13 and Student["age"] <= 19

# Print student record
print("======Student Record======")
print(f"Name: {Student['name']}\nAge: {Student['age']}\nScores: {Student['scores']}\nPassed: {Student['passed']}\nTeenager: {Student['teenager']}")
