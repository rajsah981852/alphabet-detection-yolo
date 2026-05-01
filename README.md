# Alphabet Detection using YOLO

This project implements a character detection system using the Ultralytics YOLO model to recognize alphabets and numeric characters from images. It supports multiple character detection and reconstructs the final output in correct left-to-right sequence.

## Overview

The system processes an input image, detects individual characters using a trained YOLO model, and generates the final predicted text based on spatial arrangement.

## Features

- Detection of alphabets and digits from images  
- Supports multiple characters in a single image  
- Left-to-right sorting for correct sequence generation  
- Confidence-based filtering to improve predictions  
- Streamlit-based user interface for easy interaction  
- Batch prediction support using Python script  

## Project Structure

alphabet-detection-yolo/
│
├── app.py
├── predict.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── test_images/
│   ├── sample1.jpg
│   └── sample2.jpg

## Installation

Clone the repository:

git clone https://github.com/your-username/alphabet-detection-yolo.git  
cd alphabet-detection-yolo  

Install dependencies:

pip install -r requirements.txt  

## Model File

The trained model file (best.pt) is not included due to size limitations.

Download it from the link below and place it in the following directory:

runs/detect/train/weights/

[Add your Google Drive link here]

## Usage

Run Streamlit interface:

streamlit run app.py  

Run batch prediction:

python predict.py  

## Example Result

![Result](test_images/sample1.jpg)

Predicted Output: 52D

## Working Methodology

1. Input image is passed to the YOLO model  
2. Model detects character bounding boxes  
3. Predictions are filtered using confidence threshold  
4. Characters are sorted based on x-coordinate  
5. Duplicate detections are removed  
6. Final text is generated  

## Technologies Used

- Python  
- Ultralytics YOLO  
- Streamlit  
- NumPy  
- Pillow  

## Limitations

- Accuracy depends on dataset quality  
- Misclassification may occur for similar-looking characters  
- Performance may vary on low-resolution images  

## Future Improvements

- Improve model accuracy with better dataset and augmentation  
- Add bounding box visualization  
- Support real-time webcam detection  
- Deploy as a web application  

## License

This project is intended for educational and research purposes.
