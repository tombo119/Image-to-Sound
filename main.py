import numpy as np
import math
from PIL import Image
import os, argparse

from processImage import generateMatrix
from hilbertCurve import hilbertMatrix
from createSound import generateMusic


# Initialises the argument parser
parser = argparse.ArgumentParser()
# Adds the required arguments
parser.add_argument("imageFilePath", help="The file path of the image to be processed") # by default this is a string
parser.add_argument("--usage", help="python ProcessImage.py <path_to_file>\nPreferably the image should be in the same folder as this python module")
# Enables the use of these arguments in the code below
args = parser.parse_args()
 
colorMatrix = generateMatrix(args.imageFilePath) #Generate the colour matrix

colorVector = hilbertMatrix(colorMatrix) #Turns matrix into vector using Hilbert curve



tempo = int(input('Enter desired tempo:'))

generateMusic(colorVector, tempo) #Generates the music as a MIDI file using the vector
