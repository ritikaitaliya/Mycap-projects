# Student Management System
"""
Fields :- ['roll', 'name', 'age', 'email', 'phone']
1. New Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Quit
"""

import csv
# Define global variables
fields = ['roll', 'name', 'age', 'email', 'phone']
database = 'students.csv'


def display_menu():
  print("---STUDENT MANAGEMENT SYSTEM---")
  print("1. New Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Update Student")
  print("5. Delete Student")
  print("6. Quit")

#add student
def add_student():
  print("---Add Student Information---")
  global fields
  global database

  student_data = []
  for key in fields:
    value = input("Enter " + key + ": ")
    student_data.append(value)

  with open(database, "a") as f:
    writer = csv.writer(f)
    writer.writerows([student_data])

  print("Data saved successfully")
  input("Press enter to continue")
  return

#view students
def view_students():
  global fields
  global database
  print("---Student Record---")

  with open(database, "r") as f:
    view = csv.reader(f)
    for x in fields:
      print(x, end='\t')
    print("\n---------------------------------------------------")

    for row in view:
      for item in row:
        print(item, end="\t")
      print("\n")
    input("Press enter to continue")

#search students
def search_student():
  global fields
  global database

  print("---Search Student---")
  data = input("Enter roll no. to search: ")
  with open(database, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      if len(row) > 0:
        if data == row[0]:
          print("---Student Found---")
          print("Roll: ", row[0])
          print("Name: ", row[1])
          print("Age: ", row[2])
          print("Email: ", row[3])
          print("Phone: ", row[4])
          break
    else:
      print("Data not found in our database")
  input("Press enter to continue")

#update student
def update_student():
    global fields
    global database

    print("---Update Student---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(database, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    # Check if data is found or not
    if index_student is not None:
        with open(database, "w") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")
    input("Press enter to continue")

#delete student
def delete_student():
  global field
  global database

  print("--- Deleted Student ---")
  data = input("Enter roll no. to delete: ")
  updated_data = []
  with open(database, "r") as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
        if len(row) > 0:
          if data != row[0]:
            updated_data.append(row)
            counter += 1
          else:
            break

#select the option                   
while True:
  display_menu()

  choice = input("Enter your option: ")
  if choice == '1':
    add_student()
  elif choice == '2':
    view_students()
  elif choice == '3':
    search_student()
  elif choice == '4':
    update_student()
  elif choice == '5':
    delete_student()
  else:
    break

print("---Thank you for using our system---")
