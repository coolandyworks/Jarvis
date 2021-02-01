import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning ANAND SIR")
    elif hour>=12 and hour<18:
        speak("good afternooon ANAND SIR")
    else:
        speak("good evening ANAND SIR")
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname)
    speak("please tell me how may i help you")

    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please.....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'hanuman' in query:
            speak("""Jai hanuman gyan gun saagar
            Jai kapis tihun lok ujaagar
            Ram doot atulit bal dhaama
            Anjani-putra pavan sut naama
            Mahavir vikram bajrangi
            Kumati nivaar sumati ke sangi
            Kanchan varan viraaj subesa
            Kaanan kundal kunchit kesaa
            Haath vajra aur dhuvaje viraaje
            Kandhe moonj janehu saajey""")

        elif 'ganesh' in query:
            speak("""Jai Ganesh, Jai Ganesh,Jai Ganesh Deva
            Mata Jaki Parvati,Pita Mahadeva
            Ekadanta Dayavanta,Char Bhujadhaari
            Mathe Par Tilak Sohe,Muse Ki Savari
            Mathe Par Sindoor Sohe,Muse Ki Savari
            Paan Charhe, Phool Charhe,Aur Charhe Meva
            Haar Charhe, Phool Charhe,Aur Charhe Meva
            Ladduan Ka Bhog Lage,Sant Karein Seva
            Jai Ganesh, Jai Ganesh,Jai Ganesh Deva
            Mata Jaki Parvati,Pita Mahadeva
            """)
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\tripa\\OneDrive\\Desktop\\jarvis"
            os.startfile(codePath)
        
        elif 'close' in query:
            speak("thanks for using jarvis")
            exit()