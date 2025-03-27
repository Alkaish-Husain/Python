'''Experiment No:-6
   Title:-  Student Enrollment Manager *
   Aim:-    Create a Python code to demonstrate the use of sets and perform set operations
            (union, intersection, difference) to manage student enrollments in multiple courses
            / appearing for multiple entrance exams like CET, JEE, NEET etc.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                           '''
Jee_Students = {"Alkaish","Asfaque","Ayan","Aamir"}
CET_Students = {"Alkaish","Atharav","Alpha","Sohan"}
NEET_Students = {"Anish","Anas","Alice","Alpha","Aamir"}
# Union of set
All_Students = Jee_Students | CET_Students | NEET_Students
print("Students appearing at least one exam",All_Students)
# Inserction of set
Cet_and_Jee = Jee_Students & CET_Students
print("Students appearing at both CET and Jee exam",Cet_and_Jee)
Neet_and_Jee = Jee_Students & NEET_Students
print("Students appearing at both Neet and Jee exam",Neet_and_Jee)
Neet_and_Cet = CET_Students & NEET_Students
print("Students appearing at both CET and Neet exam",Neet_and_Cet)
# Difference: Students who are in CET but not in JEE
Cet_not_in_Jee = CET_Students - Jee_Students
print("Students who are in CET but not in JEE",Cet_not_in_Jee)
Jee_not_in_Cet = Jee_Students - CET_Students
print("Students who are in JEE but not in CET",Jee_not_in_Cet)
