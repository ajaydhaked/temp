#Imports
from PIL import Image
# import random

class CropImage():
    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape=shape
        self.crop_type=crop_type


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if(self.crop_type=="center"):
            (width,height)= image.size
            top=(height/2)-self.shape[0]/2
            bottom=(height/2)+self.shape[0]/2
            left=(width/2)-self.shape[1]/2
            right=(width/2)+self.shape[1]/2
        else:
            top=0
            bottom=self.shape[0]
            left=0
            right=self.shape[1]

        try:
            im=image.crop((left,top,right,bottom))
            im.show()
        except:
            print("Invalid size!!!")



 