# Code for object and face detection with a webcam and a Raspeberry pi

The repository contains Python code for face detection, object recognition and other machine learning application using a webcam.
A part of the demos are made to run on a Raspberry Pi (3 or 4).

It uses several open-source libraries where neural networks have already been pre-trained for the task at hand.

* Simple face detection and recognition uses opencv library.
* Face detection with gender, age and emotion recognition is DeepFace code : [https://github.com/serengil/deepface](https://github.com/serengil/deepface)

The code is under the MIT license.

## What is inside the repository

There are Jupyter notebooks and Python scripts. The notebooks are meant to guide the user, explain the different steps, and explore the possibilities of image analysis. The Python scripts contain the code to be run directly in the command line, so that it works out of the box on the Raspberry Pi (or other platforms).

## Tutorial on face detection with webcam

Here is a list of relevant webpages for
Relevant websites:
https://iotdesignpro.com/projects/face-recognition-door-lock-system-using-raspberry-pi
https://github.com/mowshon/age-and-gender
https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/object_detection_camera.html
https://learnopencv.com/training-a-custom-object-detector-with-dlib-making-gesture-controlled-applications/
http://dlib.net/ml.html

Haar cascades, face and eyes
https://towardsdatascience.com/computer-vision-detecting-objects-using-haar-cascade-classifier-4585472829a9

Raspberry pi and others:
https://qengineering.eu/deep-learning-with-raspberry-pi-and-alternatives.html

## Experiments on the Raspberry Pi

### Enable Raspberry Pi camera
You need to run the following code so that opencv can get the image with `VideoCapture`:

`sudo modprobe bcm2835-v4l2`

See:
https://stackoverflow.com/questions/29583533/videocapture-open0-wont-recognize-pi-cam/37530016#37530016

Make also sure the interface for (legacy) video is enabled in the raspberry Pi configuration `sudo raspi-config` -> 'Interfacing Options' -> 'Camera'

### Scripts

`test_video.py` is the first and simplest script you can run to test if Python with opencv can access your camera and display it.