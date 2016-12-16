# EC601_door
This is the repository for the course EC601 offered at Boston University, College of Engineering during fall 2016. Group Hodor- automatic door opener for the wheelchair bound.
Download the Hodor_app apk file and install in your android mobile.
In the Raspberry Pi 3 (requires bluetooth in other versions) terminal, run this command " sudo rfcomm watch hci0".
Open the application and click refresh. The list of all bluetooth devices will be shown. Connect to the Raspberry Pi 3 bluetooth device.
Run the "hodor.py" python  file from another terminal on the Raspberry Pi using command, 
    python3 hodor.py
In the application, hit the push button. The command window on pi will show message received and the program will work to open the door.

Dependencies
Python 3.x/2.7
uArm : https://github.com/uArm-Developer/pyuarm Install using 'pip install pyuarm'
OpenCV : 2.4 or higher

The folder "Bracket-3D-print" has the sketchup and .stl files for printing the camera bracket attached to the arm.

Image processing:

a)Initialise the rpi camera module using the below

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate =32
rawCapture = picamera.array.PiRGBArray(camera, size=(640,480))

b) Perform a canny on each frame with these thresholds. This will detect the edges.
100,200

c) Blur the image applying the opencv blur function
d) Feed the input to the cv2.HoughCircles to detect the circles in the image.
e) For each hit find the coordinates and the count with regards to the min & max radius
f) Draw a rounding circle against the Center of the coordinates.
