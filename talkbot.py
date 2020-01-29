#Importing necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import pyttsx3

#Defining talkbot profile
bot = ChatBot('CHOTTU')
bot.set_trainer(ChatterBotCorpusTrainer)

#invoking this factory function gives reference to speech synthesizer engine
talk = pyttsx3.init()

#Training the talkbot
bot.train("chatterbot.corpus.english")

#Talkbot Activity
while True:
    speech = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:                                                                       
        print("Chottu listening..")
        audio = speech.listen(source)
        
    try:
        message=speech.recognize_google(audio)
        print("You: ",message)
        
        if(message=="see you later"):
            reply="Thankyou for talking, Bye"
            print("{}: {}".format(bot.name, reply))
            talk.say(reply)
            talk.runAndWait()
            break
            
        else:
            reply=str(bot.get_response(message))
        
    except:
        reply ="Pardon, Chottu listening again"
        
    print("{}: {}".format(bot.name,reply))
    print()
    
    talk.say(reply)
    talk.runAndWait()
