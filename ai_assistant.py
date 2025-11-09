import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import pyjokes
import webbrowser
import os

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', engine.getProperty('voices')[0].id)  # You can change voice here

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio, language='en-in')
            command = command.lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet.")
            return ""

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning! How can I help you?")
    elif 12 <= hour < 18:
        speak("Good Afternoon! How can I assist?")
    else:
        speak("Good Evening! What would you like to do?")

def run_assistant():
    wish_me()
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time}")

        elif "date" in command:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        elif "play" in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif "search" in command:
            speak("What should I search?")
            query = listen()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are results for {query}")

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "music" in command or "song" in command:
            music_dir = "C:\\Users\\YourUserName\\Music"  # change this path
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music")
            else:
                speak("No songs found in your music folder")

        elif "exit" in command or "quit" in command or "bye" in command:
            speak("Goodbye! Have a great day.")
            break

        elif command == "":
            continue

        else:
            speak("I'm not sure about that. Try asking about time, date, or search something.")

if __name__ == "__main__":
    run_assistant()
# Ai Voice Assistance   
# --- IGNORE ---
