import pyttsx3
import webbrowser
import os
import datetime
pyttsx3.speak("Hello , how may i help you ")
print("Hello , how may i help you ?")
pyttsx3.speak("please give your requirements :")
print("please give your requirements :")
p=input()
while "exit" not in p:
   if ("open" in p) or ("run" in p) or ("execute" in p) or ("launch" in p) :
       if ("chrome" in p):
             webbrowser.open('https://www.google.com')
             pyttsx3.speak("google chrome is launched tell me your other requirement")
             print("google chrome is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("current" in p) or ("date" in p) or ("time" in p):
             noww=datetime.datetime.now()
             print(noww)
             pyttsx3.speak("current date and time is launched tell me your other requirement")
             print("current date and time is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("notepad" in p) or ("text editor" in p) or ("note" in p) :
             os.system("notepad")
             pyttsx3.speak("notepad is launched tell me your other requirement")
             print("Notepad is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("gmail" in p) or ("mail" in p) or ("mailbox" in p) :
             webbrowser.open('https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox')
             pyttsx3.speak("gmail is launched tell me your other requirement")
             print("Gmail is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("facebook" in p) :
             webbrowser.open("https://www.facebook.com/")
             pyttsx3.speak("facebook is launched tell me your other requirement")
             print("Facebook is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("my profile" in p) or ("ritika" in p) or ("my account" in p) and ("linkedin" in p) :
             webbrowser.open("https://www.linkedin.com/in/ritika-jain-a9228b194/")
             pyttsx3.speak("Ritika jain account on linkedin is launched tell me your other requirement")
             print("Ritika Jain account on linkedin is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("windows media player" in p) or ("media player" in p) :
             webbrowser.open("wmplayer")
             pyttsx3.speak("vlc media player is launched tell me your other requirement")
             print("VLC media player is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("youtube" in p)  :
             webbrowser.open("https://www.youtube.com/")
             pyttsx3.speak("youtube is launched tell me your other requirement")
             print("youtube is launched")
             print("please tell me your other requirement :")
             p=input()
       elif ("exit" in p) or ("stop" in p) or ("dont" in p):
             print("okay bye , i am happy to help you")
             break
       else :
             pyttsx3.speak("sorry , dont support tell me your other requirement")
             print("Sorry , dont support")
             print("please tell me your other requirement :")
             p=input()


