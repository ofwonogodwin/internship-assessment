import os
import requests
import wave
from dotenv import load_dotenv

# Load token from .env
load_dotenv()
access_token = os.getenv("AUTH_TOKEN")

# Transcription endpoint (Sunbird ASR)
url = "https://api.sunbird.ai/tasks/speech_recognition"

# Supported languages
languages = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}

def check_audio_duration(path):
    """Checks if the audio is under 5 minutes"""
    try:
        with wave.open(path, 'rb') as audio:
            frames = audio.getnframes()
            rate = audio.getframerate()
            duration = frames / float(rate)
            return duration <= 300  # 300 seconds = 5 minutes
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return False

def transcribe(audio_path, language_code):
    """Send the audio file to the Sunbird API for transcription"""
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    files = {
        "audio": open(audio_path, "rb"),
    }

    data = {
        "language": language_code
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("text", "No transcription returned.")
    else:
        return f"Error {response.status_code}: {response.text}"

def main():
    print("Note!! (Audio length should be less than 5 minutes)\nPlease provide path to the audio file in Format below:\n >>(Linux)/Users/yourname/Desktop/greeting.wav:")
    # print(">>(Windows)C:\Users\YourName\Desktop\greeting.wav")
    audio_path = input().strip()

    if not os.path.exists(audio_path):
        print("File does not exist.")
        return

    if not check_audio_duration(audio_path):
        print("Audio must be less than 5 minutes.")
        return

    print("Please choose the target language:")
    for lang in languages:
        print(f"- {lang}")
    target = input("Target language: ").strip().title()

    if target not in languages:
        print("Invalid language selected.")
        return

    print("\nTranscribing...\n")
    transcription = transcribe(audio_path, languages[target])
    print(f"Audio transcription text in {target}:")
    print(transcription)

if __name__ == "__main__":
    main()
