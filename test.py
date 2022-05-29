import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask,send_from_directory
import tkinter as tk
from tkinter.filedialog import askopenfile
import pandas as pd


app = Flask(__name__)



def start():


        put_button('sdf',onclick=None)



app.add_url_rule('/tool','webio.view',webio_view(start)
                 ,provide_automatic_options=True,methods=['GET','POST','OPTIONS','PUT'])

if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(start,port=args.port)
