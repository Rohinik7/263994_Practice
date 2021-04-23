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
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str
n=input("Enter Value: ")
print(get_type(n))