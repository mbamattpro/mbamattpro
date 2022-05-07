import csv

high = 0
low = 150
high2 = 0
low2 = 150
high3 = 0
low3 = 150


lows = []
c_high = ''
c_low = ''
c_high2 = ''
c_low2 = ''
c_high3 = ''
c_low3 = ''


user_choice = 0
count_y = 0
count_c = 0
total_y = 0
total_c = 0
print()


with open('life-expectancy.csv', 'r') as life_expectancy_file:
      main_file = life_expectancy_file.readlines()
data = main_file[1: ]
data.sort( reverse= True)
my_input = input(' what is the year of interest: ')
my_input2 = input(' what is the country of interest: ')
for x in data:
      x = x.strip()
      parts = x.split(',')
      country = parts[0]
      country_code = parts[1]
      year = parts[2]
      life_expectancy = float(parts[3])
      if high < life_expectancy:
            high = life_expectancy
            c_high = country
            year_oh = year
      elif life_expectancy < low:
            low = life_expectancy
            c_low = country
            year_ol = year
      if my_input == year: 
            count_y += 1
            total_y = total_y + life_expectancy
            if high2 < life_expectancy:
                  high2 = life_expectancy
                  c_high2 = country
                  year_yh = year
            elif life_expectancy < low2:
                  low2 = life_expectancy
                  c_low2 =  country
                  year_yl = year
      if my_input2.capitalize() == country:
            count_c += 1
            total_c = total_c + life_expectancy
            if high3 < life_expectancy:
                  high3 = life_expectancy
                  c_high3 = country 
                  year_ch = year 
            elif life_expectancy < low3:
                  low3 = life_expectancy 
                  c_low3 = country 
                  year_cl = year 
  # now we can find average when the choice is a year
average_y = total_y/count_y
# and then we can find the average when the choice is country
average_c = total_c/ count_c
print()

print(f'the overall life expectancy is {high} from {c_high} in {year_oh}')
print(f'the overall life expectancy is {low} from {c_low} in {year_ol}')

print(f'{my_input2.capitalize()}')
print()

print(f'the average life expectnacy across all countries in {my_input2} was {average_y: .2f} ')
print(f'the maximum life expectance was in {c_high2} with {high2} in {year_yh}')
print(f'the minimum life expectancy was in { c_low2} from {c_low2} in {year_yl}')
print()

print(f'the life expectancy from {my_input2} : ')

print(f' the average life expectancy of {my_input2.capitalize()} was {average_c: .2f}')
print(f'the maximum life expectancy of {my_input2.capitalize()} was {high3} in {year_ch} ')
print(f'the minimum life expectancy of {my_input2.capitalize()} was {low3} in {year_cl}  ')
print()






# chosen_volume = input('which volume of scriptuure would you like to learn about? ')
# max_chapters = -1
# book_with_max = ""

# with open('books_and_chapters (1).txt') as books_file:
#       for line in books_file:
#             parts = line.split(":")
#             book = parts[0].strip()
#             chapters = int(parts[1])
#             scripture = parts[2].strip()
#             if scripture.lower() == chosen_volume.lower():
#                   print(f'scripture: {scripture}, book: {book}, chapters: {chapters}')
#                   if chapters > max_chapters:
#                         max_chapters = chapters
#                         book_with_max = book
# print(f'the book with the most chapters in the {chosen_volume} is: {book_with_max}')
# print(f'it has {max_chapters} chapters.')



# chosen_volume = input("Which volume of scripture would you like to learn about? ")

# max_chapters = -1
# book_with_max = ""

# # Open the file with the information
# with open("books_and_chapters (1).txt") as books_file:

#     # Iterate through the file one line at a time
#     for line in books_file:
#         # Split up the line based on the ":"
#         parts = line.split(":")

#         # Get the book and strip off any leading/trailing whitespace
#         book = parts[0].strip()

#         # Get the number of chapters as an integer
#         chapters = int(parts[1])

#         # Get the volume of scripture and strip off any leading/trailing whitespace
#         scripture = parts[2].strip()

#         # Check if this belongs to the user's chosen volume:
#         if scripture.lower() == chosen_volume.lower():
#             # Only display and check for the max inside the body
#             # of this if statement. That way we are limiting it
#             # to the user's chosen volume.
#             print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

#             # Check to see if this book has the most chapters we've seen so far
#             if chapters > max_chapters:
#                 # This book is the new best one!
#                 max_chapters = chapters # The max chapters is now this one
#                 book_with_max = book # Remember the name of the book

# # This is now after the loop has finished
# print(f"The book with the most chapters in the {chosen_volume} is: {book_with_max}")
# print(f"It has {max_chapters} chapters.")



