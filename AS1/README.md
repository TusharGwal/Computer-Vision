# CS512 F24 - Assignment 1 (Image Formation)

## Overview
This assignment focuses on **geometric transformations** in computer vision, including representation in homogeneous coordinates (2D and 3D), image projection in camera coordinates, and transformations such as translation, rotation, and scaling. The solutions are implemented in **Python** using **NumPy** and **OpenCV**.

---

## Tasks and Solutions

### 1. Homogeneous Coordinates Representation (2D)
- **Task**: Convert a 2D Cartesian point to homogeneous coordinates, find an equivalent point with a different scale, and verify the conversion back to Cartesian coordinates.
- **Solution**:
  - Implemented functions to convert between Cartesian and homogeneous coordinates.
  - Verified that different scaled homogeneous coordinates represent the same Cartesian point.

---

### 2. Homogeneous Coordinates Representation (3D)
- **Task**: Convert a 3D Cartesian point to homogeneous coordinates, scale it, and verify the conversion back to Cartesian coordinates.
- **Solution**:
  - Extended the 2D homogeneous coordinate logic to 3D.
  - Scaled the homogeneous coordinates and confirmed the result matches the original point.

---

### 3. Affine Transformations in 2D
- **Task**: Apply scaling, rotation, and translation to a 2D point using transformation matrices in homogeneous coordinates.
- **Solution**:
  - Computed transformation matrices for scaling, rotation, and translation.
  - Combined the transformations and applied them to the point.
  - Verified the result using NumPy.

---

### 4. Inverse Transformations (2D)
- **Task**: Reverse a sequence of transformations (scaling, rotation, translation) applied to a 2D point.
- **Solution**:
  - Computed the inverse transformation matrix.
  - Applied the inverse matrix to return the point to its original position.
  - Verified the result using NumPy.

---

### 5. Transformations Between 3D Coordinate Systems
- **Task**: Transform a 3D point from one coordinate system to another using a transformation matrix.
- **Solution**:
  - Computed the transformation matrix to convert between the two coordinate systems.
  - Applied the transformation to the point and verified the result.

---

### 6. Projection in Camera Coordinates (3D to 2D)
- **Task**: Project a 3D point onto a 2D image plane using a camera intrinsic matrix.
- **Solution**:
  - Implemented the projection using the intrinsic matrix `K`.
  - Computed the 2D pixel coordinates of the projected point.
  - Explained the role of each element in the intrinsic matrix.

---

### 7. General Camera Model (3D World Points to 2D Image Points)
- **Task**: Transform a 3D world point to 2D image coordinates using camera intrinsic and extrinsic parameters.
- **Solution**:
  - Computed the extrinsic matrix from rotation and translation.
  - Projected the 3D point onto the 2D image plane.
  - Verified the 2D pixel coordinates.

---

### 8. Image Transformation using `cv2.warpAffine` (2D)
- **Task**: Apply a combination of transformations (translation, rotation, scaling) to an image using OpenCV.
- **Solution**:
  - Computed the affine transformation matrix manually.
  - Used `cv2.warpAffine` to apply the transformation to the image.
  - Displayed the original and transformed images.

---

### 9. Order of Transformations
- **Task**: Apply transformations in different orders and observe the effect on the final position of a 2D point.
- **Solution**:
  - Applied transformations in the specified order and reversed order.
  - Observed and explained how the final position changes based on the order of transformations.

---

## Technologies Used
- **Python 3**
- **Libraries**:
  - `NumPy` for matrix operations.
  - `OpenCV` for image transformations.
  - `math` for trigonometric calculations.

---

## Repository Structure
