"""Write a Python program to find the repeated items of a tuple"""


def distinct(n):
    a=[]
    for i in n:
        if i not in a:
            a.append(i)
    return a


n=tuple(input("Enter the tuple items: ").split())
multi=[]
print("Tuple: {}".format(n))
for i in n:
    if n.count(i)>1:
        multi.append(i)
multi=distinct(multi)
for i in multi:
    print("tuple item {} : count= {}".format(i,n.count(i)))