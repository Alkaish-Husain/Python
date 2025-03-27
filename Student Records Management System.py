'''Experiment No:-7
   Title:-  Student Record Keeper *
   Aim:-    Write a Python program to create, update, and manipulate a dictionary of student records,
            including their grades and attendance.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                             '''
students = {}
while True:
    print("\n1. Add/Update Student  2. Update Student Info  3. View Students  4. Remove Student  5. Exit")
    choice = input("Enter choice:- ")
    if choice == "1":  # Add or Update Student
        roll_no = input("Enter Roll Number:- ")
        name = input("Enter Name:- ")
        grade = input("Enter Grade:- ")
        attendance = input("Enter Attendance (%):- ")
        # Use update() to add or update student information
        students.update({roll_no: {"Name": name, "Grade": grade, "Attendance": attendance}})
        print("Student added or updated.")
    elif choice == "2":  # Update Student Info
        roll_no = input("Enter Roll Number to update:- ")
        if roll_no in students:
            print("Current Record:- ", students[roll_no])
            grade = input("Enter new Grade (or press Enter to keep unchanged):- ")
            attendance = input("Enter new Attendance (or press Enter to keep unchanged):- ")
            if grade:
                students[roll_no]["Grade"] = grade
            if attendance:
                students[roll_no]["Attendance"] = attendance
            print("Record updated.")
        else:
            print("Student not found.")
    elif choice == "3":  # View Students
        if students:
            for roll_no, info in students.items():
                print(f"Roll No:- {roll_no}, Name:- {info['Name']}, Grade:- {info['Grade']}, Attendance:- {info['Attendance']}%")
        else:
            print("No student records available.")
    elif choice == "4":  # Remove Student
        roll_no = input("Enter Roll Number to remove:- ")
        if roll_no in students:
            del students[roll_no]
            print("Student record removed.")
        else:
            print("Student not found.")
    elif choice == "5":  # Exit
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
