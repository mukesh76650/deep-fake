# Deepfake Detector

This project aims to detect whether an image or video is a deepfake or real using deep learning.

## Features

- Analyze images to detect deepfakes.
- Analyze videos to detect deepfakes (frame by frame).
- (Optional) Simple web interface for uploading and checking media.

## Getting Started

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run detection (see usage in src/image_detector.py and src/video_detector.py).

## Project Structure
- `src/` - Source code for image and video deepfake detection
- `models/` - Pretrained or saved models
- `data/` - Example/test datasets

## Future Work
- Improve detection accuracy
- Add GUI/web interface
