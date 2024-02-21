"""
Author: Jacob Pitsenberger
Date: 2-18-2024
Module: app.py

This Python application is designed to interface with a DJI Tello drone, providing a Graphical User Interface (GUI)
with flight status indicators, such as battery level, for real-time video feed and control through an
Xbox One controller. It leverages several libraries including OpenCV for image processing, djitellopy for
drone control, Tkinter for GUI, and PIL for image manipulation.

"""

import cv2
from djitellopy import tello
from tkinter import *
from PIL import Image, ImageTk
from indicators import Indicators
from xbox_one_controller import XboxController
import time
import threading


class App:
    def __init__(self):

        # Initialize the root window and set its state to fill the screen (JP)
        self.root = Tk()
        self.root.title("Tello Drone HUD-HGS")  # Add a title to the window
        self.root.minsize(800, 600)  # Set the minimum gui size

        # Initialize the video stream capture label
        self.cap_lbl = Label(self.root)

        # Connect to the drone and start receiving video
        self.drone = tello.Tello()
        self.drone.connect()
        self.drone.streamon()

        # Drones fly state for takeoff/land button functionality
        self.flying = False

        ### **** NEW **** ###
        # Define the height and width to resize the current frame to
        self.h = 480
        self.w = 720
        ### ************* ###

        # Initialize the state of the image for the video stream
        self.image = None

        # Initialize a variable to get the video frames from the drone
        self.frame = self.drone.get_frame_read()

        # this is to store the joystick rc values as they are updated in realtime.
        self.rc_controls = [0, 0, 0, 0]  # the initial movement velocity values for lr, fb, ud, and yaw motions

        # Initialize the xbox controller object
        self.xbox_controller = XboxController()

        ### **** NEW **** ###
        # Initialize the indicators object
        self.indicators = Indicators(self.drone, self.w, self.h)
        ### ************* ###

    def takeoff_land(self):
        """Set the command for the takeoff/land button depending on the drones flying state"""
        if self.drone.is_flying:
            threading.Thread(target=lambda: self.drone.land()).start()
        else:
            threading.Thread(target=lambda: self.drone.takeoff()).start()

    def update_joystick(self):
        """Method to update joystick values."""
        try:
            # Read current joystick values using the XboxController class
            joystick_values = self.xbox_controller.read()

            # Extract individual joystick values for easier reference
            left_joystick_x = joystick_values[0]
            left_joystick_y = joystick_values[1]
            right_joystick_x = joystick_values[2]
            right_joystick_y = joystick_values[3]
            start_button = joystick_values[14]

            # Check if the start button is pressed
            if start_button:
                self.takeoff_land()  # Call the takeoff/land method if the start button is pressed
                time.sleep(
                    0.15)  # sleep long enough to register button as not pressed so no false send of land command.

            # Map joystick values to specific RC control channels
            self.rc_controls[0] = right_joystick_x  # lr RC value
            self.rc_controls[1] = right_joystick_y  # fb RC value
            self.rc_controls[2] = left_joystick_y  # ud RC value
            self.rc_controls[3] = left_joystick_x  # yaw RC value

            # If rc control values aren't zero then send them to the drone using the send_rc_control(lr, fb, ud, yv) command.
            if self.rc_controls != [0, 0, 0, 0]:
                self.drone.send_rc_control(self.rc_controls[0], self.rc_controls[1], self.rc_controls[2],
                                           self.rc_controls[3])

            # and if not zero then send the equivalent command for the drone to hover in place
            else:
                self.drone.send_rc_control(0, 0, 0, 0)
            # Call the update_joystick method again after a delay (50 milliseconds)
            self.root.after(50, self.update_joystick)

        # Handle exceptions that may occur during joystick update
        except Exception as joystickUpdateException:
            print(
                f"Exception occurred when updating joystick values.\nJoystickUpdateException: {joystickUpdateException}")

    def run_app(self):
        try:

            # Pack the video stream label to the GUI window
            self.cap_lbl.pack(anchor="center")

            # Call the video_stream method to start displaying video
            self.video_stream()

            # Call the update_joystick method to start the joystick control
            self.update_joystick()

            self.root.mainloop()

        except Exception as e:
            print(f"Error running the application: {e}")
        finally:
            # When the root window is exited out of ensure to clean up any resources.
            self.cleanup()

    def video_stream(self):
        """Method to display video stream."""
        try:
            # Read a frame from our drone
            frame = self.frame.frame

            frame = cv2.resize(frame, (self.w, self.h))

            ### **** NEW **** ###
            # Draw the battery indicator on the frame
            self.indicators.draw_battery_indicator(frame)
            ### ************* ###

            # Convert the current frame to the rgb colorspace
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            # Convert this to a Pillow Image object
            img = Image.fromarray(cv2image)

            # Convert this then to a Tkinter compatible PhotoImage object
            imgtk = ImageTk.PhotoImage(image=img)

            # Place the image label at the center of the window
            self.cap_lbl.pack(anchor="center", pady=15)

            # Set it to the photo image
            self.cap_lbl.imgtk = imgtk

            # Configure the photo image as the displayed image
            self.cap_lbl.configure(image=imgtk)

            # Update the video stream label with the current frame
            # by recursively calling the method itself with a delay.
            self.cap_lbl.after(5, self.video_stream)
        except Exception as videoStreamException:
            print(f"Exception occurred when updating the video stream.\nvideoStreamException: {videoStreamException}")

    # Method for cleaning up resources
    def cleanup(self) -> None:
        try:
            # Release any resources
            print("Cleaning up resources...")
            ### **** NEW **** ###
            self.indicators.update = False
            ### ************* ###
            self.drone.end()
            self.root.quit()  # Quit the Tkinter main loop
            exit()
        except Exception as e:
            print(f"Error performing cleanup: {e}")


if __name__ == "__main__":
    # Initialize the App
    gui = App()

    # Call the run_app method to run tkinter mainloop
    gui.run_app()
