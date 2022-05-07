number_items = int(input('please enter the number of items: '))
number_items_in_1_box = int(input('enter the number of items per box: '))
number_of_boxes = number_items / number_items_in_1_box
print(f'for {number_items} packing {number_items_in_1_box} in each box, you will need {round(number_of_boxes)} ')






## v = [π * w^2 * a * (w * a + 2,540 * d)] / 10^10
#v is the volume in liters,
#π is the constant PI, which is the ratio of the 
# circumference of a circle divided by its diameter (use math.pi),
#w is the width of the tire in millimeters,
#a is the aspect ratio of the tire, and
#d is the diameter of the wheel in inches.


# from the abovbe formula, i can compute each variable
# when i devide both sides by πw^2a they give the following: 
#(10^10 * v) / πw^2a = w + 2540d
 # so now i can find the value of each variable in the formula 
 # w = (10^10 * v) / πw^2a - 2540d

# a = (10^10 * V) / πw^2 (w + 2540d)
# d = [(10^10 / πw^2 * a ) - w] / 2540

# import math


# w = float(input (' enter the width of the tire in mm: '))
# a = float(input('enter the aspect ratio of the tire:'))
# d = float(input(' enter the diameter of the wheel: '))

# v =  (math.pi * w**2) * a * (w * a  + 2540 * d)/10**10

# print(f' the approximate volume is: {v : .2f} liters')
# n = float(input('please enter a number: '))
# r = round(n , 3)
# print(r)
# x = "sun"
# y = "moon"
# z = "stars"
# print(x, y, z, sep="|", flush= True)







# """"""
# #When you physically exercise to strengthen your heart, you
# #should maintain your heart rate within a range for at least 20
# #minutes. To find that range, subtract your age from 220. This
# #difference is your maximum heart rate per minute. Your heart
# #simply will not beat faster than this maximum (220 - age).
# #When exercising to strengthen your heart, you should keep your
# #heart rate between 65% and 85% of your heart's maximum rate.
# #get the user's age as a string
# from cgitb import text


# Text_1 = input('please enter your age: ')
# # to convert the string that the user intered into the integer 
# age = int(Text_1)
# # compute the slowest and fastest beneficial 
# # heart rates from the user's age 
# max_rate = 220 - age 
# slowest_rate = max_rate * 0.65
# fastest_rate = max_rate * 0.85
# # use f-string to print a message to user 
# print(' when you exercise to strengthen your heart, you should')
# print(f'keep your heart rate between {slowest_rate :.0f} and {fastest_rate :.0f}')
# print ('beats per minute')



# # # Copyright 2020, Brigham Young University-Idaho. All rights reserved.

# # """
# # When you physically exercise to strengthen your heart, you
# # should maintain your heart rate within a range for at least 20
# # minutes. To find that range, subtract your age from 220. This
# # difference is your maximum heart rate per minute. Your heart
# # simply will not beat faster than this maximum (220 - age).
# # When exercising to strengthen your heart, you should keep your
# # heart rate between 65% and 85% of your heart's maximum rate.
# # """

# # # Get the user's age as a string.
# # text = input("Please enter your age: ")

# # # Convert the string that the user entered into an integer.
# # age = int(text)

# # # Compute the slowest and fastest beneficial
# # # heart rates from the user's age.
# # max_rate = 220 - age
# # slowest = max_rate * 0.65
# # fastest = max_rate * 0.85

# # # Use an f-string to create and print a message for the user to see.
# # print("When you exercise to strengthen your heart, you should")
# # print(f"keep your heart rate between {slowest:.0f} and {fastest:.0f}")
# # print("beats per minute.")


