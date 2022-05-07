

from datetime import datetime
import math
current_date = datetime.now(tz= None)

w = float(input (' Enter the width of the tire in mm: '))
a = float(input('Enter the aspect ratio of the tire:'))
d = float(input(' Enter the diameter of the wheel: '))
# in order to get two lines printed, I repeated the questions
# to the user but I marked variable names with 1 so that the program can read them. 
w1 = float(input (' Enter the width of the tire in mm: '))
a1 = float(input('Enter the aspect ratio of the tire:'))
d1 = float(input(' Enter the diameter of the wheel: '))
v =  (math.pi * w**2) * a * (w * a  + 2540 * d)/10**10
# even on the volume i have to mark it 1 so that it would be found by program 
v1 =  (math.pi * w1**2) * a1 * (w1 * a1  + 2540 * d1)/10**10
with open("volume.txt") as volume_file : 
    for line in volume_file : 
        print(line)
        print(f'{current_date: %y-%m-%d}, {round(w)}, {round(a)}, {round(d)}, {v : .2f}')
with open("volume.txt") as volume_file1:
    for line in volume_file1:
        print(line)
        print(f"{current_date: %y-%m-%d}, {round(w1)}, {round(a1)}, {round(d1)}, {v1: .2f} ")
        print()
        print()
        # here i print first line
print(f'{current_date: %y-%m-%d}, {round(w)}, {round(a)}, {round(d)}, {v : .2f}')
# and here i print the second line. 
print(f"{current_date: %y-%m-%d}, {round(w1)}, {round(a1)}, {round(d1)}, {v1: .2f} ")






