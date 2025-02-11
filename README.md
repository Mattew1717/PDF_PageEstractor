# PDF Page Extractor

This is a Python application that allows users to extract specific pages or page ranges from an existing PDF file and generate a new PDF containing only the selected pages. The tool uses Tkinter for the graphical user interface (GUI), PyQt5 for handling file dialog boxes, and the `fpdf` and `PyPDF4` libraries to manipulate PDF files.

## Features

- **Select a PDF file**: Use a file dialog to choose the PDF you want to extract pages from.
- **Choose specific pages**: Enter a list of pages you want to extract. You can specify individual pages (e.g., `12, 13, 14`) or ranges (e.g., `15-20`).
- **Save the new PDF**: After selecting the pages, you can choose where to save the newly created PDF file.
- **Error handling**: If the user enters invalid page numbers or there are other issues, appropriate error messages will be displayed.

## Libraries Used

- **Tkinter**: For the graphical user interface and file selection dialogs.
- **PyQt5**: For additional file dialog support.
- **FPDF**: For generating the new PDF file.
- **PyPDF4**: For reading and extracting specific pages from the existing PDF.

## How to Use

1. Run the script.
2. Click the **"Choose PDF"** button to select the PDF file you want to extract pages from.
3. Enter the pages you want to extract, separated by commas. For page ranges, use a hyphen (e.g., `12-15,17,20-25`).
4. Choose a directory where the new PDF will be saved.
5. The new PDF will be generated and saved in the selected directory.

## Example Usage

- Input: `12,13,14,15-20,19,40-60`
- This will extract pages 12, 13, 14, pages 15 to 20, page 19 again, and pages 40 to 60 from the original PDF.

## Error Handling

If you enter invalid data (e.g., non-existent pages, incorrect formatting), the program will display an error message.

## Requirements

To run this script, you need to install the following libraries:

```bash
pip install tkinter PyQt5 fpdf PyPDF4
