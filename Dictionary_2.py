"""Write a Python program to convert a list into a nested dictionary of keys"""


def Convert (list_):
    a = res={}
    for i in list_:
        a[i] = {}
        a = a[i]
    return res


input_list = input("Enter the list items: ").split()
print(input_list)
print(Convert(input_list))