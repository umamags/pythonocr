# Improting Image class from PIL module 
from PIL import Image 
import sys 
import tesseract
import pandas as pd 
import xlrd 
import os

def main(argv):
    # basedir = "C:/workspace/python/pythonocr"
    basedir = os.getcwd()
    excel_mapping_file = basedir + "/mappings/image_mappings.xlsx"
     
    df = pd.read_excel(excel_mapping_file, sheet_name="Main")
    for index, row in df.iterrows():
        if row["Process"] == "Y":
            process(basedir, row)
    foldername = "find_the_error"
    
def process(basedir, row):
    foldername = row['foldername']    
    fullpath = basedir + "/images/" + foldername 
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
        
    topfile = basedir + "/images/" + foldername + "/top_image_out_"
    bottomfile = basedir + "/images/" + foldername + "/bottom_image_out_"
    im = Image.open(r"" + basedir + "/images/" + foldername + ".png") 
    im.save(basedir + "/images/" + foldername + "/image.png", 'png')
        
    orig_width, orig_height = im.size 
    
    # Top file
    #width = 161
    #height = 253    
    #left = 364
    #top = 113
    
    width = row['top_width']
    height = row['top_height']
    left = row['top_left']
    top = row['top_top']
    
    right = left+width
    bottom = top+height
    
    for col in range(int(row['columns'])):        
        im1 = im.crop((left, top, right, bottom)) 
        ch_width, ch_height = im1.size 
        im1.save(topfile + str(col) + ".png", 'png')
        left = left + width
        right = right + width
    
    # Bottom file
    width = row['bottom_width']
    height = row['bottom_height']
    left = row['bottom_left']
    top = row['bottom_top']
    
    right = left+width
    bottom = top+height
    for col in range(int(row['columns'])):        
        im1 = im.crop((left, top, right, bottom)) 
        
        ch_width, ch_height = im1.size 
        new_size = ch_width*2, ch_height*2
        
        im2 = im1.resize(new_size, Image.ANTIALIAS)
        im2.save(bottomfile + str(col) + ".png", 'png')
        left = left + width
        right = right + width
    
    tesseract.process_images(topfile, bottomfile, row['columns'], fullpath)    
    
if __name__ == "__main__":
   print("Program started")
   main(sys.argv[1:])
   print("Program ended")
   