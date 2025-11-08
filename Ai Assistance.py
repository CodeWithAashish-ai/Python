import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen to user input via microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the internet.")
            return ""

def get_time():
    """Get current time."""
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def get_date():
    """Get current date."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def main():
    speak("Hello! I'm your AI assistant. How can I help you today?")
    
    while True:
        command = listen()
        
        if "hello" in command or "hi" in command:
            speak("Hello! What can I do for you?")
        
        elif "time" in command:
            current_time = get_time()
            speak(f"The current time is {current_time}")
        
        elif "date" in command:
            current_date = get_date()
            speak(f"Today's date is {current_date}")
        
        elif "search" in command:
            speak("What do you want to search for?")
            query = listen()
            if query:
                url = f"https://www.google.com/search?q={query}"
                webbrowser.open(url)
                speak(f"Searching for {query} on Google.")
        
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        
        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        
        elif "play music" in command:
            # This assumes you have a music folder; adjust path as needed
            music_dir = "C:\\Users\\YourUsername\\Music"  # Change this to your music folder
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
                speak("Playing music.")
            else:
                speak("No music found in your directory.")
        
        elif "exit" in command or "quit" in command or "bye" in command:
            speak("Goodbye! Have a great day.")
            break
        
        else:
            speak("I'm sorry, I didn't understand that. Try saying 'time', 'search', or 'open YouTube'.")

if __name__ == "__main__":
    main()
