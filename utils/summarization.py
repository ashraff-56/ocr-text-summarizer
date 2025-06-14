import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_spicy_summary_gemini(text, model_name=None):
    free_models = [
        'models/gemini-2.0-flash-exp',
        'models/gemini-exp-1206', 
        'models/gemini-exp-1121',
        'models/gemini-1.5-flash',
        'models/gemini-1.5-flash-8b',
        'models/gemini-1.5-pro'
    ]
    
    if model_name:
        free_models.insert(0, model_name)
    
    prompt = f"""
    Read the following text and create a spicy, engaging summary that captures the essence while adding some creative flair.
    Make it punchy, maybe a little sassy, but always accurate to the original content.
    Write it like a viral social media post - attention-grabbing and memorable.

    Text to summarize:
    {text}

    Spicy Summary:
    """
    
    for model_name in free_models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return f"✅ Used: {model_name}\n\n{response.text.strip()}"
        except Exception as e:
            continue
    
    return "❌ Unable to generate summary. All models failed or are unavailable."

def simple_text_summarizer(text, max_sentences=3):
    sentences = text.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) <= max_sentences:
        return text
    
    summary_sentences = []
    if len(sentences) >= 1:
        summary_sentences.append(sentences[0])
    if len(sentences) >= 3:
        summary_sentences.append(sentences[len(sentences)//2])
        summary_sentences.append(sentences[-1])
    elif len(sentences) == 2:
        summary_sentences.append(sentences[1])
    
    return '. '.join(summary_sentences) + '.'