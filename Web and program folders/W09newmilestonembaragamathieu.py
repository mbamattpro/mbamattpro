
from msilib.schema import ListView
from operator import index
from optparse import Option
from select import select
from unittest.util import sorted_list_difference
from xml.sax.xmlreader import InputSource
import math
sellected = []
sorted_list_difference
prices = []
total = 0


print('welcome to the shopping cart program!')
print()
print('please select one of the following: ')
actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
# indexed at 0
print(actions[0]) #add item
print(actions[1]) #view the cart
print(actions[2]) #mremove item
print(actions[3]) # compute the total
print(actions[4]) # quit

option = int(input('please enter an action: '))
while option != 0:
    if option == 1:
        item_added =input('what item would you like to add? ')
        item_price = float(input(f'what is the price of {item_added}? '))
        print(f"'{item_added}' has been added to the cart.")
        print('please select one of the following: ')
        print()
        actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
        
        print(actions[0]) # add item
        print(actions[1]) # view the cart
        print(actions[2]) # remove item
        print(actions[3]) # compute the total
        print(actions[4]) # quit
        option = int(input('please enter an action: '))
        list()
        sellected.append(item_added)
        prices.append(item_price)
        

    elif option == 2:
        print(f'the contents of the shopping cart are: ')
        for i in range(len(sellected)):
            print(f'{i}. {sellected[i]} -${prices[i]}')
       # print('\n'.join(map(str,sellected)))
    elif option == 3:
        for i in range(len(sellected)): # i first print the list so that the user can identify  the index of item to remove
            print(f'{i}. {sellected[i]} -${prices[i]}')
            #cmnt# here i stop the question of removing but conditioning to zero as the ending decision of the user for adding items
        removed_item = int(input( "which item would you like to remove? type ''0 = (zero)'' when you are done to remove items on the list:  "))
        for i in range(len(sellected)):
            lis = sellected[i]
        sellected.pop(removed_item) # i use pop to remove item because remove is not working for input of indexes 
        print( 'item has removed', end='\n ' ) # i add \n to get a new list
        if removed_item == 0:
            list()
            actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
            print(actions[0]) # add item
            print(actions[1]) # view the cart
            print(actions[2]) # remove item
            print(actions[3]) # compute the total
            print(actions[4]) # quit
            option = int(input('please enter an action: '))
            list()
            sellected.append(item_added)
            prices.append(item_price)
    elif option == 4:
        for i in range(len(sellected)):
            prices.append(item_price)
            total += prices[i]
            print(f'${total:.2f}')
    elif option == 5:
        quitting = input('are you sure you want to quit? yes/no: ')
        if quitting.lower() == 'yes':
            print('thank you. goodbye!')
        elif quitting.lower() == 'no':
            print('what else do you want to do?: ')
            list # if the user chooses no, here i can repeat all actions and let the program stat from the beggining
        else:
            print('invalid')
            print('welcome to the shopping cart program!')
            print()
        print('please select one of the following: ')
        actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
         # indexed at 0
        print(actions[0]) #add item
        print(actions[1]) #view the cart
        print(actions[2]) #mremove item
        print(actions[3]) # compute the total
        print(actions[4]) # quit






        print()
        print('please select one of the following: ')
        actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
# indexed at 0
        print(actions[0]) #add item
        print(actions[1]) #view the cart
        print(actions[2]) #mremove item
        print(actions[3]) # compute the total
        print(actions[4]) # quit

        option = int(input('please enter an action: '))
while option != 0:
    if option == 1:
        item_added =input('what item would you like to add? ')
        item_price = float(input(f'what is the price of {item_added}? '))
        print(f"'{item_added}' has been added.")
        print('please select one of the following: ')
        print()
        actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
        
        print(actions[0]) # add item
        print(actions[1]) # view the cart
        print(actions[2]) # remove item
        print(actions[3]) # compute the total
        print(actions[4]) # quit
        option = int(input('please enter an action: '))
        list()
        sellected.append(item_added)
        prices.append(item_price)
        

    elif option == 2:
        print(f'the contents of the shopping cart are: ')
        for i in range(len(sellected)):
         print(f'{i}. {sellected[i]} -${prices[i]}')
       # print('\n'.join(map(str,sellected)))
    elif option == 3:
        for i in range(len(sellected)): # i first print the list so that the user can identify  the index of item to remove
            print(f'{i}. {sellected[i]} -${prices[i]}')
        removed_item = int(input( "which item would you like to remove? write ''0 = zero'' when you are done to remove items on the list:  "))
        for i in range(len(sellected)):
            lis = sellected[i]
        sellected.pop(removed_item) # i use pop to remove item because remove is not working for input of indexes 
        print( 'item has removed', end='\n ' ) # i add \n to get a new list
        if removed_item == 0:
            list()
            actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
            print(actions[0]) # add item
            print(actions[1]) # view the cart
            print(actions[2]) # remove item
            print(actions[3]) # compute the total
            print(actions[4]) # quit
            option = int(input('please enter an action: '))
            list()
            sellected.append(item_added)
            prices.append(item_price)
    elif option == 4:
        prices.append(item_price)
        total += prices[i]
        print(f'${total:.2f}')
    elif option == 5:
        quitting = input('are you sure you want to quit? yes/no: ')
        if quitting.lower() == 'yes':
            print('thank you. goodbye!')
        elif quitting.lower() == 'no':
            print('what else do you want to do?: ')
            list # if the user chooses no, here i can repeat all actions and let the program stat from the beggining
            
            

            
        
        
















