import streamlit as st
import speech_recognition as sr
import tempfile
import wave

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Voice to Text Converter",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Voice-to-Text Converter")
st.write("Upload a WAV audio file to convert speech into text.")

recognizer = sr.Recognizer()

# ---------------- FILE UPLOADER ----------------
audio_file = st.file_uploader(
    "Upload WAV audio file",
    type=["wav"]
)

# ---------------- WAV VALIDATION ----------------
def is_valid_wav(path):
    try:
        with wave.open(path, 'rb'):
            return True
    except:
        return False

# ---------------- MAIN LOGIC ----------------
if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.read())
        audio_path = tmp.name

    if not is_valid_wav(audio_path):
        st.error("❌ Invalid WAV file. Please upload a valid WAV audio.")
    else:
        with st.spinner("🔍 Transcribing audio..."):
            with sr.AudioFile(audio_path) as source:
                audio_data = recognizer.record(source)

            try:
                transcript = recognizer.recognize_google(audio_data)
                st.success("✅ Transcription completed!")
            except sr.UnknownValueError:
                st.error("❌ Could not understand the audio.")
                transcript = ""
            except sr.RequestError:
                st.error("❌ Speech Recognition service error.")
                transcript = ""

        if transcript:
            st.subheader("📄 Transcript")
            st.text_area("Text Output", transcript, height=250)
