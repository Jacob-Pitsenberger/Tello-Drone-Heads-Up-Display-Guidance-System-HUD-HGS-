"""
Author: Jacob Pitsenberger
Date: 2-18-2024
Module: indicators.py

This module contains the Indicators class, designed to interface with a Tello drone object to monitor and display
various flight indicators such as battery level. It utilizes OpenCV for drawing indicators on a video feed,
threading for background updates, and time for update intervals.

Features:
- Continuously updates flight indicators in a separate thread.
- Draws a battery level indicator on the video feed based on the drone's current battery status.

Dependencies:
- cv2: For drawing indicators on the video feed.
- time: For controlling the update intervals of flight indicators.
- threading: For running indicator updates in a background thread.
"""

import cv2
import time
import threading

class Indicators:
    def __init__(self, drone, w, h):

        # Initialize a variable to start/stop our indicator updates
        self.update = False

        # Initialize the width, height, and drone for updates to work properly
        self.w = w
        self.h = h
        self.drone = drone

        # Initialize the batter level as the drones current battery level
        self.battery = self.drone.get_battery()

        # Start a thread to update the indicator values while self.update is True
        threading.Thread(target=lambda: self.update_indicators()).start()

    def update_indicators(self) -> None:
        """Set update to True and continuously update the indicator values by calling the drones
        associated methods for getting that indicators respective current value reading."""
        self.update = True
        while self.update:
            print("self.drone is true, updating indicators")
            self.battery = self.drone.get_battery()
            print(f"self.battery = {self.battery}")
            time.sleep(1)

    def draw_battery_indicator(self, frame) -> None:
        """Draw the base battery shape and then check the battery level and draw the appropriate number of colored
        bars in the battery shape for that battery level percentages respective representation.

        Notes:
            - The start and end positions for drawing the battery are hardcoded as a calculation taken with the frame's
              width/height to position the drawn indicator in the upper left corner of the displayed video stream.

            - The batteries form is drawn in the color white (255, 255, 255) and has a thickness of -1 to have the
              rectangles filled with this color.

            - The battery level bars are drawn as lines within the battery form. These bars are positioned within this
              form such that they are separated by 5 pixels between each bar in the form along its x-axis. These bars

            - All bars are drawn with a thickness value of 2
        """

        # Draw the two rectangle that form the batteries body and positive terminal (for the look we want; only aesthetic)
        cv2.rectangle(frame, (self.w // 128 + 3, self.h // 32 + 29), (self.w // 128 + 52, self.h // 32 + 51),
                      (255, 255, 255), -1)
        cv2.rectangle(frame, (self.w // 128 + 52, self.h // 32 + 35), (self.w // 128 + 55, self.h // 32 + 45),
                      (255, 255, 255),
                      -1)

        # Check if the battery level is above 70%
        if self.battery >= 70:

            # If above 70%, color the bars green.
            color = (0, 255, 0)

            # Check if the battery is equal to 100%
            if self.battery == 100:

                # 10 lines for 10 percent intervals between no charge 0% and full charge 100%
                # So, each line represents a 10% fraction of the total possible battery percentage and the battery is full.
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 25, self.h // 32 + 30), (self.w // 128 + 25, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 30, self.h // 32 + 30), (self.w // 128 + 30, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 35, self.h // 32 + 30), (self.w // 128 + 35, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 40, self.h // 32 + 30), (self.w // 128 + 40, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 45, self.h // 32 + 30), (self.w // 128 + 45, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 50, self.h // 32 + 30), (self.w // 128 + 50, self.h // 32 + 50), color,
                         2)

            # If the battery is between 90% and 100% draw 9 green lines to represent this.
            elif 90 <= self.battery < 100:
                # 9 lines
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 25, self.h // 32 + 30), (self.w // 128 + 25, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 30, self.h // 32 + 30), (self.w // 128 + 30, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 35, self.h // 32 + 30), (self.w // 128 + 35, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 40, self.h // 32 + 30), (self.w // 128 + 40, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 45, self.h // 32 + 30), (self.w // 128 + 45, self.h // 32 + 50), color,
                         2)
            # If between 80% and 90% draw 8 Green lines to represent this.
            elif 80 <= self.battery < 90:
                # 8 lines
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 25, self.h // 32 + 30), (self.w // 128 + 25, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 30, self.h // 32 + 30), (self.w // 128 + 30, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 35, self.h // 32 + 30), (self.w // 128 + 35, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 40, self.h // 32 + 30), (self.w // 128 + 40, self.h // 32 + 50), color,
                         2)
            # If between 70% and 80% draw 7 Green lines to represent this.
            else:
                # 7 lines
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 25, self.h // 32 + 30), (self.w // 128 + 25, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 30, self.h // 32 + 30), (self.w // 128 + 30, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 35, self.h // 32 + 30), (self.w // 128 + 35, self.h // 32 + 50), color,
                         2)

        # Check if the battery level is between 40% and 70% capacity.
        elif 40 <= self.battery < 70:

            # If it is, then set the bar color to yellow.
            color = (0, 255, 255)

            # If greater than 60% but less than 70% draw 6 yellow lines.
            if self.battery >= 60:
                # 6 lines
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 25, self.h // 32 + 30), (self.w // 128 + 25, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 30, self.h // 32 + 30), (self.w // 128 + 30, self.h // 32 + 50), color,
                         2)

            # if between 50% and 60% draw 5 yellow lines.
            elif 50 <= self.battery < 60:
                # 5 lines
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 25, self.h // 32 + 30), (self.w // 128 + 25, self.h // 32 + 50), color,
                         2)

            # if between 40% and 50% draw 4 yellow lines.
            else:
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 20, self.h // 32 + 30), (self.w // 128 + 20, self.h // 32 + 50), color,
                         2)

        # Check if the battery is less than 40% capacity.
        else:

            # If so, set the color to red.
            color = (0, 0, 255)

            # If the battery is between 30% and 40% draw 3 red lines.
            if self.battery >= 30:
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 15, self.h // 32 + 30), (self.w // 128 + 15, self.h // 32 + 50), color,
                         2)

            # If the battery is between 20% and 30% draw 2 red lines.
            elif 20 <= self.battery < 30:
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)
                cv2.line(frame, (self.w // 128 + 10, self.h // 32 + 30), (self.w // 128 + 10, self.h // 32 + 50), color,
                         2)

            # If the battery is between 10% and 20% draw 3 red lines.
            else:
                cv2.line(frame, (self.w // 128 + 5, self.h // 32 + 30), (self.w // 128 + 5, self.h // 32 + 50), color,
                         2)

        # Write the current batter level as a percentage text next to the indicator.
        cv2.putText(frame, f"{self.battery} %", (self.w // 128 + 60, self.h // 32 + 45), cv2.FONT_HERSHEY_COMPLEX, .5,
                    (43, 157, 255),
                    1)
