import os
from pathlib import Path
import argparse
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFSyntaxError

def has_text(pdf_path: Path) -> bool:
    """
    Checks if a PDF file contains any extractable text.

    Args:
        pdf_path: The path to the PDF file.

    Returns:
        True if the PDF contains text, False otherwise.
    """
    try:
        # Extract text from the first page only for efficiency.
        # If the first page has no text, it's a strong indicator
        # that the document is a scanned image.
        text = extract_text(pdf_path, page_numbers=[0], maxpages=1)
        # Consider it text-less if the extracted text is empty or just whitespace
        return text.strip() != ""
    except PDFSyntaxError:
        print(f"Warning: Could not parse '{pdf_path}'. Skipping.")
        return False # Treat unparseable PDFs as not having text for safety
    except Exception as e:
        print(f"An unexpected error occurred with '{pdf_path}': {e}")
        return False

def find_pdfs_without_text(root_dir: Path) -> list[Path]:
    """
    Recursively finds all PDF files in a directory that do not have a text layer.

    Args:
        root_dir: The root directory to start the search from.

    Returns:
        A list of Path objects for PDF files that need OCR.
    """
    pdfs_to_process = []
    print(f"Scanning for PDF files in '{root_dir}'...")

    # Use rglob for recursive search
    all_pdfs = sorted(list(root_dir.rglob("*.pdf")))
    
    if not all_pdfs:
        print("No PDF files found.")
        return []

    print(f"Found {len(all_pdfs)} PDF files. Checking for text layers...")

    for pdf_path in all_pdfs:
        if not has_text(pdf_path):
            print(f"  -> Found for processing: {pdf_path.relative_to(root_dir)}")
            pdfs_to_process.append(pdf_path)

    return pdfs_to_process

def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Find non-searchable (no text layer) PDFs in a directory and its subdirectories."
    )
    parser.add_argument(
        "search_directory",
        type=str,
        help="The directory to search for PDFs recursively."
    )
    parser.add_argument(
        "-o", "--output-file",
        type=str,
        default="files_to_ocr.txt",
        help="The file to save the list of PDFs that need OCR. (Default: files_to_ocr.txt)"
    )
    args = parser.parse_args()

    search_path = Path(args.search_directory)
    output_path = Path(args.output_file)

    if not search_path.is_dir():
        print(f"Error: The specified directory does not exist: '{search_path}'")
        return

    pdfs_needing_ocr = find_pdfs_without_text(search_path)

    if pdfs_needing_ocr:
        print(f"\nFound {len(pdfs_needing_ocr)} PDFs without a text layer.")
        with open(output_path, "w", encoding="utf-8") as f:
            for pdf_path in pdfs_needing_ocr:
                # Write the relative path to the output file
                f.write(str(pdf_path.relative_to(search_path.parent)) + "\n")
        print(f"List of files to process has been saved to '{output_path}'")
    else:
        print("\nNo PDFs requiring OCR were found.")

if __name__ == "__main__":
    main()
