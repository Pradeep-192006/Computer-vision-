Description

This project detects moving objects in a video and tracks them using Kalman Filter with OpenCV.

Requirements

pip install opencv-python
pip install numpy

How to Run

Put video file in project folder
Change video path in code
video_path = "videoplayback.mp4"

Run
python kalman_code.py
Press ESC to stop

Parameters

history = 100
Used for background subtraction
varThreshold = 40
Controls detection sensitivity

Output

Green box → Detected object
Red line → Object path (trace)
Blue dot → Predicted position

Output Video

Download video here:
https://github.com/Pradeep-192006/Computer-vision-/raw/main/Kalman/output%20(3).mp4

Note

Camera should be fixed
Works best with moving objects
Tracking may vary for fast motion
