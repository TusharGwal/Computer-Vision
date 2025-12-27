# CS512 F24 - Computer Vision Assignments

## Overview
This repository contains solutions for five computer vision assignments covering fundamental concepts to advanced deep learning techniques. Below is a high-level summary of each assignment's focus and key implementations.

## Visual Outputs

Visual outputs from the assignments are available in two formats:

### PowerPoint Presentations (Recommended for Portfolio)

Individual PowerPoint presentations with aggressively filtered, unique images:

- **[AS1_outputs.pptx](AS1_outputs.pptx)** - Image Formation & Geometric Transformations (1 slide, 383KB)
- **[AS2_outputs.pptx](AS2_outputs.pptx)** - Image Filtering & Edge Detection (7 slides, 1.4MB)
- **[AS3_outputs.pptx](AS3_outputs.pptx)** - Robust Estimation & CNN Classification (5 slides, 227KB)
- **[AS4_outputs.pptx](AS4_outputs.pptx)** - Semantic Segmentation & Object Detection (6 slides, 886KB)
- **[AS5_outputs.pptx](AS5_outputs.pptx)** - Vision Transformers (4 slides, 724KB)

**Presentation Features:**
- ✅ **Aggressive filtering**: Removed repetitive images (e.g., AS4: 23 → 6 unique slides)
- ✅ **Portfolio-ready**: Each image on a separate slide for easy extraction
- ✅ **High quality**: Full-resolution images centered on slides
- ✅ **No duplicates**: Similar images deduplicated using perceptual hashing

To create presentations:
```bash
python3 create_presentations.py
```

### Animated GIFs (Alternative View)

Portfolio-optimized GIFs with intelligent filtering:

- **[All Outputs Combined](all_outputs.gif)** - Curated visualization with 25 frames
- **[Assignment 1 Outputs](AS1_outputs.gif)** - 1 frame
- **[Assignment 2 Outputs](AS2_outputs.gif)** - 8 frames
- **[Assignment 3 Outputs](AS3_outputs.gif)** - 5 frames
- **[Assignment 4 Outputs](AS4_outputs.gif)** - 7 frames
- **[Assignment 5 Outputs](AS5_outputs.gif)** - 4 frames

To create GIFs:
```bash
python3 create_gifs.py
```

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
