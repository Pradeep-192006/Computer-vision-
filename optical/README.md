Vehicle Speed Detection

Description

This project detects vehicles in a video and calculates speed using OpenCV Optical Flow.

Requirements

Install libraries:

pip install opencv-python numpy

How to run

1. Put video file in folder
2. Change video path in code

video_path = "traffic.mp4"

3. Run program

python speed_detection.py

Press Q to stop.

Parameter

scale_factor = 0.05

Used to convert pixel to meter.

Output

- Green box → Vehicle
- Text → Speed in km/h

Note

Camera must be fixed
Video should be clear
Scale factor must be adjusted
