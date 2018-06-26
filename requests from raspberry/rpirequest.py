import requests
import picamera

#set image name
imageName = "image.jpg"

#initialize pi camera
camera = picamera.PiCamera()

#set pi camera resolution
camera.resolution = (400,400)

#take a picture
camera.capture(imageName)

#put the image in the request body,with the key "imagine"
files = {'imagine': open(imageName, 'rb')}

#send the request containing the image
req = requests.post('your_request_url', files=files)

#print the response
print (str(req.text))

#delete the image taken previously by the camera.
os.remove(imageName)