import numpy as np

class MyClassifier():
    
    ''' Do not change the class name. Do not change any of the existing function names. You may add extra functions as you see fit.'''
    
    def __init__(self):
        self.class_labels = ['edible_1', 'edible_2', 'edible_3', 'edible_4', 'edible_5',
                            'poisonous_1', 'poisonous_2', 'poisonous_3', 'poisonous_4', 'poisonous_5']
        
        
    def setup(self):
        ''' This function will initialise your model. 
            You will need to load the model architecture and load any saved weights file your model relies on.
        '''

        pass
        
    def test_image(self, image):
        ''' This function will be given a PIL image, and should return the predicted class label for that image. 
            Currently the function is returning a random label.
                
        '''
              
        predicted_cls = np.random.choice(self.class_labels)
        
        return predicted_cls
        
