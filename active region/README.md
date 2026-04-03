Face Distance Estimation using OpenCV

Description

This project detects a human face in a video and calculates distance from the camera using OpenCV.

Requirements

pip install opencv-python
pip install numpy

How to Run

Put video file in project folder
Change video path in code
video_path = "face detect.mp4"

Run
python your_file_name.py
Press Q to stop

Parameter

KNOWN_WIDTH = 14.0
Average face width (cm)
FOCAL_LENGTH = 600
Used for distance calculation

Output

Green box → Face
Text → Distance in cm

Output Video

Download video here:

https://github.com/Pradeep-192006/Computer-vision-/raw/main/face/output%20(2).mp4⁠

Note

Distance is approximate
Focal length should be adjusted
Face must be clear
