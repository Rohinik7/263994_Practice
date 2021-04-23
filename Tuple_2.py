""" Write a Python program to convert a list of tuples into a dictionary"""
n = [("akash", 10), ("gaurav", 12), ("anand", 14),
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
def convert(tup):
    a={}
    for key,value in tup:
        a[key]=value
    return a

print("Tuple: {}".format(n))
print("Dictionary: {}".format(convert(n)))


