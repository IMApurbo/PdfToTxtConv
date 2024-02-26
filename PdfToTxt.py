import tkinter as tk
from tkinter import filedialog
import PyPDF2
import os


def select_file():
    pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, pdf_file_path)

def select_output_location():
    output_location = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if output_location:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_location)

def convert_pdf_to_text():
    pdf_file_path = file_entry.get()
    if not pdf_file_path:
        status_label.config(text="Please select a PDF file.")
        return
    
    try:
        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            text = ""
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
            output_location = output_entry.get()
            if not output_location:
                status_label.config(text="Please select an output file location.")
                return
            with open(output_location, "w") as output_file:
                output_file.write(text)
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)
            status_label.config(text="PDF converted to text successfully!")
    except Exception as e:
        status_label.config(text=f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("PDF to Text Converter")
root.geometry("800x500+500+0")

# Create label for title
label = tk.Label(root, text="KORISHEE THE CYBERMASTER", font=("Comic Sans MS", 18 , "bold"))
label.grid(row=0, column=0, columnspan=5, pady=10, sticky="nsew")  # Center vertically and horizontally

# Create label and entry for file selection
file_label = tk.Label(root, text="Select PDF File:",fg="red")
file_label.grid(row=1, column=0, padx=10, pady=10)

file_entry = tk.Entry(root, width=50,fg="blue")
file_entry.grid(row=1, column=1, padx=10, pady=10)

file_button = tk.Button(root, text="Browse", command=select_file,fg="green")
file_button.grid(row=1, column=2, padx=10, pady=10)

# Create label and entry for output file location
output_label = tk.Label(root, text="Select Output Location:",fg="red")
output_label.grid(row=2, column=0, padx=10, pady=10)

output_entry = tk.Entry(root, width=50,fg="blue")
output_entry.grid(row=2, column=1, padx=10, pady=10)

output_button = tk.Button(root, text="Browse", command=select_output_location,fg="green")
output_button.grid(row=2, column=2, padx=10, pady=10)

# Create text box to display converted text
text_box = tk.Text(root, wrap="word", height=20, width=50,fg="green")
text_box.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Add scrollbar to text box
scrollbar = tk.Scrollbar(root, command=text_box.yview)
scrollbar.grid(row=3, column=3, sticky="ns")
text_box.config(yscrollcommand=scrollbar.set)

# Create button to convert PDF to text
convert_button = tk.Button(root, text="Convert PDF to Text", command=convert_pdf_to_text,fg="green")
convert_button.grid(row=4, column=0, columnspan=3, pady=10)

# Create label to display status
status_label = tk.Label(root, text="",fg="red")
status_label.grid(row=5, column=0, columnspan=3)

# Configure grid row and column weights
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)

# Start the main event loop
root.mainloop()
