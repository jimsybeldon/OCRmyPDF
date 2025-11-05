a very useful command line in bash:


python "c:\Users\jimsy\github\projects\Ocr_Projects\OCRmyPDF\src\batch_process\batch_ocrmypdf.py" "C:\Users\jimsy\OneDrive" "c:\Users\jimsy\github\projects\Ocr_Projects\OCRmyPDF\scan_log.txt"





Purpose
The find_no_text_pdfs.py script is a utility designed to recursively scan a specified directory for PDF files. It analyzes each PDF to determine if it contains an extractable text layer. PDFs that lack a text layer (typically scanned image-based documents) are identified as "non-searchable" and are listed in an output file. This is useful for creating a batch list of files that need to be processed by an OCR application like OCRmyPDF.

How to Use the Script
You can run the script from your command line terminal.

Command Syntax
```bash
python find_no_text_pdfs.py <search_directory> [options]
```
Arguments and Options
search_directory (Required): This is the full path to the directory you want the script to search for PDFs. The script will scan this directory and all of its subdirectories.
-o, --output-file <output_file> (Optional): Use this to specify a name for the output file that will contain the list of PDFs needing OCR. If you omit this option, the script will create a file named files_to_ocr.txt by default.
Example Command
```bash
python find_no_text_pdfs.py "C:\MyDocuments\Scans" -o "files_to_process.txt"
```
When you run this command, the script will:

Scan the C:\MyDocuments\Scans folder and all its subfolders for any file ending with .pdf.
Check each PDF to see if it contains text.
Print the names of the files that are found to have no text to the console.
Save the list of these files into files_to_process.txt.
Where to Find the Results
The script generates two forms of output:

Console Output: As the script runs, it will print messages to your terminal. It will first indicate how many PDFs it found and then list each PDF that it determines needs OCR processing.

```plaintext
Scanning for PDF files in 'C:\MyDocuments\Scans'...
Found 5 PDF files. Checking for text layers...
  -> Found for processing: Scans\meeting_notes.pdf
  -> Found for processing: Scans\receipts\invoice_123.pdf

Found 2 PDFs without a text layer.
List of files to process has been saved to 'files_to_process.txt'
```
Output File: The main result is a text file (e.g., files_to_ocr.txt or whatever you specified with the -o flag). This file will be created in the directory from which you ran the script.

Location: The current working directory of your terminal.
Content: The file contains a list of the paths to the PDFs that do not have a text layer, with one file path per line. The paths are relative to the parent of the search directory.
Example content of files_to_process.txt:

```plaintext
Scans\meeting_notes.pdf
Scans\receipts\invoice_123.pdf
```
This output file can then be used as an input for a batch processing script to run OCR on all the identified files.
