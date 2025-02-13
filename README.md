# EasyConvert

This tool was created to fulfill the course requirements for "Software Testing Principles & Techniques" at Harrisburg University of Science and Technology.

EasyConvert is a file conversion tool that allows users to convert various file formats easily. The application supports conversions between formats such as PDF, DOCX, TXT, JPG, PNG, MP4, AVI, MP3, WAV, XLSX, and CSV.

## Features

- Convert PDF to DOCX and vice versa
- Convert TXT files to PDF
- Convert JPG to PNG and vice versa
- Convert TIFF to JPG
- Convert MP4 to AVI and vice versa
- Convert MP3 to WAV and vice versa
- Convert XLSX to CSV and vice versa
- User-friendly interface with drag-and-drop functionality

## Requirements

- Python 3.6 or higher
- Flask
- MoviePy
- Pandas
- Pillow
- Pydub
- pdf2docx
- FPDF (for TXT to PDF conversion)
- docx2pdf (for DOCX to PDF conversion)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/EasyConvert.git
   cd EasyConvert
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   Start the Flask application by running:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and go to `http://127.0.0.1:5000/` to access the EasyConvert interface.

3. **Convert Files**:
   - Drag and drop files into the designated area or use the "Select Files" button to upload files.
   - Select the source format from the dropdown menu.
   - Select the target format from the dropdown menu.
   - Click the "Convert" button to perform the conversion.
   - The converted files will be available for download.

## Possible Conversions

- PDF ↔ DOCX
- TXT → PDF
- JPG ↔ PNG
- TIFF → JPG
- MP4 ↔ AVI
- MP3 ↔ WAV
- XLSX ↔ CSV