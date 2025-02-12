from pdf2docx import Converter
from PIL import Image
import os
import pandas as pd
from moviepy import *
import wave
import pydub

# Create a directory for converted files if it doesn't exist
os.makedirs('converted_files', exist_ok=True)

def convert_pdf_to_docx(pdf_file):
    try:
        # Save the uploaded PDF file temporarily
        pdf_path = f'temp_{pdf_file.filename}'
        pdf_file.save(pdf_path)

        # Convert PDF to DOCX
        docx_file = os.path.join('converted_files', pdf_path.replace('.pdf', '.docx'))
        cv = Converter(pdf_path)
        cv.convert(docx_file, start=0, end=None)
        cv.close()

        # Clean up the temporary PDF file
        os.remove(pdf_path)
        return docx_file
    except Exception as e:
        return str(e)  # Return the error message

def convert_txt_to_pdf(txt_file):
    try:
        txt_path = f'temp_{txt_file.filename}'
        txt_file.save(txt_path)
        pdf_file = os.path.join('converted_files', txt_path.replace('.txt', '.pdf'))
        # Use a library like FPDF or ReportLab to create a PDF from TXT
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
    try:
        # Save the uploaded JPG file temporarily
        jpg_path = f'temp_{jpg_file.filename}'
        jpg_file.save(jpg_path)

        # Convert JPG to PNG
        png_file = os.path.join('converted_files', jpg_path.replace('.jpg', '.png'))
        img = Image.open(jpg_path)
        img.save(png_file, 'PNG')

        # Clean up the temporary JPG file
        os.remove(jpg_path)
        return png_file
    except Exception as e:
        return str(e)  # Return the error message

def convert_tiff_to_jpg(tiff_file):
    try:
        tiff_path = f'temp_{tiff_file.filename}'
        tiff_file.save(tiff_path)
        jpg_file = os.path.join('converted_files', tiff_path.replace('.tiff', '.jpg'))
        img = Image.open(tiff_path)
        img.save(jpg_file, 'JPEG')
        os.remove(tiff_path)
        return jpg_file
    except Exception as e:
        return str(e)

def convert_mp4_to_avi(video_file):
    try:
        video_path = f'temp_{video_file.filename}'
        video_file.save(video_path)
        avi_file = os.path.join('converted_files', video_path.replace('.mp4', '.avi'))
        clip = VideoFileClip(video_path)
        clip.write_videofile(avi_file)
        os.remove(video_path)
        return avi_file
    except Exception as e:
        return str(e)

def convert_mp3_to_wav(audio_file):
    try:
        audio_path = f'temp_{audio_file.filename}'
        audio_file.save(audio_path)
        wav_file = os.path.join('converted_files', audio_path.replace('.mp3', '.wav'))
        sound = pydub.AudioSegment.from_mp3(audio_path)
        sound.export(wav_file, format="wav")
        os.remove(audio_path)
        return wav_file
    except Exception as e:
        return str(e)

def convert_xlsx_to_csv(spreadsheet_file):
    try:
        xlsx_path = f'temp_{spreadsheet_file.filename}'
        spreadsheet_file.save(xlsx_path)
        print(f"Saving temporary file: {xlsx_path}")

        csv_file = os.path.join('converted_files', xlsx_path.replace('.xlsx', '.csv'))
        df = pd.read_excel(xlsx_path)
        df.to_csv(csv_file, index=False)
        print(f"Converted to CSV: {csv_file}")

        os.remove(xlsx_path)
        return csv_file
    except Exception as e:
        print(f"Error converting XLSX to CSV: {e}")
        return str(e)

def convert_docx_to_pdf(docx_file):
    try:
        docx_path = f'temp_{docx_file.filename}'
        docx_file.save(docx_path)
        pdf_file = os.path.join('converted_files', docx_path.replace('.docx', '.pdf'))
        
        from docx2pdf import convert
        convert(docx_path, pdf_file)
        
        os.remove(docx_path)
        return pdf_file
    except Exception as e:
        return str(e)

def convert_png_to_jpg(png_file):
    try:
        png_path = f'temp_{png_file.filename}'
        png_file.save(png_path)
        jpg_file = os.path.join('converted_files', png_path.replace('.png', '.jpg'))
        
        img = Image.open(png_path)
        img.convert('RGB').save(jpg_file, 'JPEG')  # Convert to RGB before saving as JPG
        
        os.remove(png_path)
        return jpg_file
    except Exception as e:
        return str(e)

def convert_files(files, source_format, target_format):
    converted_files = []
    for file in files:
        if source_format == 'pdf' and target_format == 'docx' and file.filename.endswith('.pdf'):
            result = convert_pdf_to_docx(file)
            converted_files.append(result)
        elif source_format == 'docx' and target_format == 'pdf' and file.filename.endswith('.docx'):
            result = convert_docx_to_pdf(file)
            converted_files.append(result)
        elif source_format == 'txt' and target_format == 'pdf' and file.filename.endswith('.txt'):
            result = convert_txt_to_pdf(file)
            converted_files.append(result)
        elif source_format == 'jpg' and target_format == 'png' and file.filename.endswith('.jpg'):
            result = convert_jpg_to_png(file)
            converted_files.append(result)
        elif source_format == 'png' and target_format == 'jpg' and file.filename.endswith('.png'):
            result = convert_png_to_jpg(file)
            converted_files.append(result)
        elif source_format == 'tiff' and target_format == 'jpg' and file.filename.endswith('.tiff'):
            result = convert_tiff_to_jpg(file)
            converted_files.append(result)
        elif source_format == 'mp4' and target_format == 'avi' and file.filename.endswith('.mp4'):
            result = convert_mp4_to_avi(file)
            converted_files.append(result)
        elif source_format == 'avi' and target_format == 'mp4' and file.filename.endswith('.avi'):
            result = convert_avi_to_mp4(file)
            converted_files.append(result)
        elif source_format == 'mp3' and target_format == 'wav' and file.filename.endswith('.mp3'):
            result = convert_mp3_to_wav(file)
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

def convert_avi_to_mp4(avi_file):
    try:
        avi_path = f'temp_{avi_file.filename}'
        avi_file.save(avi_path)
        mp4_file = os.path.join('converted_files', avi_path.replace('.avi', '.mp4'))
        
        clip = VideoFileClip(avi_path)
        clip.write_videofile(mp4_file, codec='libx264')
        
        os.remove(avi_path)
        return mp4_file
    except Exception as e:
        return str(e)

def convert_wav_to_mp3(wav_file):
    try:
        wav_path = f'temp_{wav_file.filename}'
        wav_file.save(wav_path)
        mp3_file = os.path.join('converted_files', wav_path.replace('.wav', '.mp3'))
        
        sound = pydub.AudioSegment.from_wav(wav_path)
        sound.export(mp3_file, format='mp3')
        
        os.remove(wav_path)
        return mp3_file
    except Exception as e:
        return str(e)

def convert_csv_to_xlsx(csv_file):
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

# Additional conversion functions can be added here 