# CS512 F24 - Assignment 3 (Fitting and Recognition)

## Overview
This assignment focuses on **robust estimation** and **image classification** using **convolutional neural networks (CNNs)**. The tasks involve simulating noisy data, estimating geometric parameters, and building/training CNN models for image classification on the **Kaggle Cats and Dogs** and **CIFAR-10** datasets. The goal is to understand the impact of noise, outliers, and different network architectures on model performance.

---

## Tasks and Solutions

### 1. Robust Estimation
- **Task 1**: Generate points on a line segment with given parameters (angle and distance from origin) and plot the results.
  - **Solution**: Generated points using the line equation \( y = mx + c \), where \( m \) is the slope and \( c \) is the intercept. Plotted lines for angles between 0° and 90°.

- **Task 2**: Add Gaussian noise to the points and plot the noisy points.
  - **Solution**: Added Gaussian noise using `numpy.random.normal` and visualized the noisy points.

- **Task 3**: Estimate line parameters from noisy points and compute error.
  - **Solution**: Used least squares to estimate line parameters and calculated error against ground truth.

- **Task 4**: Plot error as a function of noise level.
  - **Solution**: Varied noise levels and plotted the corresponding errors to observe the impact of noise on estimation accuracy.

- **Task 5**: Introduce outliers and re-estimate line parameters.
  - **Solution**: Added random outliers to the point set and re-estimated parameters. Plotted error as a function of outlier percentage.

- **Task 6**: Use `cv2.fitLine` with `CV_DIST_HUBER` for robust line estimation.
  - **Solution**: Compared robust estimation results with least squares and plotted error as a function of outlier percentage.

- **Task 7**: Evaluate and report results.
  - **Solution**: Observed that robust estimation (e.g., `CV_DIST_HUBER`) performs better in the presence of outliers compared to least squares.

---

### 2. Image Classification (Kaggle Cats and Dogs)
- **Task 1**: Download and preprocess the Kaggle Cats and Dogs dataset.
  - **Solution**: Selected 2000 cat and 2000 dog images, split into training, validation, and test sets.

- **Task 2**: Build and evaluate a custom CNN.
  - **Solution**: Designed a CNN with convolutional, pooling, normalization, and dense layers. Achieved moderate accuracy on the validation set.

- **Task 3**: Add data augmentation and re-evaluate.
  - **Solution**: Augmented data using rotations, flips, and zooms. Observed improved validation accuracy due to better generalization.

- **Task 4**: Replace custom CNN with pre-trained VGG16.
  - **Solution**: Used VGG16 as a feature extractor and added a dense layer for classification. Achieved higher accuracy compared to the custom CNN.

- **Task 5**: Evaluate and report results.
  - **Solution**: Pre-trained models (e.g., VGG16) outperformed custom CNNs, especially with limited data.

---

### 3. Image Classification (CIFAR-10)
- **Task 1**: Load and preprocess the CIFAR-10 dataset.
  - **Solution**: Loaded the dataset using `pickle` and normalized pixel values.

- **Task 2**: Build and evaluate a basic CNN.
  - **Solution**: Designed a CNN with multiple convolution blocks (convolution, pooling, normalization) and a dense layer with softmax activation. Achieved baseline accuracy.

- **Task 3**: Replace convolution blocks with Inception blocks.
  - **Solution**: Implemented Inception blocks to capture multi-scale features. Observed improved accuracy due to better feature extraction.

- **Task 4**: Replace Inception blocks with residual blocks.
  - **Solution**: Used residual blocks to enable deeper networks without vanishing gradients. Achieved further improvement in accuracy.

- **Task 5**: Evaluate and report results.
  - **Solution**: Residual blocks performed best, demonstrating the effectiveness of skip connections in deep networks.

---

## Technologies Used
- **Python 3**
- **Libraries**:
  - `NumPy` for numerical computations.
  - `OpenCV` for robust line estimation.
  - `TensorFlow/Keras` for building and training CNNs.
  - `Matplotlib` for visualization.
  - `Pickle` for loading CIFAR-10 data.

---

## Repository Structure
