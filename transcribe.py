import os
import requests
from dotenv import load_dotenv

# Loading the token from the .env file
load_dotenv()
access_token= os.getenv("AUTH_TOKEN")

# the API URL
API_URL = "https://api.sunbird.ai/tasks/stt"

# languages supported and there codes
languages = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}
def transcribe(audio_path, language_code):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
    }

    file_type = "audio/wav" if audio_path.endswith(".wav") else "audio/mpeg"

    with open(audio_path, "rb") as f:
        files = {
            "audio": (
                os.path.basename(audio_path),
                f,
                file_type,
            ),
        }

        data = {
            "language": language_code,
            "adapter": language_code,
            "whisper": True,
        }

        response = requests.post(API_URL, headers=headers, files=files, data=data)

    #  print("Raw response:", response.text)

    if response.status_code == 200:
        return response.json().get("audio_transcription", "No transcription returned.")

    else:
        return f"Error {response.status_code}: {response.text}"


def main():
    audio_path = input("Please provide path to the audio file:\neg.(Linux) /home/godwin-ofwono/Desktop/voices/yes-i-believe-you-176782.mp3\nAudio Path :").strip()
# /home/godwin-ofwono/Desktop/python/sunbird_AI/internship-assessment/voices/..
# /home/godwin-ofwono/Desktop/voices/how-are-you-doing-today-103598.mp3
# /home/godwin-ofwono/Desktop/voices/yes-i-believe-you-176782.mp3
    if not os.path.exists(audio_path):
        print("File does not exist.")
        return

    print("\nNote!! Target language should be Same as Audio Language")
    print("Please choose the target language From list below:")
    # target language should be the same as the language in audio
    for language in languages:
        print(f">> {language}")
    language = input("Target language: ").strip().title()

    if language not in languages:
        print(f"Sorry,{language} is an invalid language.")
        return

    print("\nTranscribing...\n")
    end_result = transcribe(audio_path, languages[language])
    print(f"Audio transcription text in {language.lower()}:\n{end_result}")

if __name__ == "__main__":
    main()
