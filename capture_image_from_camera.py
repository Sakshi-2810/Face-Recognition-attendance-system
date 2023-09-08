import cv2
import tkinter as tk

# Function to handle button click

def capture():
    def get_input():
        inp = entry.get()  # Get text from the Entry widget

        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        # reading the input using the camera

        # show result
        while (1):
            result, image = cam.read()
            cv2.imshow(inp, image)
            key=cv2.waitKey(0)
            if(key==ord(' ')):
                cv2.imwrite(inp + ".png", image)
                print("image taken")

            else:
                cam.release()
                cv2.destroyAllWindows()
                break


    # Create the main window
    root = tk.Tk()
    root.title("Capture image")

    # Create and configure a Frame for better layout control
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill=tk.BOTH)

    # Create a Label to provide instructions
    instructions_label = tk.Label(frame, text="Enter your name")
    instructions_label.pack()

    # Create an Entry widget with some styling
    entry = tk.Entry(frame, font=("Arial", 12))
    entry.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.BOTH, expand=True)


    # Create a styled Button
    button = tk.Button(frame, text="Capture face", command=get_input, bg="#007ACC", fg="white", font=("Arial", 12))
    button.pack(pady=10, ipadx=10, ipady=5, fill=tk.BOTH, expand=True)


    # Center the window on the screen
    root.geometry("400x200")


    # Start the Tkinter main loop
    root.mainloop()






# capture()