# from ast import Break, Continue
# from ssl import Purpose
# Purpose 

# Purpose
# #cmnt# first to prepare the list of shopping 
# from traceback import print_list


# print(' please enter the items of the shopping list(type: quit to finish):')

# shopping_list = []
# item = None

# while item != quit:
#     item = input('item: ')

#     if item.lower() != 'quit':
#         shopping_list.append(item)
#     elif item.lower() == 'quit': Continue




#         #cnt# we now have the list, please print it out to verify
#     print('the shopping list is: ')

#     print('\n'.join(map(str,shopping_list)))
#     if item.lower() == 'quit': Continue

#     print('the shopping list with indexes is:')
#     for i in range(len(shopping_list)):
#      item = shopping_list[i]
#     print(f'{i}. {item}')
#     #CMNT#  I could have just put shopping_list[i] directly in my print statement
#     #CMNT# rather than creating a separate variable if I wanted. I decided to do it
#     #CMNT# this way to make it easier to read.
#     print()

#     index = int(input(' which item would you like to change: '))
#     new_item = input('what is the new item: ')
# shopping_list[index] = new_item
# print(' the shopping list with indexes is: ')
# for i in range(len(shopping_list)):
#         item = shopping_list[i]
#         print(f'{i}. {item}')
    












# first = list[0]
# second = list[1]

# index = int(input('which index would you like to get? '))
# ucer_choice = list[index]
# books = [1,2,3,4,5,6,7,8,9,10]
# numbers_of_books = len(books)
# for i in range(len(books)):
#     book = [i]
# books.pop(3)
# print(book)
    

#     #cmnt# If you want to print the index numbers next to the elements of the list
#     #cmnt#  as you iterate through, you can print the value of the i variable:

# for i in range(len(books)):
#     book = books[i]
#     print(f'{i}. {books}')
# print()
# #cmnt# WORKING WITH PARALLEL LISTS
# names = []
# numbers = []
#  #cmnt# code here that popilates the two lists
# for i in range(len(names)):
#     name = names[i]
#     number = numbers[i]
#     print(f'{name} - {number}')
     #CMNT# REMOVING ITEMS FROM A LISTbook[3]book.pop[]


# from msilib.schema import ListView
# from optparse import Option
# from unittest.util import sorted_list_difference
# from xml.sax.xmlreader import InputSource
# import math
# sellected = []
# sorted_list_difference

# print('welcome to the shopping cart program!')
# print()
# print('please select one of the following: ')
# actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
# # indexed at 0
# print(actions[0]) #add item
# print(actions[1]) #view the cart
# print(actions[2]) #mremove item
# print(actions[3]) # compute the total
# print(actions[4]) # quit

# option = int(input('please enter an action: '))
# while option != 0:
#     if option == 1:
#         item_added =input('what item would you like to add? ')
#         print(f"'{item_added}' has been added.")
#         print('please select one of the following: ')
#         print()
#         actions = ['1. add item', '2. view the cart', '3. remove item', '4. compute the total','5. Quit']
        
#         print(actions[0]) # add item
#         print(actions[1]) # view the cart
#         print(actions[2]) # remove item
#         print(actions[3]) # compute the total
#         print(actions[4]) # quit
#         option = int(input('please enter an action: '))
#         list()
#         sellected.append(item_added)
#     if option == 2:
#         print(f'the content of the shopping cart are : ')
#         print('\n'.join(map(str,sellected)))
#         print()
#     elif option == 5:
#         print('thank you. goodbye.')
# else:
#     print(' invalid')
# print()
# print()










# print('please enter the numbers, type zero when you finished: ')
# # Please note: For this program especially, there are MANY ways to accomplish the task.
# # The following shows one way it can be done, but it's not the only way. In particular, many
# # of these tasks can be done with built-in functions (such as max(numbers)), but this
# # approach highlights how to compute those values directly using loops.
# numbers =[]
# number = -1
# while number != 0:
#     number = int(input(' enter the number: '))
#     if number != 0:
#         numbers.append(number)
# # The list "numbers" now has all the numbers the user typed

# # Step 1: Find the sum or total
# sum = 0
# for number in numbers: 
#     sum += number
#     print(f'the sum is: {sum}')
#     # The list "numbers" now has all the numbers the user typed

# # Step 1: Find the sum or total
# count = len(numbers)
# average = sum/count
# print(f'the average is: {average}')
# # Step 3: Find the max
# # We will walk through the numbers again, this time keeping track
# # of the best so far, or the highest number to that point.
# best_so_far = number
# for number in numbers:
#     if number > best_so_far:
#          # This is the new best number, so save it to that variable
#          best_so_far = number
# print(f'the largest number is: {best_so_far}')


