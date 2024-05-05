import cv2

cam_port = 0
cam = cv2.VideoCapture(cam_port)

# Reading the input using the camera
inp = input('Enter person name: ')

# If image will detected without any error, show result
while True: 
    ret, image = cam.read()
    if ret:
        cv2.imshow(inp, image)
        key = cv2.waitKey(1)
        # Save the image if any key is pressed
        if key != -1:
            cv2.imwrite(inp + ".png", image)
            print("Image captured successfully.")
            break
    else:
        print("No image detected. Please try again.")
        break

cam.release()
cv2.destroyAllWindows()
