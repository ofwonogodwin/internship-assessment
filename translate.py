import os
import requests
from dotenv import load_dotenv

# Loading the token from .env file
load_dotenv()
access_token = os.getenv("AUTH_TOKEN")

# translation endpoint
url = "https://api.sunbird.ai/tasks/nllb_translate"

# languages supported and  there codes
languages = {
    "English": "eng",
    "Luganda": "lug",
    "Runyankole": "nyn",
    "Ateso": "teo",
    "Lugbara": "lgg",
    "Acholi": "ach"
}
def translate(text, source_code, target_code):
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    data = {
        "source_language": source_code,
        "target_language": target_code,
        "text": text,
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        json_data = response.json()
        return json_data.get("output", {}).get("translated_text", "No translation returned.")
    else:
        return f"Error {response.status_code}: {response.text}"


def main():
    print("Please choose the source language from List Below:")
    for language in languages:
        print(f">> {language}")
    source_language = input("Source language: ").strip().title()

    if source_language not in languages:
        print("Invalid source language.")
        return

    print("\nPlease choose the target language from list below:")
    for language in languages:
        print(f">> {language}")
    target_language = input("Target language: ").strip().title()

    if target_language not in languages:
        print("Invalid target language.")
        return

    if source_language == target_language:
        print("Sorry, The Source and target language cant be the same.")
        return

    text = input("\nType the text you want to translate :")

    print("\nTranslating...\n")
    translated = translate(text, languages[source_language], languages[target_language])
    print(f"Translation in {target_language}:\n {translated}")

if __name__ == "__main__":
    main()
