import cv2
import numpy as np
import os
from datetime import date

import tkinter as tk
import xlrd
from xlutils.copy import copy as xl_copy
import face_recognition

def run():
    def attendence():
        CurrentFolder = os.getcwd()  # Read current folder path
        image = CurrentFolder + '\\sakshi.png'
        # image2 = CurrentFolder + '\\romil.png'
        # image3 = CurrentFolder + '\\sandali.png'
        # image4 = CurrentFolder + '\\vivek.png'


        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)

        # Load a sample picture and learn how to recognize it.
        person1_name = "sakshi"
        person1_image = face_recognition.load_image_file(image)
        person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

        # Load a second sample picture and learn how to recognize it.
        # person2_name = "romil"
        # person2_image = face_recognition.load_image_file(image2)
        # person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

        # person3_name = "sandali"
        # person3_image = face_recognition.load_image_file(image3)
        # person3_face_encoding = face_recognition.face_encodings(person3_image)[0]

        # person4_name = "vivek"
        # person4_image = face_recognition.load_image_file(image4)
        # person4_face_encoding = face_recognition.face_encodings(person4_image)[0]

        # Create arrays of known face encodings and their names
        known_face_encodings = [
            person1_face_encoding,
            # person2_face_encoding,
            # person3_face_encoding,
            # person4_face_encoding

        ]
        known_face_names = [
            person1_name,
            # person2_name,
            # person3_name,
            # person4_name
        ]

        # Initialize some variables
        face_locations = []
        face_names = []
        process_this_frame = True

        rb = xlrd.open_workbook('attendence_excel.xls', formatting_info=True)
        wb = xl_copy(rb)
        inp = entry.get()
        sheet1 = wb.add_sheet(inp)
        sheet1.write(0, 0, 'Name/Date')
        sheet1.write(0, 1, str(date.today()))
        row = 1
        col = 0
        already_attendence_taken = ""
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    name = "Unknown"

                    #  use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
                    if (already_attendence_taken != name) and (name != "Unknown"):
                        sheet1.write(row, col, name)
                        col = col + 1
                        sheet1.write(row, col, "Present")
                        row = row + 1
                        col = 0
                        print("attendence taken")
                        wb.save('attendence_excel.xls')
                        already_attendence_taken = name


            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xff == ord('q'):
                # print("data save")
                break

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()

        # Create the main window

    root = tk.Tk()
    root.title("Mark Attendence")

    # Create and configure a Frame for better layout control
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)

    # Create a Label to provide instructions
    instructions_label = tk.Label(frame, text="Enter Lecture Name")
    instructions_label.pack()

    # Create an Entry widget with some styling
    entry = tk.Entry(frame, font=("Arial", 12))
    entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH, expand=True)

    # Create a styled Button
    button = tk.Button(frame, text="Mark Attendence", command=attendence, bg="#007ACC", fg="white", font=("Arial", 12))
    button.pack(pady=10, ipadx=10, ipady=5, fill=tk.BOTH, expand=True)

    # Center the window on the screen
    root.geometry("400x200")

    # Start the Tkinter main loop
    root.mainloop()

# run()
