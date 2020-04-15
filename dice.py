from PIL import Image , ImageOps , ImageDraw
print ("salam")

img = Image.open('image.png')
img = ImageOps.grayscale(img)
img = ImageOps.equalize(img)


dicew = 20

dicesize = int((img.width * 1.0 / dicew))
diceh  =  int(img.height * 1.0 / img.width  * dicew)

print(dicew , diceh , dicesize)


# img.show()

nim = Image.new("L" , (img.width , img.height) , 'white')

nimd = ImageDraw.Draw(nim)

for y in range(0 , img.height - dicesize , dicesize ):
    for x in range(0 , img.width - dicesize , dicesize):
        thisSectorColor = 0
        for dicex in range(0,dicesize):
            for dicey in range(0 , dicesize):
                thisColor = img.getpixel((x+dicex,y+dicey))
                thisSectorColor += thisColor
        thisSectorColor = int(thisSectorColor / (dicesize ** 2))
        nimd.rectangle([(x,y) , (x+dicesize , y + dicesize)] , thisSectorColor)

        diceNumber = int((255 -thisSectorColor) * 6.0/255 + 1)
        print  diceNumber ,
    print  
    


nim.show()



