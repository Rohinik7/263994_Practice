"""Write a python program to check if the input number is
-real number
-float number
-string
-complex number
-Zero (0)"""
from ast import literal_eval

def get_type(input_data):
    if input_data=='0':
        return 'Zero(0)'
    try:
        return (literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str
n=input("Enter Value: ")
c=get_type(n)
if c is float:
    print("Float number: True")
else:
    print("Float number: False")
if c is not str or c is not complex:
    print("Real number: True")
else:
    print("Real number: False")
if c is str