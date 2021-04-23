"""Write a Python program to change the position of every n-th value with the (n+1)th in a list"""

def swap(arr):
    for i in range(len(n) - 1):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
n=input("Enter the list values: ").split()
print(swap(n))

