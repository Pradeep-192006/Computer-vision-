Vehicle Speed Detection using Optical Flow

Description

This project detects vehicles in a video and calculates speed using OpenCV Optical Flow method.

Requirements

pip install opencv-python
pip install numpy

How to Run

1. Put video file in project folder
2. Change video path in code

video_path = "car.mp4"

3. Run

python speed_detection.py

Press Q to stop

Parameter

scale_factor = 0.05

Used to convert pixel to meter.

Output

Green box → Vehicle
Text → Speed in km/h

Output Video

Download video here:

https://github.com/Pradeep-192006/Computer-vision-/raw/main/output(1).mp4


Note

Camera must be fixed
Video should be clear
Scale factor must be adjusted
