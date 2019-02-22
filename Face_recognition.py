import face_recognition
from PIL import Image

image = face_recognition.load_image_file("stock_people.jpg") #Name of image file

face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

i=0

for face_location in face_locations:
    top,right,bottom,left = face_location
    print("A Face Located at pixel Location Top: {},Left: {},Bottom: {},Right: {}".format(top,left,bottom,right))


    face_image = image[top:bottom,left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save("face-{}.jpg".format(i))
    i=i+1
