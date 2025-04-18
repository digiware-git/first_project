# Nexa – AI-Powered Voice Assistant 🎙️🤖

Nexa is a smart, voice-activated personal assistant built with Python. Inspired by Alexa and Google Assistant, Nexa can understand voice commands, open websites, play music, fetch latest news, and even talk back using AI (OpenAI's GPT).

---

## 🧠 Features

- 🎤 Voice-controlled interaction using SpeechRecognition
- 🌐 Open popular websites (Google, YouTube, WhatsApp, etc.)
- 📰 Get real-time news headlines using NewsAPI
- 🎵 Play songs from a custom music library
- 🤖 Smart AI replies via OpenAI GPT-3.5 Turbo
- 🗣️ Speak responses using Google Text-to-Speech (gTTS) and Pygame
- 🎧 Clean, responsive, and interactive experience

---

## 🔧 Technologies Used

- Python
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [OpenAI API](https://platform.openai.com/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Pygame](https://www.pygame.org/)
- [NewsAPI](https://newsapi.org/)
- Webbrowser, pyttsx3, and more

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nexa-voice-assistant.git
cd nexa-voice-assistant

. Install Required Libraries

pip install -r requirements.txt

If requirements.txt is not there, install manually:

pip install SpeechRecognition openai gTTS pygame requests pyttsx3

3. Setup API Keys

    Replace enter your api key here in the script with your OpenAI API key.

    Replace enter your newsapi key here with your NewsAPI key.

4. Add Your Music Library

In musicLibrary.py, define your custom songs like:

music = {
    "tum hi ho": "https://link-to-song",
    "believer": "https://link-to-song"
}

/////*****Run the Assistant

python nexavoice.py*******///////



Sample Commands

    “Nexa, open YouTube”

    “Nexa, play Tum Hi Ho”

    “Nexa, tell me the news”

    “Nexa, what is AI?”

    “Nexa, open Instagram”


Author

Abhishek singh (@digiware1)
Made with ❤️ using Python

