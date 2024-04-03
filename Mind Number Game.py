import pyttsx3
''''
 1)It is pre built in module in python.
 2)"pyttsx3" stands for "python text to speech version_3".
 3)It is used to convert text to speech.
'''
import datetime  # This Module is Used to Find Current Date,Time,Hours,Minutes and Seconds.
import speech_recognition as sr
# This Module is Used to Recognise our speech or audio.
# "as" is Keyword in python used to refer short name.
import time # sleep() function is only Available in "time" module.

sounds=pyttsx3.init("sapi5")
# sapi5 stands for speech API5 and this Teachnology provided by Microsoft.
# sounds is Variable.
# pyttsx3.init("sapi5") class support many and diffrent "sounds" eg:humans sounds and animal sounds etc....
# "sapi5" for windows
# sapi5   =  windows
# nsss    =  mac os
# espeak  =  evey other platform

gender_voice=sounds.getProperty("voices")
# getproperty is used for get voices frome "sapi5".
# "voices" contain two voices "0 index is male" and "1 index is female".
sounds.setProperty("voice",gender_voice[1].id)
# setproperty is used for set one voice to sounds.
# "voice" means singular it set only one voice.
# "gender_voice[1].id" you set 1st index voice and id attribute is always defined it is default.

def speak(audio):
    sounds.say(audio)    # say function is used to Read the Text in setted voice.
    sounds.runAndWait()  # It is used to don't finish the code and it is waiting for another command.


def wishme():
    hour=int(datetime.datetime.now().hour)
    # datetime module - datetime class - now() funtion - hour nested funtion.
    # It is used to find the current hour.
    if hour>=0 and hour<12:
        print("Good morning Boss 🥱")
        speak("Good morning Boss")
        print()
    elif hour>=12 and hour<16:
        print("Good Afternoon Boss 🥰")
        speak("Good Afternoon Boss")
        print()
    elif hour>=16 and hour<21:
        print("Good Evening Boss 😘")
        speak("Good Evening Boss")
        print()
    else:
        print("Good Night Boss 😴")
        speak("Good Night Boss")
        print()

def takecommand():
    with sr.Microphone() as source:
    # "with" Keyword is to automrtically close your file when the code is executed.
        print("I am Listening  Your Voice........")
        sr.Recognizer().pause_threshold=1   # seconds of non-speakingaudio after a word is considering complete.
        sr.Recognizer().adjust_for_ambient_noise(source,duration=1)  # It is used to remove unwanted noise in your audio with 1_Seconds.
        audio=sr.Recognizer().listen(source)
        # listen method is used for listen audio via sr.Microphone().
        # Microphone() is used for accept sound.
    try:
        print("Wait a Few Minitues Guys")
        query=sr.Recognizer().recognize_google(audio,language="en-in") 
        # It use internet because this "recognize_google" funtion  is only available in internet.
        # "en-in" means "english india".
        # It is used to change your audio in english india.
        print("User Said :",query)
        print() # It is used for empty line.
    except Exception as e:
    # if any error in your query it handle the error autometically.
        print(e)
        # it is used to print what  error occured.
        query="Say that Again Please"
        time.sleep(1)
        print(query)
        speak(query)
    return query
    # The return keyword is used to return your query in function calling.

if __name__ == "__main__" :
    # it is used to check this file is main file or imported file.
    # the "if" condition is only true if the file is main otherwise it will "false" the condition.
    wishme()   #It calling the wishme() function.
    print("This Game Name is 'Number Game' or 'Mind Thought Game'.")      # game Name is "Mind Number Game"
    speak("This Game Name is 'Number Game' or 'Mind Thought Game'")
    print("I am Your Game partner, My Name is Alpha.")  # Your Partner name is Alpha.
    speak("I am Your Game partner, My Name is Alpha")
    print()
    while True:   # "while True" is infinitly run the loop when the condition is false.
        print("Play  this game please tell 'START GAME'.")  # Start Game
        speak("Play  this game please tell 'START GAME'")
        print("Close this game please tell 'CLOSE GAME'.")  # End Game
        speak("Close this game please tell 'CLOSE GAME'")
        print()

        play=takecommand().lower()
        if "start game" in play:
            print("It is your time. Know your are going to play this Game very Carefully.")      # User Instructions
            speak("It  is  your  time. Know  your  are  going  to  play  this  Game  very  Carefully")
            time.sleep(2)  # sleep() function is used to  delay in the execution of program with 2 seconds.
            print("Your Game is know has been starting ........")
            speak("Your Game is know has been starting")
            print()
            time.sleep(2)  # sleep() function is used to  delay in the execution of program with 2 seconds.
            print("  Rule No 1 :  Imagine Any Number in Your Mind.")    # Ask an audience member to choose any number.
            speak("Rule Number 1, Imagine Any Number in Your Mind.")
            time.sleep(5)
            print("  Rule No 2 :  You can Multiply their chosen number by 2.")          # Tell your audience to Multiply their New Number by 2.
            speak("Rule Number 2, You can Multiply their chosen number by 2.")
            time.sleep(7)
            print("  Rule No 3 :  You can adding their multiplied number by 10.")       # It is your choice, you can give any number.
            speak("Rule Number 3, You can adding their multiplied number by 10.")       # But The answer is half of the number you given. (eg: answer is : given no/2)
            time.sleep(9)
            print("  Rule No 4 :  You can divide their Added  number by 2.")            # Tell your audience to divide their New number by 2
            speak("Rule Number 4, You can divide their Added  number by 2.")
            time.sleep(9)
            print("  Rule No 5 :  You can subtract thier Original number with your divided number.")   #Instruct the audience to Subtract Current Number with original Number.
            speak("Rule Number 5, You can subtract thier Original number with your divided number.")
            print()
            time.sleep(9)
            print("Ok, Your are sccessfully complete the Rules of This Game")  
            speak("Ok, Your are sccessfully complete the Rules of This Game")
            time.sleep(1)
            print("Do not worry, I find your imagine Number ")
            speak("Do not worry, I find your imagine Number ")
            time.sleep(5)
            print()
            print("Your Imagine Number is : '5'")     # It is Your answer.
            speak("Your Imagine Number is : '5'")     # The answer is half of the number you given.
            print()
            time.sleep(1)
            print("Please, Give Feedback About This Game")
            speak("Please, Give Feedback About This Game")
            time.sleep(2)
        elif "close game" in play:
            print("Ok, I know you are very happy to Play this game. So, You Close The Game. Know, the Game has been closed.")
            print("See You Next Time, GoodBye")
            speak("Ok ,I  know  you  are  very  happy  to  Play  this  game  So, You  Close  The  Game  Know, the  Game  has  been  closed")
            speak("See You Next Time, GoodBye")
            exit() 

        else:
            print("Sorry You Could Not 'START' or 'CLOSE' The game.")
            print("So, Please Play The Game")
            speak("Sorry  You  Could  Not  'START'  OR  'CLOSE'  The  game.")
            speak("So, Please Play  The  Game")
            print()
            time.sleep(3)  # sleep() function is used to  delay in the execution of program with 2 seconds.
    