#!usr/bin/python

print "Hello world"
"""
# Student Data
students = []

def menu():
  print """=== Student Management ===
  1. Display List of students
  2. Add Student
  3. Edit Student by Name
  4. Delete Student
  5. Exit"""

def list():
  print "---------------------------------"
  print "#\tRoll\tName\tClass"
  print "---------------------------------"
  for i in range(len(students)):
    stud = students[i]
    print (i+1), "\t", stud['roll'], "\t", stud['name'], "\t", stud['class']

def add():
  count = input("Number of students: ")
  for i in range(count):
    stud = {}
    stud['name'] = raw_input("Name of Student " + str(i+1) + ": ")
    stud['roll'] = raw_input("Roll of Student " + str(i+1) + ": ")
    stud['class'] = raw_input("Class of Student " + str(i+1) + ": ")
    students.append(stud)

def edit(index):
  index = index - 1
  stud = students[index]
  stud['name'] = raw_input("Name of Student (" + stud['name'] + "): ")
  stud['roll'] = raw_input("Roll of Student (" + stud['roll'] + "): ")
  stud['class'] = raw_input("Class of Student (" + stud['class'] + "): ")
  students.pop(index)
  students.insert(index, stud)

def delete(index):
  index = index - 1
  stud = students[index]
  students.pop(index)

while True:
  menu()
  choice = input("Choice: ")
  if choice == 1:
    # List Students
    list()
  elif choice == 2:
    # Add Student
    add()
  elif choice == 3:
    # Edit Student
    index = input("Which student to edit ? ")
    edit(index)
  elif choice == 4:
    # Delete Student
    index = input("Which student to delete ? ")
    delete(index)
  elif choice == 5:
    # Exit
    print "Thank you for using SMS.\n\n"
    break

"""