# max_chapters = -1
# book_with_max = ""

# # Open the file with the information
# with open("books_and_chapters (1).txt") as books_file:

#     # Iterate through the file one line at a time
#     for line in books_file:
#         # Split up the line based on the ":"
#         parts = line.split(":")

#         # Get the book and strip off any leading/trailing whitespace
#         book = parts[0].strip()

#         # Get the number of chapters as an integer
#         chapters = int(parts[1])

#         # Get the volume of scripture and strip off any leading/trailing whitespace
#         scripture = parts[2].strip()

#         print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

#         # Check to see if this book has the most chapters we've seen so far
#         if chapters > max_chapters:
#             # This book is the new best one!
#             max_chapters = chapters # The max chapters is now this one
#             book_with_max = book # Remember the name of the book

# # This is now after the loop has finished
# print(f"The book with the most chapters is: {book_with_max}")
# print(f"It has {max_chapters} chapters.")



# from unicodedata import name


# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]

# oldest_age = 1
# oldest_name = ""
# for person_line in people:
#       parts = person_line.split()
#       name = parts[0]
#       age = int(parts[1])
#       if age > oldest_age:
#             oldest_age = age 
#             oldest_name = name
# print(f' the oldest person is: {oldest_name} and he is {oldest_age} years old')

# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]

# # Start our youngest_age variable at something larger than anyone we'll find
# youngest_age = 9999

# # This will keep track of the person with the youngest age
# youngest_name = ""

# # Go through each person in the list
# for person_line in people:

#     parts = person_line.split() # by default this will split on the space

#     # Set variables for the two different parts
#     name = parts[0]
#     age = int(parts[1])

#     # Check to see if this current person is younger than the youngest
#     # that we have seen so far
#     if age < youngest_age:
#         # This person is the new "youngest"

#         # Save their age as the new youngest
#         youngest_age = age

#         # Save their name as the youngest name
#         youngest_name = name

# # Outside of the loop, so we are all done now
# print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")



# people = [
#     ["Stephanie 36"],
#     ["John 29"],
#     ["Emily 24"],
#     ["Gretchen 54"],
#     ["Noah 12"],
#     ["Penelope 32"],
#     ["Michael 2"],
#     ["Jacob 10"]
# ]
# oldest = 99999
# oldest_name = ''
# for a_person in people:
#       person_name = a_person[0]
#       age = a_person[0]
#       if age > oldest:
#             oldest = age
#             oldest_name = person_name
# print(f'the oldest person is: {oldest} years old.')
# print(f' the name of the oldest person is: {oldest_name}')




# shopping_cart = [
      
# ['chips', 2.99],
# ['bread', 2.50],
# ['milk', 1.99],
# ['ice cream', 3.99],
# ['cheese', 5.99],
# ['caandy bar', 0.99]
# ]
# max_price = -1
# max_product =  ""
# for item in shopping_cart:
#       product_name = item[0]
#       price = item[1]
#       if price > max_price:
#             max_price = price
#             max_product = product_name

# print(f'the maximum price is: {max_price}')
# print(f'the product with the maximum price is: {max_product}')





# numbers = [1, 42 , 24 ,28 , 5 , 60 , 10 , 2 , 11 , 25 , 21 ]
# largest_so_far = numbers[0]
# for number in numbers:
#       if number > largest_so_far:
#             largest_so_far = number
# print(f'the largest number is: {largest_so_far}')




# from tarfile import PAX_NAME_FIELDS


# PAX_NAME_FIELDS

# with open('life_expectancy.csv') as file :
#    for line in file :
#      # print(line)
#       line = line.strip()
#       parts = line.split(" ")
#       print(parts[0])

      # name = parts[0]
      # code = parts[1]
      # year = parts[2]
      # life_expctncy = float(parts[3])
      # print(life_expctncy)














#course_file = open('courses_list.text')
#cmnt# here i can substitute the above code by: the following line 
#with open('courses_list.text') as course_file :
 #   for line in course_file :
  #      print(line)
   #     print('Godbye')
# with open('books.txt') as book_file:
#     for line in book_file:
#         #print(line) # i can deactivate this so that strip function can work 

#          # The .strip() function returns a new line that doesn't have leading
#         # or trailing whitespace. In other words, it strips off the "\n" that
#         # would otherwise be at the end of each line.
#         book = line.strip()
#         print(book)



# with open('hr_system.txt') as a_list:
#      for line in a_list:

#     #     print(line)
#           line = line.strip()
#           parts = line.split(' ')

#           name = parts[0]
#           id_no = parts[1]
#           job_title =parts[2]
#           salary = parts[3]
#           print(name, id_no, job_title,salary)
