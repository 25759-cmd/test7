# docstring- Ziyue Ma- student_grades databse application
# imports导入
import sqlite3
# Database name
DATABASE = "student_grades.db"


# functions
def print_all_student_grader_id():
    """print all the student_grader_id"""
    # connect to the database and name the variable
    db = sqlite3.connect(DATABASE)
    # Create a cursor object to execute SQL commands and query the database
    cursor = db.cursor()
    # Define the SQL query to select all columns and rows from the table
    sql = "SELECT * From student_grades;"
    # Execute the SQL query string
    cursor.execute(sql)
    # Fetch all the resulting rows from the executed query and store them in a list
    results = cursor.fetchall()
    # Print the table headers (spaces are manually added to align with the column widths below)
    print("id     name    student_id   grade_level      email")
    # Loop through each individual student record in the results list
    for student_grader in results:
    # Print each column with left-alignment padding to keep the columns neatly lined up
        print(f"{student_grader[0]:<6}{student_grader[1]:<13}{student_grader[2]:<8}{student_grader[3]:<10}{student_grader[4]:<10}")
    # loop finished here 预防混淆数据
    db.close()


def print_all_student_grader_by_name():
    '''print all the student_grader name'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * From student_grades ORDER BY name DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop theroughall the results
    print("id     name    student_id   grade_level      email")
    for student_grader in results:
        print(f"{student_grader[0]:<6}{student_grader[1]:<6}{student_grader[2]:<8}{student_grader[3]:<10}{student_grader[4]:<10}")
    # loop finished here
    db.close()   


def print_all_student_grader_by_student_id():
    '''print all the student_grader student_id'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * From student_grades ORDER BY student_id DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop theroughall the results
    print("id     name    student_id   grade_level      email")
    for student_grader in results:
        print(f"{student_grader[0]:<6}{student_grader[1]:<6}{student_grader[2]:<8}{student_grader[3]:<10}{student_grader[4]:<10}")
    # loop finished here
    db.close()   


def print_all_student_grader_by_grade_level():
    '''print all the student_grader_level'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * From student_grades ORDER BY grade_level DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop theroughall the results
    print("id     name    student_id   grade_level      email")
    for student_grader in results:
        print(f"{student_grader[0]:<6}{student_grader[1]:<6}{student_grader[2]:<8}{student_grader[3]:<10}{student_grader[4]:<10}")
    # loop finished here
    db.close()  


def print_all_student_grader_by_email():
    '''print all the student_grader email'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * From student_grades ORDER BY email DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # loop theroughall the results
    print("id     name    student_id   grade_level      email")
    for student_grader in results:
        print(f"{student_grader[0]:<6}{student_grader[1]:<6}{student_grader[2]:<8}{student_grader[3]:<10}{student_grader[4]:<10}")
    # loop finished here
    db.close()  


while True:
    user_input = input("""
What do you want to do

1. Show all the id
2. Show all the id sorted by name
3. Show all the id sorted by student_id
4. Show all the id sorted by grade_level
5. Show all the id sorted by email
6. Exit

""")
    if user_input == "1":
        print_all_student_grader_id()
    elif user_input == "2":
        print_all_student_grader_by_name()
    elif user_input == "3":
        print_all_student_grader_by_student_id()
    elif user_input == "4":  
        print_all_student_grader_by_grade_level()
    elif user_input == "5":
        print_all_student_grader_by_email()
    elif user_input == "6":
        break
    else:
        print("That was not a option\n")
