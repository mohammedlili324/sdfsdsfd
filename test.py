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


def s():
        window = tk.Tk()

        file = askopenfile(filetypes=[('csv Files', '*.csv')])
        pdf_file = open(file.name, 'rb')

        s = pd.read_csv(pdf_file)
        h = open('dsf.html', 'w')
        e = s.to_html(h)
        h.close()
        put_html(e)

        se = open('dsf.html', 'rb').read()
        put_file('dsf.html', se, 'dsf.html')
        window.destroy()
def start():


        put_button(label='dsf', onclick=s)



app.add_url_rule('/tool','webio.view',webio_view(start,s)
                 ,provide_automatic_options=True,methods=['GET','POST','OPTIONS'])

if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p" , "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(start,port=args.port)
