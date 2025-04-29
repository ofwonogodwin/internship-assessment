import requests

def get_translation(text, source_lang, target_lang):
    url = "https://api.sunbird.ai/v1/translate"  # Replace with actual endpoint
    headers = {
        "Content-Type": "application/json",
        # "Authorization": "Bearer YOUR_API_KEY",  # Uncomment and insert key if required
    }
    data = {
        "source_language": source_lang.lower(),
        "target_language": target_lang.lower(),
        "text": text
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("translated_text", "Translation not found.")
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    languages = ["English", "Luganda", "Runyankole", "Ateso", "Lugbara", "Acholi"]

    print("Please choose the source language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi)")
    source = input().strip().title()
    if source not in languages:
        print("Invalid source language.")
        return

    print("Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi)")
    target = input().strip().title()
    if target not in languages:
        print("Invalid target language.")
        return

    if source == target:
        print("Source and target languages cannot be the same.")
        return

    print("Enter the text to translate:")
    text = input().strip()

    print("Translating...")
    translation = get_translation(text, source, target)
    print("Translated text:")
    print(translation)

if __name__ == "__main__":
    main()
