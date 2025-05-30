# 🐾 Animalese Text-to-Speech Translator

This is a fun Python project that converts typed text into "Animalese"-style speech — inspired by the voice sounds from Animal Crossing!

## 🎯 What It Does

- Takes input text from the user
- Converts each letter into a corresponding `.wav` sound file
- Plays the sound files in sequence to mimic Animalese speech

## 📁 Folder Structure
Animalese-Translator/
├── animalese.py # Your main Python script
├── animal sounds/ # Folder containing sound files
│ ├── a.wav
│ ├── b.wav
│ ├── ...
│ └── z.wav

## 🛠️ Requirements

- Python 3.x
- `playsound` library for audio playback

Install `playsound` with:

```bash
pip install playsound
```
## ▶️ How to Run


-Make sure your .wav files (named a.wav, b.wav, etc.) are placed inside a folder called animal sounds.

-Run the script:
   ``` python animalese.py ```
   
-Type your message when prompted — you'll hear it spoken in Animalese!

## 💡 Features to Add (Future Ideas)

1.Export final speech as an audio file
2.Add a GUI for input
3.Adjust speed/pitch of speech
4.Support punctuation and emojis

## 📚 Credits
Inspired by Animal Crossing's signature speech style. This project is for fun and learning purposes.

Have fun speaking Animalese! 🐶🐱🎶
