"""Write a Python program to get next day of a given date using if-elif-else"""
month_1=[1,3,5,7,8,10,12]
month_2=[4,6,9,11]
flag=0
def check_leap(year):
    leap=False
    if year%4==0 and year%100!=0:
        leap=True
    if year%100==0 and year%400==0:
        leap=True
    return leap

def check_monthend(month,year):
    if month in month_1:
        end=31
    elif month==2:
        if check_leap(year):
            end=29
        else:
            end=28
    else:
        end=30
    return end

day,month,year=input("Enter the date in format dd/mm/yy ").split("/")
day=int(day)
month=int(month)
year=int(year)
day_end=check_monthend(month,year)
if day==day_end and month!= 12:
    day=1
    month+=1
elif day==day_end and month==12:
    day=1
    month=1
    year+=1
elif day>day_end or month>12:
    print("Invalid day or month")
    flag=1
else:
    day+=1
if flag==0:
    print("Next day: {}/{}/{}".format(day,month,year))

