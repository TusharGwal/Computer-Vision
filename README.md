# CS512 F24 - Computer Vision Assignments

## Overview
This repository contains solutions for five computer vision assignments covering fundamental concepts to advanced deep learning techniques. Below is a high-level summary of each assignment's focus and key implementations.

---

## Assignment 0: Vector/Matrix Operations & Neural Network Basics
- **Focus**: Core mathematical foundations and neural network implementation.
- **Key Tasks**:
  - Vector operations (dot/cross products, projections).
  - Matrix transformations (inverses, eigenvalues, linear systems).
  - Basic neural network implementation (sigmoid/ReLU activation, multi-layer networks).
- **Technologies**: NumPy, SymPy, OpenCV.

---

## Assignment 1: Image Formation & Geometric Transformations
- **Focus**: Geometric transformations and camera models.
- **Key Tasks**:
  - Homogeneous coordinates (2D/3D conversions).
  - Affine transformations (scaling, rotation, translation).
  - 3D-to-2D projection using camera intrinsic/extrinsic matrices.
- **Technologies**: NumPy, OpenCV, Matplotlib.

---

## Assignment 2: Image Filtering & Edge Detection
- **Focus**: Image preprocessing and feature extraction.
- **Key Tasks**:
  - Noise addition and SNR calculation.
  - Manual/Optimized convolution (Gaussian, Sobel filters).
  - Edge detection with Laplacian of Gaussian (LoG) and gradient histograms.
- **Technologies**: NumPy, OpenCV, SciPy.

---

## Assignment 3: Robust Estimation & CNN Classification
- **Focus**: Robust line fitting and CNN-based classification.
- **Key Tasks**:
  - Line parameter estimation under noise/outliers (RANSAC, Huber loss).
  - CNN architectures (custom, VGG16, Inception, ResNet) for CIFAR-10 and Cats vs Dogs.
  - Data augmentation and transfer learning.
- **Technologies**: TensorFlow/Keras, OpenCV, Matplotlib.

---

## Assignment 4: Semantic Segmentation & Object Detection
- **Focus**: Pixel-wise segmentation and bounding box detection.
- **Key Tasks**:
  - U-Net with skip connections for semantic segmentation.
  - YOLOv3 for object detection on Oxford-IIIT Pet dataset.
  - Evaluation using mAP and IoU metrics.
- **Technologies**: TensorFlow, OpenCV, YOLO utilities.

---

## Assignment 5: Vision Transformers (ViT)
- **Focus**: Transformer-based image classification.
- **Key Tasks**:
  - Standard Vision Transformer (ViT) implementation.
  - Hybrid VGG16 + ViT model for feature extraction.
  - Performance comparison (accuracy, training time).
- **Technologies**: Hugging Face Transformers, TensorFlow, VGG16.

---

## Technologies Used Across All Assignments
- **Python 3**
- **Libraries**: NumPy, OpenCV, TensorFlow/Keras, Matplotlib, Hugging Face Transformers.
- **Tools**: Jupyter Notebook, Google Colab (GPU support).

---

## Key Insights
1. **Mathematical Foundations**: Linear algebra and homogeneous coordinates are critical for geometric transformations.
2. **Architecture Trade-offs**: Skip connections (U-Net), residual blocks (ResNet), and hybrid models (VGG16+ViT) improve performance.
3. **Robustness**: Techniques like RANSAC and Huber loss mitigate noise/outlier effects.
4. **Efficiency**: OpenCV and optimized libraries (e.g., TensorFlow) significantly speed up computations.

---

## Conclusion
These assignments provide hands-on experience in core computer vision concepts, from geometric transformations and filtering to advanced deep learning architectures like Vision Transformers and YOLO. The solutions highlight the importance of both theoretical understanding and practical implementation in real-world applications.
