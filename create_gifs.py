#!/usr/bin/env python3
"""
Script to extract images from Jupyter notebooks and create GIFs.
This script processes all assignments and generates:
1. Individual GIFs for each assignment with curated output images
2. A combined GIF with representative images from all assignments

The script intelligently filters similar images and combines related input/output pairs.
"""

import nbformat
import os
import base64
from PIL import Image
import io
import hashlib

def calculate_image_hash(img):
    """Calculate a perceptual hash of an image for similarity detection."""
    # Resize to small size for comparison
    small = img.resize((8, 8), Image.Resampling.LANCZOS).convert('L')
    pixels = list(small.getdata())
    avg = sum(pixels) / len(pixels)
    # Create hash based on whether pixel is above/below average
    bits = ''.join('1' if p > avg else '0' for p in pixels)
    return bits

def are_images_similar(img1, img2, threshold=0.85):
    """Check if two images are similar based on hash comparison."""
    hash1 = calculate_image_hash(img1)
    hash2 = calculate_image_hash(img2)
    
    # Calculate similarity (Hamming distance)
    matches = sum(b1 == b2 for b1, b2 in zip(hash1, hash2))
    similarity = matches / len(hash1)
    
    return similarity > threshold

def extract_images_from_notebook(notebook_path, deduplicate=True):
    """
    Extract images from a Jupyter notebook with intelligent filtering.
    
    Args:
        notebook_path: Path to the .ipynb file
        deduplicate: Whether to remove similar consecutive images
        
    Returns:
        List of dicts with image info: {'image': PIL.Image, 'cell': int, 'output': int}
    """
    images = []
    
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        
        for cell_idx, cell in enumerate(nb.cells):
            if cell.cell_type == 'code' and hasattr(cell, 'outputs'):
                cell_images = []
                for output_idx, output in enumerate(cell.outputs):
                    if hasattr(output, 'data') and 'image/png' in output.data:
                        # Decode base64 image data
                        image_data = output.data['image/png']
                        image_bytes = base64.b64decode(image_data)
                        
                        # Convert to PIL Image
                        img = Image.open(io.BytesIO(image_bytes))
                        cell_images.append({
                            'image': img,
                            'cell': cell_idx,
                            'output': output_idx
                        })
                
                # If multiple images in same cell, intelligently filter
                if len(cell_images) > 1:
                    # Check if all images have the same size (likely same type of plot)
                    sizes = [img_info['image'].size for img_info in cell_images]
                    all_same_size = len(set(sizes)) == 1
                    
                    if all_same_size and len(cell_images) > 2:
                        # Multiple images of same size - likely training progress
                        # Keep only first and last to show progression
                        images.append(cell_images[0])
                        images.append(cell_images[-1])
                        print(f"    Filtered {len(cell_images)} similar-sized images to 2 (start/end)")
                    else:
                        # Different sizes or small group - check similarity
                        similar_groups = []
                        for img_info in cell_images:
                            added = False
                            for group in similar_groups:
                                if are_images_similar(img_info['image'], group[0]['image'], threshold=0.90):
                                    group.append(img_info)
                                    added = True
                                    break
                            if not added:
                                similar_groups.append([img_info])
                        
                        # For each group, keep only representative images
                        for group in similar_groups:
                            if len(group) == 1:
                                images.append(group[0])
                            elif len(group) == 2:
                                images.extend(group)
                            else:
                                # Keep first and last
                                images.append(group[0])
                                images.append(group[-1])
                                print(f"    Filtered {len(group)} similar images to 2")
                else:
                    images.extend(cell_images)
        
        print(f"  Extracted {len(images)} images (after filtering)")
    
    except Exception as e:
        print(f"  Error reading {notebook_path}: {e}")
    
    return images

def combine_side_by_side(images, max_per_row=2):
    """
    Combine multiple images into a single image, arranged in a grid.
    Optimized for portfolio presentation - keeps combinations compact.
    
    Args:
        images: List of PIL Image objects
        max_per_row: Maximum images per row (default 2 for readability)
        
    Returns:
        Single combined PIL Image
    """
    if len(images) == 1:
        return images[0]
    
    # Limit to maximum 4 images for portfolio presentation
    if len(images) > 4:
        # Keep first, middle, and last images
        indices = [0, len(images) // 2, -1]
        images = [images[i] for i in indices]
        print(f"      Limited to 3 representative images for clarity")
    
    # Calculate grid dimensions
    num_cols = min(len(images), max_per_row)
    num_rows = (len(images) + num_cols - 1) // num_cols
    
    # Find maximum dimensions
    max_width = max(img.size[0] for img in images)
    max_height = max(img.size[1] for img in images)
    
    # Add some padding
    padding = 10
    
    # Create canvas
    canvas_width = num_cols * max_width + (num_cols + 1) * padding
    canvas_height = num_rows * max_height + (num_rows + 1) * padding
    canvas = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))
    
    # Place images
    for idx, img in enumerate(images):
        row = idx // num_cols
        col = idx % num_cols
        
        x = col * (max_width + padding) + padding
        y = row * (max_height + padding) + padding
        
        # Center image in its cell
        x_offset = (max_width - img.size[0]) // 2
        y_offset = (max_height - img.size[1]) // 2
        
        canvas.paste(img, (x + x_offset, y + y_offset))
    
    return canvas


