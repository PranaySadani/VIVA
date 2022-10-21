import subprocess
import wolframalpha
import pyttsx3
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import ctypes
import requests
import shutil
from twilio.rest import Client
from urllib.request import urlopen
from tkinter import *
from PIL import ImageTk, Image


print("INITIALIZING VIVA....")


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak('Good morning sir')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon sir')
    else:
        speak('Good Evening sir')

    assname = ("VIVA")
    speak("I am your Assistant")
    speak(assname)


def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()


    server.login('YOUR_EMAIL', 'YOUR_EMAIL_PASSWORD')
    server.sendmail('YOUR_EMAIL', to, content)
    server.close()





class Widget:
    def __init__(self):
        root = Tk()
        root.title('VIVA - SECURE VIRTUAL PARTNER')
        root.config(background='Red')
        root.geometry('1280x720')
        root.resizable(0, 0)
        img = ImageTk.PhotoImage(Image.open(r"C:\Users\MME_LAPTOP1\Documents\vivalogo.PNG"))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand="no")

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Run\' to Give commands')

        userFrame = LabelFrame(root, text="User", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")

        left2 = Message(userFrame, textvariable=self.userText, bg='#3B3B98', fg='white')
        left2.config(font=("Century Gothic", 24, 'bold'))
        left2.pack(fill='both', expand='yes')

        compFrame = LabelFrame(root, text="VIVA", font=('Black ops one', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")

        left1 = Message(compFrame, textvariable=self.compText, bg='#3B3B98', fg='white')
        left1.config(font=("Century Gothic", 24, 'bold'))
        left1.pack(fill='both', expand='yes')

        btn = Button(root, text='Run', font=('Black ops one', 10, 'bold'), bg='#4b4b4b', fg='white',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',
                      command=root.destroy).pack(fill='x', expand='no')

        self.compText.set('Hello, I am Viva! What can i do for you Sir ?')

        root.bind("<Return>", self.clicked)  # handle the enter key event of your keyboard
        root.mainloop()

    def clicked(self):
        print('Working')
        query = takeCommand().lower()
        self.userText.set('Listening...')
        self.userText.set(query)

        while True:

            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("Here you go to Youtube\n")
                webbrowser.open("youtube.com")

            elif 'please open google' in query:
                speak("Here you go to Google\n")
                webbrowser.open("google.com")

            elif 'open whatsapp' in query:
                speak("Here you go to WhatsApp\n")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'hai vivah' in query :
                speak("Hello , how are you sir")

            elif 'hello' in query :
                speak("Hello , how are you sir")

            elif 'what is the time' in query:

                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time)
            elif 'which student do you like the most in this zoom meeting' in query:
                speak('Dificult but i would like to go with Nirmaan Basu')

            elif 'great' in query:
                speak('Thank you sir')

            elif 'open opera' in query:
                codePath = r"C:\Users\MME_LAPTOP1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Opera Browser.lnk"
                os.startfile(codePath)
                speak("Here you go to Opera\n")

            elif 'please open zoom' in query:
                codePath = r"C:\Users\MME_LAPTOP1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zoom\Zoom.lnk"
                os.startfile(codePath)
                speak("Here you go to Zoom\n")


            elif 'open chrome' in query:
                codePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                os.startfile(codePath)
                speak("Here you go to Chrome\n")

            elif 'open word' in query:
                codePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk"
                os.startfile(codePath)
                speak("Here you go to MS Word\n")

            elif 'open excel' in query:
                codePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk"
                os.startfile(codePath)
                speak("Opening Microsoft Excel\n")

            elif 'email to dhruv' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "Receiver email address"
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'send a mail' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whome should i send")
                    to = input()
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print(e)
                    speak("I am not able to send this email")

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")

            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")

            elif "change my name to" in query:
                query = query.replace("change my name to", "")
                assname = query

            elif "change name" in query:
                speak("What would you like to call me, Sir ")
                assname = takeCommand()
                speak("Thanks for naming me")

            elif "what's your name" in query or "What is your name" in query:
                speak("My friends call me")
                speak(assname)
                print("My friends call me", assname)

            elif 'exit' in query:
                speak("Thanks for giving me your time")
                exit()

            elif 'bye' in query:
                speak("Thanks for giving me your time")
                exit()

            elif "who made you" in query or "who created you" in query:
                speak("I have been created by Pranay Sadani & Aniroodh Chaudhary.")

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'please calculate' in query:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question = takeCommand()
                app_id = "7KQXLY-PJK8RJ6TPW"
                client = wolframalpha.Client('7KQXLY-PJK8RJ6TPW')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)


            elif 'search' in query or 'play' in query:


                query = query.replace("search", "")
                query = query.replace("play", "")
                webbrowser.open(query)

            elif "who i am" in query:
                speak("If you talk then definitely your human.")

            elif "why you came to world" in query:
                speak("Thanks to Pranay & Aniroodh. further It's a secret")

            elif 'power point presentation' in query:
                speak("opening Power Point presentation")
                power = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\PowerPoint 2013.lnk"
                os.startfile(power)

            elif 'is love' in query:
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in query:
                speak("I am your virtual assistant created by Dhruv & Pranay Sadani")

            elif 'reason for you' in query:
                speak("I was created as a SECURE RELIABLE VIRTUAL ASSISTANT")




            elif 'news' in query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                    data = json.load(jsonObj)
                    i = 1

                    speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + '\n')

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:

                    print(str(e))


            elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')



            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop VIVA from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")



            elif "restart" in query:
                subprocess.call(["shutdown", "/r"])

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")

            elif "log off" in query or "sign out" in query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "write a note" in query:
                speak("What should i write, sir")
                note = takeCommand()
                file = open('VIVA.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in query:
                speak("Showing Notes")
                file = open("VIVA.txt", "r")
                print(file.read())
                speak(file.read(6))



            elif "what is the weather" in query:


                api_key = "b5d86e2f17b926369822e970d0e7d428"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("what is the city name")
                city_name = takeCommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))

                else:
                    speak(" City Not Found ")



            elif "wikipedia" in query:
                webbrowser.open("wikipedia.com")

            elif "Good Morning" in query:
                speak("A warm" + query)
                speak("How are you Mister")
                speak(assname)

            elif "will you be my gf" in query or "will you be my bf" in query:
                speak("I'm not sure about, may be you should give me some time")

            elif "how are you" in query:
                speak("I'm fine, glad you asked me that")

            elif "i love you" in query:
                speak("It's hard to understand")

            elif "what is" in query or "who is" in query:


                client = wolframalpha.Client("7KQXLY-V6RWATHQGG")
                res = client.query(query)

                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No results")

            elif 'create a python environment' in query:
                speak('Creating Your IDE')
                codePath = r"C:\Users\MME_LAPTOP1\PycharmProjects\IDE\main.py"
                os.startfile(codePath)

            elif 'find my phone location' in query:
                speak('finding phone loction')
                codePath = r"C:\Users\MME_LAPTOP1\PycharmProjects\Phonelocationtracker\main.py"
                os.startfile(codePath)



            elif 'thoughts' in query:
                speak('The Computer Science Fair today was very well organized.All the participants came up with some wonderful projects.So,I would like to congratulate each one of them.Remember:The quest for knowledge should never end.And a big thank you to all the judges for coming here today and having a look at all our projects.The fair would have been incomplete without you all')



if __name__ == '__main__':
    speak("INITIALIZING VIVA")
    wishme()
    widget = Widget()