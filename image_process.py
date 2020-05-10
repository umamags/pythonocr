# Improting Image class from PIL module 
from PIL import Image 
import sys 
import tesseract
import pandas as pd 
import xlrd 

def main(argv):
    basedir = "C:/workspace/python/pythonocr"
    excel_mapping_file = basedir + "/mappings/image_mappings.xlsx"
     
    df0 = pd.read_excel(excel_mapping_file, sheet_name="Main")
    print(df0.shape)
    
    foldername = "find_the_error"
    if len(argv) > 0:
        foldername = argv[0]
    topfile = basedir + "/images/" + foldername + "/top_image_out_"
    bottomfile = basedir + "/images/" + foldername + "/bottom_image_out_"
    im = Image.open(r"" + basedir + "/images/" + foldername + "/image.png") 
        
    orig_width, orig_height = im.size 
    
    # Top file
    width = 161
    height = 253    
    left = 364
    top = 113
    right = left+width
    bottom = top+height
    
    for col in range(6):        
        im1 = im.crop((left, top, right, bottom)) 
        ch_width, ch_height = im1.size 
        im1.save(topfile + str(col) + ".png", 'png')
        left = left + width
        right = right + width
    
    # Bottom file
    width = 100
    height = 154    
    left = 445
    top = 408
    right = left+width
    bottom = top+height
    for col in range(6):        
        print(left, top, right, bottom)
        im1 = im.crop((left, top, right, bottom)) 
        
        ch_width, ch_height = im1.size 
        new_size = ch_width*2, ch_height*2
        
        im2 = im1.resize(new_size, Image.ANTIALIAS)
        im2.save(bottomfile + str(col) + ".png", 'png')
        left = left + width
        right = right + width
    
    tesseract.process_images(topfile, bottomfile)    
    #save_grayscale(infile, outfile)
    #im2 = im1.resize(new_size, Image.ANTIALIAS)
    #ch2_width, ch2_height = im2.size 
    #print(ch2_width, ch2_height)
    #im2.save(outfile2, 'png')
    
if __name__ == "__main__":
   print("Program started")
   main(sys.argv[1:])
   print("Program ended")
   