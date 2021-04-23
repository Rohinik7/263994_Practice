"""Write a Python script to merge two Python dictionaries"""
a = {}
b={}
def Merge(dict1,dict2):
    res={**dict1,**dict2}
    return res
n = int(input("Enter number of pairs in dictionary 1:  "))
for i in range(n):
    key,value=input("Enter the "+str(i)+" pair").split()
    a[key]=value
m = int(input("Enter number of pairs in dictionary 2:  "))
for i in range(m):
    key,value=input("Enter the "+str(i+1)+" pair").split()
    b[key]=value
c=Merge(a,b)
print(c)