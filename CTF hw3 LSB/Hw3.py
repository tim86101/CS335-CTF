from PIL import Image
img1 = Image.open("flag1.jpg").convert('L')
img2 = Image.open("flag2.jpg").convert('L')
img3 = Image.open("flag3.jpg").convert('L')
code1 = 0
code2 = 0
code3 = 0
for x in range (img1.size[0]):
    for y in range (img1.size[1]):
        code1 += img1.getpixel((x,y)) % 2
for x in range (img2.size[0]):
    for y in range (img2.size[1]):
        code2 += img2.getpixel((x,y)) % 2
for x in range (img3.size[0]):
    for y in range (img3.size[1]):
        code3 += img3.getpixel((x,y)) % 2
print (code1,",",code2,",",code3)
