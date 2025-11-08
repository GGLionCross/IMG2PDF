#!/usr/bin/env python3
"""
Image to PDF converter that combines multiple images into a single PDF
with page size matching the maximum dimensions across all images.
"""

import sys
from pathlib import Path
from PIL import Image
import img2pdf


def get_image_dimensions(image_path):
    """Get the dimensions of an image file."""
    try:
        with Image.open(image_path) as img:
            return img.size  # Returns (width, height)
    except Exception as e:
        print(f"Error reading image {image_path}: {e}", file=sys.stderr)
        return None


def get_max_dimensions(image_paths):
    """Get the maximum width and height across all images."""
    max_width = 0
    max_height = 0
    
    for image_path in image_paths:
        dims = get_image_dimensions(image_path)
        if dims:
            width, height = dims
            max_width = max(max_width, width)
            max_height = max(max_height, height)
    
    return max_width, max_height


def create_pdf(image_paths, output_name="untitled.pdf"):
    """Create a PDF from image paths with page size matching max dimensions."""
    if not image_paths:
        print("No image paths provided.", file=sys.stderr)
        return False
    
    # Validate that all image files exist
    valid_paths = []
    for path_str in image_paths:
        path = Path(path_str)
        if not path.exists():
            print(f"Warning: File not found: {path_str}", file=sys.stderr)
            continue
        if not path.is_file():
            print(f"Warning: Not a file: {path_str}", file=sys.stderr)
            continue
        valid_paths.append(path)
    
    if not valid_paths:
        print("No valid image files found.", file=sys.stderr)
        return False
    
    # Get maximum dimensions across all images
    print("Analyzing image dimensions...")
    max_width, max_height = get_max_dimensions(valid_paths)
    
    if max_width == 0 or max_height == 0:
        print("Error: Could not determine image dimensions.", file=sys.stderr)
        return False
    
    print(f"Maximum dimensions: {max_width} x {max_height} pixels")
    
    # Create page size tuple (img2pdf handles pixel to point conversion)
    # Page size: max_width x max_height (tallest x widest)
    page_size = (max_width, max_height)
    
    # Create layout function for img2pdf
    layout_fun = img2pdf.get_layout_fun(pagesize=page_size)
    
    # Generate PDF in output folder
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)  # Create output folder if it doesn't exist
    
    output_path = output_dir / output_name
    print(f"Creating PDF: {output_name}")
    
    try:
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(
                [str(path) for path in valid_paths],
                layout_fun=layout_fun
            ))
        print(f"Successfully created PDF: {output_path.absolute()}")
        return True
    except Exception as e:
        print(f"Error creating PDF: {e}", file=sys.stderr)
        return False


def main():
    print("Image to PDF Converter")
    print("=" * 40)
    
    # Prompt for image paths
    image_paths = []
    print("\nEnter image paths (you can paste multiple paths at once, one per line):")
    print("Example:")
    print('  "C:\\Users\\Username\\Downloads\\image1.png"')
    print('  "C:\\Users\\Username\\Downloads\\image2.jpg"')
    print("\nPaste your paths (press Enter on empty line when done):")
    
    while True:
        try:
            path_input = input().strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        
        if not path_input:
            break
        
        # Remove surrounding quotes if present
        if (path_input.startswith('"') and path_input.endswith('"')) or (path_input.startswith("'") and path_input.endswith("'")):
            path_input = path_input[1:-1]
        
        if path_input:
            image_paths.append(path_input)
    
    if not image_paths:
        print("No image paths provided. Exiting.", file=sys.stderr)
        return
    
    # Prompt for output PDF name
    print(f"\nEnter output PDF name (default: [untitled.pdf]):")
    output_name = input("PDF name: ").strip()
    
    if not output_name:
        output_name = "untitled.pdf"
    elif not output_name.endswith('.pdf'):
        output_name += '.pdf'
    
    print()  # Empty line for spacing
    create_pdf(image_paths, output_name)


if __name__ == "__main__":
    main()

