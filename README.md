# Wreck Detect
## Summary
A deep learning image classifier using a convolutional neural network that can detect whether or not an image of a vehicle is damaged or wrecked. A model was created that had a binary prediction accuracy of about 89% and an AUC score of about 95%.

You can check out the results in the [Jupyter Notebook](https://github.com/tpham222/Wreck_Detect/blob/master/WreckDetect_Tensorflow.ipynb).

## Introduction
Deep learning has many applications and uses and can be a very powerful tool used to predict all sorts of things as well as assist with automation. However, this comes at the cost of interpretability of the model. Regardless, I think it is an amazing, complex field that is worth learning and understanding. This project is my attempt at learning all the tools necessary to build out a deep learning model that can classify an image of a car as having damage or not. 

## Steps
* The first thing I needed to do was obtain a bunch of images of cars that are wrecked and cars that have no damage at all. I also needed to write a script to help me efficiently label the images. 

* I also had to figure out how convolutional neural networks worked as well as how they are commonly architecured. 

* Then, I needed to pick a deep learning library for python and learn how to use it. For this project, I went with TensorFlow!

* Finally, I experimented with making my own model as well as transfer learning with fine-tuning.

## Obtaining and Labeling an Image Dataset
After spending more time than I'd like to admit searching around the internet to find a dataset of car images that met my needs, I realized that I would need to build my own dataset. This was a daunting task that would require a lot of manual work in downloading and labeling every single image I wanted to use. But Before worrying about the labeling part, I needed some images. 

My search led me to a chrome plugin called "Fatkun Batch Download Image" which, along with google images, I used to easily download large amounts of images at once. This plugin also allowed me to ignore irrelevant images.

Now that I had about 1,200 images, I was ready to manually open up each image, look at it, and then click and drag it into a folder with it's label. After about 5 of them, I had enough of the process. I decided that my time was better spent learning instead! Therefore, I decided to learn some basics of a popular computer vision library called "OpenCV".

Using what I learned and much more time than it would have taken me to label the images instead, I wrote a script [here](https://github.com/tpham222/Wreck_Detect/blob/master/LabelImages.py) that would help make this process a lot easier!

What this script does is, given a directory containing the images, automatically open the image. From there, you can look at the image and decide whether or not it has damage. Pressing '1' will copy the image into a 'positives' folder and pressing '2' will copy it into a 'negatives' folder. Another image would pop up and the process can be repeated until there are no more images. Moving to the next or previous image is as easy as pressing 'D' or 'A', respectively. Another feature I added into this script is the ability to select a part of the image that you wanted to capture. A blue bounding box would show the area that would be captured.

Now, don't get me wrong, the labeling process was still pretty manual, but I believe the script reduced the number of steps it necessary...and it was pretty fun to learn and build out.

## Learning About Convolutional Neural Networks
The internet is a wonderful resource for learning new things, most of the time for free! My path I took was to use the free version of Coursera's deep learning specialization taught by Andrew Ng, as well as random supplemental articles and videos. The specialization can be found [here](https://www.coursera.org/specializations/deep-learning) and you can audit the courses for free. Auditing the course gives you access to all the videos. I believe they can be found on youtube as well.

After watching a good majority of all the videos, I was able to obtain a basic understanding about how convolutional neural networks worked. This helped me learn some new terms and ideas that I could google if I needed to understand them better while working on my project. 


## TensorFlow
In order to practice using my basic understanding of convolutional neural networks, I also had to learn about a popular deep learning library developed by Google, TensorFlow.
The first thing I did was check out the [beginner tutorials](https://www.tensorflow.org/tutorials) on the tensorflow website. I then watched and coded along with a [youtube tutorial playlist](https://www.youtube.com/watch?v=5Ym-dOS9ssA&list=PLhhyoLH6IjfxVOdVC1P1L5z5azs0XjMsb&ab_channel=AladdinPersson) published by youtuber who makes some great educational content, Aladdin Persson.

After having some hands on experience and learning the basics of TensorFlow, I was finally ready to attempt building my very own image classifier!

## Model Experimentation
My goal for this project was not to build a perfect model that could predict car images with 100% accuracy. I wanted to use this project as a way to learn some basics of deep learning and convolutional neural networks along with how to train them. Given that, let's now talk about the coolest part of this project and some of the results.





