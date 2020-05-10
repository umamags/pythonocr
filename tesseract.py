# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# load the example image and convert it to grayscale
def save_grayscale(infile, outfile):
    image = cv2.imread(infile)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            
    cv2.imwrite(outfile, gray)        
    print("Writing " + outfile)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
def run_tesseract(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    print(text)
    
if __name__ == "__main__":
   #infile = "C:\workspace\python\images\image_out_large.png"
   infile = "C:\workspace\python\images\image_out.png"
   outfile = "C:\workspace\python\images\image_out_large_grey.png"
   #save_grayscale(infile, outfile)
   run_tesseract(infile)