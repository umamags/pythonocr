# Improting Image class from PIL module 
from PIL import Image 
import sys 
import tesseract

def main(argv):
    # Opens a image in RGB mode 
    topfile = "C:/workspace/python/pythonocr/images/find_the_error/top_image_out_"
    bottomfile = "C:/workspace/python/pythonocr/images/find_the_error/bottom_image_out_"
    im = Image.open(r"C:/workspace/python/pythonocr/images/find_the_error/image.png") 
        
    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    orig_width, orig_height = im.size 
    print(orig_width, orig_height)
    
    # Setting the points for cropped image 
    #left = 300
    #top = 80
    #right = 1000
    #bottom = 600
    #width = 415 -333 = 82
    
    # Top file
    width = 161
    height = 253    
    left = 364
    top = 113
    right = left+width
    bottom = top+height
    
    if len(argv) == 4:
        left = int(argv[0])
        top = int(argv[1])
        right = int(argv[2])
        bottom = int(argv[3])
    
    for col in range(6):        
        print(left, top, right, bottom)
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
   