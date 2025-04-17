# this is my first project : 
# author : abhishek singh (@digiware1)


import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


# pip install pyttsx3
# pip install requests
# pip install openai
# pip install gTTS
# pip install pygame
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "enter your newsapi key here"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    

def speak(text):
    
    tts = gTTS(text)
    tts.save('temp.mp3')
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load the mp3 file
    pygame.mixer.music.load('temp.mp3')
    
    # Play the mp3 file
    pygame.mixer.music.play()
    
    #keep the program unning until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) 
        
    pygame.mixer.music.unload()  # Unload the mp3 file after playing
        
    # this is for the ggts and pygame error to remove the temp file
    # Remove the temporary file after playing 
    os.remove('temp.mp3')  
       
      
def aiProcess(command):
    
    client= OpenAI(api_key= "enter your api key here"
    
    )
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        { "role": "system", "content": "You are a virtual assistant name nexa, skilled in general tasks like alexa,  google assistant. Give sort response to the user please."},
        
        {"role": "user", "content": command}
        
    ]
    )
    return completion.choices[0].message.content
# print(completion.choices[0].message.content)

        
    
    
def processCommand(c): 
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():  
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")   
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://www.chat.openai.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://mail.google.com")
    elif "open stack overflow" in c.lower():
        webbrowser.open("https://stackoverflow.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")      
    elif "open amazon" in c.lower():
        webbrowser.open("https://www.amazon.com")    
    elif "open flipkart" in c.lower():
        webbrowser.open("https://www.flipkart.com")          
    elif "open copilot" in c.lower():
        webbrowser.open("https://copilot.microsoft.com")
    elif c.lower().startswith("play"):
        parts = c.split(" ", 1)
        if len(parts) > 1:
            song = parts[1].strip().lower()
            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                webbrowser.open(link)
            else:
                speak(f"Sorry, I don't have {song} in your library.")
        else:
            speak("Please say the name of the song after 'play'.")
    elif "news" in c.lower():
        response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Limit to 5 headlines
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news.")
    else:
        # Let OpenAI handle the command
        try:
            output = aiProcess(c)
            speak(output)
        except Exception as e:
            print(f"OpenAI error: {e}")
            speak("Sorry, I couldn't process that with AI.")

               
       
    # pass

if __name__ == "__main__":
    speak("nexa ai is listening.....")
    while True:
        # listen for the wake word "Aura"
    #obten audio from the microphone
        r = sr.Recognizer()
            
        # recognize speech using google
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=6, phrase_time_limit=10)
            word  = r.recognize_google(audio)
            if(word.lower() == "nexa"):
                print("nexa active...")
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("nexa active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    
                    processCommand(command)
                

        except Exception as e:
            print("Error; {0}".format(e)) 
            
      
      