def create_gif(images, output_path, duration=1500):
    """
    Create a GIF from a list of images.
    
    All frames are normalized to a consistent canvas size (maximum width and height
    across all images) with smaller images centered on a white background.
    
    Args:
        images: List of PIL Image objects
        output_path: Path to save the GIF
        duration: Duration per frame in milliseconds (default: 1500ms = 1.5 seconds)
    """
    if not images:
        print(f"  No images to create GIF at {output_path}")
        return
    
    # Find the maximum dimensions across all images to create consistent canvas size
    max_width = max(img.size[0] for img in images)
    max_height = max(img.size[1] for img in images)
    canvas_size = (max_width, max_height)
    
    # Convert all images to RGB mode and center on canvas
    rgb_images = []
    for img in images:
        # Convert to RGB first
        if img.mode == 'RGBA':
            # Create white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
            rgb_img = background
        elif img.mode != 'RGB':
            rgb_img = img.convert('RGB')
        else:
            rgb_img = img
        
        # Create a canvas of consistent size with white background
        canvas = Image.new('RGB', canvas_size, (255, 255, 255))
        
        # Calculate position to center the image on the canvas
        x_offset = (canvas_size[0] - rgb_img.size[0]) // 2
        y_offset = (canvas_size[1] - rgb_img.size[1]) // 2
        
        # Paste the image onto the canvas
        canvas.paste(rgb_img, (x_offset, y_offset))
        rgb_images.append(canvas)
    
    # Save as GIF
    rgb_images[0].save(
        output_path,
        save_all=True,
        append_images=rgb_images[1:],
        duration=duration,
        loop=0
    )
    print(f"  Created GIF: {output_path} ({len(images)} frames, {canvas_size[0]}x{canvas_size[1]})")


def main():
    """Main function to process all notebooks and create GIFs."""
    
    print("=== Extracting images from Jupyter notebooks (with intelligent filtering) ===\n")
    
    # Assignment directories to process
    # Note: AS0 is excluded as it contains no output images
    assignments = {
        'AS1': ['AS1.ipynb'],
        'AS2': ['AS2.ipynb'],
        'AS3': ['AS3_P1.ipynb', 'AS3_P2.ipynb', 'AS3_P3.ipynb'],
        'AS4': ['AS4_Q1.ipynb', 'AS4_Q2.ipynb'],
        'AS5': ['AS5.ipynb']
    }
    
    all_images = []
    assignment_image_counts = {}
    
    # Process each assignment
    for assignment, notebooks in assignments.items():
        print(f"Processing {assignment}...")
        assignment_images = []
        
        for notebook in notebooks:
            notebook_path = os.path.join(assignment, notebook)
            if os.path.exists(notebook_path):
                print(f"  Reading {notebook_path}...")
                image_infos = extract_images_from_notebook(notebook_path, deduplicate=True)
                
                # Group images by cell and combine if multiple from same cell
                cell_groups = {}
                for img_info in image_infos:
                    cell_id = img_info['cell']
                    if cell_id not in cell_groups:
                        cell_groups[cell_id] = []
                    cell_groups[cell_id].append(img_info['image'])
                
                # Process each cell's images
                for cell_id, cell_images in cell_groups.items():
                    if len(cell_images) == 1:
                        assignment_images.append(cell_images[0])
                    elif len(cell_images) == 2:
                        # Two images - combine them side by side (likely input/output)
                        combined = combine_side_by_side(cell_images, max_per_row=2)
                        assignment_images.append(combined)
                        print(f"    Combined 2 images from cell {cell_id} (input/output pair)")
                    else:
                        # Multiple images - combine with limit for readability
                        combined = combine_side_by_side(cell_images, max_per_row=2)
                        assignment_images.append(combined)
                        print(f"    Combined {len(cell_images)} images from cell {cell_id}")
            else:
                print(f"  Notebook not found: {notebook_path}")
        
        # Add assignment images to all_images ONCE per assignment
        all_images.extend(assignment_images)
        
        # Create GIF for this assignment if there are images
        if assignment_images:
            gif_path = f"{assignment}_outputs.gif"
            create_gif(assignment_images, gif_path, duration=2000)
            assignment_image_counts[assignment] = len(assignment_images)
        else:
            print(f"  No images found in {assignment}")
        
        print()
    
    # Create combined GIF with all images
    print("Creating combined GIF with all images...")
    if all_images:
        create_gif(all_images, "all_outputs.gif", duration=2000)
    else:
        print("No images found across all assignments")
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Total frames in GIFs: {len(all_images)} (reduced from many more by intelligent filtering)")
    for assignment, count in assignment_image_counts.items():
        print(f"  {assignment}: {count} frames")
    
    print("\nGIFs created:")
    for assignment in assignment_image_counts.keys():
        print(f"  {assignment}_outputs.gif")
    if all_images:
        print(f"  all_outputs.gif")
    
    print("\nNote: Similar images have been combined and repetitive frames removed for portfolio presentation.")


if __name__ == '__main__':
    main()
