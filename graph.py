import random
from PIL import Image, ImageDraw

mode = int(input('mode:')) #Считываем номер преобразования. 
image = Image.open("44.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	
pix = image.load() #Выгружаем значения пикселей.
print(width, height)
if (mode == 0):
    for i in range(width):
        for j in range(height):            
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            #S = (a + b + c) // 3
            S = (c)
            draw.point((i, j), (S, S, S))
if (mode == 1):
    factor = int(input('factor:'))
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                a, b, c = 255, 255, 255
            else:
                a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))
image.save("ans.jpg", "JPEG")
del draw