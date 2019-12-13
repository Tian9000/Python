from PIL import Image, ImageFilter

img = Image.open('./Image/pikachu.jpg')
filtered_img = img.convert('L')

filtered_img.save('funny.png', 'png')