#docstring- Steve Rodkiss- airb=plan databse application
#imports
import sqlite3

#contants and variables
DATABASE = "fighters.db"


#functions
def print_all_aircraft():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighters;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop theroughall the results
    print(f"name                         speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()


def print_all_aircraft_by_speed():
    '''print all the aircraft sorted by speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighters ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop theroughall the results
    print(f"name                         speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()


def print_all_aircraft_by_max_g():
    '''print all the aircraft sorted by max g'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighters ORDER BY max_g DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop theroughall the results
    print(f"name                         speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()


def print_all_aircraft_by_climb_rate():
    '''print all the aircraft sorted by climb speed'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighters ORDER BY climb DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop theroughall the results
    print(f"name                         speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()


def print_all_aircraft_by_range_km():
    '''print all the aircraft sorted by range'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighters ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop theroughall the results
    print(f"name                         speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()


def print_all_aircraft_by_payload():
    '''print all the aircraft sorted by payload'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from fighters ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop theroughall the results
    print(f"name                         speed   max_g climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close() 

#main code
while True:
    user_input = input("""
what would you like to do.
1. print all aircraft
2. Print all aircraft sorted by speed
3. Print all aircraft sorted by max g
4. Print all aircraft sorted by climb rate
5. Print all aircraft sorted by range (km)
6. Print all aircraft sorted by payload (kg)
7. Exit
""")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_by_speed()
    elif user_input == "3":
        print_all_aircraft_by_max_g()
    elif user_input == "4":  
        print_all_aircraft_by_climb_rate()
    elif user_input == "5":
        print_all_aircraft_by_range_km()
    elif user_input == "6":
        print_all_aircraft_by_payload()
    elif user_input == "7":
        break
    else:
        2print("That was not a option\n")

