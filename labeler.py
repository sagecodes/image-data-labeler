# Import libraries
import cv2
import glob
import os
import keyboard


# Point to Dataset
# in future use argparse

unlabeled_data_path = 'data/'
labeled_output_path = 'labeled_data'


# Define classes for labeling
# in future define from Argparse
# Set key for each class


class1 = "female" 
class1_key = 'f'

class2 = "male" 
class2_key = 'm'


# create output folder & folder for classes
if not os.path.exists(labeled_output_path):
    os.mkdir(labeled_output_path)
    os.mkdir(os.path.join(labeled_output_path, class1))
    os.mkdir(os.path.join(labeled_output_path, class2))
    os.mkdir(os.path.join(labeled_output_path, 'nolabel'))

class1_path = os.path.join(labeled_output_path, class1)
class2_path = os.path.join(labeled_output_path, class2)
nolabel_path = os.path.join(labeled_output_path, 'nolabel')

for imagePath in glob.glob(f'{unlabeled_data_path}*.jpg'):

    # Get number of files for each class
    count_class1 = len(os.listdir(f'{class1_path}'))
    count_class2 = len(os.listdir(f'{class2_path}'))
    count_nolabel = len(os.listdir(f'{nolabel_path}'))
    print(count_class1)
    print(count_class2)

    try: 
        if keyboard.is_pressed('f'):
            cv2.imwrite(f'{class1_path}/{class1}{count_class1+1}.jpg', image)
            print(f'Added to {class1} label')
        
        elif keyboard.is_pressed('m'):
            cv2.imwrite(f'{class2_path}/{class2}{count_class2+1}.jpg', image)
            print(f'Added to {class2} label')
        
        else:
            cv2.imwrite(f'{nolabel_path}/{count_nolabel+1}.jpg', image)
            print("No label assigned to key")

    except:
        pass

    # Read & Display image to be labeled
    image = cv2.imread(imagePath)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

