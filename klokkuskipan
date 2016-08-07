import time
import datetime
import sqlite3

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
name = ''
position = int()

# Temporary Database config and functions below
conn = sqlite3.connect('database.db')
c = conn.cursor()

# This is for making the user table. Only run this once!
def SQL_Table():
    c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, position INTEGER, signIn REAL, signOut REAL)')
    return True

time_in = st
time_out = st

# Verifies that the user id is in the database.
def Verify():
    input_id = input('>> ID: ')
    input_position = input('>> Position: ')
    c.execute("SELECT %s FROM %s WHERE %s = ?" % ('id', 'users', 'id'), (input_id,))
    data = str(c.fetchall())
    try:
        int(input_id), int(input_position)
    except ValueError:
        print('ValueError: name takes string, position takes int.')
    if input_id in data:
        answer = int(input(""">> Choose an option:

        1. Sign In
        2. Sign Out
        9. Administration \n"""))
        
        if answer == 1:
            return Clock_In(int(input_id), int(input_position))
        elif answer == 2:
            return Clock_Out(int(input_id))
        elif answer == 9:
            return Create_User()
        else:
            print('Not a valid option')
            return Verify()
    else:
        print('User not in database')
        return False

def Create_User():
    input_id = input('>> ID: ')
    input_name = input('>> Name: ')
    c.execute("INSERT INTO users(id, name) VALUES (?, ?)",(input_id, input_name))
    conn.commit()
    print('>> User %s has been created, with ID: %s' % (input_name, input_id))
    return Verify()


def Clock_In(input_id, input_position):
    c.execute("SELECT %s FROM %s WHERE %s = ?" % ('signIn', 'users', 'id'), (input_id,))
    c.execute("SELECT %s FROM %s WHERE %s = ?" % ('name', 'users', 'id'), (input_id,))
    data = data_in = str(c.fetchall()).strip("[]()'',,")
    c.execute("UPDATE %s SET %s = ?, %s = ? WHERE %s = ?" % ('users', 'signIn', 'position', 'id'), (time_in, input_position, input_id))
    conn.commit()
    print('%s ID: %s signed in at %s' % (data, input_id, time_in))
    return Verify()

def Clock_Out(input_id):
    c.execute("SELECT %s FROM %s WHERE %s = ?" % ('signIn', 'users', 'id'), (input_id,))
    data_in = str(c.fetchall()).strip("[]()'',,")
    c.execute("UPDATE %s SET %s = ? WHERE %s = ?" % ('users', 'signOut', 'id'), (time_out, input_id))
    conn.commit()
    print('%s signed in at %s and signed out at %s' % (input_id, data_in, time_out))
    return Verify()


#SQL_Table()
Verify()
#Clock_Out()
#Clock_In()
#Create_User()
