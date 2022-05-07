a = 1
b = 3
c = -2
result = a + b * 7 % 4 - c
print(result)

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






# # print('it is successfully loaded')
# # beach_image = Image.open('beach.jpg')
# # #cmnt# image will be loaded and show
# # beach_image.show()
# # #cmnt#In order to access the pixels of the image,
# # # cmnt# you'll need to use a few library functions.

# # #cmnt#If you have loaded an image into a variable image_original,
# #  #cmnt#you can use that variable to perform various operations that
# #   #cmnt#related to the image. For example, you can get the size like this
# # width, height = beach_image.size
# # #If you want to access the pixels of the image, 
# # # you can use the image variable to get access to another,
# # #  internal variable that holds all of the information about the pixels.
# # #  You can get the pixels of the image and store them into a variable like this
# # pixel_original = beach_image.load()
# # #Once you have the pixels stored in a variable,
# # #  you can access the red, green,
# # #  and blue (RGB) values of an individual pixel at any spot in the image,
# # #  for example, the coordinates (100, 200),
# # #  using the square bracket notation [100, 200] like this
# # r, g, b = pixel_original[100,200]
# # #do not forget to put parantheses around your (r,g,b)
# # pixel_original[100,200] = (r,g,b)
# # #When you are ready to save an image out to a new file,
# # #  you can call the save function like this
# # beach_image.save('the_file_goes_here.jpg')
# # #if i want to print the size of the image or format etc
# # print(beach_image.size)
# # print(beach_image.format)
# # pixel_original = beach_image.load()
# # print(pixel_original[200,100])
# # # pixel_original[200,100] = (255,0,255)
# # # pixel_original[201,100] = (255,0,255)
# # # pixel_original[202,100] = (255,0,255)
# # # pixel_original[203,00] = (255,0,255)
# # # pixel_original[204,100] = (255,0,255)
# # for y in range (100,500):
# #     for x in range (0,300):
# #         pixel_original[x,100] = (255,0,255)

# #     for x in range (0,300):
# #         pixel_original[x,100] = (255,0,255)
    
# #     for x in range (0,300):
# #         pixel_original[x,101] = (255,0,255)
    
# #     for x in range (0,300):
# #         pixel_original[x,102] = (255,0,255)
    
# #     for x in range (0,300):
# #         pixel_original[x,103] = (255,0,255)
    
# #     for x in range (0,300):
# #         pixel_original[x,104] = (255,0,255)
    
# #     for x in range (0,300):
# #         (r,g,b) = pixel_original[x,y]
# #         new_blue = b= 50 
        