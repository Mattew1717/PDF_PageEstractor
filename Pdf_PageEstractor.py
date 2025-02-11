import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from fpdf import FPDF
from PyPDF4 import PdfFileReader, PdfFileWriter

# Function to choose PDF file and extract selected pages
def choosePDF():
    file_path = filedialog.askopenfilename(title="Select PDF file", filetypes=[("PDF files", "*.pdf")])
    numbers = simpledialog.askstring("Enter pages to extract", prompt="Enter pages separated by commas (e.g., 12,13,14,15-20)")
    messagebox.showinfo(title="Great!", message="Now, choose where to save the new PDF")
    filedir = filedialog.askdirectory(title="Select save location")
    genPDF(file_path, filedir, numbers)

# Function to generate new PDF with selected pages
def genPDF(file_path, filedir, numbers):
    try:
        pdf = FPDF()
        pdf.set_auto_page_break(0)
        num = numbers.split(",")
        selected_pages = []

        for n in num:
            if "-" not in n:
                selected_pages.append(int(n))
            else:
                start, end = map(int, n.split("-"))
                selected_pages.extend(range(start, end + 1))

        reader = PdfFileReader(file_path)
        writer = PdfFileWriter()

        for page in selected_pages:
            try:
                writer.addPage(reader.getPage(page - 1))
            except IndexError:
                print(f"Page {page} is out of range.")

        with open(f"{filedir}/NewPDF.pdf", "wb") as out:
            writer.write(out)

        messagebox.showinfo(title="Done", message=f"New PDF saved in {filedir}")
    
    except Exception:
        messagebox.showinfo(title="Error", message="Something went wrong. Please check your input.")

# Main program to run the GUI
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("400x200")
    window.title("PDF Page Extractor")

    # Center window on screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - 200
    y = (screen_height // 2) - 100
    window.geometry(f"+{x}+{y}")

    button = tk.Button(window, text="Choose PDF", command=choosePDF, width=40, height=3, bg='#0052cc', fg='#ffffff', activebackground='#0052cc', activeforeground='#aaffaa')
    button.pack()

    window.mainloop()
