# Object Detection

### Setup

- Install DepthAI [version 2.22.0.0, dated 9/29/2023] ([Documentation](https://docs.luxonis.com/projects/api/en/latest/install/#supported-platforms))
- Connect to OAK camera ([Documentation](https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/#device-setup))
- Install required packages from PyPI:
    
    ```bash
    pip install depthai blobconverter
    ```
    

### Usage

- Run the program using Python
    
    ```bash
    python3 object_detection.py
    ```
    

### Output

The program outputs a [SpatialImgDetections](https://docs.luxonis.com/projects/api/en/latest/components/messages/spatial_img_detections/#spatialimgdetections) message. For visualization purposes, I have printed all detections and information about them to the console. 

Expected output:

```bash
Label: person
Confidence: 0.8230600357055664
Coordinates: (109.34834289550781, -205.5748748779297, 677.9410400390625)
```

### Model Information

**YOLOv8 nano**

Trained on the [COCO dataset](https://cocodataset.org) downloaded from https://github.com/luxonis/depthai-model-zoo

[Documentation](https://docs.ultralytics.com/)

[Source](https://github.com/ultralytics/ultralytics)

**Labels:**

- person
- bicycle
- car
- motorbike
- aeroplane
- bus
- train
- truck
- boat
- traffic light
- fire hydrant
- stop sign
- parking meter
- bench
- bird
- cat
- dog
- horse
- sheep
- cow
- elephant
- bear
- zebra
- giraffe
- backpack
- umbrella
- handbag
- tie
- suitcase
- frisbee
- skis
- snowboard
- sports ball
- kite
- baseball bat
- baseball glove
- skateboard
- surfboard
- tennis racket
- bottle
- wine glass
- cup
- fork
- knife
- spoon
- bowl
- banana
- apple
- sandwich
- orange
- broccoli
- carrot
- hot dog
- pizza
- donut
- cake
- chair
- sofa
- pottedplant
- bed
- diningtable
- toilet
- tvmonitor
- laptop
- mouse
- remote
- keyboard
- cell phone
- microwave
- oven
- toaster
- sink
- refrigerator
- book
- clock
- vase
- scissors
- teddy bear
- hair drier
- toothbrush