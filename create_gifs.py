#!/usr/bin/env python3
"""
Script to extract images from Jupyter notebooks and create GIFs.
This script processes all assignments and generates:
1. Individual GIFs for each assignment with output images
2. A combined GIF with all images from all assignments
"""

import nbformat
import os
import base64
from PIL import Image
import io

def extract_images_from_notebook(notebook_path):
    """
    Extract all images from a Jupyter notebook.
    
    Args:
        notebook_path: Path to the .ipynb file
        
    Returns:
        List of PIL Image objects
    """
    images = []
    
    try:
        nb = nbformat.read(notebook_path, as_version=4)
        
        for cell_idx, cell in enumerate(nb.cells):
            if cell.cell_type == 'code' and hasattr(cell, 'outputs'):
                for output_idx, output in enumerate(cell.outputs):
                    if hasattr(output, 'data') and 'image/png' in output.data:
                        # Decode base64 image data
                        image_data = output.data['image/png']
                        image_bytes = base64.b64decode(image_data)
                        
                        # Convert to PIL Image
                        img = Image.open(io.BytesIO(image_bytes))
                        images.append(img)
                        print(f"  Extracted image {len(images)} from cell {cell_idx}, output {output_idx}")
    
    except Exception as e:
        print(f"  Error reading {notebook_path}: {e}")
    
    return images


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
    
    print("=== Extracting images from Jupyter notebooks ===\n")
    
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
                images = extract_images_from_notebook(notebook_path)
                assignment_images.extend(images)
                all_images.extend(images)
            else:
                print(f"  Notebook not found: {notebook_path}")
        
        # Create GIF for this assignment if there are images
        if assignment_images:
            gif_path = f"{assignment}_outputs.gif"
            create_gif(assignment_images, gif_path, duration=1500)
            assignment_image_counts[assignment] = len(assignment_images)
        else:
            print(f"  No images found in {assignment}")
        
        print()
    
    # Create combined GIF with all images
    print("Creating combined GIF with all images...")
    if all_images:
        create_gif(all_images, "all_outputs.gif", duration=1500)
    else:
        print("No images found across all assignments")
    
    # Print summary
    print("\n=== Summary ===")
    print(f"Total images extracted: {len(all_images)}")
    for assignment, count in assignment_image_counts.items():
        print(f"  {assignment}: {count} images")
    
    print("\nGIFs created:")
    for assignment in assignment_image_counts.keys():
        print(f"  {assignment}_outputs.gif")
    if all_images:
        print(f"  all_outputs.gif")


if __name__ == '__main__':
    main()
