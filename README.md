# Face Recognition

This is a quick trial of OpenCV and Dlib libraries to perform face recognition. It also used a trained model for the shape predictor from Dlib (you can train your own if you fancy it, see here for instance: https://www.pyimagesearch.com/2019/12/16/training-a-custom-dlib-shape-predictor/). 

The goal is tto recognise faces and draw a mask with dots in 68 precise points of the face (eyes, mouth, nose...).

Two options can be tried:
- Static face recognition  (StaticFaceRecognition.py):  performs face recognition on an image (jpg format);
- Live face recognition (LiveFaceRecognition.py): performs face recognition on a live recording using the computer's camera. 

How to use:

- Clone this repository
- Install pip3 (using Brew for instance, see instructions here: https://docs.brew.sh/Homebrew-and-Python)
- Create a virtual enviroment (using venv for instance, see instructions here: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- Install dependencies: pip install requirements.txt
- To launch the Static face recognition: python3 StaticFaceRecognition.py
This will use the image already available in the repository. You can upload into the repository your own image (jpg format) and replace all mentions of "zidane" to the name of your image. Press any key to exit. 
- To launch the Live face recognition: python3 LiveFaceRecognition.py
The program will launch your cam and perform live face recognition. Press escape key to exit. 

