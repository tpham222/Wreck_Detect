# Wreck Detect
## Summary
A deep learning image classifier using a convolutional neural network that can detect whether or not an image of a vehicle is damaged or wrecked. A model was created that had a binary prediction accuracy of about 89% and an AUC score of about 95%.

You can check out the results in the [Jupyter Notebook](https://github.com/tpham222/Wreck_Detect/blob/master/WreckDetect_Tensorflow.ipynb).

## Introduction
Deep learning has many applications and uses and can be a very powerful tool used to predict all sorts of things as well as assist with automation. However, this comes at the cost of interpretability of the model. Regardless, I think it is an amazing, complex field that is worth learning and understanding. This project is my attempt at learning all the tools necessary to build out a deep learning model that can classify an image of a car as having damage or not. 

## Steps
* The first thing I needed to do was obtain a bunch of images of cars that are wrecked and cars that have no damage at all. I also needed to write a program to help me efficiently label the images. 

* I also had to figure out how convolutional neural networks worked as well as how they are commonly architecured. 

* Then, I needed to pick a deep learning library for python and learn how to use it. For this project, I went with TensorFlow!

* Finally, I experimented with making my own model as well as transfer learning with fine-tuning.

## Obtaining and Labeling an Image Dataset
After spending more time than I'd like to admit searching around the internet to find a dataset of car images that met my needs, I realized that I would need to build my own dataset. This was a daunting task that would require a lot of manual work in downloading and labeling every single image I wanted to use. But Before worrying about the labeling part, I needed some images. 

My search led me to a chrome plugin called "Fatkun Batch Download Image" which, along with google images, I used to easily download large amounts of images at once. This plugin also allowed me to ignore irrelevant images.

Now that I had about 1,200 images, I was ready to manually open up each image, look at it, and then click and drag it into a folder with it's label. After about 5 of them, I had enough of the process. I decided that my time was better spent learning instead! Therefore, I decided to learn some basics of a popular computer vision library called "OpenCV".

Using what I learned and much more time than it would have taken me to label the images instead, I wrote a script [here](https://github.com/tpham222/Wreck_Detect/blob/master/LabelImages.py) that would help make this process a lot easier!
