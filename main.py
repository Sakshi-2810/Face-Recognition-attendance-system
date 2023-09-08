import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import capture_image_from_camera  # Import your face capture module
import face_recognition_code  # Import your mark attendance module

# Function to capture and store faces
def capture_faces():
    # Call the function from your face capture module
    capture_image_from_camera.capture()
    # messagebox.showinfo("Face Capture", "Faces captured and stored successfully!")

# Function to mark attendance
def mark_attendance():
    # Call the function from your mark attendance module
    face_recognition_code.run()
    # messagebox.showinfo("Mark Attendance", "Attendance marked successfully!")

# Create the main tkinter window
root = tk.Tk()
root.title("Attendance System")
# root.geometry("800x600")


image1 = Image.open("register.png")
image1 = image1.resize((100, 100), Image.BILINEAR)
image1 = ImageTk.PhotoImage(image1)

image2 = Image.open("attendance.png")
image2 = image2.resize((100, 100), Image.BILINEAR)
image2 = ImageTk.PhotoImage(image2)

label1 = ttk.Label(root, image=image1)
label1.grid(row=0, column=0, padx=10, pady=10)
label2 = ttk.Label(root, image=image2)
label2.grid(row=0, column=1, padx=10, pady=10)

# Create a button to capture and store faces
capture_button = ttk.Button(root, text="Capture Faces", command=capture_faces,style='TButton')
capture_button.grid(row=1, column=0, padx=10, pady=10)
# capture_button.pack(fill=tk.BOTH, expand=True)

# Create a button to mark attendance
attendance_button = ttk.Button(root, text="Mark Attendance", command=mark_attendance,style='TButton')
attendance_button.grid(row=1, column=1, padx=10, pady=10)
# attendance_button.pack(fill=tk.BOTH, expand=True)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12))
# Start the tkinter main loop
root.mainloop()