from PIL import Image
import random

# размеры изображения
width = 256
height = 256

# создаем новое изображение
img = Image.new('RGB', (width, height), color='white')

# получаем доступ к пикселям изображения
pixels = img.load()

# проходим по каждому пикселю и задаем случайный цвет
for i in range(width):
    for j in range(height):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pixels[i, j] = (r, g, b)
print(pixels)
# сохраняем изображение
img.show() #'random_color_pixels.png')