# # Stretch Challenge 1: Find the smallest positive number:

# # We need to start with something large
# smallest_so_far = 99999999999
# # Note: If we wanted to be the most accurate here, instead of starting with a big
# # number like above, we should loop through the list until we find a positive number
# # and use that as the smallest_so_far. I'm going with the approach here, because it's
# # simpler to see and understand, but what if the list didn't have any positive numbers?
# # What if it didn't have any less than the big number I picked? These would create
# # problems that would be solved by the approach mentioned.
# for number in numbers:
#     if number > 0 and number < smallest_so_far:

#         #we have a new smallest number
#         smallest_so_far = number 
# print(f'the smallest positive number is: {smallest_so_far}')
#  # Stretch Challenge 2: Sorting the list
# sorted_list = sorted(numbers)
# print('sorted list is: ')
# for number in sorted_list:
#     print(numbers)
    


         











# # First, I'm going to set up an empty list called, friends.
# # Notice that I call it friends (with an s) not friend. This will help me
# # remember throughout my code that it is a list of potentially many friends
# # rather than a single friend.
# friends = []
# # This will be used in my loop to get the name of each friend that I want
# # to put in the list. I can start it will any value, as long as that value
# # is not "end", otherwise, it won't ever go into the loop I made to gather
# # the names.
# name = None
# while name != 'end':
#     name = input('type the name of a friend: ')
#     # Without this if statement, I would put "end" into my list as well
#     if name != 'end':
#         friends.append(name)

# print()
# print('your friends are: ')

# # Now I'm going to loop through them each one at a time to display them.
# # Notice that the list is called "friends" (with an s) but as I go through
# # it I'm going to refer to each individual name as "friend" (no s)
# for friends in friends:
#     print(friends)
    



# from PIL import Image

# image_foreground = Image.open('cat.jpg')
# image_background = Image.open('snowscape.jpg')

# image_new = Image.new('RGB', image_background.size)

# pixel_foreground = image_foreground.load()
# pixel_background = image_background.load()
# pixel_new = image_new.load()

# for width_index in range(image_foreground.width): #0, 1, 2, 3...799
#     for height_index in range(image_foreground.height): #0,1, 2, 3...599
#         red, green, blue = pixel_foreground [width_index, height_index]
#         if green > 220 and red < 80 and blue < 50:
#             pixel_new[width_index, height_index] = pixel_background[width_index, height_index]
#         else:
#             pixel_new[width_index, height_index] = pixel_foreground[width_index, height_index]

# image_new.show()





# print('it is successfully loaded')
# beach_image = Image.open('beach.jpg')
# #cmnt# image will be loaded and show
# beach_image.show()
# #cmnt#In order to access the pixels of the image,
# # cmnt# you'll need to use a few library functions.

# #cmnt#If you have loaded an image into a variable image_original,
#  #cmnt#you can use that variable to perform various operations that
#   #cmnt#related to the image. For example, you can get the size like this
# width, height = beach_image.size
# #If you want to access the pixels of the image, 
# # you can use the image variable to get access to another,
# #  internal variable that holds all of the information about the pixels.
# #  You can get the pixels of the image and store them into a variable like this
# pixel_original = beach_image.load()
# #Once you have the pixels stored in a variable,
# #  you can access the red, green,
# #  and blue (RGB) values of an individual pixel at any spot in the image,
# #  for example, the coordinates (100, 200),
# #  using the square bracket notation [100, 200] like this
# r, g, b = pixel_original[100,200]
# #do not forget to put parantheses around your (r,g,b)
# pixel_original[100,200] = (r,g,b)
# #When you are ready to save an image out to a new file,
# #  you can call the save function like this
# beach_image.save('the_file_goes_here.jpg')
# #if i want to print the size of the image or format etc
# print(beach_image.size)
# print(beach_image.format)
# pixel_original = beach_image.load()
# print(pixel_original[200,100])
# # pixel_original[200,100] = (255,0,255)
# # pixel_original[201,100] = (255,0,255)
# # pixel_original[202,100] = (255,0,255)
# # pixel_original[203,00] = (255,0,255)
# # pixel_original[204,100] = (255,0,255)
# for y in range (100,500):
#     for x in range (0,300):
#         pixel_original[x,100] = (255,0,255)

#     for x in range (0,300):
#         pixel_original[x,100] = (255,0,255)
    
#     for x in range (0,300):
#         pixel_original[x,101] = (255,0,255)
    
#     for x in range (0,300):
#         pixel_original[x,102] = (255,0,255)
    
#     for x in range (0,300):
#         pixel_original[x,103] = (255,0,255)
    
#     for x in range (0,300):
#         pixel_original[x,104] = (255,0,255)
    
#     for x in range (0,300):
#         (r,g,b) = pixel_original[x,y]
#         new_blue = b= 50 print()