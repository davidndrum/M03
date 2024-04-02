# M02 Lab - Case Study: if...else and while
# David N Drummond
# SDEV220 Lab assignment

# This application will query for the name and GPA of students.  It will then evaluate inputs against preset criteria to see if the student makes the Dean's List or the Honor Roll.
# After evaluating, it will print the result to the screen.

lName = input("What is the student's last name?\n")

while lName != "ZZZ":
    GPA = float(input("What is the student's GPA?\n"))
    if GPA >= 3.5:
        print("\nCongratulations!\n\nStudent " + str(lName) + " has made the Dean's List.")
    elif GPA >= 3.0:
        print("\nCongratulations!\n\nStudent " + str(lName) + " has made the Honor Roll.")
    else:
        print("Student " + str(lName) + " has not achieved a grade point average sufficient to qualify them for the Dean's List or Honor Roll.")
    lName = input('\nEnter the last name of another student or enter "ZZZ" to quit.\n')