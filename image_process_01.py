# Improting Image class from PIL module 
from PIL import Image 
import sys 

def main(argv):
    # Opens a image in RGB mode 
    outfile = "images\image_out.png"
    outfile2 = "images\image_out_large.png"
    im = Image.open(r"C:\workspace\python\images\image.png") 
        
    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    orig_width, orig_height = im.size 
    print(orig_width, orig_height)
    
    new_size = int(orig_width*1.5), int(orig_height*1.5) 
    # Setting the points for cropped image 
    #left = 300
    #top = 80
    #right = 1000
    #bottom = 600
    #width = 415 -333 = 82
    left = 333
    top = 97
    right = 333+82
    bottom = 380
    
    if len(argv) == 4:
        left = int(argv[0])
        top = int(argv[1])
        right = int(argv[2])
        bottom = int(argv[3])
    
    print(left, top, right, bottom)
    # Cropped image of above dimension 
    # (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 
    ch_width, ch_height = im1.size 
    print(ch_width, ch_height)
    
    # Shows the image in image viewer 
    im1.save(outfile, 'png')
    im1.show()
    
    im2 = im1.resize(new_size, Image.ANTIALIAS)
    ch2_width, ch2_height = im2.size 
    print(ch2_width, ch2_height)
    im2.save(outfile2, 'png')
    
if __name__ == "__main__":
   main(sys.argv[1:])