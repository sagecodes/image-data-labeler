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
# create folder for classes



# Display first image from dataset

# Assign to new dataset with key
# move image to designated class folder

for imagePath in glob.glob(f'{unlabeled_data_path}*.jpg'):

    # Get number of files for each class
    count_class1 = len(os.listdir('female/'))
    count_class2 = len(os.listdir('male/'))
    print(count_class1)
    print(count_class2)

    # Read & Display image to be labeled
    image = cv2.imread(imagePath)
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    try: 
        if keyboard.is_pressed('f'):
            cv2.imwrite(f'female/female{count_class1+1}.jpg', image)
            print('Added to female label')
        
        elif keyboard.is_pressed('m'):
            cv2.imwrite(f'male/male{count_class2+1}.jpg', image)
            print('Added to male label')
        
        else:
            cv2.imwrite("notlabeled/newimage.jpg", image)
            print("that key is not defined")

    except:
        break

