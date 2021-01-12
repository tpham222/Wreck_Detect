import cv2
from datetime import datetime
import os
import numpy as np
# from tensorflow import keras
# from tensorflow.keras.preprocessing import image

# Creating Folders
# if not os.path.exists('images/positives'):
#     os.makedirs('images/positives')
#
# if not os.path.exists('images/negatives'):
#     os.makedirs('images/negatives')


x_start, y_start, x_end, y_end = 0, 0, 0, 0
cropping = False


def mouse_crop(event, x, y, flags, param):
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
    global img_num, x_start, y_start, x_end, y_end

    cv2.destroyAllWindows()
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    if direction == 'next':
        img_num += 1
    elif direction == 'previous':
        img_num -= 1


def get_pics(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(os.getcwd(), directory, f))]


# def load_model(path):
#     model = keras.models.load_model(path)
#     model.compile(optimizer=keras.optimizers.Adam(1e-5)
#                          , loss=keras.losses.BinaryCrossentropy(from_logits=True)
#                          , metrics=[keras.metrics.BinaryAccuracy()])
#     return model


def process_test_image(path):
    img = image.load_img(path, target_size=(150,150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    return img_array


# def predict_image(model, img):
#     img = process_test_image(img)
#     prediction = model.predict(img)
#
#     if prediction[0][0] < 0.50:
#         print('Not Wreck')
#         print(round((1 - prediction[0][0]) * 100, 2))
#     else:
#         print('Wreck')
#         print(round(prediction[0][0] * 100, 2))


# # Load model to predict image class
# model = load_model('model_h5.h5')

window_name = '1P, 2N, 3tP, 4tN'
img_num = 0
#predict_num = 1

while True:
    # Looping through all images
    img_dir = 'images'
    images = get_pics(img_dir)

    if len(images) == 0:
        print('No pictures in Images folder')
        break
    img_name = images[img_num]

    #Current Positives
    pos_img_dir = 'images/positives'
    current_pos = get_pics(pos_img_dir)

    #Current Negatives
    neg_img_dir = 'images/negatives'
    current_neg = get_pics(neg_img_dir)

    #reading image
    img = cv2.imread(os.path.join(img_dir, img_name))

    #Showing Rectangle Selection
    cv2.setMouseCallback(window_name, mouse_crop)
    cv2.rectangle(img, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)

    #Showing Images
    cv2.imshow(window_name, img)
    k = cv2.waitKey(1)

    # # Use loaded model to predict image class
    # if predict_num != img_num:
    #     predict_image(model, os.path.join(img_dir, img_name))
    #     predict_num = img_num


    if k == ord('q'):
        break

    elif k == ord('d'):
        if img_num < len(images)-1:
            change_pic('next')
        else:
            print('No Next picture')
    elif k == ord('a'):
        if img_num > 0:
            change_pic('previous')
        else:
            print('No Previous picture')

    # saves cropped images in positive and moves original to categorized
    #1 for pos, 2 for neg, 3 for none

    elif k in [ord('1'), ord('2'), ord('3'), ord('4')]:
        x = [x_start, x_end]
        y = [y_start, y_end]

        x_start = min(x)
        x_end = max(x)
        y_start = min(y)
        y_end = max(y)

        imgCrop = img[y_start + 2:y_end - 1, x_start + 2:x_end - 1]
        try:
            timestamp = str(int(datetime.timestamp(datetime.now())))
            if k == ord('1'):
                cv2.imwrite(os.path.join('images', 'positives', timestamp + img_name), imgCrop)
            elif k == ord('2'):
                cv2.imwrite(os.path.join('images', 'negatives', timestamp + img_name), imgCrop)
            # elif k == ord('3'):
            #     cv2.imwrite(os.path.join(img_dir, 'test_1', timestamp + img_name), imgCrop)
            # elif k == ord('4'):
            #     cv2.imwrite(os.path.join(img_dir, 'test_0', timestamp + img_name), imgCrop)

        except Exception as err:
            print('ERROR in writing image: ' + str(err))

        if img_num < len(images)-1:
            change_pic('next')
            #os.rename('images/' + img_name, 'labeled/' + img_name)
        else:
            print('No Next picture')
            break

