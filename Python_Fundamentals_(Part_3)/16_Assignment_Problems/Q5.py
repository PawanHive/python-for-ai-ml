'''
Q5. Create a dictionary where:

Keys = student names
Values = marks (integer)
Write a menu-based program where the user presses a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the dictionary:

A - Add a student
B - Update marks
C - Search for a student
D - Display all students and marks
'''

students = {}

while True: 
  print("\n ===== STUDENT MANAGEMENT SYSTEM =====")
  print("A. Add a student")
  print("B. Update marks")
  print("C. Search for a student")
  print("D. Display all students and marks")
  print("E. Exit")

  choice = input("Enter your choice: ").upper()

  if choice == "A":
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students[name] = marks

    print("Student added successfully!")

  elif choice == "B":
    name = input("Enter student name: ")

    if name in students: 
      marks = int(input("Enter updated marks: "))
      students[name] = marks
      print("Marks updated successfully!")
    else: 
      print("Student not found!")

  elif choice == "C":
    name = input("Enter student name: ")

    if name in students: 
      print("Student:", name)
      print("Marks:", students[name])
    else: 
      print("Student not found!")

  elif choice == "D":
    if students: 
      print("\n Student Name\tMarks")

      for name, marks in students.items():
        print(name, "\t\t", marks)

    else: 
      print("No students records available!")