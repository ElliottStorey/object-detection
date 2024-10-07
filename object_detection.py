import depthai as dai
import blobconverter

yoloSpacialDetectionNetworkBlobPath = blobconverter.from_zoo(
    "yolov8n_coco_640x352", zoo_type="depthai", shaves=5
)

labels = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]

# Create pipeline
pipeline = dai.Pipeline()

# Define sources and outputs
colorCamera = pipeline.createColorCamera()
monoCameraLeft = pipeline.createMonoCamera()
monoCameraRight = pipeline.createMonoCamera()
stereoDepth = pipeline.createStereoDepth()
yoloSpacialDetectionNetwork = pipeline.createYoloSpatialDetectionNetwork()

xoutYoloSpacialDetectionNetwork = pipeline.createXLinkOut()

# Properties
colorCamera.setPreviewSize(640, 352)
colorCamera.setInterleaved(False)

monoCameraLeft.setCamera("left")
monoCameraRight.setCamera("right")

stereoDepth.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
stereoDepth.setDepthAlign(dai.CameraBoardSocket.CAM_A)
stereoDepth.setOutputSize(
    monoCameraLeft.getResolutionWidth(), monoCameraLeft.getResolutionHeight()
)
stereoDepth.setSubpixel(True)

yoloSpacialDetectionNetwork.setBlobPath(yoloSpacialDetectionNetworkBlobPath)
yoloSpacialDetectionNetwork.setConfidenceThreshold(0.5)
yoloSpacialDetectionNetwork.input.setBlocking(False)
yoloSpacialDetectionNetwork.setBoundingBoxScaleFactor(0.5)
yoloSpacialDetectionNetwork.setDepthLowerThreshold(100)  # Min 10 centimeters
yoloSpacialDetectionNetwork.setDepthUpperThreshold(5000)  # Max 5 meters
yoloSpacialDetectionNetwork.setNumClasses(80)
yoloSpacialDetectionNetwork.setCoordinateSize(4)
yoloSpacialDetectionNetwork.setAnchors(
    [10, 14, 23, 27, 37, 58, 81, 82, 135, 169, 344, 319]
)
yoloSpacialDetectionNetwork.setAnchorMasks({"side26": [1, 2, 3], "side13": [3, 4, 5]})
yoloSpacialDetectionNetwork.setIouThreshold(0.5)

xoutYoloSpacialDetectionNetwork.setStreamName("Yolo Spacial Detection Network")

# Linking
monoCameraLeft.out.link(stereoDepth.left)
monoCameraRight.out.link(stereoDepth.right)
colorCamera.preview.link(yoloSpacialDetectionNetwork.input)
stereoDepth.depth.link(yoloSpacialDetectionNetwork.inputDepth)
yoloSpacialDetectionNetwork.out.link(xoutYoloSpacialDetectionNetwork.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:
    yoloSpacialDetectionNetworkQueue = device.getOutputQueue(
        "Yolo Spacial Detection Network", maxSize=1, blocking=False
    )

    while True:
        spatialImgDetections = yoloSpacialDetectionNetworkQueue.get().detections
        for detection in spatialImgDetections:
            print(
                f"""
                  Label: {labels[detection.label]}
                  Confidence: {detection.confidence}
                  Coordinates: ({detection.spatialCoordinates.x}, {detection.spatialCoordinates.y}, {detection.spatialCoordinates.z})
                  """
            )
