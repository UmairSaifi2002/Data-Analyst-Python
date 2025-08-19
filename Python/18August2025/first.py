# Q1 Create a dictionary to store names and marks of 5 students. Then print all Student score along with their percentage
# - write a function to search a particular student from dictionary by using its name and print student's marks
# - write a function to modify student marks

# now let's begin

# Dictionary of students
students = {
    "Ali": 85,
    "Aisha": 92,
    "Rahul": 76,
    "Sara": 88,
    "Umair": 95
}

# Function to display all students with percentage
def display_scores():
    print("\nStudent Scores with Percentage:")
    for name, marks in students.items():
        print(f"{name}: {marks} marks ({marks}%)")

# Function to search student by name
def search_student(name):
    if name in students:
        print(f"\n{name}'s Marks: {students[name]} ({students[name]}%)")
    else:
        print(f"\n{name} not found in records.")

# Function to modify marks
def modify_marks(name, new_marks):
    if name in students:
        students[name] = new_marks
        print(f"\n{name}'s marks updated to {new_marks}.")
    else:
        print(f"\n{name} not found in records.")

# --- Execution ---
display_scores()
search_student("Sara")        # Example search
modify_marks("Rahul", 82)     # Example modify
display_scores()              # Check updates

