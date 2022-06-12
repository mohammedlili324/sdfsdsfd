import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio.session import download
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio.platform import *
from pywebio import STATIC_PATH
from flask import Flask,send_from_directory
import random
import time
import speech_recognition as sr
import pyttsx3


app = Flask(__name__)




# Initialize the recognizer
r = sr.Recognizer()


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak
def rr():


            while (1):

                # Exception handling to handle
                # exceptions at the runtime


                    # use the microphone as source for input.
                    with sr.Microphone() as source2:

                        # wait for a second to let the recognizer
                        # adjust the energy threshold based on
                        # the surrounding noise level
                        r.adjust_for_ambient_noise(source2, duration=0.1)

                        # listens for the user's input
                        audio2 = r.listen(source2)

                        # Using google to recognize audio
                        MyText = r.recognize_google(audio2)
                        MyText = MyText.lower()

                        put_text(MyText)
                        SpeakText(MyText)



def start():
    put_html('<hr>')
    put_grid([[None,None,None,None,put_button(label='Speek',onclick=rr),None,None,None]])

app.add_url_rule('/tool','webio.view',webio_view(start)
                 ,methods=['GET','POST','OPTIONS'])

if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(start,port=args.port,debug=True)
