import cv2
from datetime import datetime
import os
import numpy as np
# =======================================================================
IMAGES_TO_LABEL_DIR = 'images'
# =======================================================================

#  Creating Folders
if not os.path.exists('images/positives'):
    os.makedirs('images/positives')

if not os.path.exists('images/negatives'):
    os.makedirs('images/negatives')

# Starting position of bounding box
x_start, y_start, x_end, y_end = 0, 0, 0, 0
cropping = False


def mouse_crop(event, x, y):
    global x_start, y_start, x_end, y_end, cropping

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        cropping = False


def change_pic(direction):
    global img_idx, x_start, y_start, x_end, y_end

    cv2.destroyAllWindows()
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    if direction == 'next':
        img_idx += 1
    elif direction == 'previous':
        img_idx -= 1


def get_pics(directory):
    # Returns a list of image files
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(os.getcwd(), directory, f))]


window_name = '1P, 2N'
img_idx = 0
while True:
    # Looping through all images
    images = get_pics(IMAGES_TO_LABEL_DIR)

    # If no images, break loop
    if len(images) == 0:
        print('No pictures in Images folder')
        break

    # Reading image
    img_name = images[img_idx]
    img_path = os.path.join(IMAGES_TO_LABEL_DIR, img_name)
    img = cv2.imread(img_path)

    # Showing Rectangle Bounding Box Selection
    cv2.setMouseCallback(window_name, mouse_crop)
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)

    # Showing Images
    cv2.imshow(window_name, img)
    k = cv2.waitKey(1)

    if k == ord('q'):
        break

    elif k == ord('d'):
        if img_idx < len(images)-1:
            change_pic('next')
        else:
            print('No Next image')
    elif k == ord('a'):
        if img_idx > 0:
            change_pic('previous')
        else:
            print('No Previous image')

    # Saves cropped images in positive and moves original to categorized
    # 1 for pos, 2 for neg
    elif k in [ord('1'), ord('2')]:
        x = [x_start, x_end]
        y = [y_start, y_end]

        x_start = min(x)
        x_end = max(x)
        y_start = min(y)
        y_end = max(y)

        imgCrop = img[y_start + 2:y_end - 1, x_start + 2:x_end - 1]
        try:
            if k == ord('1'):
                label = 'positive'
            elif k == ord('2'):
                label = 'negative'
            else:
                continue

            timestamp = str(int(datetime.timestamp(datetime.now())))
            cv2.imwrite(os.path.join('images', label, timestamp + img_name), imgCrop)
            print(f'image copied to {label}s folder...')

        except Exception as err:
            print('ERROR in writing image: ' + str(err))

        if img_idx < len(images)-1:
            change_pic('next')
            os.remove(img_path)
        else:
            print('No Next image')
            break

