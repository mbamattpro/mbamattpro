from tarfile import PAX_NAME_FIELDS


PAX_NAME_FIELDS

with open('life_expectancy.csv') as file :
   for line in file :
     # print(line)
      line = line.strip()
      parts = line.split(" ")
      print(parts[0])

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
