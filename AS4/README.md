# CS512 F24 - Assignment 4 (Semantic Segmentation & Object Detection)

## Overview
This assignment focuses on **semantic segmentation** and **object detection** using deep learning techniques. The tasks involve implementing CNNs for pixel-wise segmentation (with and without skip connections) and evaluating a YOLO model for object detection on the Oxford-IIIT Pet dataset. Key metrics such as precision, recall, and mAP are analyzed to assess model performance.

---

## Tasks and Solutions

### 1. Semantic Segmentation
#### Part 1: Dataset Loading
- **Task**: Load the Oxford-IIIT Pet dataset.
  - **Solution**: Used `tensorflow_datasets` to load the dataset, including images and segmentation masks.

#### Part 2: Preprocessing and Splitting
- **Task**: Preprocess images/masks and split into training/validation/test sets.
  - **Solution**:
    - Resized images/masks to a fixed resolution (e.g., 128x128).
    - Normalized pixel values to `[0, 1]`.
    - Split data into 70% training, 15% validation, and 15% test.

#### Part 3: Simple CNN (Without Skip Connections)
- **Task**: Train a basic CNN for segmentation.
  - **Solution**:
    - Built an encoder-decoder CNN using `Conv2D` and `UpSampling2D` layers.
    - Used `Adam` optimizer and `SparseCategoricalCrossentropy` loss.
    - Achieved moderate accuracy (~75% validation IoU).

#### Part 4: U-Net (With Skip Connections)
- **Task**: Train a U-Net model.
  - **Solution**:
    - Implemented skip connections between encoder and decoder blocks.
    - Improved validation IoU to ~85% due to better feature retention.

---

### 2. Object Detection
#### Part 1: Dataset Preparation
- **Task**: Compute bounding boxes from segmentation masks.
  - **Solution**: Derived bounding boxes from masks using `np.where` to find object boundaries.

#### Part 2: YOLO Model Setup
- **Task**: Load and configure YOLO.
  - **Solution**:
    - Used pretrained YOLOv3 from Keras with weights from `darknet`.
    - Tweaked utility functions from [MachineLearningMastery](https://machinelearningmastery.com/how-to-perform-object-detection-with-yolov3-in-keras/) for data formatting.

#### Part 3: Model Testing
- **Task**: Detect objects in Oxford-IIIT Pet images.
  - **Solution**:
    - Passed images through YOLO and filtered predictions by confidence threshold.
    - Visualized bounding boxes using `matplotlib`.

#### Part 4: Evaluation
- **Task**: Compute metrics for object detection.
  - **Results**:
    - **IoU 0.25**: mAP = 0.8886  
      - Class 0 (e.g., pets): Precision = 0.9932, Recall = 0.8704  
      - Class 1 (e.g., background): Precision = 0.9743, Recall = 0.9004  
    - **IoU 0.5**: mAP = 0.8616  
      - Class 0: Precision = 0.9884, Recall = 0.8662  
      - Class 1: Precision = 0.9560, Recall = 0.8835  

---

## Technologies Used
- **Python 3**
- **Libraries**:
  - `TensorFlow/Keras` for model building.
  - `OpenCV` for image processing.
  - `Matplotlib` for visualization.
  - `Numpy` for bounding box calculations.

---

## Repository Structure
