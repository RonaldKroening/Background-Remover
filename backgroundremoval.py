from PIL import Image
import math
import random
def background_remover(imageName):
    im = Image.open(imageName)

    si = im.size
    img = im.convert("RGBA")
    pix = img.load()
    xmax = int(si[0])
    ymax = int(si[1])
    r1 = pix[0, 0][0]
    g1 = pix[0, 0][1]
    b1 = pix[0, 0][2]
    #array for red values
    avgr = []
    #array for green values
    avgg = []
    #array for blue values
    avgb = []
    avgr1 = 0
    avgg1 = 0
    avgb1 = 0
    #this gets the rgb values of every pixel in the first line of the image and stores them in arrays
    for x in range(xmax):
        r2 = pix[x, 0][0]
        g2 = pix[x, 0][1]
        b2 = pix[x, 0][2]
        avgr.append(r2)
        avgg.append(g2)
        avgb.append(b2)
    #gets sum of all values
    for x in range(len(avgr)):
        avgr1 = avgr1 + avgr[x]
        avgg1 = avgg1 + avgg[x]
        avgb1 = avgb1 + avgb[x]
    #finds average
    avgr1 = avgr1 / len(avgr)
    avgg1 = avgg1 / len(avgg)
    avgb1 = avgb1 / len(avgb)
    for x in range(xmax):
        for y in range(ymax):
            r2 = int(pix[x, y][0])
            g2 = int(pix[x, y][1])
            b2 = int(pix[x, y][2])
            # a = (r2 - r1)**2
            # b = (g2 - g1)**2
            # c = (b2 - b1)**2
            # d = math.sqrt(a + b + c)
            difr = abs(r2 - avgr1)
            difg = abs(g2 - avgg1)
            difb = abs(b2 - avgb1)
            #get difference between average and pixel's respective values
            difavg = (difr + difg + difb) / 3
            #find average difference 
            if (difavg < 7):
                pix[x, y] = (255, 255, 255, 0)
    newn = str(imageName).split(".")
    name = newn[0] + "-BGRemoved.png"
    print(name)
    img.save(name, "PNG")

#name of image, number codes for Red, Green, Blue
def isWhite(p):
    c = 0
    if(p[0] == 255):
        c = c + 1
    if(p[1] == 255):
        c = c + 1
    if(p[2] == 255):
        c = c + 1
    if(c == 3):
        return True
    else:
        return False

def isBlack(p):
    c = 0
    if(p[0] == 0):
        c = c + 1
    if(p[1] == 0):
        c = c + 1
    if(p[2] == 0):
        c = c + 1
    if(c == 3):
        return True
    else:
        return False


def black_white(imageName):
    im = Image.open(imageName)

    si = im.size
    img = im.convert("RGBA")
    pix = img.load()
    xmax = int(si[0])
    ymax = int(si[1])
    for x in range(xmax):
        for y in range(ymax):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            s = r + g + b
            s1 = s / 3
            c = 0
            if (s1 >= 128):
                pix[x,y] = (255,255,255)
            else:
                pix[x, y] = (0, 0, 0)


    img.save("imgg.png", "PNG")

background_remover("earth.jpg")
#black_white("img2.png")