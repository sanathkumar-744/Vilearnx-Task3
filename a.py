from gtts import gTTS
import pyttsx3
import os

# Function for Google Text-to-Speech (gTTS)
def text_to_speech_gtts(text, lang='en', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save("output.mp3")
    os.system("start output.mp3")  # For Windows; use "afplay output.mp3" for MacOS and "mpg321 output.mp3" for Linux

# Function for pyttsx3 Text-to-Speech
def text_to_speech_pyttsx3(text, voice_id=None, rate=150):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if voice_id:
        engine.setProperty('voice', voice_id)
    engine.setProperty('rate', rate)
    
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    print("Choose the Text-to-Speech engine:")
    print("1. Google Text-to-Speech (gTTS)")
    print("2. Offline Text-to-Speech (pyttsx3)")
    choice = int(input("Enter your choice (1 or 2): "))

    text = input("Enter the text you want to convert to speech: ")

    if choice == 1:
        lang = input("Enter the language code (e.g., 'en' for English, 'es' for Spanish): ")
        slow = input("Do you want slow speech? (yes or no): ").lower() == 'yes'
        text_to_speech_gtts(text, lang, slow)
    elif choice == 2:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        print("Available voices:")
        for i, voice in enumerate(voices):
            print(f"{i+1}. {voice.name} ({voice.languages})")
        voice_choice = int(input("Choose a voice by number: ")) - 1
        rate = int(input("Enter the speech rate (default is 150): "))
        text_to_speech_pyttsx3(text, voices[voice_choice].id, rate)
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
