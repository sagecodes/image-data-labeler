# Import libraries
import cv2
import glob
import os
import keyboard


# Point to Dataset
# in future use argparse

unlabeled_data_path = 'data/'


# Define classes for labeling
# in future define from Argparse
# Set key for each class


class1 = "female" 
class1_key = 'f'

class2 = "male" 
class2_key = 'm'

# create folder for classes
#TODO
# Currently you must make folders with matching class names

for imagePath in glob.glob(f'{unlabeled_data_path}*.jpg'):

    # Get number of files for each class
    count_class1 = len(os.listdir(f'{class1}/'))
    count_class2 = len(os.listdir(f'{class2}/'))
    count_nolabel = len(os.listdir('nolabel/'))
    print(count_class1)
    print(count_class2)

    try: 
        if keyboard.is_pressed('f'):
            cv2.imwrite(f'{class1}/{class1}{count_class1+1}.jpg', image)
            print(f'Added to {class1} label')
        
        elif keyboard.is_pressed('m'):
            cv2.imwrite(f'{class2}/{class2}{count_class2+1}.jpg', image)
            print(f'Added to {class2} label')
        
        else:
            cv2.imwrite(f'nolabel/nolabel{count_nolabel+1}.jpg', image)
            print("that key is not defined")

    except:
        pass

    # Read & Display image to be labeled
    image = cv2.imread(imagePath)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

