#Imports
from PIL import Image, ImageFilter
import os

class BlurImage(object):
    __slots__= "rad"
    def __init__(self, radius):
        self.rad=radius
  

    def __call__(self,image):
        # directory= os.getcwd()
        im2=image.filter(ImageFilter.GaussianBlur(radius=self.rad))
        im2.show()
            

if __name__=="__main__":
    temp=BlurImage(10)
    temp()
    

