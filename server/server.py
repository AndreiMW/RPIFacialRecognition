import os
import face_recognition
from flask import Flask, request
from flask_uploads import UploadSet, configure_uploads, IMAGES

#initialise flask
app = Flask(__name__)
photos = UploadSet("photos", IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'img'
configure_uploads(app, photos)

#image encoding with the face you want the recognition to compare with
known_image = face_recognition.load_image_file("image_location")
known_image_encoding = face_recognition.face_encodings(known_image)[0]

#the route of the request
@app.route("/recognize", methods=["GET", "POST"])
def recognize():
    if request.method == 'POST':
        #this methos is expecting an image with the key "imagine",if you change it,be sure to also change it in the request
        parameter = request.files['imagine']
        #image saved on hard drive
        filename = photos.save(parameter)
        #encoding of the request image
        request_image = face_recognition.load_image_file("img/%s" % filename)
        unknown_encoding = face_recognition.face_encodings(request_image)[0]
        #comparing the result
        result = face_recognition.compare_faces([known_image_encoding], unknown_encoding)
        if result[0] == True:
            response = "Face recognized"
        else:
            response = "Face not recognized"
         os.remove("img/%s" % filename)
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug="true")
