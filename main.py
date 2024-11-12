import speech_recognition as sr #i can write sr in place of speech_recoginition
import webbrowser #inbuilt webbrowser for [ython]
import pyttsx3 #engine for text to speech(this is how jarvis is able to speak)
import pocketsphinx
import musicLibrary
import requests

recognizer = sr.Recognizer() # initializing the recognizer
engine = pyttsx3.init() #pyttsx will be initialized
newsapi = "63a069d1358c4a799e2a5fcc5d318de0"

def speak(text): #creating the function to use pyttsx3 
    engine.say(text)
    engine.runAndWait() #this is important, so that program will wait and listen to us
   

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        
    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        # song1 = c.lower().split(" ")[1:]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
        if r.status_code == 200:#check the status code
            #convert the data into json format
            data = r.json()
            #fetches the article from the site
            articles = data.get('atricle', [])
            # prints only the titles
            for article in articles:
                print(article['title'])


if __name__ == "__main__": #this basically initiatest the while loop 
    #so that the jarvis is initianilized again and again
    speak(" Initializing Jarvis....... ")

    while True:
        #listen to the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech using Sphinx
        
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
                word = r.recognize_google(audio)
                print("Recognizing.....")

            
            if(word.lower()== "jarvis"):  
                #we have triggered the initialiing word, and will work in this if only
                speak("  Yes Sir!")
                #now this is for 2nd time microphone activation
                with sr.Microphone() as source:
                    print("Jarvis activated......")
                    audio = r.listen(source,timeout=3,phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    processcommand(command)
                    break
                    


        except Exception as e:
            print(" Didn't recognise, please say it again; {0}".format(e)) #format(e) prints the current error
            speak("Didn't recognise, please say it again")




