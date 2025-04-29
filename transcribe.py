import os
import requests
from pydub import AudioSegment

def get_audio_duration(filepath):
    try:
        audio = AudioSegment.from_file(filepath)
        duration_seconds = len(audio) / 1000
        return duration_seconds
    except Exception as e:
        print(f"Error reading audio file: {e}")
        return None

def transcribe_audio(filepath, language):
    url = "https://api.sunbird.ai/v1/speech-to-text"  # Replace with actual Sunbird endpoint
    headers = {
        # "Authorization": "Bearer YOUR_API_KEY",  # Uncomment if API key required
    }
    files = {
        'file': open(filepath, 'rb'),
    }
    data = {
        'language': language.lower()
    }

    print("Sending audio to Sunbird AI for transcription...")
    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        result = response.json()
        return result.get("transcription", "No transcription found.")
    else:
        return f"Error {response.status_code}: {response.text}"

def main():
    supported_languages = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]

    # Step 1: Get audio file path
    print("Please provide path to the audio file (Audio length less than 5 minutes):")
    filepath = input().strip()

    if not os.path.exists(filepath):
        print("Audio file not found.")
        return

    # Step 2: Check audio duration
    duration = get_audio_duration(filepath)
    if duration is None:
        return

    if duration > 300:  # 5 minutes = 300 seconds
        print("Audio file is longer than 5 minutes. Please provide a shorter file.")
        return

    # Step 3: Ask for language
    print("Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi):")
    language = input().strip().title()

    if language not in supported_languages:
        print("Invalid language choice.")
        return

    # Step 4: Transcribe
    transcription = transcribe_audio(filepath, language)

    # Step 5: Output
    print(f"\nAudio transcription text in {language.lower()}:")
    print(transcription)

if __name__ == "__main__":
    main()
