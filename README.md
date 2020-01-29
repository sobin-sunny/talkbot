# Talkbot
Create a TalkBot to which you could talk and hear them talking back to you

A talk-bot or voice-bot is an advanced chat-bot which will recognize the speech and speak back the replies. Inorder to do this, firstly it's necessary to understand how this works.
### ALGORITHM FLOW
Get input as speech ---> Recognize the speech ---> Convert speech to text ---> Use algorithm ---> Get response as text from corpus ---> Convert the response text to speech ---> Speak the reply

### Requirements
Microphone                   - Inorder to get input speech
Speech Recognition Module    - Inorder to recognize the speech input
Speech synthesizer (pyttsx3) - Inorder to convert text to speech
Chatterbot module            - Inorder to work NLP on corpus

### Installation commands
   #### pip install speechrecognition
   #### pip install PyAudio
   #### pip install pyttsx3

If PyAudio shows problems on installation, download suitable wheel for your system configuration from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio and then try pip installation command for that wheel file.
#### pip install NAME_OF_THE_WHEEL_WITH_WHL_EXTENSION

If that wheel file fails, try another wheel file for PyAudio and keep trying. Nothing working, if applicable for your system configuration, go for
#### pip install pipwin
#### pipwin install PyAudio
