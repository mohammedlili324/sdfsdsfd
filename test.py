import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio.session import download
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio.platform import *
from pywebio import STATIC_PATH
from flask import Flask,send_from_directory
import cv2

app = Flask(__name__)

def start():
    def tk():
        a = cv2.VideoCapture(0)
        ret, im = a.read()
        cv2.imwrite('asdasd.png', im)

        img = open(r'asdasd.png', 'rb').read()
        popup('', put_image(img))

    put_grid([[None,None,put_button(label='take pic',onclick=tk),None,None]])

app.add_url_rule('/tool','webio.view',webio_view(start)
                 ,methods=['GET','POST','OPTIONS'])

if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(start,port=args.port,debug=True)
