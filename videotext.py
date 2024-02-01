import os
import moviepy.editor as mp
import speech_recognition as sr
import streamlit as st

def video_to_text(video_file):
    # Ekstrak audio dari video
    video = mp.VideoFileClip(video_file)
    audio_file = "audio.wav"
    video.audio.write_audiofile(audio_file, codec='pcm_s16le')

    # Transkripsi audio menjadi teks
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as file_audio:
        audio_data = recognizer.record(file_audio)

    try:
        result_text = recognizer.recognize_google(audio_data, language="id-ID")
        return result_text
    except sr.UnknownValueError:
        return "Google Web Speech API tidak mengenali audio"
    except sr.RequestError as e:
        return f"Error pada permintaan API: {e}"

# Penggunaan Streamlit
st.title("Konversi Video ke Teks")

video_path = st.text_input("Masukkan video")

if st.button("Konversi Video"):
    if video_path:
        if os.path.exists(video_path):
            result_text = video_to_text(video_path)
            st.write("Hasil konversi teks:")
            st.write(result_text)
            with open("hasilteks.txt", "w", encoding="utf-8") as hasil_teks:
                hasil_teks.write(result_text)
        else:
            st.error("File video tidak ditemukan. Mohon periksa path yang dimasukkan.")
    else:
        st.warning("Mohon masukkan path video terlebih dahulu.")
