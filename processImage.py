import numpy as np

from PIL import Image

#---Creates and populates a matrix with RGB values, for a given colour palette

def generateMatrix(filePath):

    myImage = Image.open(filePath).convert('RGB') # converts image to greyscale
    pix = myImage.load() # loads it as a Pixel Access Object
    if myImage.size[1] != myImage.size[0]:
        raise ValueError('Input image must be square')

    #--Construct the colour matrix, before any palette conversions

    global width
    global colorMatrix
    width = myImage.size[0] # the height & width of the image
    colorMatrix = [[0 for num in range(width)] for num in range(width)] # Obtain matrix (all elements are zero)

    populateMatrix(pix) # Populate the matrix with the RGB values

    #---Convert the colour palette.

    convertPalette() #Convert RGB to color palette

    return colorMatrix


def populateMatrix(pix):
    for w in range(0, width):
        for h in range(0, width):
            colorMatrix[w][h] = pix[w, h] #Stored as RGB values in an array

def convertPalette():
    for w in range(0, width):
        for h in range(0, width):
            RGB = colorMatrix[w][h]
            convertedRGB = [-1,-1,-1]
            for i in range(3):
                convertedRGB[i] = int(RGB[i] / 128) * 255
            colorMatrix[w][h] = tuple(convertedRGB)
