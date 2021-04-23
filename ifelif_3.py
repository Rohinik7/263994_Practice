"""Write Python code that asks a user how many pizza slices they want.
The pizzeria charges Rs 123.00 a slice. if user order even number of slices, price per slice is Rs 120.00.
Print the total price depending on how many slices user orders."""


def cost(n):
    if n % 2 == 0:
        n = float(n)*120.00
    else:
        n = float(n)*123.00
    return n


n = int(input("How many pizza slices required: "))
print("Price: {}".format(cost(n)))
