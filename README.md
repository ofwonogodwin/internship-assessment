# Sunbird AI Internship Assessment Exercise

This assessment consists of 3 parts:
- Programming exercises.
- Build a simple command line app using the Sunbird AI API.

## Getting started
- Fork this repository to create your own copy. ([More info about forking a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo))
- Clone your repository to access it locally: `git clone https://github.com/<your-username>/internship-assessment.git`. (Replace `<your-username>` with your Github username.)
- Change directory into the `internship-assessment` folder after cloning the repository.
- Create a python virtual environment: `python -m venv venv`
- Activate the virtual environment: 
  - Linux/Mac: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate.bat`
- Install the required python packages: `pip install -r requirements.txt`
- Run the command `pytest`. (The tests should be failing, it's your task to make them pass. See below for instructions)

## Part 1: Programming exercises
There are 2 programming exercises designed to test your competency with the python programming language. 

You can find the starter code and task descriptions in the `exercises/basics.py` file in this repo.

Run the following command: `pytest`. You will see that all the tests are failing.

Your goal is to implement the 2 functions `collatz` and `distinct_numbers` to make the above failing tests pass.

You can keep running the `pytest` command to see which tests are still failing and fix your code accordingly.

## Part 2: Write a simple python translation script
Write a simple python script in a file `translate.py` that translates text to-and-from English to 5 local Ugandan languages and viseversa.

Your script should do the following:
- Ask the user to choose a source language (English, Luganda, Runyankole, Ateso, Lugbara or Acholi).
- Ask the user to choose a target language (English, Luganda, Runyankole, Ateso, Lugbara or Acholi). A target language can't be the same as the source language.
- Ask the user for text to translate (should be in the source language chosen).
- Translate the input text into the target language.

A sample interaction is as follows:
```
(your program): Please choose the source language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi)
(the user): English
(your program): Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi):
(the user): Luganda
(your program): Enter the text to translate:
(the user): How are you?
(your program): Oli otya?
```

## Part 3: Write a simple python audio transcription script
Write a simple python script in a file `transcribe.py` that transcribes a given audio file to text in a given language text(English and any other 5 local Ugandan languages).

Your script should do the following:
- Ask the user to provide path to the audio file (/path/to/audio_file).
- Ask the user to choose a target language (English, Luganda, Runyankole, Ateso, Lugbara or Acholi) in which the audio is.
- Transcribe the audio file into text into the target language.

A sample interaction is as follows:
```
(your program): Please provide path to the audio file: 
(the user): /path/to/audio_file
(your program): Please choose the target language: (one of English, Luganda, Runyankole, Ateso, Lugbara or Acholi):
(the user): Luganda
(your program): Audio transcription text in luganda:
(the program): Transcribed audio text output
```

This will require you to make use of Sunbird's API. You can find a [tutorial](https://salt.sunbird.ai/API/) here. 

To use the API, you'll need an **access token** which will be sent in the email inviting you to this assessment. Please use this **access token** for this assignment and 
don't try to signup to create an account as indicated in the tutorial above.
