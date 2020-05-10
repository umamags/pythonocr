# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# load the example image and convert it to grayscale
def save_grayscale(infile, outfile):
    print(infile, outfile)
    image = cv2.imread(infile)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.threshold(gray, 0, 255,
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            
    cv2.imwrite(outfile, gray)        
    print("Writing " + outfile)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
def process_images(top_image, bottom_image, columns, fullpath):
    file = open(fullpath +"/output.txt","w", encoding="utf-8")
    for col in range(int(columns)):   
        top_image1 = top_image + str(col) + ".png"        
        bottom_image1 = bottom_image + str(col) + ".png"
        top_array, bottom_array, difference = run_tesseract(top_image1, bottom_image1, col)
        
        file.write("Top:")
        for entry in top_array:
            file.write(entry + " ")
        file.write("\n") 
        file.write("Bot:")
        for entry in bottom_array:
            file.write(entry + " ")
        file.write("\n")
        file.write("Diff:" + str(difference))
        file.write("\n") 
        file.writelines("------------------\n")
    file.close() 
        
def run_tesseract(top_image, bottom_image, col):
    print(top_image)
    top_text = pytesseract.image_to_string(Image.open(top_image))
    bottom_text = pytesseract.image_to_string(Image.open(bottom_image))
    return compare(top_text, bottom_text, col)
    
def compare(top_text, bottom_text, col):
    bottom_array = []
    list = bottom_text.split("\n")
    for entry in list:
        if len(entry) > 0:
            bottom_array.append(entry)
    no_of_elements = len(bottom_array)
    print("Bot:", bottom_array)
    
    top_array = []
    list = top_text.split("\n")
    for entry in list:
        if len(entry) > 0:
            top_array.append(entry)    
    
    print("Top:", top_array)
    
    difference = ""
    seq = 0
    for entry in bottom_array:
        if len(top_array) > seq:
            if entry != top_array[seq]:
                difference = difference + "col:" + str(col+1) + "::row:" + str(seq+1) + "::Value::" + entry + "\n"
        seq = seq + 1
    if len(difference) == 0:
        difference = "No difference"       
    print("Diff:", difference)
    
    return top_array, bottom_array, difference

def Diff(li1, li2): 
    return (list(set(li1) - set(li2))) 
       
if __name__ == "__main__":
   #infile = "C:\workspace\python\images\image_out_large.png"
   top_image = "C:/workspace/python/pythonocr/images/find_the_error/top_image_out_"
   bottom_image = "C:/workspace/python/pythonocr/images/find_the_error/bottom_image_out_"
   #save_grayscale(infile, outfile)
   process_images(top_image, bottom_image)