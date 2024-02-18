# Tello Drone Heads Up Display-Guidance System (HUD-HGS)

## Overview

The Tello Drone Heads Up Display-Guidance System (HUD-HGS) is an innovative software solution designed to enhance the 
flying experience of the DJI Tello drone through a sophisticated graphical user interface (GUI). This system integrates 
real-time flight data visualization, including video streaming and battery status, with responsive drone control using 
an Xbox One controller. Developed with the aim of providing an immersive and intuitive flying experience, HUD-HGS 
leverages cutting-edge technologies across video processing, drone communication, and user interface design.

At the core of this system is the ability to seamlessly blend the drone's operational data into a visually intuitive 
interface, allowing pilots to make informed decisions quickly. The HUD-HGS is not just about enhancing the visual 
experience; it also introduces an efficient control mechanism through the Xbox One controller, making drone flight 
more accessible and enjoyable. Whether it's for recreational flying, educational purposes, or research and 
development, the HUD-HGS brings a new level of interaction and control to Tello drone operators.


## Key Highlights:
- Real-Time Video Streaming: Experience the flight through the drone's eyes with live video feedback, 
  directly integrated into the GUI.
- Flight Status Indicators: Stay informed with on-screen indicators such as battery level, ensuring you're always 
  aware of your drone's status.
- Xbox One Controller Integration: Take control of your Tello drone with the precision and familiarity of an Xbox One 
  controller, offering a more natural and responsive flying experience.
- Customizable GUI: The system's GUI is designed for ease of use, providing quick access to essential flight controls 
  and data, all within a user-friendly interface.
- Enhanced Safety and Responsiveness: With real-time data and responsive controls, pilots can fly their drones more 
  safely and effectively, making the most out of every flight session.

Whether you're a drone enthusiast looking to explore the skies with greater control and insight, an educator seeking to enrich your STEM curriculum, or a developer in need of a robust testing platform, the Tello Drone Heads Up Display-Guidance System offers the tools and capabilities to elevate your flying experience.

## Modules

### [app.py](app.py)

This Python application is designed to interface with a DJI Tello drone, providing a Graphical User Interface (GUI)
with flight status indicators, such as battery level, for real-time video feed and control through an 
Xbox One controller. It leverages several libraries including OpenCV for image processing, djitellopy for 
drone control, Tkinter for GUI, and PIL for image manipulation.

#### Features:
1. **GUI Initialization**:
    The GUI class initializes the main window, sets up a video stream capture label, and connects to the Tello drone 
    to start receiving the video stream. It defines the GUI's appearance, including its title and minimum size.

2. **Drone Connection**: 
    Utilizes `djitellopy` library to connect to the Tello drone, enabling video streaming and providing methods 
    to control drone's takeoff, landing, and real-time movement based on Xbox controller inputs.

3. **Video Stream Display**: 
    Implements a method to display the drone's video feed within the GUI. The video frames are captured, resized, 
    and then processed using OpenCV before being displayed. The application also includes a feature to draw battery 
    indicators on the video feed, enhancing the HUD experience.

4. **Xbox Controller Integration**: 
    Although the code related to initializing and updating joystick values from an Xbox controller is present, 
    it's commented out in the `run_app` method, suggesting that this feature may be optional or in development. 
    The controller's inputs are intended to control the drone's movements.

5. **Threaded Operations**: 
    For actions like takeoff and landing, the application uses threading to ensure these commands do not block 
    the main thread, allowing the GUI to remain responsive.

6. **Cleanup and Resource Management**: 
    Implements a cleanup method to properly release resources when the application is closed. 
    This includes stopping the drone's video stream and disconnecting from the drone.

Key Methods:
- `takeoff_land()`: Controls the drone's takeoff and landing based on its current flying state.

- `update_joystick()`: Reads inputs from the Xbox controller and sends corresponding commands to the drone. 
                       It's designed to be called repeatedly for real-time control.
                       
- `video_stream()`: Captures video frames from the drone, applies image processing, and updates the GUI with the live feed.

- `cleanup()`: Ensures a graceful shutdown by releasing resources and exiting the application.

Dependencies:
- OpenCV (`cv2`): For image processing tasks.
- `djitellopy`: Python package for controlling DJI Tello drones.
- Tkinter: Standard Python interface to the Tk GUI toolkit.
- PIL (Python Imaging Library): For image manipulation tasks.
- `indicators` module: Custom module for drawing HUD elements like battery indicators.
- `xbox_one_controller`: Custom module for integrating Xbox One controller inputs (commented out in this version).

### [indicators.py](indicators/indicators.py)

This module contains the Indicators class, designed to interface with a Tello drone object to monitor and display
various flight indicators such as battery level. It utilizes OpenCV for drawing indicators on a video feed,
threading for background updates, and time for update intervals.

#### Features:
- Continuously updates flight indicators in a separate thread.
- Draws a battery level indicator on the video feed based on the drone's current battery status.

Dependencies:
- cv2: For drawing indicators on the video feed.
- time: For controlling the update intervals of flight indicators.
- threading: For running indicator updates in a background thread.

### [xbox_one_controller.py](xbox_one_controller.py)
This module (taken from [this](https://github.com/Jacob-Pitsenberger/Tello-Drone-Gamepad-Xbox-One-Control-GUI) repository) provides a comprehensive interface for interacting with an Xbox One game controller. 
It features normalization and noise filtering of joystick inputs to ensure precise control.

## Future Enhancements

More indicators coming in the future including but not limited to:
- flight status
- height off ground
- speedometer
- pitch, roll, yaw indicators
- direction indicator (compass)
- more to come!

## Author
[Jacob Pitsenberger](https://github.com/Jacob-Pitsenberger)

Date: 2-18-2024

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.