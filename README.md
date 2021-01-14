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
After spending more time than I'd like to admit searching around the internet to find a dataset of car images that met my needs, I realized that I would need to build my own dataset. This was a daunting task that would require a lot of manual work in downloading and labeling every single image I wanted to use. Before worrying about the labeling part, I would need some images. 

My search led me to a chrome plugin called "Fatkun Batch Download Image"
