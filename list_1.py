"""Write a Python program to find the second smallest number in a list"""


def second_smallest(a):
    min_number = min(a)
    second = max(a)
    for i in a:
        if i < second and i != min_number:
            second = i
    return second


n = list(map(int, input("Enter elements in list").split()))
print("Second smallest: {}".format(second_smallest(n)))
