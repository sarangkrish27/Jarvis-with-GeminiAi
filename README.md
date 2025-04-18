# 🧠 Jarvis - Your Personal AI Voice Assistant (Python)

Jarvis is a smart voice assistant built with Python. It listens to your voice, understands your commands, and responds back using natural-sounding speech. Powered by the **Google Gemini API**, it brings conversational AI right into your terminal!

---

## 🚀 Features

- 🎙️ **Voice Input**  
  Uses `speech_recognition` to convert your speech into text.

- 🗣️ **Voice Output**  
  Replies using `pyttsx3`, a text-to-speech engine that works offline.

- 🤖 **AI Responses**  
  Integrates with **Google Gemini API** to give intelligent and context-aware answers.

- 💻 **Simple Terminal App**  
  No fancy GUI, just clean and efficient voice interaction.

---

## 🛠️ Tech Stack

- Python 3  
- `pyttsx3`  
- `speech_recognition`  
- Google Gemini API (`google.generativeai`)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/sarangkrish27/Jarvis-with-GeminiAi.git
cd Jarvis-with-GeminiAi
```

2. **Set up your Google Gemini API key:**
   - Visit Google AI Studio and get your API key.
   - Open `main.py` and replace this line:

```python
client = genai.Client(api_key="Your API Key")
```
with:

```python
client = genai.Client(api_key="your_actual_api_key")
```

## ▶️ Running the Assistant

Simply run:

```bash
python main.py
```
Speak your question or command — Jarvis will listen, process it, and reply with a voice response.

## Made with ❤️ by Sarang
