import pyttsx3  #pyttsx3 is a text-to-speech conversion library in Python
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')      #getting details of current voice
engine.setProperty('voice',voices[1].id)   # setting the voice
#voices[0].id means voices at zeroth index i.e David desktop
#voices[1].id means voices at first index i.e David desktop

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #Blocks while processing all currently queued commands.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("This is Zira, your voice assistant,how can i help you!")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  #optional
        audio = r.listen(source) # to listen the audio

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #this is google search engine
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    if True:
        query = takeCommand().lower()    #converting to lowercase
        #logic for executing task based on query
        if 'wikipedia' in query:  #if wikipedia is there in query then the search will go
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")  #removing wikipedia from query
            results = wikipedia.summary(query,sentences = 2)  #.summary is used to return the summary of the information
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("okay..")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("okay..")
            webbrowser.open("https://www.google.com/search?q=google&rlz=1C1CHBF_enIN913IN913&oq=google&aqs=chrome..69i57j35i39l2j0j69i61j69i60l2j69i65.6546j0j1&sourceid=chrome&ie=UTF-8")
        elif 'open stack overflow' in query:
            speak("okay..")
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open("spotify")
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir, the time is{str_time}")
        elif 'code with harry' in query:
            webbrowser.open("https://www.youtube.com/watch?v=Lp9Ftuq2sVI&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=121")
