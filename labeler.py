# Import libraries
import cv2
import glob
import os


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

    image = cv2.imread(imagePath)
    print("width: %d pixels" % (image.shape[1]))
    print("height: %d pixels" % (image.shape[0]))
    print("channels: %d" % (image.shape[2]))

    cv2.imshow("Image", image)
    cv2.waitKey(0)


    # cv2.imwrite("/{class}/newimage.jpg", image)