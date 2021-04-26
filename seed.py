from random import seed,randint

seed_value = int(input("Enter the seed value: "))
seed(seed_value)
a=randint(0,599)
b=randint(0,1000)
print("Numbers generated: ",a,"and",b)
