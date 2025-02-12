from flask import Flask, request, jsonify, render_template
from conversion import convert_files, convert_jpg_to_png, convert_pdf_to_docx  # Import the conversion functions
# other imports...

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    files = request.files.getlist('file')  # Get multiple files
    source_format = request.form.get('sourceFormat')
    target_format = request.form.get('targetFormat')

    if not files:
        return jsonify({"error": "No files provided"}), 400

    converted_files = convert_files(files, source_format, target_format)

    return jsonify({"message": "Files converted successfully!", "files": converted_files}), 200

if __name__ == '__main__':
    app.run(debug=True)
