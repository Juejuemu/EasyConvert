from pdf2docx import Converter
from PIL import Image
import os
from moviepy import *
import pydub
import pandas as pd

# Create a directory for converted files if it doesn't exist
os.makedirs('converted_files', exist_ok=True)

def convert_pdf_to_docx(pdf_file):
    """Convert PDF to DOCX."""
    try:
        pdf_path = f'temp_{pdf_file.filename}'
        pdf_file.save(pdf_path)
        docx_file = os.path.join('converted_files', pdf_path.replace('.pdf', '.docx'))
        
        cv = Converter(pdf_path)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        
        os.remove(pdf_path)
        return docx_file
    except Exception as e:
        return str(e)

def convert_txt_to_pdf(txt_file):
    """Convert TXT to PDF."""
    try:
        txt_path = f'temp_{txt_file.filename}'
        txt_file.save(txt_path)
        pdf_file = os.path.join('converted_files', txt_path.replace('.txt', '.pdf'))
        
        from fpdf import FPDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        with open(txt_path, 'r') as f:
            for line in f:
                pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(pdf_file)
        
        os.remove(txt_path)
        return pdf_file
    except Exception as e:
        return str(e)

def convert_jpg_to_png(jpg_file):
    """Convert JPG to PNG."""
    try:
        jpg_path = f'temp_{jpg_file.filename}'
        jpg_file.save(jpg_path)
        png_file = os.path.join('converted_files', jpg_path.replace('.jpg', '.png'))
        
        img = Image.open(jpg_path)
        img.save(png_file, 'PNG')
        
        os.remove(jpg_path)
        return png_file
    except Exception as e:
        return str(e)

def convert_avi_to_mp4(video_file):
    """Convert AVI to MP4."""
    try:
        video_path = f'temp_{video_file.filename}'
        video_file.save(video_path)
        mp4_file = os.path.join('converted_files', video_path.replace('.avi', '.mp4'))
        
        clip = VideoFileClip(video_path)
        clip.write_videofile(mp4_file, codec='libx264')
        
        os.remove(video_path)
        return mp4_file
    except Exception as e:
        return str(e)

def convert_wav_to_mp3(audio_file):
    """Convert WAV to MP3."""
    try:
        audio_path = f'temp_{audio_file.filename}'
        audio_file.save(audio_path)
        mp3_file = os.path.join('converted_files', audio_path.replace('.wav', '.mp3'))
        
        sound = pydub.AudioSegment.from_wav(audio_path)
        sound.export(mp3_file, format='mp3')
        
        os.remove(audio_path)
        return mp3_file
    except Exception as e:
        return str(e)

def convert_xlsx_to_csv(xlsx_file):
    """Convert XLSX to CSV."""
    try:
        xlsx_path = f'temp_{xlsx_file.filename}'
        xlsx_file.save(xlsx_path)
        csv_file = os.path.join('converted_files', xlsx_path.replace('.xlsx', '.csv'))
        
        df = pd.read_excel(xlsx_path)
        df.to_csv(csv_file, index=False)
        
        os.remove(xlsx_path)
        return csv_file
    except Exception as e:
        return str(e)

def convert_csv_to_xlsx(csv_file):
    """Convert CSV to XLSX."""
    try:
        csv_path = f'temp_{csv_file.filename}'
        csv_file.save(csv_path)
        xlsx_file = os.path.join('converted_files', csv_path.replace('.csv', '.xlsx'))
        
        df = pd.read_csv(csv_path)
        df.to_excel(xlsx_file, index=False)
        
        os.remove(csv_path)
        return xlsx_file
    except Exception as e:
        return str(e)

def convert_files(files, source_format, target_format):
    """Convert files based on source and target formats."""
    converted_files = []
    for file in files:
        if source_format == 'pdf' and target_format == 'docx' and file.filename.endswith('.pdf'):
            result = convert_pdf_to_docx(file)
            converted_files.append(result)
        elif source_format == 'txt' and target_format == 'pdf' and file.filename.endswith('.txt'):
            result = convert_txt_to_pdf(file)
            converted_files.append(result)
        elif source_format == 'jpg' and target_format == 'png' and file.filename.endswith('.jpg'):
            result = convert_jpg_to_png(file)
            converted_files.append(result)
        elif source_format == 'avi' and target_format == 'mp4' and file.filename.endswith('.avi'):
            result = convert_avi_to_mp4(file)
            converted_files.append(result)
        elif source_format == 'wav' and target_format == 'mp3' and file.filename.endswith('.wav'):
            result = convert_wav_to_mp3(file)
            converted_files.append(result)
        elif source_format == 'xlsx' and target_format == 'csv' and file.filename.endswith('.xlsx'):
            result = convert_xlsx_to_csv(file)
            converted_files.append(result)
        elif source_format == 'csv' and target_format == 'xlsx' and file.filename.endswith('.csv'):
            result = convert_csv_to_xlsx(file)
            converted_files.append(result)
        else:
            converted_files.append(f"Unsupported conversion from {source_format} to {target_format} for {file.filename}.")
    return converted_files 