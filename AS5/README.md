# CS512 F24 - Assignment 5 (Vision Transformer)

## Overview
This assignment focuses on implementing and comparing **Vision Transformer (ViT)**-based models for image classification. Two models are implemented:
1. **Standard Vision Transformer (ViT)**: A pure ViT model for classification.
2. **Hybrid VGG16 + ViT Model**: Combines pretrained VGG16 layers for feature extraction with ViT blocks for classification.

The models are trained and evaluated on the **CIFAR-10** or **Cats and Dogs** dataset. The goal is to understand the performance, trade-offs, and computational requirements of these architectures.

---

## Tasks and Solutions

### 1. Dataset Preparation
- **Task**: Load and preprocess the dataset.
- **Solution**:
  - Loaded the **CIFAR-10** or **Cats and Dogs** dataset using `tensorflow.keras.datasets`.
  - Resized images to **224x224** pixels and normalized pixel values to `[0, 1]`.
  - Split the dataset into **training**, **validation**, and **testing** subsets.
  - Created data pipelines using `tf.data.Dataset` for efficient loading and preprocessing.

---

### 2. Standard Vision Transformer (ViT) Model
- **Task 1**: Implement the ViT model.
  - **Solution**:
    - Loaded a pretrained ViT model from Hugging Face using `TFViTModel`.
    - Added a classification head with `num_classes` output units (10 for CIFAR-10, 1 for Cats and Dogs).
    - Compiled the model with `Adam` optimizer, `sparse_categorical_crossentropy` loss, and `accuracy` metric.

- **Task 2**: Train the ViT model.
  - **Solution**:
    - Trained the model on the training set for a specified number of epochs.
    - Saved checkpoints periodically to allow resuming training.
    - Logged training and validation loss/accuracy for visualization.

- **Task 3**: Evaluate the ViT model.
  - **Solution**:
    - Evaluated the model on the test set, reporting accuracy and loss.
    - Plotted training and validation accuracy/loss curves to analyze performance.

---

### 3. Hybrid VGG16 + ViT Model
- **Task 1**: Use pretrained VGG16 for feature extraction.
  - **Solution**:
    - Loaded pretrained VGG16 up to `block5_conv3` to extract low-level features.
    - Froze VGG16 layers to use them as a fixed feature extractor.

- **Task 2**: Implement the hybrid model.
  - **Solution**:
    - Fed VGG16 output into ViT blocks, ensuring compatibility with ViT input shape requirements.
    - Added a classification head after ViT blocks for final predictions.

- **Task 3**: Train and evaluate the hybrid model.
  - **Solution**:
    - Trained the hybrid model on the training set.
    - Evaluated on the test set, tracking accuracy and loss.
    - Visualized predictions on test images to validate model performance.

---

### 4. Analysis and Comparison
- **Task 1**: Compare performance of standard ViT and hybrid VGG16 + ViT models.
  - **Solution**:
    - Compared quantitative metrics (accuracy, loss, training time) between the two models.
    - Observed that the hybrid model achieved better accuracy due to VGG16's ability to extract low-level features.

- **Task 2**: Discuss trade-offs and improvements.
  - **Solution**:
    - Discussed computational complexity, training time, and memory usage.
    - Suggested improvements such as data augmentation, fine-tuning VGG16 layers, or using larger datasets.

---

## Technologies Used
- **Python 3**
- **Libraries**:
  - `TensorFlow/Keras` for model building and training.
  - `Transformers` (Hugging Face) for pretrained ViT models.
  - `Matplotlib` for visualization.
  - `NumPy` for numerical computations.

---
