James Yu

Programming language: Python
Operating System: Windows 10

Project Code:
- Cascade Folder:
	- cascade.xml : Self trained Haar Cascade used for dog facial feature detection
- Image Folder: Images used to test the code
- Positive Folder: images used to train the Haar Cascade
- Negative Folder: images used to train the Haar Cascade
- haarcascade_frontalcatface_extended.xml : Pre-Trained Haar Cascade provided by OpenCV repository
- haarcascade_frontalface_default.xml : Pre-Trained Haar Cascade provided by OpenCV repository
- neg.txt : names of the files in the negative folder used for training Haar cascade
- pos.txt : names of the files in the positive folder used for training Haar cascade
- pos.vec : VEC file used for training Haar cascade
- ObjectDetection.py : python code for the project
- opencv_annotation.exe : Executable provided by OpenCV in 3.4 version to train your own Haar Cascade
- opencv_createsamples.exe : Executable provided by OpenCV in 3.4 version to train your own Haar Cascade
- opencv_traincascade.exe : Executable provided by OpenCV in 3.4 version to train your own Haar Cascade

Modules needed to be installed:
- OpenCV

Instructions:
First if you don't already have OpenCV installed, download it using the following command "pip install opencv-python". 
Then run the "ObjectDetection.py" file in the commandline using "python ObjectDetection.py"
Once the program is running you can move through the outputted images by pressing any key.
