import picamera
camera = picamera.PiCamera()
camera.resolution = (1920, 1080)
camera.hflip = True
#camera.rotation = 180
camera.vflip = True
camera.capture('image.jpg')