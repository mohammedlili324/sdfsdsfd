import argparse
import pandas as pd
from pywebio.output import *
from pywebio import start_server
import tkinter as tk
from tkinter.filedialog import askopenfile







def o():
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
    put_button(label='dsf',onclick=s)


if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p" , "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(o,port=args.port)
