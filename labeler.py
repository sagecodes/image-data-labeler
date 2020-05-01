# Import libraries
import cv2
import glob
import os
import keyboard
import click
import json

# TODO:
# Keep track of labels in DF / csv
# start index option

# unlabeled_data_path = 'data/'
# labeled_output_path = 'labeled_data'
@click.command()
@click.option('--classes', default=None, help='class', type=str)
@click.option('--input_path', default=None, help='input')
@click.option('--output_path', default=None, help='output')
def labeler(classes, input_path, output_path):
    # convert classes arg to dict
    classes = classes.replace("'", '"')
    json.loads(classes)
    classes = eval(classes)
    print(type(classes))
    print(classes)

    # create output folder if it does not exsist
    if not os.path.exists(output_path):
            os.mkdir(output_path)
    
    # create nolabel output folder if it does not exsist
    nolabel_path = os.path.join(output_path, 'nolabel')
    if not os.path.exists(nolabel_path):
            os.mkdir(nolabel_path)
    
    # Check for label data folder and each sub folder for classes
    # Creates the folder if it does not exsist
    class_obj = {}
    for class_key in classes:
        class_path = os.path.join(output_path, classes[class_key])
        class_obj[class_key] = {"class": classes[class_key], 
                                    "path": class_path, 
                                    "count": None}
        
        if not os.path.exists(class_path):
            os.mkdir(class_path)

        class_obj[class_key]["count"] = len(os.listdir(f'{class_path}'))
    print(class_obj)

    # create loop for each file in unlabeled_data_path that is jpg
    for imagePath in glob.glob(f'{input_path}*.jpg'):

        

        # If Label keyboard key is pressed assign displayed image to label folder
        # If unsassigned key pressed assign displayed image to nolabel folder
        try:
            key = keyboard.read_key(suppress=False)

            if key in classes.keys():
                class_obj[key]["count"] += 1
                cv2.imwrite(f'{class_obj[key]["path"]}/{class_obj[key]["class"]}{class_obj[key]["count"]}.jpg', image)                
                print(f'Added to {class_obj[key]} label')

            # # press esc to quit script
            elif keyboard.is_pressed('esc'):
                raise SystemExit
                
            else:
                cv2.imwrite(f'{nolabel_path}/{count_nolabel+1}.jpg', image)
                print("No label assigned to key")

        except SystemExit:
            print("Quitting Program")
            print("Quit on image: " + imagePath)
            quit()
        except:
            print("pass")
            pass

        # # assign image to "image" variable
        image = cv2.imread(imagePath)
        
        # display image for labeling
        cv2.imshow("Image", image)
        cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Image', 600,600)
        cv2.waitKey(0)

    # Get number of files for each class
    # count_class1 = len(os.listdir(f'{class1_path}'))
    # count_nolabel = len(os.listdir(f'{nolabel_path}'))

    # # Print data count for each class
    # print(f'{count_class1} in {class1}')
    # print(f'{count_nolabel} in nolabel')

if __name__ == '__main__':
    labeler()