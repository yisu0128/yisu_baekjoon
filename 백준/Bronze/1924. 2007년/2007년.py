a, b = map(int, input().split())

daysum = 0
list = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
if a == 1:
    daysum = 0
    day = b%7 

else:
    for i in range(a-1):
        daysum += list[i]
    day = (daysum + b) %7

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

print(days[day])