import cv2
import os

# Initialize cascade variables for cots, dogs and humans
frontFaceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
catFaceCascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
dogFaceCascade = cv2.CascadeClassifier('cascade/cascade.xml')

# Store the images from inside the ./image folder into a list
testImages = os.listdir('./Images')

# Iterate through every element of the images list 
for ( x ) in testImages:
    # Read the image and set it to a variable called tempImage
    tempImage = cv2.imread('Images/'+x)
    # Converting tempImage to grayscale
    grayImage = cv2.cvtColor(tempImage, cv2.COLOR_BGR2GRAY)
    
    # Slide a window across every coordinate on the image to check if it has front face features
    # If a feature is detected during this process then store the coordinates of the location inside a list
    # catFace is the list for the coordinates of cat facial features
    catFace = catFaceCascade.detectMultiScale(
                grayImage, 
                scaleFactor=1.1, 
                minNeighbors=4,
                )
    
    # For all the coordinates found in the catFace list, draw a rectangle to highlight the location of the cats found within the image
    # Also include the text 'cat' within the boundaries of the drawn rectangle indicating that a cat was detected in the image
    for (x,y,w,h) in catFace:
            cv2.rectangle(tempImage, (x,y), (x+w, y+h), (138,43,226), 1)
            cv2.putText(tempImage, 'Cat', (x,y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (138,43,226), 2)

    # If the detectMultiScale function does not detect features then it will return an empty list
    # So if no cats were detected in tempImage then check for human features
    if(len(catFace) == 0):
        # front is the list for the coordinates of human facial features
        frontFace = frontFaceCascade.detectMultiScale(
            grayImage, 
            scaleFactor=1.1, 
            minNeighbors=6,
            minSize=(64,64),
            flags=cv2.CASCADE_SCALE_IMAGE
            )
        # For all the coordinates found in the frontFace list, draw a rectangle to highlight the location of the humans found within the image
        # Also include the text 'human' within the boundaries of the drawn rectangle indicating that a human was detected in the image
        for (x,y,w,h) in frontFace:
            cv2.rectangle(tempImage, (x,y), (x+w, y+h), (36,255,12), 1)
            cv2.putText(tempImage, 'Human', (x,y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 2)
        # If both the catFace list and the frontFace list are empty then check if the object(s) in the image are dogs
        if(len(frontFace) == 0):
            # dogface is the list for the coordinates of dog facial features
            dogFace = dogFaceCascade.detectMultiScale(
                grayImage, 
                scaleFactor=1.1, 
                minNeighbors=10,
                minSize=(69,69),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            # For all the coordinates found in the dogFace list, draw a rectangle to highlight the location of the dogs found within the image
            # Also include the text 'dog' within the boundaries of the drawn rectangle indicating that a dog was detected in the image
            for (x,y,w,h) in dogFace:
                cv2.rectangle(tempImage, (x,y), (x+w, y+h), (255,140,0), 1)
                cv2.putText(tempImage, 'Dog', (x,y+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,140,0), 2)

    # displays the results in a window called tempImage
    # pink rectangles indicate that the object in the image is a cat
    # green rectangles indicate that the object in the image is a human
    # blue rectangles indicate that the object in the image is a dog
    cv2.imshow('tempImage', tempImage)
    # waits until a key is pressed to go to the next image
    cv2.waitKey()