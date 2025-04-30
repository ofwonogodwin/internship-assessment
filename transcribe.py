import os
import requests
from dotenv import load_dotenv

# Load token
load_dotenv()
access_token= os.getenv("AUTH_TOKEN")

# Sunbird API URL
API_URL = "https://api.sunbird.ai/tasks/stt"

# Supported languages
languages = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}
def transcribe(audio_path, lang_code):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    mime_type = "audio/wav" if audio_path.endswith(".wav") else "audio/mpeg"

    with open(audio_path, "rb") as f:
        files = {
            "audio": (
                os.path.basename(audio_path),
                f,
                mime_type,
            ),
        }

        data = {
            "language": lang_code,
            "adapter": lang_code,
            "whisper": True,
        }

        response = requests.post(API_URL, headers=headers, files=files, data=data)

    # print("Raw response:", response.text)

    if response.status_code == 200:
        return response.json().get("audio_transcription", "No transcription returned.")

        # return response.json().get("output", {}).get("text", "No transcription returned.")
    else:
        return f"Error {response.status_code}: {response.text}"


# def transcribe(audio_path, lang_code):
#     headers = {
#         "accept": "application/json",
#         "Authorization": f"Bearer {access_token}",
#     }

#     mime_type = "audio/wav" if audio_path.endswith(".wav") else "audio/mpeg"

#     files = {
#         "audio": (
#             os.path.basename(audio_path),
#             open(audio_path, "rb"),
#             mime_type,
#         ),
#     }

#     data = {
#         "language": lang_code,
#         "adapter": lang_code,
#         "whisper": True,
#     }

#     response = requests.post(API_URL, headers=headers, files=files, data=data)

#     if response.status_code == 200:
#         return response.json().get("output", {}).get("text", "No transcription returned.")
#     else:
#         return f"Error {response.status_code}: {response.text}"

def main():
    audio_path = input("Please provide path to the audio file: ").strip()
# /home/godwin-ofwono/Desktop/python/sunbird_AI/internship-assessment/voices/..
# /home/godwin-ofwono/Desktop/voices/how-are-you-doing-today-103598.mp3
# /home/godwin-ofwono/Desktop/voices/yes-i-believe-you-176782.mp3
    if not os.path.exists(audio_path):
        print("File does not exist.")
        return

    print("Please choose the target language:")
    for lang in languages:
        print(f"- {lang}")
    lang = input("Target language: ").strip().title()

    if lang not in languages:
        print("Invalid language.")
        return

    print("\nTranscribing...\n")
    result = transcribe(audio_path, languages[lang])
    print(f"Audio transcription text in {lang.lower()}:\n{result}")

if __name__ == "__main__":
    main()
