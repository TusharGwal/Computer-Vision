# CS512 F24 - Assignment 2 (Image Filtering)

## Overview
This assignment focuses on **image filtering techniques** such as noise addition, convolution, Gaussian smoothing, edge detection, and Gaussian pyramids. Solutions are implemented in **Python** using **NumPy** and **OpenCV**, with manual implementations of core algorithms to deepen understanding of mathematical operations in computer vision.

---

## Tasks and Solutions

### 1. Add Gaussian Noise and Compute SNR
- **Task**: Generate 10 noisy versions of a grayscale image, compute noise variance, signal power, and SNR in dB.
- **Solution**:
  - Added Gaussian noise using `numpy.random.normal`.
  - Computed noise variance as the mean of pixel-wise standard deviation across noisy images.
  - Derived signal power from the original image's variance.
  - Calculated SNR using the formula: \( \text{SNR (dB)} = 10 \cdot \log_{10}(\text{Signal Power} / \text{Noise Power}) \).

---

### 2. Implement a Convolution Filter for Smoothing
- **Task**: Manually implement a 3x3 convolution filter and compare performance with OpenCV.
- **Solution**:
  - Created a sliding window convolution with zero padding using `numpy.pad`.
  - Compared execution time of manual implementation vs. `cv2.filter2D`.
  - Observed significant performance differences due to OpenCV's optimized C++ backend.

---

### 3. Convolution with Stride
- **Task**: Implement convolution with stride to reduce output dimensions.
- **Solution**:
  - Modified the sliding window loop to step by `stride` value.
  - Visualized output for different stride values (e.g., 2, 3) to observe resolution reduction.

---

### 4. Gaussian Smoothing Filter
- **Task**: Generate a 2D Gaussian kernel, apply it to an image, and determine maximum allowed σ for a 5x5 filter.
- **Solution**:
  - Implemented `gaussian_kernel(size, sigma)` using the Gaussian function.
  - Applied the kernel with `cv2.filter2D`.
  - Derived maximum σ ≈ 1.5 for a 5x5 kernel to avoid truncating significant values.

---

### 5. Gaussian Pyramid Construction
- **Task**: Build a Gaussian pyramid and visualize scaled layers.
- **Solution**:
  - Used `cv2.pyrDown` iteratively to create pyramid levels.
  - Scaled layers back to original size with `cv2.resize` for visualization.
  - Observed progressive blurring and resolution reduction in successive layers.

---

### 6. Image Gradients and Histogram of Gradient Directions
- **Task**: Compute gradients, visualize vectors, and plot direction histogram.
- **Solution**:
  - Calculated gradients using Sobel operators (`cv2.Sobel`).
  - Drew gradient vectors with `cv2.arrowedLine` for magnitudes above a threshold.
  - Generated a histogram of gradient directions using `plt.hist`.

---

### 7. Gaussian Derivatives Gradients
- **Task**: Compute x/y derivatives using separable Gaussian derivative filters.
- **Solution**:
  - Generated 1D Gaussian and derivative kernels.
  - Applied horizontal and vertical filters sequentially for separable convolution.
  - Visualized x/y derivatives as edge-enhanced images.

---

### 8. Laplacian of Gaussian (LoG) Filtering
- **Task**: Detect edges using LoG zero crossings.
- **Solution**:
  - Created a LoG filter by combining Gaussian smoothing and Laplacian.
  - Detected zero crossings using horizontal/vertical edge filters.
  - Validated results with synthetic test images (e.g., squares, circles).

---

## Technologies Used
- **Python 3**
- **Libraries**:
  - `NumPy` for matrix operations and noise generation.
  - `OpenCV` for image I/O, filtering, and pyramids.
  - `Matplotlib` for visualization.
  - `SciPy` (optional) for advanced filtering.

---

## Repository Structure
