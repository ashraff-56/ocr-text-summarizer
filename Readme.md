OCR Text Summarizer
A Streamlit web application for extracting text from images using EasyOCR and generating engaging summaries with Google Gemini or a rule-based approach.
Features

Extract text from images (PNG, JPG, JPEG, BMP, TIFF) using EasyOCR
Enhance image quality with OpenCV for improved OCR accuracy
Generate AI-powered summaries with Google Gemini or simple rule-based summaries
Display OCR analysis with confidence scores and text blocks
Download extracted text and summaries

Project Structure
├── ocr_text_summarizer/
│   ├── app.py
│   ├── config.py
│   ├── utils/
│   │   ├── image_processing.py
│   │   ├── summarization.py
│   │   └── model_utils.py
│   ├── requirements.txt
│   ├── .gitignore
│   ├── README.md
│   ├── .streamlit/
│   │   └── secrets.toml

Setup

Clone the Repository:
git clone https://github.com/ashraff-56/ocr-text-summarizer.git
cd ocr-text-summarizer


Set Up Virtual Environment:
python -m venv ../myenv
source ../myenv/bin/activate  # Windows: ..\myenv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Configure API Key:

Create ocr_text_summarizer/.streamlit/secrets.toml:
GEMINI_API_KEY = "your-gemini-api-key"




Run Locally:
streamlit run app.py





Dependencies

streamlit==1.29.0
opencv-python==4.8.1
easyocr==1.7.1
numpy==1.26.2
google-generativeai==0.8.1

See requirements.txt for details.
Notes

Use clear, high-contrast images for optimal OCR results.
Ensure a valid Google Gemini API key is set in secrets.


