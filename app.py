import streamlit as st
import cv2
import numpy as np
import time
from utils.image_processing import preprocess_image_opencv, extract_text_with_easyocr
from utils.summarization import generate_spicy_summary_gemini, simple_text_summarizer
from utils.model_utils import list_available_models
from config import GEMINI_API_KEY, set_page_config

def main():
    set_page_config()

    st.title("🔥 OCR Text Summarizer")
    st.markdown("**Upload a text-based image and get a spicy, AI-powered summary!**")
    
    with st.sidebar:
        st.header("⚙️ Options")
        enhance_image = st.checkbox(
            "✨ Enhance Image Quality", 
            value=True,
            help="Apply image enhancement for better OCR results"
        )
        summary_length = st.slider(
            "📝 Summary Length (sentences)",
            min_value=1,
            max_value=5,
            value=3,
            help="Number of sentences for rule-based summary"
        )
        st.markdown("---")
        st.markdown("**💡 Tips:**")
        st.markdown("• Use clear, high-contrast images")
        st.markdown("• Ensure text is readable")
        st.markdown("• Try both summary methods")
    
    with st.expander("🔍 Check Available Models"):
        if st.button("List Available Models"):
            with st.spinner("Fetching available models..."):
                models = list_available_models()
                if models:
                    st.success("Available Models:")
                    for model in models:
                        st.write(f"• {model}")
                else:
                    st.warning("No models found or error occurred")

    st.subheader("📤 Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image", 
        type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'],
        help="Supported formats: PNG, JPG, JPEG, BMP, TIFF"
    )

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.subheader("🖼️ Original Image")
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            st.image(image_rgb, caption="Uploaded Image", use_column_width=True)
            height, width = image.shape[:2]
            st.info(f"📏 Image Size: {width} × {height} pixels")
        
        with col2:
            st.subheader("🎯 Summary Method")
            summary_method = st.radio(
                "Choose Summary Method:",
                ["AI-Powered (Gemini)", "Simple Rule-Based"],
                help="AI-Powered uses Google's Gemini models, Simple uses basic text extraction"
            )

        if st.button("🚀 Process Image", type="primary"):
            try:
                progress_col1, progress_col2 = st.columns([3, 1])
                with progress_col1:
                    progress_bar = st.progress(0)
                with progress_col2:
                    status_text = st.empty()
                
                status_text.text("🔍 Extracting text...")
                progress_bar.progress(30)
                extracted_text, results, processed_image = extract_text_with_easyocr(
                    image, 
                    enhance_quality=enhance_image
                )
                progress_bar.progress(60)
                
                if extracted_text:
                    status_text.text("🤖 Generating summary...")
                    progress_bar.progress(90)
                    if summary_method == "AI-Powered (Gemini)":
                        summary = generate_spicy_summary_gemini(extracted_text)
                    else:
                        summary = f"📝 Simple Summary:\n\n{simple_text_summarizer(extracted_text, max_sentences=summary_length)}"
                    
                    progress_bar.progress(100)
                    status_text.text("✅ Complete!")
                    time.sleep(1)
                    progress_bar.empty()
                    status_text.empty()
                    
                    st.success("🎉 Processing completed successfully!")
                    tab1, tab2, tab3 = st.tabs(["📝 Results", "🖼️ Processed Image", "📊 Details"])
                    
                    with tab1:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.subheader("📄 Extracted Text")
                            st.text_area("", value=extracted_text, height=300, key="original_text")
                            st.download_button(
                                label="📄 Download Text",
                                data=extracted_text,
                                file_name="extracted_text.txt",
                                mime="text/plain"
                            )
                        with col2:
                            st.subheader("🔥 Generated Summary")
                            st.text_area("", value=summary, height=300, key="summary_text")
                            st.download_button(
                                label="🔥 Download Summary",
                                data=summary,
                                file_name="text_summary.txt",
                                mime="text/plain"
                            )
                    
                    with tab2:
                        st.subheader("🖼️ Enhanced Image (used for OCR)")
                        st.image(processed_image, caption="Processed Image", use_column_width=True, channels="GRAY")
                        st.info("This is the enhanced version of your image that was used for text extraction.")
                    
                    with tab3:
                        st.subheader("📊 OCR Analysis")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("📝 Words Detected", len(extracted_text.split()))
                        with col2:
                            st.metric("🔍 Text Blocks", len(results))
                        with col3:
                            if results:
                                avg_confidence = np.mean([conf for _, _, conf in results])
                                st.metric("📈 Avg Confidence", f"{avg_confidence:.1%}")
                        if results:
                            st.subheader("🔍 Detailed OCR Results")
                            for i, (bbox, text, confidence) in enumerate(results):
                                confidence_color = "🟢" if confidence > 0.8 else "🟡" if confidence > 0.5 else "🔴"
                                st.write(f"{confidence_color} **{confidence:.1%}** - {text}")
                
                else:
                    progress_bar.empty()
                    status_text.empty()
                    st.error("❌ No text extracted from the image. Try with a clearer image containing text.")
                    st.subheader("🔍 Processed Image (for debugging)")
                    st.image(processed_image, caption="Enhanced Image", channels="GRAY")
                    st.info("💡 **Tips to improve results:**\n- Use images with clear, readable text\n- Ensure good contrast between text and background\n- Try enabling 'Enhance Image Quality' option")

            except Exception as e:
                st.error(f"❌ An error occurred during processing: {e}")
                st.info("💡 Try using the 'Simple Rule-Based' summary method as a backup.")

    st.markdown("---")
    st.markdown("**🔥 OCR Text Summarizer** - Powered by OpenCV, EasyOCR, and Google Gemini")

if __name__ == "__main__":
    main()