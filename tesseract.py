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
def process_images(top_image, bottom_image):
    for col in range(6):   
        top_image1 = top_image + str(col) + ".png"
        bottom_image1 = bottom_image + str(col) + ".png"
        run_tesseract(top_image1, bottom_image1)
        
def run_tesseract(top_image, bottom_image):
    print(top_image)
    top_text = pytesseract.image_to_string(Image.open(top_image))
    bottom_text = pytesseract.image_to_string(Image.open(bottom_image))
    compare(top_text, bottom_text)
    
def compare(top_text, bottom_text):
    top_array = []
    list = top_text.split("\n")
    for entry in list:
        if len(entry) > 0:
            top_array.append(entry)    
    top_array = top_array[0:7]
    print(top_array)
    
    bottom_array = []
    list = bottom_text.split("\n")
    for entry in list:
        if len(entry) > 0:
            bottom_array.append(entry)
    print(bottom_array)
    print("Difference::")
    print(Diff(top_array,bottom_array))
    

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 
       
if __name__ == "__main__":
   #infile = "C:\workspace\python\images\image_out_large.png"
   top_image = "C:/workspace/python/pythonocr/images/find_the_error/top_image_out_"
   bottom_image = "C:/workspace/python/pythonocr/images/find_the_error/bottom_image_out_"
   #save_grayscale(infile, outfile)
   process_images(top_image, bottom_image)