# Task 3: Days and Activities Pairing
# Store days of the week in a tuple
Days = ("Monday", "Tuesday", "Wednesday")

# Ask user to input an activity for each day
activities = []
for day in Days:
    activity = input(f"Enter activity for {day}: ").strip()
    activities.append(activity)

day_activity_dict = {day: activity for day, activity in zip(Days, activities)}

# Print dictionary
print("\n***** Days and Activities *****")
print(day_activity_dict)
