import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import random
import pyjokes
import pyautogui
from plyer import notification
from datetime import date
import requests
import smtplib
from tkinter import*
from PIL import ImageTk,Image
import os
import sys
import wolframalpha

root = Tk()
root.title("J.A.R.V.I.S")
root.geometry("1000x1000")

root.config(background = "red")

img = ImageTk.PhotoImage(Image.open("JARVIS ui con.jpg"))

label_image = Label(root, image = img)
label_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def runner():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir I am your personal voice assistant, JARVIS. How may I help you")
    elif hour>=12 and hour <16:
        speak("Good AFternoon sir I am your personal voice assistant, JARVIS. How may I help you?")
        
        
    else:
        speak("Good Evening Sir ,  I  am   your   personal   voice assistant , JARVIS. How may I help you?")
    
    
    
def me():
    s = "hello sir Im Jarvus. point o " \
        "Created by Harshil Shah "

    speak(s)

    speak("how can i help you !")
    
btnrunner = Button(root, text = "Press to start", command = runner)
btnrunner.place(relx = 0.5, rely = 0.5, anchor = CENTER)

def username(s1):
    try:
     speak(f"what i should to call you{s1}")
     s=takecommend()
     s=s.replace("call me",'')
     speak(f"helle{s1} ")
     speak(s)
     with open("data of user.text","a") as e:
        st = datetime.datetime.now()
        st1=date.today()
        e.write(f"{s} use me on {st1}at{st} \n ")
        e.close()
        speak(f"how can i help you {s1}")
    except Exception as e:
        speak(f"{s1} i dont understant sir what did you say ")
        username(s1)


def Take_Command():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n" )
        
    except Exception as e:
        #print(e)
        print("Say that again please")
        return "None"
    return query
    
if __name__ == "__main__":
    while True:
         query = Take_Command().lower()
         
         # Logic for executing tasks based on query
         
         if 'wikipedia' in query:
             speak("Browsing Wikipedia...")
             query = query.replace("wikipedia" , "")
             results = wikipedia.summary(query, sentences = 2)
             speak("According to wikipedia")
             print(results)
             speak(results)
             
         elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = Take_Command().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")
            
         elif 'open google' in query:
             speak("opening")
             webbrowser.open("google.com")
            
         elif 'play my favourite playlist' in query:
             speak("playing")
             webbrowser.open("https://open.spotify.com/playlist/38c3yrVHaL6WhRew2cDWcH")
            
         elif 'play my favorite song' in query:
             speak("playing")
             webbrowser.open("https://www.youtube.com/watch?v=fKopy74weus")
             
         elif 'open my website' in query:
             speak("opening")
             webbrowser.open("https://harshilgauravshah.github.io/Portfolio/")
             
         elif 'open chess com' in query:
             speak("opening")
             webbrowser.open("https://www.chess.com/home")
             
         elif 'rickroll' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
             
         elif 'play come and get your love' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/watch?v=bc0KhhjJP98")
             
         elif 'play we will rock you' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/watch?v=-tJYN-eG1zk")
             
         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir the time is {strTime}")
             print(f"Sir the time is {strTime}")
             
         elif 'open spotify' in query:
             speak("opening")
             musicPath = "C:\\Users\\HP\\AppData\\Roaming\\Spotify\\Spotify.exe"
             os.startfile(musicPath)
             
         elif 'open whatsapp' in query:
             speak("opening")
             webbrowser.open("https://web.whatsapp.com/")
             
         elif 'open discord browser' in query:
             speak("opening")
             webbrowser.open("https://discord.com/channels/@me")
             
         elif 'open shellshock' in query:
             speak("Opening")
             webbrowser.open("https://shellshock.io/?showAd=false")
             
         elif 'sleep' in query:
             speak("Ok Sir, bye.")
             sys.exit()
             
         elif 'screenshot' in query:
             image = pyautogui.screenshot()
             image.save('screenshot.png')
             speak('Screenshot taken.')
             
         elif 'initiate Drone Strike' in query:
             speak('Target required')
             
         elif 'open beluga' in query:
             speak("opening")
             webbrowser.open("https://www.youtube.com/c/Beluga1%22")
             
         elif 'Krishna Jha' in query:
             speak("Good decision Sir, she is an absolute nincompoop")
             
         elif 'open classroom' in query:
             speak("opening")
             webbrowser.open("https://classroom.google.com/u/1/c/MzA3OTY2MDU0NjM3")
                
         elif 'open meet' in query:
             speak("opening")
             webbrowser.open("https://meet.google.com/")
             
         elif 'search' in query:
               speak("What do you want me to search for (please type) ? ")
               search_term = input()
               search_url = f"https://www.google.com/search?q={search_term}"
               webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
               speak(f"here are the results for the search term: {search_term}")
               
         elif 'joke' in query:
             random_joke = pyjokes.get_joke()
             print(random_joke)
             speak(random_joke)
             
         elif 'covid stats' in query:
              html_data = make_request('https://www.worldometers.info/coronavirus/')
              # print(html_data)
              soup = BeautifulSoup(html_data, 'html.parser')
              total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
              total_cases = total_global_row.find_all('td')[2].get_text()
              new_cases = total_global_row.find_all('td')[3].get_text()
              total_recovered = total_global_row.find_all('td')[6].get_text()
              print('total cases : ', total_cases)
              print('new cases', new_cases[1:])
              print('total recovered', total_recovered)
              notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
              notification.notify(
        title="COVID-19 Statistics",
        message=notification_message,
        timeout=5
              )
              speak("here are the stats for COVID-19")
              
         elif 'thank you' in query:
             speak("Always at your service sir")
             
         elif 'wake up' in query:
             speak("Jarvis is online")
             runner()
         
         elif 'lichess' in query:
             speak("opening")
             webbrowser.open("https://lichess.org/")

         elif 'hello' in query:
                me()
                speak(f"hello {sex} ! How are you")

         elif 'good' in query or 'well' in query:
                speak(f'great to that you are well {sex}')

         elif 'who are you' in query:
                me()

         elif "how are you" in query:
                speak("I'm fine, glad you asked me that")

         elif 'today' in query:
                speak("It is")
                speak(date.today())
                speak("today")
                
         elif 'hello' in query:
            gf = "O hello sir", "Hi sir", "I am here for your help sir!", "hello sir", "I was surfing the web, and gethering information, how can i help?", "Online and ready"
            speak(random.choice(gf))
            
         elif 'bye' in query:
             speak("Bye sir...have a great day ahead")
             speak("JARVIS is offline")
             sys.exit()
             
             
         elif 'open file' in query:
             speak("which file sir ")

             d = Toplevel()
             Toplevel.configure(bg="black")
             e = Entry(d,bg = "black", fg = "white" ,width = 20)
             e.pack()

         def open_file():

            os.system(e.get())

            speak("ok sir i will open "+e.get())

            s = Button(d,bg = "black",font = ('arial',18,'bold'),fg  = "white",width = 10,activeforeground = "grey",activebackground = "black",text = "open it",command=open_file).pack()
            
        
      
while True:
    activate_va()
     
root.mainloop()