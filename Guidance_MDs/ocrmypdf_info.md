ocr info[https://ocrmypdf.readthedocs.io/en/latest/introduction.html]


Based on the examples in the documentation you've provided, the input.pdf file should be placed in the current working directory—that is, the directory you are in when you run the ocrmypdf command from your terminal.

Let's break down why:

For Standard Command-Line Use
When you run a command like:

bash
ocrmypdf input.pdf output.pdf
You are using a relative path. The command line looks for input.pdf in the directory you are currently in.

If your file were located somewhere else, you would need to provide the path to it.

Relative Path Example: If input.pdf is in a subdirectory named scans, you would run:

bash
ocrmypdf scans/input.pdf output.pdf
Absolute Path Example (Windows):

bash
ocrmypdf "C:\Users\jimsy\Documents\scans\input.pdf" "C:\Users\jimsy\Documents\output.pdf"
For Docker Use
The Docker examples in your documentation often use a volume mount like -v "$PWD:/data".

bash
docker run --rm -v "$PWD:/data" jbarlow83/ocrmypdf-alpine /data/input.pdf /data/output.pdf
Here's what that command does:

-v "$PWD:/data" maps your current working directory (represented by $PWD on Linux/macOS or %CD% on Windows) on your computer to a folder named /data inside the Docker container.
The command then tells OCRmyPDF (running inside the container) to look for /data/input.pdf.
So, even in this Docker example, input.pdf must be in the current working directory on your machine from where you are running the docker command.

In short, for all the examples you've referenced, the simplest approach is to navigate to the directory containing your input.pdf file and run the ocrmypdf command from there.
