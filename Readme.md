
# **OCR Text Summarizer**

A **Streamlit** web application for extracting text from images using **EasyOCR** and generating engaging summaries with **Google Gemini** or a rule-based approach.

---

## 🚀 Features
- Extract text from images (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`) using **EasyOCR**
- Enhance image quality with **OpenCV** for improved OCR accuracy
- Generate AI-powered summaries with **Google Gemini** or simple rule-based summaries
- Display OCR analysis with confidence scores and text blocks
- Download extracted text and summaries

---

## 📁 Project Structure
```plaintext

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
```

---

## ⚙️ Setup

### Clone the Repository
```bash
git clone https://github.com/ashraff-56/ocr-text-summarizer.git
cd ocr-text-summarizer
```



### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure API Key
Create `ocr_text_summarizer/.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

### Run Locally
```bash
streamlit run app.py
```

---

## 🌐 Deployment
1. Push the repository to GitHub.
2. Sign in to Streamlit Cloud with GitHub.
3. Create a new app, selecting the repository, main branch, and `app.py`.
4. Add `GEMINI_API_KEY` to Streamlit secrets.
5. Deploy and access the app via the provided URL.

---

## 📦 Dependencies
- `streamlit`
- `opencv-python-headless`
- `easyocr`
- `numpy`
- `google-generativeai`

See `requirements.txt` for details.

---

## 📝 Notes
- Use clear, high-contrast images for optimal OCR results.
- Ensure a valid Google Gemini API key is set in secrets.
- The app supports both AI-powered and rule-based summarization.
