link to https://ocrmypdf.readthedocs.io/en/latest/batch.html#id1


* My batch check for no text pdfs

python src/pdf_no_txt_convert/find_no_text_pdfs.py "C:\Users\jimsy\OneDrive" -o "C:\Users\jimsy\OneDrive\Desktop\files_to_process.txt"


Explanation of batch_ocrmypdf.py

Based on the code in 

c:\Users\jimsy\github\projects\Ocr_Projects\OCRmyPDF\src\batch_process\batch_ocrmypdf.py, 

here is an explanation of its usage and options.

Purpose

The batch_ocrmypdf.py script is designed to automate the process of running OCR on a large number of PDF files. It recursively scans a specified directory, identifies all PDF files, and then applies OCRmyPDF to each one, modifying them in-place. It includes features for archiving original files and logging the results of its operations.

How to Use the Script

You run the script from your command line terminal, providing the directory to scan as an argument.

Command Syntax

bash

python c:\Users\jimsy\github\projects\Ocr_Projects\OCRmyPDF\src\batch_process\batch_ocrmypdf.py [search_directory] [log_file]

Arguments

[search_directory] (Optional): 

This is the path to the directory you want the script to search for PDFs. The script will scan this directory and all of its subdirectories. If you do not provide this argument, it defaults to the current directory (.).

[log_file] (Optional): 

This is the path to the file where the script will save its log messages. If you do not provide this argument, it defaults to a file named ocr-tree.log located in the same directory as the script itself.
Key Features and Behavior

In-Place Processing: 

The script is hardcoded to modify files in-place. The output file is the same as the input file for the ocrmypdf.ocr() call.

Recursive Search: 

It will find every file with a .pdf extension in the search_directory and all folders within it.

Automatic Deskew: 

The script automatically enables the deskew feature by calling OCRmyPDF with deskew=True. This attempts to correct pages that were scanned at a crooked angle.

Archiving Originals: 

The script has a hardcoded archive directory set to /pdfbak. Before processing a file, it will copy the original version to this archive location. It creates the necessary subdirectory structure to mirror the source.

Note: 

This archive path is absolute and may need to be changed directly in the script if you are not on a Linux-like system or if you want to use a different location.

Logging: 

All actions, including which file is being processed, the result of the OCR, and any errors or skips, are logged to the specified log file.

Skipping Files: 

The script includes logic to skip processing a file under several conditions:

-If the file already claims to be a PDF/A.
-If the file is encrypted.
-If OCRmyPDF detects that the file already has an OCR text layer (PriorOcrFoundError).
-If the file contains a digital signature.
-If the file is a "tagged PDF", which implies it is a structured, born-digital document that does not need OCR.

Example Command

To scan a folder named 

C:\MyScans 

and save the log to 

C:\MyScans\scan_log.txt, 

you would run:

bash
python c:\Users\jimsy\github\projects\Ocr_Projects\OCRmyPDF\src\batch_process\batch_ocrmypdf.py "C:\MyScans" "C:\MyScans\scan_log.txt"

When you run this command, the script will:

Begin logging its actions to C:\MyScans\scan_log.txt.

Search through C:\MyScans and its subfolders for all PDF files.

For each PDF found, it will copy the original to a corresponding path inside /pdfbak.

It will then run OCRmyPDF on the PDF in C:\MyScans, deskewing it and overwriting the original with the new OCR'd version.

If a file is skipped for any reason, a message will be recorded in the log file.
