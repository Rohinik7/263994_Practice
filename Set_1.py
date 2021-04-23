"""Write a Python program to find maximum and the minimum value in a set"""

n = list(map(int,input("Enter values in set: ").split()))
n = set(n)
print(n)
print("Maximum: {}".format(max(n)))
print("Minimum: {}".format(min(n)))
