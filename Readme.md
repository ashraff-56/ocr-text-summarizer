OCR Text Summarizer

A Streamlit app that extracts text from images using EasyOCR and generates vibrant summaries with Google Gemini or a rule-based approach.
✨ Features

📸 Extract text from images (PNG, JPG, JPEG, BMP, TIFF)
🖌️ Enhance images with OpenCV for better OCR accuracy
🤖 Generate AI-powered summaries with Google Gemini
📝 Create concise rule-based summaries
📊 View OCR analysis with confidence scores
💾 Download extracted text and summaries

📂 Project Structure

├──ocr_text_summarizer/
    ├── app.py
    ├── config.py
    ├── utils/
    │   ├── image_processing.py
    │   ├── summarization.py
    │   └── model_utils.py
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    └── .streamlit/
        └── secrets.toml

🚀 Setup

Clone Repository:
git clone https://github.com/ashraff-56/ocr-text-summarizer.git
cd ocr-text-summarizer


Set Up Virtual Environment:
python -m venv ../myenv
source ../myenv/bin/activate  # Windows: ..\myenv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Configure API Key:

Create .streamlit/secrets.toml:GEMINI_API_KEY = "your-gemini-api-key"




Run Locally:
streamlit run app.py




🛠️ Dependencies

streamlit==1.29.0
opencv-python==4.8.1
easyocr==1.7.1
numpy==1.26.2
google-generativeai==0.8.1

See requirements.txt for details.
📋 Notes

Use high-contrast images for best OCR results.
Ensure a valid Gemini API key in secrets.


