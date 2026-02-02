Wavelet-Based Multi Resolution Analysis (MRA) – Image Feature Extraction

📌 Project Overview

This project demonstrates Multi Resolution Analysis (MRA) of an image using 2D Discrete Wavelet Transform (DWT). The image is decomposed into multiple frequency sub-bands and statistical features are extracted from each band. This approach is widely used in computer vision, medical image analysis (MRI/CT), texture analysis, and pattern recognition.


---

🛠️ Technologies Used

Python

NumPy – Numerical operations

OpenCV (cv2) – Image loading and preprocessing

PyWavelets (pywt) – Wavelet decomposition

Matplotlib – Visualization

Pandas – Feature vector representation



---

📂 Input Image

Grayscale image (.jpg, .png, etc.)

Example: scan.jpg

If no image path is provided, a synthetic image with noise is generated automatically.



---

⚙️ Processing Steps

1️⃣ Image Loading

Image is loaded in grayscale mode

Converted to float format for accurate wavelet processing

Optional Gaussian noise added (for demo purpose)


2️⃣ Wavelet Decomposition (MRA)

Uses 2D Discrete Wavelet Transform

Wavelet type: db2

Decomposition level: 3


Sub-bands generated at each level:

LL – Approximation (Low-Low)

LH – Horizontal details

HL – Vertical details

HH – Diagonal details


3️⃣ Visualization

Displays:

Final approximation image
