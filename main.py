import pyttsx3
import speech_recognition as sr
from google import genai
client = genai.Client(api_key="Your API Key")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        return query

    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'None'
    
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text


input = ''
speak("Hello, I am Jarvis. How can I help you today?")
while input != 'exit':
    input = takeCommand()
    print(f'User: {input}')
    print('Processing...')
    response = generate_response(input)
    modified_responce = ''
    for chr in response:
        if chr != '*':
            modified_responce += chr
    response = modified_responce
    print(f'Jarvis: {response}')
    speak(response)
