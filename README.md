# IMG2PDF

A Python script that converts multiple images into a single PDF file with automatic page sizing based on the maximum dimensions across all images.

## Features

- Combine multiple images (PNG, JPG, etc.) into a single PDF
- Automatic page sizing: PDF pages are sized to match the tallest and widest dimensions across all images
- Interactive command-line interface
- Supports pasting multiple image paths at once
- Automatically saves PDFs to an `output` folder

## Requirements

- Python 3.6 or higher
- `img2pdf` library
- `Pillow` library

## Installation

1. Create a virtual environment (if you haven't already):
   ```powershell
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```powershell
   pip install img2pdf Pillow
   ```

## Usage

1. Make sure your virtual environment is activated.

2. Run the script:
   ```powershell
   python main.py
   ```

3. Enter image paths when prompted:
   - You can paste multiple paths at once, one per line
   - Paths can be quoted or unquoted
   - Example:
     ```
     "C:\Users\Username\Downloads\image1.png"
     "C:\Users\Username\Downloads\image2.jpg"
     ```
   - Press Enter on an empty line when you're done entering paths

### Windows Tips for Copying File Paths

**Easy way to get multiple file paths:**
1. In File Explorer, select multiple image files (hold `Ctrl` and click each file, or use `Ctrl+A` to select all)
2. Right-click on the selected files
3. Choose "Copy as path" from the context menu
4. This will copy all file paths to your clipboard, one per line

**Pasting into the terminal:**
- If you see `^V` when trying to paste with `Ctrl+V`, use `Ctrl+Shift+V` instead
- When pasting multiple lines, the terminal may prompt you to confirm pasting multiple lines or on one line - choose to paste on multiple.

4. Enter the output PDF name:
   - Enter a custom name, or press Enter to use the default `untitled.pdf`
   - The `.pdf` extension will be added automatically if you don't include it

5. The PDF will be created in the `output` folder in the current directory.

## Example

```
Image to PDF Converter
========================================

Enter image paths (you can paste multiple paths at once, one per line):
Example:
  "C:\Users\Username\Downloads\image1.png"
  "C:\Users\Username\Downloads\image2.jpg"

Paste your paths (press Enter on empty line when done):
"C:\Users\Username\Pictures\photo1.png"
"C:\Users\Username\Pictures\photo2.jpg"

Enter output PDF name (default: [untitled.pdf]):
PDF name: my_photos

Analyzing image dimensions...
Maximum dimensions: 1920 x 1080 pixels
Creating PDF: [my_photos.pdf]
Successfully created PDF: C:\Projects\IMG2PDF\output\my_photos.pdf
```

## How It Works

1. The script reads all provided image paths
2. Analyzes each image to determine its dimensions
3. Finds the maximum width and maximum height across all images
4. Creates a PDF with page size matching those maximum dimensions
5. Converts all images to PDF pages and saves to the `output` folder

## Notes

- The `output` folder will be created automatically if it doesn't exist
- All images are placed on pages sized to the largest dimensions found
- Invalid or missing image files will be skipped with a warning
- The script preserves image quality during conversion

