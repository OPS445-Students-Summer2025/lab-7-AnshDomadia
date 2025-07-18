#!/usr/bin/env python3
# Student ID: Ansh Domadia

def function1():
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)
    return schoolName  
def function2():
    global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

# global schoolName
schoolName = 'Seneca'

# Main program
print('print() in main on schoolName:', schoolName)  # This prints the initial value of schoolName

schoolName = function1()  
print('print() in main on schoolName:', schoolName)  # This prints the updated schoolName after function1

function2() 
print('print() in main on schoolName:', schoolName)  # This prints the global schoolName after function2
