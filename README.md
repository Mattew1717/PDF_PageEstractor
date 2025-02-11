# PDF Page Extractor

This is a Python application that allows users to extract specific pages or page ranges from an existing PDF file and generate a new PDF containing only the selected pages. The tool uses Tkinter for the graphical user interface (GUI), PyQt5 for handling file dialog boxes, and the `fpdf` and `PyPDF4` libraries to manipulate PDF files.

## How to Use

1. Run the script.
2. Click the **"Choose PDF"** button to select the PDF file you want to extract pages from.
3. Enter the pages you want to extract, separated by commas. For page ranges, use a hyphen (e.g., `12-15,17,20-25`).
4. Choose a directory where the new PDF will be saved.
5. The new PDF will be generated and saved in the selected directory.

## Example Usage

- Input: `12,13,14,15-20,19,40-60`
- This will extract pages 12, 13, 14, pages 15 to 20, page 19 again, and pages 40 to 60 from the original PDF.

## Requirements

To run this script, you need to install the following libraries:

```bash
pip install tkinter PyQt5 fpdf PyPDF4
