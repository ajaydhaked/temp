#Imports
from PIL import Image,ImageOps

class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type=flip_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        try:
            if self.flip_type=="horizontal":
                img= ImageOps.flip(image)
                img.show()
            elif self.flip_type=="vertical":
                img=ImageOps.mirror(image)
                img.show()
            else:
                print("invalid flip_type")
        except:
            print("Could Not library")
        

            

