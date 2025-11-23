# Object Detection

Implementation of object detection for a stereo depth camera with Neural Network inferencing and Computer Vision capabilities.

## Getting Started

### Installation

Install DepthAI [version 2.22.0.0, dated 9/29/2023] ([Documentation](https://docs.luxonis.com/projects/api/en/latest/install/#supported-platforms))

Connect to OAK camera ([Documentation](https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/#device-setup))

Install required packages from PyPI:

```bash
pip install depthai blobconverter
```

### Usage

Run the program using Python:

```bash
python3 object_detection.py
```

#### Output

The program outputs a [SpatialImgDetections](https://docs.luxonis.com/projects/api/en/latest/components/messages/spatial_img_detections/#spatialimgdetections) message. For visualization purposes, I have printed all detections and information about them to the console.

Expected output:

```bash
Label: person
Confidence: 0.823060035705566 4
Coordinates: (109.34834289550781, -205.57487487792297, 677.94104003906 25)
```
