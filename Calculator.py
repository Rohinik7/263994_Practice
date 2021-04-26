"""Perform operations on two numbers"""
import random


def sum(a,b):
    return a+b


def sub(a,b):
    return a-b


def mul(a,b):
    return a*b


def exp(a,b):
    return a**b


def div(a,b):
    if b!=0:
        return a//b,a%b
    return "Invalid input"


def take_input():
    a=random.randrange(0,100)
    b=random.randrange(1,100)
    if a>=b:
        return a,b
    else:
        return take_input()


if __name__=="__main__":
    a,b=take_input()
    print("Numbers:",a,b)
    print("Sum:",sum(a,b))
    print("Difference:",sub(a,b))
    print("Product:",mul(a,b))
    print("Exponent: {}".format(exp(a,b)))
    q,r=div(a,b)
    print("Division:",a,"/",b,"\n Quotient : {} \n Remainder: {}".format(q,r))



