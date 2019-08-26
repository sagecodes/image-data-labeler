# Import libraries
import cv2
import glob
import os
import keyboard


######################################
############ Settings ###############   
######################################

# Point to Dataset
# in future use argparse
unlabeled_data_path = 'data/'

# Output path for labeled images
labeled_output_path = 'labeled_data'

# Delete Original Image?
# !!if True This will remove image from orginal dataset!!
delete_original_image = False

# Define classes for labeling
# in future define from Argparse
# Set keyboard k for each class (used for assignment)
class1 = "female" 
class1_key = 'f'

class2 = "male" 
class2_key = 'm'

######################################
############## Program ###############   
######################################

# get path names for classes
class1_path = os.path.join(labeled_output_path, class1)
class2_path = os.path.join(labeled_output_path, class2)
nolabel_path = os.path.join(labeled_output_path, 'nolabel')


# create output folder & folder for classes
if not os.path.exists(labeled_output_path):
    os.mkdir(labeled_output_path)
    os.mkdir(class1_path)
    os.mkdir(class2_path)
    os.mkdir(nolabel_path)

# create loop for each file in unlabeled_data_path that is jpg
for imagePath in glob.glob(f'{unlabeled_data_path}*.jpg'):

    # Get number of files for each class
    count_class1 = len(os.listdir(f'{class1_path}'))
    count_class2 = len(os.listdir(f'{class2_path}'))
    count_nolabel = len(os.listdir(f'{nolabel_path}'))

    # If Label keyboard key is pressed assign displayed image to label folder
    # If unsassigned key pressed assign displayed image to nolabel folder
    try: 
        if keyboard.is_pressed(class1_key):
            cv2.imwrite(f'{class1_path}/{class1}{count_class1+1}.jpg', image)
            print(f'Added to {class1} label')
        
        elif keyboard.is_pressed(class2_key):
            cv2.imwrite(f'{class2_path}/{class2}{count_class2+1}.jpg', image)
            print(f'Added to {class2} label')

        else:
            cv2.imwrite(f'{nolabel_path}/{count_nolabel+1}.jpg', image)
            print("No label assigned to key")
    except:
        pass

    # assign image to "image" variable
    image = cv2.imread(imagePath)

    # Delete original image (if enabled)
    if delete_original_image == True:
        os.remove(imagePath)
    
    # display image for labeling
    cv2.imshow("Image", image)
    cv2.waitKey(0)

# Print data count for each class
print(f'{count_class1} in {class1}')
print(f'{count_class2} in {class2}')
print(f'{count_nolabel} in nolabel')