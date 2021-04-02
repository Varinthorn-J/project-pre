import face_recognition
import cv2
 
videoCapture = cv2.VideoCapture(0)
database_image = face_recognition.load_image_file("Image/game.jpg")
data_base_encoding1 = face_recognition.face_encodings(database_image)[0]
database_image = face_recognition.load_image_file("Image/Warinthon2.jpg")
data_base_encoding2 = face_recognition.face_encodings(database_image)[0]
database_image = face_recognition.load_image_file("Image/an.jpg")
data_base_encoding3 = face_recognition.face_encodings(database_image)[0]
database_image = face_recognition.load_image_file("Image/job.jpg")
data_base_encoding4 = face_recognition.face_encodings(database_image)[0]
database_image = face_recognition.load_image_file("Image/oat.jpg")
data_base_encoding5 = face_recognition.face_encodings(database_image)[0]
database_image = face_recognition.load_image_file("Image/oii.jpg")
data_base_encoding6 = face_recognition.face_encodings(database_image)[0]

person_face_encodings = [data_base_encoding1,data_base_encoding2,data_base_encoding3,data_base_encoding4,data_base_encoding5,data_base_encoding6]
person_face_names = ["game","Warinthon","an","job","oat","oii"]

 
data_locations = []
data_encodings = []
data_names = []
frameProcess = True
 
while True:
    ret, frame = videoCapture.read()
    resizing = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_resizing = resizing[:, :, ::-1]
 
    if frameProcess:
        data_locations = face_recognition.face_locations(rgb_resizing)
        data_encodings = face_recognition.face_encodings(rgb_resizing, data_locations)
        data_names = []
        for dc in data_encodings:
            matches = face_recognition.compare_faces(person_face_encodings, dc)
            name = "UNKNOWN"
            if True in matches:
                first_match_index = matches.index(True)
                name = person_face_names[first_match_index]
 
            data_names.append(name)
 
    frameProcess = not frameProcess
    for (top, right, bottom, left), name in zip(data_locations, data_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
videoCapture.release()
cv2.destroyAllWindows()
