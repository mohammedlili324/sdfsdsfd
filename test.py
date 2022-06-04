import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask,send_from_directory
import random
from pytube import YouTube


app = Flask(__name__)



def tryy():
    with use_scope(name='link', clear=True):
        clear(scope='start')
        put_grid([[None, None, None, put_html('''<svg xmlns="http://www.w3.org/2000/svg" style="margin:auto;background:#ffffff;display:block;" width="216" height="34" preserveAspectRatio="xMidYMid">
                <style type="text/css">
                  text {
                    text-anchor: middle; font-size: 30px; opacity: 0;
                  }
                </style>
                <g style="transform-origin:108px 17px;transform:scale(1)">
                <g transform="translate(108,17)">
                  <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -93.72px 4.15828px; animation: 1s linear -0.621176s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M9.75-15.15L9.75-15.15L9.75-15.15Q11.67-15.15 12.97-13.47L12.97-13.47L12.97-13.47Q14.28-11.79 14.28-8.94L14.28-8.94L14.28-8.94Q14.28-4.95 12.22-2.48L12.22-2.48L12.22-2.48Q10.17 0 7.11 0L7.11 0L7.11 0Q6.48 0 5.70-0.09L5.70-0.09L5.85 5.64L1.74 6.39L2.13-7.29L2.16-7.29L2.16-7.29Q2.04-11.31 1.50-14.49L1.50-14.49L5.13-15.27L5.13-15.27Q5.31-13.68 5.43-12.12L5.43-12.12L5.43-12.12Q5.49-12.27 6.04-12.95L6.04-12.95L6.04-12.95Q6.60-13.62 7.68-14.38L7.68-14.38L7.68-14.38Q8.76-15.15 9.75-15.15zM8.58-11.25L8.58-11.25L8.58-11.25Q6.99-11.25 5.49-10.38L5.49-10.38L5.49-7.80L5.61-3.51L5.61-3.51Q7.23-3.24 8.07-3.24L8.07-3.24L8.07-3.24Q10.95-3.24 10.95-7.25L10.95-7.25L10.95-7.25Q10.95-11.25 8.58-11.25" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -78.63px 1.00828px; animation: 1s linear -0.582353s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M20.37 0L20.37 0L20.37 0Q18.75 0 17.74-1.06L17.74-1.06L17.74-1.06Q16.74-2.13 16.74-3.87L16.74-3.87L16.92-7.32L16.59-14.52L20.61-15.27L20.22-6.15L20.22-6.15Q20.22-4.86 20.68-4.26L20.68-4.26L20.68-4.26Q21.15-3.66 22.17-3.66L22.17-3.66L22.17-3.66Q23.19-3.66 24.99-4.68L24.99-4.68L24.99-6.48L24.66-14.37L28.71-15.12L28.35-7.62L28.38-5.16L28.38-5.16Q28.38-3.24 29.37-1.29L29.37-1.29L26.25 0.09L26.25 0.09Q25.26-1.86 25.05-3.03L25.05-3.03L25.05-3.03Q22.35 0 20.37 0" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -65.76px -0.686717px; animation: 1s linear -0.543529s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M31.50-14.52L33.24-14.52L33.24-17.79L37.29-18.57L36.90-14.52L40.53-14.52L40.20-12.06L36.78-12.06L36.63-5.79L36.63-5.79Q36.63-4.38 36.90-3.92L36.90-3.92L36.90-3.92Q37.17-3.45 37.89-3.45L37.89-3.45L37.89-3.45Q38.61-3.45 39.81-3.78L39.81-3.78L39.99-1.65L39.99-1.65Q38.01 0 36.51 0L36.51 0L36.51 0Q35.01 0 34.05-1.09L34.05-1.09L34.05-1.09Q33.09-2.19 33.09-3.96L33.09-3.96L33.27-7.32L33.24-12.06L31.17-12.06L31.50-14.52" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -49.08px 4.26328px; animation: 1s linear -0.504706s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M51.63 6.60L47.76 5.79L50.85-1.14L48.63-7.20L45.60-14.49L49.59-15.24L51.51-8.85L52.50-5.82L52.89-5.82L53.61-8.01L55.77-15.27L59.46-14.82L54.15-0.87L51.63 6.60" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -34.83px 1.03828px; animation: 1s linear -0.465882s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M60.39-6.27L60.39-6.27Q60.39-10.11 62.46-12.78L62.46-12.78L62.46-12.78Q64.53-15.45 67.30-15.45L67.30-15.45L67.30-15.45Q70.08-15.45 71.63-13.65L71.63-13.65L71.63-13.65Q73.17-11.85 73.17-8.88L73.17-8.88L73.17-8.88Q73.17-4.92 71.17-2.29L71.17-2.29L71.17-2.29Q69.18 0.33 66.15 0.33L66.15 0.33L66.15 0.33Q63.66 0.33 62.02-1.54L62.02-1.54L62.02-1.54Q60.39-3.42 60.39-6.27L60.39-6.27zM69.81-7.32L69.81-7.32L69.81-7.32Q69.81-11.67 66.84-11.67L66.84-11.67L66.84-11.67Q63.75-11.67 63.75-7.59L63.75-7.59L63.75-7.59Q63.75-5.46 64.62-4.26L64.62-4.26L64.62-4.26Q65.49-3.06 66.91-3.06L66.91-3.06L66.91-3.06Q68.34-3.06 69.08-4.16L69.08-4.16L69.08-4.16Q69.81-5.25 69.81-7.32" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -19.65px 1.00828px; animation: 1s linear -0.427059s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M79.35 0L79.35 0L79.35 0Q77.73 0 76.72-1.06L76.72-1.06L76.72-1.06Q75.72-2.13 75.72-3.87L75.72-3.87L75.90-7.32L75.57-14.52L79.59-15.27L79.20-6.15L79.20-6.15Q79.20-4.86 79.66-4.26L79.66-4.26L79.66-4.26Q80.13-3.66 81.15-3.66L81.15-3.66L81.15-3.66Q82.17-3.66 83.97-4.68L83.97-4.68L83.97-6.48L83.64-14.37L87.69-15.12L87.33-7.62L87.36-5.16L87.36-5.16Q87.36-3.24 88.35-1.29L88.35-1.29L85.23 0.09L85.23 0.09Q84.24-1.86 84.03-3.03L84.03-3.03L84.03-3.03Q81.33 0 79.35 0" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -6.77998px -0.686717px; animation: 1s linear -0.388235s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M90.48-14.52L92.22-14.52L92.22-17.79L96.27-18.57L95.88-14.52L99.51-14.52L99.18-12.06L95.76-12.06L95.61-5.79L95.61-5.79Q95.61-4.38 95.88-3.92L95.88-3.92L95.88-3.92Q96.15-3.45 96.87-3.45L96.87-3.45L96.87-3.45Q97.59-3.45 98.79-3.78L98.79-3.78L98.97-1.65L98.97-1.65Q96.99 0 95.49 0L95.49 0L95.49 0Q93.99 0 93.03-1.09L93.03-1.09L93.03-1.09Q92.07-2.19 92.07-3.96L92.07-3.96L92.25-7.32L92.22-12.06L90.15-12.06L90.48-14.52" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 6.30001px 1.00828px; animation: 1s linear -0.349412s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M105.30 0L105.30 0L105.30 0Q103.68 0 102.67-1.06L102.67-1.06L102.67-1.06Q101.67-2.13 101.67-3.87L101.67-3.87L101.85-7.32L101.52-14.52L105.54-15.27L105.15-6.15L105.15-6.15Q105.15-4.86 105.61-4.26L105.61-4.26L105.61-4.26Q106.08-3.66 107.10-3.66L107.10-3.66L107.10-3.66Q108.12-3.66 109.92-4.68L109.92-4.68L109.92-6.48L109.59-14.37L113.64-15.12L113.28-7.62L113.31-5.16L113.31-5.16Q113.31-3.24 114.30-1.29L114.30-1.29L111.18 0.09L111.18 0.09Q110.19-1.86 109.98-3.03L109.98-3.03L109.98-3.03Q107.28 0 105.30 0" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 21.63px -3.01172px; animation: 1s linear -0.310588s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M124.95-15.15L124.95-15.15L124.95-15.15Q126.96-15.15 128.22-13.41L128.22-13.41L128.22-13.41Q129.48-11.67 129.48-8.94L129.48-8.94L129.48-8.94Q129.48-5.01 127.42-2.50L127.42-2.50L127.42-2.50Q125.37 0 122.10 0L122.10 0L122.10 0Q120.60 0 117.06-0.48L117.06-0.48L117.36-7.29L117.00-22.47L121.11-23.22L120.72-15.48L120.72-12.24L120.72-12.24Q121.05-12.72 121.53-13.26L121.53-13.26L121.53-13.26Q122.01-13.80 123.03-14.47L123.03-14.47L123.03-14.47Q124.05-15.15 124.95-15.15zM123.78-11.25L123.78-11.25L123.78-11.25Q122.40-11.25 120.72-10.41L120.72-10.41L120.72-7.80L120.90-3.39L120.90-3.39Q122.16-3.24 123.27-3.24L123.27-3.24L123.27-3.24Q126.15-3.24 126.15-7.25L126.15-7.25L126.15-7.25Q126.15-11.25 123.78-11.25" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 35.265px 1.03828px; animation: 1s linear -0.271765s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M137.37-3.06L137.37-3.06L137.37-3.06Q138.24-3.06 139.20-3.51L139.20-3.51L139.20-3.51Q140.16-3.96 140.70-4.41L140.70-4.41L141.24-4.86L142.62-3.18L142.62-3.18Q142.32-2.67 141.69-2.01L141.69-2.01L141.69-2.01Q141.06-1.35 140.41-0.89L140.41-0.89L140.41-0.89Q139.77-0.42 138.70-0.04L138.70-0.04L138.70-0.04Q137.64 0.33 136.50 0.33L136.50 0.33L136.50 0.33Q134.07 0.33 132.54-1.51L132.54-1.51L132.54-1.51Q131.01-3.36 131.01-6.27L131.01-6.27L131.01-6.27Q131.01-9.93 133.14-12.69L133.14-12.69L133.14-12.69Q135.27-15.45 138.12-15.45L138.12-15.45L138.12-15.45Q140.31-15.45 141.52-14.22L141.52-14.22L141.52-14.22Q142.74-12.99 142.74-10.77L142.74-10.77L142.74-10.77Q142.74-9.45 142.29-7.77L142.29-7.77L141.69-7.14L134.19-6.45L134.19-6.45Q134.70-3.06 137.37-3.06zM137.37-12.36L137.37-12.36L137.37-12.36Q136.05-12.36 135.15-11.29L135.15-11.29L135.15-11.29Q134.25-10.23 134.10-8.58L134.10-8.58L139.20-9.21L139.20-9.21Q139.29-9.90 139.29-10.35L139.29-10.35L139.29-10.35Q139.29-12.36 137.37-12.36" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 50.415px -3.01172px; animation: 1s linear -0.232941s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M149.97-22.47L154.08-23.22L153.69-7.80L154.02-0.75L149.97 0L150.33-7.29L149.97-22.47" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 57.945px 0.963283px; animation: 1s linear -0.194118s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M157.56-14.52L161.58-15.27L161.22-7.80L161.55-0.75L157.53 0L157.89-7.29L157.56-14.52" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 58.08px -11.2017px; animation: 1s linear -0.155294s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M157.35-19.66L157.35-19.66L157.35-19.66Q157.35-20.67 158.13-21.46L158.13-21.46L158.13-21.46Q158.91-22.26 159.93-22.26L159.93-22.26L159.93-22.26Q160.95-22.26 161.49-21.70L161.49-21.70L161.49-21.70Q162.03-21.15 162.03-20.04L162.03-20.04L162.03-20.04Q162.03-18.93 161.26-18.13L161.26-18.13L161.26-18.13Q160.50-17.34 159.50-17.34L159.50-17.34L159.50-17.34Q158.49-17.34 157.92-18L157.92-18L157.92-18Q157.35-18.66 157.35-19.66" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 69.3px 1.03828px; animation: 1s linear -0.116471s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M173.58-7.59L173.58-7.59Q173.58-9.66 173.22-10.35L173.22-10.35L173.22-10.35Q172.86-11.04 171.54-11.04L171.54-11.04L171.54-11.04Q170.22-11.04 168.54-9.99L168.54-9.99L168.54-7.80L168.87-0.75L164.85 0L165.21-7.29L165.21-7.29Q165.09-11.31 164.55-14.49L164.55-14.49L168.18-15.27L168.18-15.27Q168.39-13.53 168.48-11.88L168.48-11.88L168.48-11.88Q168.93-12.48 169.50-13.06L169.50-13.06L169.50-13.06Q170.07-13.65 171.30-14.38L171.30-14.38L171.30-14.38Q172.53-15.12 173.89-15.12L173.89-15.12L173.89-15.12Q175.26-15.12 176.19-14.05L176.19-14.05L176.19-14.05Q177.12-12.99 177.12-11.16L177.12-11.16L176.94-7.80L177.27-0.60L173.22 0.15L173.58-7.59" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 85.35px -2.86172px; animation: 1s linear -0.0776471s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M193.35-1.98L189.93 0.30L184.29-8.01L184.29-7.80L184.62-0.75L180.57 0L180.93-7.29L180.57-22.47L184.68-23.22L184.29-8.73L190.29-15.30L193.11-13.38L187.86-8.46L193.35-1.98" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 99.675px 6.46828px; animation: 1s linear -0.0388235s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M199.11-1.96L199.11-1.96L199.11-1.96Q199.11-2.97 199.83-3.71L199.83-3.71L199.83-3.71Q200.55-4.44 201.51-4.44L201.51-4.44L201.51-4.44Q202.47-4.44 202.97-3.92L202.97-3.92L202.97-3.92Q203.46-3.39 203.46-2.37L203.46-2.37L203.46-2.37Q203.46-1.35 202.77-0.58L202.77-0.58L202.77-0.58Q202.08 0.18 201.13 0.18L201.13 0.18L201.13 0.18Q200.19 0.18 199.65-0.39L199.65-0.39L199.65-0.39Q199.11-0.96 199.11-1.96" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 100.845px -5.54672px; animation: 1s linear 0s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M200.19-20.25L204.72-21L203.04-7.71L200.19-7.29L200.19-20.25" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-101.6099853515625,8.598283116957722)" style="fill: rgb(81, 202, 204);"></path></g></g>
                </g>
                </g>
                </svg>'''), None, None, None]])

    with use_scope(name='try', clear=True):

        url = input('', type=TEXT, required=True)
        put_grid([[None, None, None, put_html('''<svg xmlns="http://www.w3.org/2000/svg" style="margin:auto;background:#ffffff;display:block;" width="150" height="20" preserveAspectRatio="xMidYMid">
                        <style type="text/css">
                          text {
                            text-anchor: middle; font-size: 18px; opacity: 0;
                          }
                        </style>
                        <g style="transform-origin:75px 10px;transform:scale(1)">
                        <g transform="translate(75,10)">
                          <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -57.43px -1.2586px; animation: 100s linear -62.1176s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M5.27 0.20L5.27 0.20L5.27 0.20Q3.28 0.20 1.91-1.48L1.91-1.48L1.91-1.48Q0.54-3.15 0.54-5.58L0.54-5.58L0.54-5.58Q0.54-8.55 2.19-10.58L2.19-10.58L2.19-10.58Q3.83-12.62 6.23-12.62L6.23-12.62L6.23-12.62Q7.16-12.62 7.97-12.43L7.97-12.43L7.97-12.43Q8.77-12.24 9.11-12.04L9.11-12.04L9.43-11.84L8.21-9.34L8.21-9.34Q7.79-9.70 7.04-10.02L7.04-10.02L7.04-10.02Q6.28-10.33 5.67-10.33L5.67-10.33L5.67-10.33Q4.43-10.33 3.68-9.31L3.68-9.31L3.68-9.31Q2.93-8.28 2.93-6.38L2.93-6.38L2.93-6.38Q2.93-4.48 3.71-3.27L3.71-3.27L3.71-3.27Q4.48-2.05 5.81-2.05L5.81-2.05L5.81-2.05Q6.68-2.05 7.38-2.59L7.38-2.59L7.38-2.59Q8.08-3.13 8.37-4.03L8.37-4.03L9.86-3.17L9.86-3.17Q9.27-1.58 8.05-0.69L8.05-0.69L8.05-0.69Q6.82 0.20 5.27 0.20" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -49.13px 0.371399px; animation: 100s linear -58.2353s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M10.76-8.69L10.76-8.69L12.94-9.16L12.94-9.16Q13.10-7.78 13.16-6.53L13.16-6.53L13.16-6.53Q14.80-9.07 16.24-9.07L16.24-9.07L16.04-6.26L16.04-6.26Q14.99-6.26 14.39-6.08L14.39-6.08L14.39-6.08Q13.79-5.89 13.16-5.33L13.16-5.33L13.16-4.68L13.36-0.45L10.94 0L11.16-4.37L11.16-4.37Q11.09-6.79 10.76-8.69" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -42.32px 0.416399px; animation: 100s linear -54.3529s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M20.61-1.84L20.61-1.84L20.61-1.84Q21.13-1.84 21.71-2.11L21.71-2.11L21.71-2.11Q22.28-2.38 22.61-2.65L22.61-2.65L22.93-2.92L23.76-1.91L23.76-1.91Q23.58-1.60 23.20-1.21L23.20-1.21L23.20-1.21Q22.82-0.81 22.44-0.53L22.44-0.53L22.44-0.53Q22.05-0.25 21.41-0.03L21.41-0.03L21.41-0.03Q20.77 0.20 20.09 0.20L20.09 0.20L20.09 0.20Q18.63 0.20 17.71-0.91L17.71-0.91L17.71-0.91Q16.79-2.02 16.79-3.76L16.79-3.76L16.79-3.76Q16.79-5.96 18.07-7.61L18.07-7.61L18.07-7.61Q19.35-9.27 21.06-9.27L21.06-9.27L21.06-9.27Q22.37-9.27 23.10-8.53L23.10-8.53L23.10-8.53Q23.83-7.79 23.83-6.46L23.83-6.46L23.83-6.46Q23.83-5.67 23.56-4.66L23.56-4.66L23.20-4.28L18.70-3.87L18.70-3.87Q19.01-1.84 20.61-1.84zM20.61-7.42L20.61-7.42L20.61-7.42Q19.82-7.42 19.28-6.78L19.28-6.78L19.28-6.78Q18.74-6.14 18.65-5.15L18.65-5.15L21.71-5.53L21.71-5.53Q21.76-5.94 21.76-6.21L21.76-6.21L21.76-6.21Q21.76-7.42 20.61-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -34.1px 0.341399px; animation: 100s linear -50.4706s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M27.20 0L27.20 0Q26.14 0 25.46-0.68L25.46-0.68L25.46-0.68Q24.79-1.35 24.79-2.49L24.79-2.49L24.79-2.49Q24.79-3.64 25.83-4.47L25.83-4.47L25.83-4.47Q26.87-5.31 28.37-5.31L28.37-5.31L29.59-5.31L29.59-5.62L29.59-5.62Q29.59-6.50 29.23-6.82L29.23-6.82L29.23-6.82Q28.87-7.15 27.88-7.15L27.88-7.15L27.88-7.15Q27.47-7.15 26.90-6.98L26.90-6.98L26.90-6.98Q26.33-6.80 25.63-6.44L25.63-6.44L25.11-7.87L25.11-7.87Q25.88-8.41 26.99-8.84L26.99-8.84L26.99-8.84Q28.10-9.27 28.82-9.27L28.82-9.27L28.82-9.27Q31.64-9.27 31.64-6.53L31.64-6.53L31.64-3.01L31.64-3.01Q31.64-2.00 32.27-0.76L32.27-0.76L30.37 0.05L30.37 0.05Q29.92-0.81 29.70-1.49L29.70-1.49L29.70-1.49Q28.71 0 27.20 0L27.20 0zM27.95-1.84L27.95-1.84L27.95-1.84Q28.67-1.84 29.59-2.57L29.59-2.57L29.59-3.78L29.59-3.78Q28.64-4.00 28.04-4.00L28.04-4.00L28.04-4.00Q26.91-4.00 26.91-2.99L26.91-2.99L26.91-2.99Q26.91-2.47 27.20-2.15L27.20-2.15L27.20-2.15Q27.49-1.84 27.95-1.84" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -26.52px -0.618601px; animation: 100s linear -46.5882s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M33.50-8.71L34.54-8.71L34.54-10.67L36.97-11.14L36.74-8.71L38.92-8.71L38.72-7.24L36.67-7.24L36.58-3.47L36.58-3.47Q36.58-2.63 36.74-2.35L36.74-2.35L36.74-2.35Q36.90-2.07 37.33-2.07L37.33-2.07L37.33-2.07Q37.76-2.07 38.48-2.27L38.48-2.27L38.59-0.99L38.59-0.99Q37.40 0 36.50 0L36.50 0L36.50 0Q35.60 0 35.03-0.66L35.03-0.66L35.03-0.66Q34.45-1.31 34.45-2.38L34.45-2.38L34.56-4.39L34.54-7.24L33.30-7.24L33.50-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -19.46px 0.416399px; animation: 100s linear -42.7059s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M43.47-1.84L43.47-1.84L43.47-1.84Q43.99-1.84 44.57-2.11L44.57-2.11L44.57-2.11Q45.14-2.38 45.47-2.65L45.47-2.65L45.79-2.92L46.62-1.91L46.62-1.91Q46.44-1.60 46.06-1.21L46.06-1.21L46.06-1.21Q45.68-0.81 45.30-0.53L45.30-0.53L45.30-0.53Q44.91-0.25 44.27-0.03L44.27-0.03L44.27-0.03Q43.63 0.20 42.95 0.20L42.95 0.20L42.95 0.20Q41.49 0.20 40.57-0.91L40.57-0.91L40.57-0.91Q39.65-2.02 39.65-3.76L39.65-3.76L39.65-3.76Q39.65-5.96 40.93-7.61L40.93-7.61L40.93-7.61Q42.21-9.27 43.92-9.27L43.92-9.27L43.92-9.27Q45.23-9.27 45.96-8.53L45.96-8.53L45.96-8.53Q46.69-7.79 46.69-6.46L46.69-6.46L46.69-6.46Q46.69-5.67 46.42-4.66L46.42-4.66L46.06-4.28L41.56-3.87L41.56-3.87Q41.87-1.84 43.47-1.84zM43.47-7.42L43.47-7.42L43.47-7.42Q42.68-7.42 42.14-6.78L42.14-6.78L42.14-6.78Q41.60-6.14 41.51-5.15L41.51-5.15L44.57-5.53L44.57-5.53Q44.62-5.94 44.62-6.21L44.62-6.21L44.62-6.21Q44.62-7.42 43.47-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -11.025px -1.9136px; animation: 100s linear -38.8235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M53.01-1.76L53.01-1.76L53.01-1.76Q51.61 0 50.58 0L50.58 0L50.58 0Q49.30 0 48.48-1.04L48.48-1.04L48.48-1.04Q47.66-2.09 47.66-3.73L47.66-3.73L47.66-3.73Q47.66-5.98 48.91-7.52L48.91-7.52L48.91-7.52Q50.17-9.07 51.98-9.07L51.98-9.07L52.99-8.93L52.99-9.27L52.78-13.48L55.24-13.93L55.01-4.68L55.01-3.10L55.01-3.10Q55.01-2.02 55.55-0.61L55.55-0.61L53.60 0.20L53.60 0.20Q53.08-0.88 53.01-1.76zM49.68-4.66L49.68-4.66L49.68-4.66Q49.68-3.51 50.10-2.86L50.10-2.86L50.10-2.86Q50.53-2.21 51.33-2.21L51.33-2.21L51.33-2.21Q52.13-2.21 52.99-2.86L52.99-2.86L52.99-6.75L52.99-6.75Q51.91-6.97 51.39-6.97L51.39-6.97L51.39-6.97Q50.58-6.97 50.13-6.39L50.13-6.39L50.13-6.39Q49.68-5.81 49.68-4.66" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 1.18px -2.0136px; animation: 100s linear -34.9412s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M64.84-9.09L64.84-9.09L64.84-9.09Q66.04-9.09 66.80-8.05L66.80-8.05L66.80-8.05Q67.55-7.00 67.55-5.36L67.55-5.36L67.55-5.36Q67.55-3.01 66.32-1.50L66.32-1.50L66.32-1.50Q65.09 0 63.13 0L63.13 0L63.13 0Q62.23 0 60.10-0.29L60.10-0.29L60.28-4.37L60.07-13.48L62.53-13.93L62.30-9.29L62.30-7.34L62.30-7.34Q62.50-7.63 62.78-7.96L62.78-7.96L62.78-7.96Q63.07-8.28 63.68-8.69L63.68-8.69L63.68-8.69Q64.30-9.09 64.84-9.09zM64.13-6.75L64.13-6.75L64.13-6.75Q63.31-6.75 62.30-6.25L62.30-6.25L62.30-4.68L62.41-2.03L62.41-2.03Q63.16-1.94 63.83-1.94L63.83-1.94L63.83-1.94Q65.56-1.94 65.56-4.35L65.56-4.35L65.56-4.35Q65.56-6.75 64.13-6.75" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 9.52999px 2.3514px; animation: 100s linear -31.0588s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M71.62 3.96L69.30 3.47L71.15-0.68L69.82-4.32L68.00-8.69L70.40-9.14L71.55-5.31L72.14-3.49L72.38-3.49L72.81-4.81L74.11-9.16L76.32-8.89L73.13-0.52L71.62 3.96" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 23.695px 0.416399px; animation: 100s linear -27.1765s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M85.41-4.55L85.41-4.55Q85.41-5.80 85.19-6.21L85.19-6.21L85.19-6.21Q84.98-6.62 84.19-6.62L84.19-6.62L84.19-6.62Q83.39-6.62 82.39-5.99L82.39-5.99L82.39-4.68L82.58-0.45L80.17 0L80.39-4.37L80.39-4.37Q80.32-6.79 79.99-8.69L79.99-8.69L82.17-9.16L82.17-9.16Q82.30-8.12 82.35-7.13L82.35-7.13L82.35-7.13Q82.62-7.49 82.96-7.84L82.96-7.84L82.96-7.84Q83.30-8.19 84.04-8.63L84.04-8.63L84.04-8.63Q84.78-9.07 85.54-9.07L85.54-9.07L85.54-9.07Q86.29-9.07 86.81-8.59L86.81-8.59L86.81-8.59Q87.34-8.10 87.48-7.25L87.48-7.25L87.48-7.25Q88.97-9.07 90.50-9.07L90.50-9.07L90.50-9.07Q91.46-9.07 92.02-8.43L92.02-8.43L92.02-8.43Q92.57-7.79 92.57-6.70L92.57-6.70L92.47-4.68L92.66-0.36L90.23 0.09L90.45-4.55L90.45-4.55Q90.45-5.80 90.23-6.21L90.23-6.21L90.23-6.21Q90.02-6.62 89.24-6.62L89.24-6.62L89.24-6.62Q88.47-6.62 87.50-6.03L87.50-6.03L87.43-4.68L87.62-0.36L85.19 0.09L85.41-4.55" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 35.305px 0.416399px; animation: 100s linear -23.2941s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M94.10-3.76L94.10-3.76Q94.10-6.07 95.35-7.67L95.35-7.67L95.35-7.67Q96.59-9.27 98.25-9.27L98.25-9.27L98.25-9.27Q99.92-9.27 100.85-8.19L100.85-8.19L100.85-8.19Q101.77-7.11 101.77-5.33L101.77-5.33L101.77-5.33Q101.77-2.95 100.58-1.38L100.58-1.38L100.58-1.38Q99.38 0.20 97.56 0.20L97.56 0.20L97.56 0.20Q96.07 0.20 95.09-0.93L95.09-0.93L95.09-0.93Q94.10-2.05 94.10-3.76L94.10-3.76zM99.76-4.39L99.76-4.39L99.76-4.39Q99.76-7.00 97.97-7.00L97.97-7.00L97.97-7.00Q96.12-7.00 96.12-4.55L96.12-4.55L96.12-4.55Q96.12-3.28 96.64-2.56L96.64-2.56L96.64-2.56Q97.16-1.84 98.02-1.84L98.02-1.84L98.02-1.84Q98.87-1.84 99.32-2.49L99.32-2.49L99.32-2.49Q99.76-3.15 99.76-4.39" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.885px 0.371399px; animation: 100s linear -19.4118s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M103.32-8.71L105.73-9.16L105.52-4.68L105.71-0.45L103.30 0L103.52-4.37L103.32-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.965px -6.9286px; animation: 100s linear -15.5294s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M103.19-11.80L103.19-11.80L103.19-11.80Q103.19-12.40 103.66-12.88L103.66-12.88L103.66-12.88Q104.13-13.36 104.74-13.36L104.74-13.36L104.74-13.36Q105.35-13.36 105.68-13.02L105.68-13.02L105.68-13.02Q106.00-12.69 106.00-12.02L106.00-12.02L106.00-12.02Q106.00-11.36 105.54-10.88L105.54-10.88L105.54-10.88Q105.08-10.40 104.48-10.40L104.48-10.40L104.48-10.40Q103.88-10.40 103.54-10.80L103.54-10.80L103.54-10.80Q103.19-11.20 103.19-11.80" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 48.025px 0.416399px; animation: 100s linear -11.6471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M110.95-1.84L110.95-1.84L110.95-1.84Q111.47-1.84 112.05-2.11L112.05-2.11L112.05-2.11Q112.63-2.38 112.95-2.65L112.95-2.65L113.27-2.92L114.10-1.91L114.10-1.91Q113.92-1.60 113.54-1.21L113.54-1.21L113.54-1.21Q113.17-0.81 112.78-0.53L112.78-0.53L112.78-0.53Q112.39-0.25 111.75-0.03L111.75-0.03L111.75-0.03Q111.11 0.20 110.43 0.20L110.43 0.20L110.43 0.20Q108.97 0.20 108.05-0.91L108.05-0.91L108.05-0.91Q107.14-2.02 107.14-3.76L107.14-3.76L107.14-3.76Q107.14-5.96 108.41-7.61L108.41-7.61L108.41-7.61Q109.69-9.27 111.40-9.27L111.40-9.27L111.40-9.27Q112.72-9.27 113.45-8.53L113.45-8.53L113.45-8.53Q114.17-7.79 114.17-6.46L114.17-6.46L114.17-6.46Q114.17-5.67 113.90-4.66L113.90-4.66L113.54-4.28L109.04-3.87L109.04-3.87Q109.35-1.84 110.95-1.84zM110.95-7.42L110.95-7.42L110.95-7.42Q110.16-7.42 109.62-6.78L109.62-6.78L109.62-6.78Q109.08-6.14 108.99-5.15L108.99-5.15L112.05-5.53L112.05-5.53Q112.10-5.94 112.10-6.21L112.10-6.21L112.10-6.21Q112.10-7.42 110.95-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.305px 0.371399px; animation: 100s linear -7.76471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M115.74-8.71L118.15-9.16L117.94-4.68L118.13-0.45L115.72 0L115.94-4.37L115.74-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.385px -6.9286px; animation: 100s linear -3.88235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M115.61-11.80L115.61-11.80L115.61-11.80Q115.61-12.40 116.08-12.88L116.08-12.88L116.08-12.88Q116.55-13.36 117.16-13.36L117.16-13.36L117.16-13.36Q117.77-13.36 118.10-13.02L118.10-13.02L118.10-13.02Q118.42-12.69 118.42-12.02L118.42-12.02L118.42-12.02Q118.42-11.36 117.96-10.88L117.96-10.88L117.96-10.88Q117.50-10.40 116.90-10.40L116.90-10.40L116.90-10.40Q116.30-10.40 115.96-10.80L115.96-10.80L115.96-10.80Q115.61-11.20 115.61-11.80" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 59.875px 0.416399px; animation: 100s linear 0s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M122.85-1.67L122.85-1.67L122.85-1.67Q123.79-1.67 123.79-2.50L123.79-2.50L123.79-2.50Q123.79-2.79 123.38-3.04L123.38-3.04L123.38-3.04Q122.98-3.29 122.39-3.55L122.39-3.55L122.39-3.55Q121.81-3.80 121.22-4.11L121.22-4.11L121.22-4.11Q120.64-4.43 120.23-4.99L120.23-4.99L120.23-4.99Q119.83-5.54 119.83-6.26L119.83-6.26L119.83-6.26Q119.83-7.47 120.89-8.37L120.89-8.37L120.89-8.37Q121.95-9.27 123.34-9.27L123.34-9.27L123.34-9.27Q123.98-9.27 124.61-9.12L124.61-9.12L124.61-9.12Q125.23-8.96 125.80-8.64L125.80-8.64L124.60-6.44L124.60-6.44Q124.47-6.55 124.27-6.71L124.27-6.71L124.27-6.71Q124.07-6.88 123.53-7.14L123.53-7.14L123.53-7.14Q122.98-7.40 122.55-7.40L122.55-7.40L122.55-7.40Q122.13-7.40 121.91-7.21L121.91-7.21L121.91-7.21Q121.68-7.02 121.68-6.69L121.68-6.69L121.68-6.69Q121.68-6.35 122.30-6.02L122.30-6.02L122.30-6.02Q122.92-5.69 123.66-5.41L123.66-5.41L123.66-5.41Q124.40-5.13 125.02-4.49L125.02-4.49L125.02-4.49Q125.64-3.85 125.64-2.97L125.64-2.97L125.64-2.97Q125.64-1.71 124.61-0.76L124.61-0.76L124.61-0.76Q123.57 0.20 122.22 0.20L122.22 0.20L122.22 0.20Q121.36 0.20 120.61-0.18L120.61-0.18L120.61-0.18Q119.86-0.56 119.54-0.94L119.54-0.94L119.21-1.31L120.64-2.97L120.64-2.97Q120.74-2.83 120.94-2.61L120.94-2.61L120.94-2.61Q121.14-2.39 121.73-2.03L121.73-2.03L121.73-2.03Q122.31-1.67 122.85-1.67" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g></g>
                        </g>
                        </g>
                        </svg>'''), None, None, None]])
        clear(scope='link')
        w = YouTube(url)


        with use_scope(name='name', clear=True):
            toast('Please wait, the video is being downloaded ....', onclick=
            True, )
            s = [x for x in range(0, 1000000)]
            put_html('<hr>')
            put_grid([[None, None, None, None, put_html('''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin:auto;background:#fff;display:block;" width="200px" height="200px" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                                <defs>
                                  <filter id="ldio-ljejml75zfq-filter" x="-100%" y="-100%" width="300%" height="300%" color-interpolation-filters="sRGB">
                                    <feGaussianBlur in="SourceGraphic" stdDeviation="2.4000000000000004"></feGaussianBlur>
                                    <feComponentTransfer result="cutoff">
                                      <feFuncA type="table" tableValues="0 0 0 0 0 0 1 1 1 1 1"></feFuncA>
                                    </feComponentTransfer>
                                  </filter>
                                </defs>
                                <g filter="url(#ldio-ljejml75zfq-filter)"><g transform="translate(50 50)">
                                <g>
                                  <circle cx="17" cy="0" r="5" fill="#ec1c24">
                                    <animate attributeName="r" keyTimes="0;0.5;1" values="3.5999999999999996;8.399999999999999;3.5999999999999996" dur="4s" repeatCount="indefinite" begin="-0.25s"></animate>
                                  </circle>
                                  <animateTransform attributeName="transform" type="rotate" keyTimes="0;1" values="0;360" dur="4s" repeatCount="indefinite" begin="0s"></animateTransform>
                                </g>
                                </g><g transform="translate(50 50)">
                                <g>
                                  <circle cx="17" cy="0" r="5" fill="#fdbd10">
                                    <animate attributeName="r" keyTimes="0;0.5;1" values="3.5999999999999996;8.399999999999999;3.5999999999999996" dur="2s" repeatCount="indefinite" begin="-0.2s"></animate>
                                  </circle>
                                  <animateTransform attributeName="transform" type="rotate" keyTimes="0;1" values="0;360" dur="2s" repeatCount="indefinite" begin="-0.05s"></animateTransform>
                                </g>
                                </g><g transform="translate(50 50)">
                                <g>
                                  <circle cx="17" cy="0" r="5" fill="#0066b2">
                                    <animate attributeName="r" keyTimes="0;0.5;1" values="3.5999999999999996;8.399999999999999;3.5999999999999996" dur="1.3333333333333333s" repeatCount="indefinite" begin="-0.15s"></animate>
                                  </circle>
                                  <animateTransform attributeName="transform" type="rotate" keyTimes="0;1" values="0;360" dur="1.3333333333333333s" repeatCount="indefinite" begin="-0.1s"></animateTransform>
                                </g>
                                </g><g transform="translate(50 50)">
                                <g>
                                  <circle cx="17" cy="0" r="5" fill="#ec1c24">
                                    <animate attributeName="r" keyTimes="0;0.5;1" values="3.5999999999999996;8.399999999999999;3.5999999999999996" dur="1s" repeatCount="indefinite" begin="-0.1s"></animate>
                                  </circle>
                                  <animateTransform attributeName="transform" type="rotate" keyTimes="0;1" values="0;360" dur="1s" repeatCount="indefinite" begin="-0.15s"></animateTransform>
                                </g>
                                </g><g transform="translate(50 50)">
                                <g>
                                  <circle cx="17" cy="0" r="5" fill="#fdbd10">
                                    <animate attributeName="r" keyTimes="0;0.5;1" values="3.5999999999999996;8.399999999999999;3.5999999999999996" dur="0.8s" repeatCount="indefinite" begin="-0.05s"></animate>
                                  </circle>
                                  <animateTransform attributeName="transform" type="rotate" keyTimes="0;1" values="0;360" dur="0.8s" repeatCount="indefinite" begin="-0.2s"></animateTransform>
                                </g>
                                </g></g>
                                </svg>'''), None, None, None, None]])
            u = str(random.choice(s)) + '.mp4'
            put_processbar('bar')
            for i in range(0, 111):
                set_processbar('bar', i / 100)
                w.streams.get_highest_resolution().download(filename=u)

    with use_scope(name='down', clear=True):
        clear(scope='name')
        put_html('<hr>')
        put_grid([[None, None, None, None, put_html('''<svg xmlns="http://www.w3.org/2000/svg" style="margin:auto;background:#ffffff;display:block;" width="295" height="34" preserveAspectRatio="xMidYMid">
                                                            <style type="text/css">
                                                              text {
                                                                text-anchor: middle; font-size: 26px; opacity: 0;
                                                              }
                                                            </style>
                                                            <g style="transform-origin: 147.5px 17px; transform: scale(0.866667);">
                                                            <g transform="translate(147.5,17)">
                                                              <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -157.56px -1.7503px; animation: 1s linear -0.6336s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M13.38 0L2.40 0L2.76-7.29L2.40-20.70L13.65-20.70L13.32-17.49L6.57-17.49L6.39-12.18L12.39-12.18L12.06-9L6.27-9L6.24-7.80L6.45-3.18L13.71-3.18L13.38 0" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -143.085px 1.0397px; animation: 1s linear -0.6072s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M25.20-7.59L25.20-7.59Q25.20-9.66 24.84-10.35L24.84-10.35L24.84-10.35Q24.48-11.04 23.16-11.04L23.16-11.04L23.16-11.04Q21.84-11.04 20.16-9.99L20.16-9.99L20.16-7.80L20.49-0.75L16.47 0L16.83-7.29L16.83-7.29Q16.71-11.31 16.17-14.49L16.17-14.49L19.80-15.27L19.80-15.27Q20.01-13.53 20.10-11.88L20.10-11.88L20.10-11.88Q20.55-12.48 21.12-13.06L21.12-13.06L21.12-13.06Q21.69-13.65 22.92-14.38L22.92-14.38L22.92-14.38Q24.15-15.12 25.52-15.12L25.52-15.12L25.52-15.12Q26.88-15.12 27.81-14.05L27.81-14.05L27.81-14.05Q28.74-12.99 28.74-11.16L28.74-11.16L28.56-7.80L28.89-0.60L24.84 0.15L25.20-7.59" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -129.645px -0.685297px; animation: 1s linear -0.5808s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M31.62-14.52L33.36-14.52L33.36-17.79L37.41-18.57L37.02-14.52L40.65-14.52L40.32-12.06L36.90-12.06L36.75-5.79L36.75-5.79Q36.75-4.38 37.02-3.92L37.02-3.92L37.02-3.92Q37.29-3.45 38.01-3.45L38.01-3.45L38.01-3.45Q38.73-3.45 39.93-3.78L39.93-3.78L40.11-1.65L40.11-1.65Q38.13 0 36.63 0L36.63 0L36.63 0Q35.13 0 34.17-1.09L34.17-1.09L34.17-1.09Q33.21-2.19 33.21-3.96L33.21-3.96L33.39-7.32L33.36-12.06L31.29-12.06L31.62-14.52" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -117.87px 1.0397px; animation: 1s linear -0.5544s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M48.24-3.06L48.24-3.06L48.24-3.06Q49.11-3.06 50.07-3.51L50.07-3.51L50.07-3.51Q51.03-3.96 51.57-4.41L51.57-4.41L52.11-4.86L53.49-3.18L53.49-3.18Q53.19-2.67 52.56-2.01L52.56-2.01L52.56-2.01Q51.93-1.35 51.29-0.89L51.29-0.89L51.29-0.89Q50.64-0.42 49.58-0.04L49.58-0.04L49.58-0.04Q48.51 0.33 47.37 0.33L47.37 0.33L47.37 0.33Q44.94 0.33 43.41-1.51L43.41-1.51L43.41-1.51Q41.88-3.36 41.88-6.27L41.88-6.27L41.88-6.27Q41.88-9.93 44.01-12.69L44.01-12.69L44.01-12.69Q46.14-15.45 48.99-15.45L48.99-15.45L48.99-15.45Q51.18-15.45 52.40-14.22L52.40-14.22L52.40-14.22Q53.61-12.99 53.61-10.77L53.61-10.77L53.61-10.77Q53.61-9.45 53.16-7.77L53.16-7.77L52.56-7.14L45.06-6.45L45.06-6.45Q45.57-3.06 48.24-3.06zM48.24-12.36L48.24-12.36L48.24-12.36Q46.92-12.36 46.02-11.29L46.02-11.29L46.02-11.29Q45.12-10.23 44.97-8.58L44.97-8.58L50.07-9.21L50.07-9.21Q50.16-9.90 50.16-10.35L50.16-10.35L50.16-10.35Q50.16-12.36 48.24-12.36" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -105.165px 0.964703px; animation: 1s linear -0.528s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M55.89-14.49L55.89-14.49L59.52-15.27L59.52-15.27Q59.79-12.96 59.88-10.89L59.88-10.89L59.88-10.89Q62.61-15.12 65.01-15.12L65.01-15.12L64.68-10.44L64.68-10.44Q62.94-10.44 61.94-10.13L61.94-10.13L61.94-10.13Q60.93-9.81 59.88-8.88L59.88-8.88L59.88-7.80L60.21-0.75L56.19 0L56.55-7.29L56.55-7.29Q56.43-11.31 55.89-14.49" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -88.875px 0.919703px; animation: 1s linear -0.5016s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M74.52 0L74.52 0Q72.75 0 71.63-1.13L71.63-1.13L71.63-1.13Q70.50-2.25 70.50-4.16L70.50-4.16L70.50-4.16Q70.50-6.06 72.24-7.46L72.24-7.46L72.24-7.46Q73.98-8.85 76.47-8.85L76.47-8.85L78.51-8.85L78.51-9.36L78.51-9.36Q78.51-10.83 77.91-11.37L77.91-11.37L77.91-11.37Q77.31-11.91 75.66-11.91L75.66-11.91L75.66-11.91Q74.97-11.91 74.03-11.63L74.03-11.63L74.03-11.63Q73.08-11.34 71.91-10.74L71.91-10.74L71.04-13.11L71.04-13.11Q72.33-14.01 74.17-14.73L74.17-14.73L74.17-14.73Q76.02-15.45 77.22-15.45L77.22-15.45L77.22-15.45Q81.93-15.45 81.93-10.89L81.93-10.89L81.93-5.01L81.93-5.01Q81.93-3.33 82.98-1.26L82.98-1.26L79.80 0.09L79.80 0.09Q79.05-1.35 78.69-2.49L78.69-2.49L78.69-2.49Q77.04 0 74.52 0L74.52 0zM75.78-3.06L75.78-3.06L75.78-3.06Q76.98-3.06 78.51-4.29L78.51-4.29L78.51-6.30L78.51-6.30Q76.92-6.66 75.93-6.66L75.93-6.66L75.93-6.66Q74.04-6.66 74.04-4.98L74.04-4.98L74.04-4.98Q74.04-4.11 74.52-3.58L74.52-3.58L74.52-3.58Q75-3.06 75.78-3.06" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -69.375px 1.0397px; animation: 1s linear -0.4752s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M98.91-7.59L98.91-7.59Q98.91-9.66 98.55-10.35L98.55-10.35L98.55-10.35Q98.19-11.04 96.87-11.04L96.87-11.04L96.87-11.04Q95.55-11.04 93.87-9.99L93.87-9.99L93.87-7.80L94.20-0.75L90.18 0L90.54-7.29L90.54-7.29Q90.42-11.31 89.88-14.49L89.88-14.49L93.51-15.27L93.51-15.27Q93.72-13.53 93.81-11.88L93.81-11.88L93.81-11.88Q94.26-12.48 94.83-13.06L94.83-13.06L94.83-13.06Q95.40-13.65 96.63-14.38L96.63-14.38L96.63-14.38Q97.86-15.12 99.22-15.12L99.22-15.12L99.22-15.12Q100.59-15.12 101.52-14.05L101.52-14.05L101.52-14.05Q102.45-12.99 102.45-11.16L102.45-11.16L102.27-7.80L102.60-0.60L98.55 0.15L98.91-7.59" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -54.495px 0.919703px; animation: 1s linear -0.4488s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M108.90 0L108.90 0Q107.13 0 106.00-1.13L106.00-1.13L106.00-1.13Q104.88-2.25 104.88-4.16L104.88-4.16L104.88-4.16Q104.88-6.06 106.62-7.46L106.62-7.46L106.62-7.46Q108.36-8.85 110.85-8.85L110.85-8.85L112.89-8.85L112.89-9.36L112.89-9.36Q112.89-10.83 112.29-11.37L112.29-11.37L112.29-11.37Q111.69-11.91 110.04-11.91L110.04-11.91L110.04-11.91Q109.35-11.91 108.41-11.63L108.41-11.63L108.41-11.63Q107.46-11.34 106.29-10.74L106.29-10.74L105.42-13.11L105.42-13.11Q106.71-14.01 108.55-14.73L108.55-14.73L108.55-14.73Q110.40-15.45 111.60-15.45L111.60-15.45L111.60-15.45Q116.31-15.45 116.31-10.89L116.31-10.89L116.31-5.01L116.31-5.01Q116.31-3.33 117.36-1.26L117.36-1.26L114.18 0.09L114.18 0.09Q113.43-1.35 113.07-2.49L113.07-2.49L113.07-2.49Q111.42 0 108.90 0L108.90 0zM110.16-3.06L110.16-3.06L110.16-3.06Q111.36-3.06 112.89-4.29L112.89-4.29L112.89-6.30L112.89-6.30Q111.30-6.66 110.31-6.66L110.31-6.66L110.31-6.66Q108.42-6.66 108.42-4.98L108.42-4.98L108.42-4.98Q108.42-4.11 108.90-3.58L108.90-3.58L108.90-3.58Q109.38-3.06 110.16-3.06" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -35.415px 1.0397px; animation: 1s linear -0.4224s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M128.67-7.59L128.67-7.59Q128.67-9.66 128.31-10.35L128.31-10.35L128.31-10.35Q127.95-11.04 126.63-11.04L126.63-11.04L126.63-11.04Q125.31-11.04 123.63-9.99L123.63-9.99L123.63-7.80L123.96-0.75L119.94 0L120.30-7.29L120.30-7.29Q120.18-11.31 119.64-14.49L119.64-14.49L123.27-15.27L123.27-15.27Q123.48-13.53 123.57-11.88L123.57-11.88L123.57-11.88Q124.02-12.48 124.59-13.06L124.59-13.06L124.59-13.06Q125.16-13.65 126.39-14.38L126.39-14.38L126.39-14.38Q127.62-15.12 128.88-15.12L128.88-15.12L128.88-15.12Q130.14-15.12 131.01-14.31L131.01-14.31L131.01-14.31Q131.88-13.50 132.12-12.09L132.12-12.09L132.12-12.09Q134.61-15.12 137.16-15.12L137.16-15.12L137.16-15.12Q138.75-15.12 139.68-14.05L139.68-14.05L139.68-14.05Q140.61-12.99 140.61-11.16L140.61-11.16L140.43-7.80L140.76-0.60L136.71 0.15L137.07-7.59L137.07-7.59Q137.07-9.66 136.71-10.35L136.71-10.35L136.71-10.35Q136.35-11.04 135.06-11.04L135.06-11.04L135.06-11.04Q133.77-11.04 132.15-10.05L132.15-10.05L132.03-7.80L132.36-0.60L128.31 0.15L128.67-7.59" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -16.65px 1.0397px; animation: 1s linear -0.396s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M149.46-3.06L149.46-3.06L149.46-3.06Q150.33-3.06 151.29-3.51L151.29-3.51L151.29-3.51Q152.25-3.96 152.79-4.41L152.79-4.41L153.33-4.86L154.71-3.18L154.71-3.18Q154.41-2.67 153.78-2.01L153.78-2.01L153.78-2.01Q153.15-1.35 152.50-0.89L152.50-0.89L152.50-0.89Q151.86-0.42 150.79-0.04L150.79-0.04L150.79-0.04Q149.73 0.33 148.59 0.33L148.59 0.33L148.59 0.33Q146.16 0.33 144.63-1.51L144.63-1.51L144.63-1.51Q143.10-3.36 143.10-6.27L143.10-6.27L143.10-6.27Q143.10-9.93 145.23-12.69L145.23-12.69L145.23-12.69Q147.36-15.45 150.21-15.45L150.21-15.45L150.21-15.45Q152.40-15.45 153.61-14.22L153.61-14.22L153.61-14.22Q154.83-12.99 154.83-10.77L154.83-10.77L154.83-10.77Q154.83-9.45 154.38-7.77L154.38-7.77L153.78-7.14L146.28-6.45L146.28-6.45Q146.79-3.06 149.46-3.06zM149.46-12.36L149.46-12.36L149.46-12.36Q148.14-12.36 147.24-11.29L147.24-11.29L147.24-11.29Q146.34-10.23 146.19-8.58L146.19-8.58L151.29-9.21L151.29-9.21Q151.38-9.90 151.38-10.35L151.38-10.35L151.38-10.35Q151.38-12.36 149.46-12.36" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 0.300011px -3.0103px; animation: 1s linear -0.3696s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M171-22.95L170.07-19.53L170.07-19.53Q168.96-19.80 168.06-19.80L168.06-19.80L168.06-19.80Q167.16-19.80 166.75-19.26L166.75-19.26L166.75-19.26Q166.35-18.72 166.35-17.37L166.35-17.37L166.32-14.52L169.56-14.52L169.23-12.06L166.32-12.06L166.29-7.80L166.62-0.75L162.57 0L162.93-7.29L162.81-12.06L160.83-12.06L161.16-14.52L162.75-14.52L162.72-16.80L162.72-16.80Q162.72-19.47 164.37-21.34L164.37-21.34L164.37-21.34Q166.02-23.22 168.39-23.22L168.39-23.22L168.39-23.22Q169.65-23.22 171-22.95L171-22.95" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 11.025px 1.0397px; animation: 1s linear -0.3432s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M170.25-6.27L170.25-6.27Q170.25-10.11 172.32-12.78L172.32-12.78L172.32-12.78Q174.39-15.45 177.16-15.45L177.16-15.45L177.16-15.45Q179.94-15.45 181.48-13.65L181.48-13.65L181.48-13.65Q183.03-11.85 183.03-8.88L183.03-8.88L183.03-8.88Q183.03-4.92 181.03-2.29L181.03-2.29L181.03-2.29Q179.04 0.33 176.01 0.33L176.01 0.33L176.01 0.33Q173.52 0.33 171.88-1.54L171.88-1.54L171.88-1.54Q170.25-3.42 170.25-6.27L170.25-6.27zM179.67-7.32L179.67-7.32L179.67-7.32Q179.67-11.67 176.70-11.67L176.70-11.67L176.70-11.67Q173.61-11.67 173.61-7.59L173.61-7.59L173.61-7.59Q173.61-5.46 174.48-4.26L174.48-4.26L174.48-4.26Q175.35-3.06 176.78-3.06L176.78-3.06L176.78-3.06Q178.20-3.06 178.94-4.16L178.94-4.16L178.94-4.16Q179.67-5.25 179.67-7.32" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 24.225px 0.964703px; animation: 1s linear -0.3168s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M185.28-14.49L185.28-14.49L188.91-15.27L188.91-15.27Q189.18-12.96 189.27-10.89L189.27-10.89L189.27-10.89Q192-15.12 194.40-15.12L194.40-15.12L194.07-10.44L194.07-10.44Q192.33-10.44 191.33-10.13L191.33-10.13L191.33-10.13Q190.32-9.81 189.27-8.88L189.27-8.88L189.27-7.80L189.60-0.75L185.58 0L185.94-7.29L185.94-7.29Q185.82-11.31 185.28-14.49" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 40.485px 4.2647px; animation: 1s linear -0.2904s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M205.20 6.60L201.33 5.79L204.42-1.14L202.20-7.20L199.17-14.49L203.16-15.24L205.08-8.85L206.07-5.82L206.46-5.82L207.18-8.01L209.34-15.27L213.03-14.82L207.72-0.87L205.20 6.60" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.735px 1.0397px; animation: 1s linear -0.264s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M213.96-6.27L213.96-6.27Q213.96-10.11 216.03-12.78L216.03-12.78L216.03-12.78Q218.10-15.45 220.88-15.45L220.88-15.45L220.88-15.45Q223.65-15.45 225.19-13.65L225.19-13.65L225.19-13.65Q226.74-11.85 226.74-8.88L226.74-8.88L226.74-8.88Q226.74-4.92 224.75-2.29L224.75-2.29L224.75-2.29Q222.75 0.33 219.72 0.33L219.72 0.33L219.72 0.33Q217.23 0.33 215.59-1.54L215.59-1.54L215.59-1.54Q213.96-3.42 213.96-6.27L213.96-6.27zM223.38-7.32L223.38-7.32L223.38-7.32Q223.38-11.67 220.41-11.67L220.41-11.67L220.41-11.67Q217.32-11.67 217.32-7.59L217.32-7.59L217.32-7.59Q217.32-5.46 218.19-4.26L218.19-4.26L218.19-4.26Q219.06-3.06 220.49-3.06L220.49-3.06L220.49-3.06Q221.91-3.06 222.65-4.16L222.65-4.16L222.65-4.16Q223.38-5.25 223.38-7.32" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 69.915px 1.0097px; animation: 1s linear -0.2376s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M232.92 0L232.92 0L232.92 0Q231.30 0 230.30-1.06L230.30-1.06L230.30-1.06Q229.29-2.13 229.29-3.87L229.29-3.87L229.47-7.32L229.14-14.52L233.16-15.27L232.77-6.15L232.77-6.15Q232.77-4.86 233.24-4.26L233.24-4.26L233.24-4.26Q233.70-3.66 234.72-3.66L234.72-3.66L234.72-3.66Q235.74-3.66 237.54-4.68L237.54-4.68L237.54-6.48L237.21-14.37L241.26-15.12L240.90-7.62L240.93-5.16L240.93-5.16Q240.93-3.24 241.92-1.29L241.92-1.29L238.80 0.09L238.80 0.09Q237.81-1.86 237.60-3.03L237.60-3.03L237.60-3.03Q234.90 0 232.92 0" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 83.235px 0.964703px; animation: 1s linear -0.2112s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M244.29-14.49L244.29-14.49L247.92-15.27L247.92-15.27Q248.19-12.96 248.28-10.89L248.28-10.89L248.28-10.89Q251.01-15.12 253.41-15.12L253.41-15.12L253.08-10.44L253.08-10.44Q251.34-10.44 250.34-10.13L250.34-10.13L250.34-10.13Q249.33-9.81 248.28-8.88L248.28-8.88L248.28-7.80L248.61-0.75L244.59 0L244.95-7.29L244.95-7.29Q244.83-11.31 244.29-14.49" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 99.525px 1.0097px; animation: 1s linear -0.1848s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M263.91-8.64L265.02-3.75L265.41-3.75L266.40-7.86L268.02-15.27L271.74-14.82L269.49-7.38L267.60-0.36L262.47 0.09L260.70-7.20L258.54-14.49L262.62-15.24L263.91-8.64" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 110.1px 0.964703px; animation: 1s linear -0.1584s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M273.72-14.52L277.74-15.27L277.38-7.80L277.71-0.75L273.69 0L274.05-7.29L273.72-14.52" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 110.235px -11.2003px; animation: 1s linear -0.132s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M273.51-19.66L273.51-19.66L273.51-19.66Q273.51-20.67 274.29-21.46L274.29-21.46L274.29-21.46Q275.07-22.26 276.09-22.26L276.09-22.26L276.09-22.26Q277.11-22.26 277.65-21.70L277.65-21.70L277.65-21.70Q278.19-21.15 278.19-20.04L278.19-20.04L278.19-20.04Q278.19-18.93 277.43-18.13L277.43-18.13L277.43-18.13Q276.66-17.34 275.66-17.34L275.66-17.34L275.66-17.34Q274.65-17.34 274.08-18L274.08-18L274.08-18Q273.51-18.66 273.51-19.66" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 121.005px -2.8453px; animation: 1s linear -0.1056s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M288.96-2.94L288.96-2.94L288.96-2.94Q286.62 0 284.91 0L284.91 0L284.91 0Q282.78 0 281.42-1.74L281.42-1.74L281.42-1.74Q280.05-3.48 280.05-6.21L280.05-6.21L280.05-6.21Q280.05-9.96 282.13-12.54L282.13-12.54L282.13-12.54Q284.22-15.12 287.25-15.12L287.25-15.12L288.93-14.88L288.93-15.45L288.57-22.47L292.68-23.22L292.29-7.80L292.29-5.16L292.29-5.16Q292.29-3.36 293.19-1.02L293.19-1.02L289.95 0.33L289.95 0.33Q289.08-1.47 288.96-2.94zM283.41-7.77L283.41-7.77L283.41-7.77Q283.41-5.85 284.12-4.77L284.12-4.77L284.12-4.77Q284.82-3.69 286.16-3.69L286.16-3.69L286.16-3.69Q287.49-3.69 288.93-4.77L288.93-4.77L288.93-11.25L288.93-11.25Q287.13-11.61 286.26-11.61L286.26-11.61L286.26-11.61Q284.91-11.61 284.16-10.65L284.16-10.65L284.16-10.65Q283.41-9.69 283.41-7.77" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 135.39px 1.0397px; animation: 1s linear -0.0792s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M301.50-3.06L301.50-3.06L301.50-3.06Q302.37-3.06 303.33-3.51L303.33-3.51L303.33-3.51Q304.29-3.96 304.83-4.41L304.83-4.41L305.37-4.86L306.75-3.18L306.75-3.18Q306.45-2.67 305.82-2.01L305.82-2.01L305.82-2.01Q305.19-1.35 304.55-0.89L304.55-0.89L304.55-0.89Q303.90-0.42 302.84-0.04L302.84-0.04L302.84-0.04Q301.77 0.33 300.63 0.33L300.63 0.33L300.63 0.33Q298.20 0.33 296.67-1.51L296.67-1.51L296.67-1.51Q295.14-3.36 295.14-6.27L295.14-6.27L295.14-6.27Q295.14-9.93 297.27-12.69L297.27-12.69L297.27-12.69Q299.40-15.45 302.25-15.45L302.25-15.45L302.25-15.45Q304.44-15.45 305.66-14.22L305.66-14.22L305.66-14.22Q306.87-12.99 306.87-10.77L306.87-10.77L306.87-10.77Q306.87-9.45 306.42-7.77L306.42-7.77L305.82-7.14L298.32-6.45L298.32-6.45Q298.83-3.06 301.50-3.06zM301.50-12.36L301.50-12.36L301.50-12.36Q300.18-12.36 299.28-11.29L299.28-11.29L299.28-11.29Q298.38-10.23 298.23-8.58L298.23-8.58L303.33-9.21L303.33-9.21Q303.42-9.90 303.42-10.35L303.42-10.35L303.42-10.35Q303.42-12.36 301.50-12.36" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 149.355px 1.0397px; animation: 1s linear -0.0528s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M308.58-6.27L308.58-6.27Q308.58-10.11 310.65-12.78L310.65-12.78L310.65-12.78Q312.72-15.45 315.50-15.45L315.50-15.45L315.50-15.45Q318.27-15.45 319.81-13.65L319.81-13.65L319.81-13.65Q321.36-11.85 321.36-8.88L321.36-8.88L321.36-8.88Q321.36-4.92 319.37-2.29L319.37-2.29L319.37-2.29Q317.37 0.33 314.34 0.33L314.34 0.33L314.34 0.33Q311.85 0.33 310.22-1.54L310.22-1.54L310.22-1.54Q308.58-3.42 308.58-6.27L308.58-6.27zM318-7.32L318-7.32L318-7.32Q318-11.67 315.03-11.67L315.03-11.67L315.03-11.67Q311.94-11.67 311.94-7.59L311.94-7.59L311.94-7.59Q311.94-5.46 312.81-4.26L312.81-4.26L312.81-4.26Q313.68-3.06 315.11-3.06L315.11-3.06L315.11-3.06Q316.53-3.06 317.26-4.16L317.26-4.16L317.26-4.16Q318-5.25 318-7.32" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 164.58px 6.4697px; animation: 1s linear -0.0264s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M328.02-1.96L328.02-1.96L328.02-1.96Q328.02-2.97 328.74-3.71L328.74-3.71L328.74-3.71Q329.46-4.44 330.42-4.44L330.42-4.44L330.42-4.44Q331.38-4.44 331.88-3.92L331.88-3.92L331.88-3.92Q332.37-3.39 332.37-2.37L332.37-2.37L332.37-2.37Q332.37-1.35 331.68-0.58L331.68-0.58L331.68-0.58Q330.99 0.18 330.05 0.18L330.05 0.18L330.05 0.18Q329.10 0.18 328.56-0.39L328.56-0.39L328.56-0.39Q328.02-0.96 328.02-1.96" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 165.75px -5.5453px; animation: 1s linear 0s infinite normal forwards running breath-d843a921-4c73-49b8-bcdb-9cfbb6c268fc;"><path d="M329.10-20.25L333.63-21L331.95-7.71L329.10-7.29L329.10-20.25" fill="#51cacc" stroke="none" stroke-width="none" transform="translate(-165.614990234375,8.599702441406249)" style="fill: rgb(81, 202, 204);"></path></g></g>
                                                            </g>
                                                            </g>
                                                            </svg>'''), None, None, None, None]])
        name = input('', required=True, onchange=True)
        toast('downloaded')

    with use_scope(name='after', clear=True):
        def doit():
            clear(scope='first')
            put_html('<hr>')
            put_grid([[None, None, None, None, None, put_file(str(name + 'ByMoiEis' + '.mp4'), content=s), None, None,
                       None, None]])
            put_html('<hr>')
            put_grid([[None, None, None, None, put_html('''


                                <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <meta http-equiv="X-UA-Compatible" content="ie=edge">
                            <title>SocialIcons Preview</title>
                        <style>.eapps-preview-widget {
                          width: 100%;
                        }
                        </style><style>.eapps-widget {
                          -webkit-animation: none;
                                  animation: none;
                          -webkit-animation-delay: 0;
                                  animation-delay: 0;
                          -webkit-animation-direction: normal;
                                  animation-direction: normal;
                          -webkit-animation-duration: 0;
                                  animation-duration: 0;
                          -webkit-animation-fill-mode: none;
                                  animation-fill-mode: none;
                          -webkit-animation-iteration-count: 1;
                                  animation-iteration-count: 1;
                          -webkit-animation-name: none;
                                  animation-name: none;
                          -webkit-animation-play-state: running;
                                  animation-play-state: running;
                          -webkit-animation-timing-function: ease;
                                  animation-timing-function: ease;
                          -webkit-backface-visibility: visible;
                                  backface-visibility: visible;
                          background: 0;
                          background-attachment: scroll;
                          background-clip: border-box;
                          background-color: transparent;
                          background-image: none;
                          background-origin: padding-box;
                          background-position: 0 0;
                          background-position-x: 0;
                          background-position-y: 0;
                          background-repeat: repeat;
                          background-size: auto auto;
                          border: 0;
                          border-style: none;
                          border-width: medium;
                          border-color: inherit;
                          border-bottom: 0;
                          border-bottom-color: inherit;
                          border-bottom-left-radius: 0;
                          border-bottom-right-radius: 0;
                          border-bottom-style: none;
                          border-bottom-width: medium;
                          border-collapse: separate;
                          -o-border-image: none;
                             border-image: none;
                          border-left: 0;
                          border-left-color: inherit;
                          border-left-style: none;
                          border-left-width: medium;
                          border-radius: 0;
                          border-right: 0;
                          border-right-color: inherit;
                          border-right-style: none;
                          border-right-width: medium;
                          border-spacing: 0;
                          border-top: 0;
                          border-top-color: inherit;
                          border-top-left-radius: 0;
                          border-top-right-radius: 0;
                          border-top-style: none;
                          border-top-width: medium;
                          bottom: auto;
                          box-shadow: none;
                          box-sizing: content-box;
                          caption-side: top;
                          clear: none;
                          clip: auto;
                          color: inherit;
                          -webkit-columns: auto;
                             -moz-columns: auto;
                                  columns: auto;
                          -webkit-column-count: auto;
                             -moz-column-count: auto;
                                  column-count: auto;
                          -webkit-column-fill: balance;
                             -moz-column-fill: balance;
                                  column-fill: balance;
                          grid-column-gap: normal;
                          -webkit-column-gap: normal;
                             -moz-column-gap: normal;
                                  column-gap: normal;
                          -webkit-column-rule: medium none currentColor;
                             -moz-column-rule: medium none currentColor;
                                  column-rule: medium none currentColor;
                          -webkit-column-rule-color: currentColor;
                             -moz-column-rule-color: currentColor;
                                  column-rule-color: currentColor;
                          -webkit-column-rule-style: none;
                             -moz-column-rule-style: none;
                                  column-rule-style: none;
                          -webkit-column-rule-width: none;
                             -moz-column-rule-width: none;
                                  column-rule-width: none;
                          -webkit-column-span: 1;
                             -moz-column-span: 1;
                                  column-span: 1;
                          -webkit-column-width: auto;
                             -moz-column-width: auto;
                                  column-width: auto;
                          content: normal;
                          counter-increment: none;
                          counter-reset: none;
                          direction: ltr;
                          empty-cells: show;
                          float: none;
                          font: normal;
                          font-family: inherit;
                          font-size: medium;
                          font-style: normal;
                          font-feature-settings: normal;
                          font-variant: normal;
                          font-weight: normal;
                          height: auto;
                          -webkit-hyphens: none;
                              -ms-hyphens: none;
                                  hyphens: none;
                          left: auto;
                          letter-spacing: normal;
                          line-height: normal;
                          list-style: none;
                          list-style-image: none;
                          list-style-position: outside;
                          list-style-type: disc;
                          margin: 0;
                          margin-bottom: 0;
                          margin-left: 0;
                          margin-right: 0;
                          margin-top: 0;
                          opacity: 1;
                          orphans: 0;
                          outline: 0;
                          outline-color: invert;
                          outline-style: none;
                          outline-width: medium;
                          overflow: visible;
                          overflow-x: visible;
                          overflow-y: visible;
                          padding: 0;
                          padding-bottom: 0;
                          padding-left: 0;
                          padding-right: 0;
                          padding-top: 0;
                          page-break-after: auto;
                          page-break-before: auto;
                          page-break-inside: auto;
                          -webkit-perspective: none;
                                  perspective: none;
                          -webkit-perspective-origin: 50% 50%;
                                  perspective-origin: 50% 50%;
                          position: static;
                          quotes: '\201C' '\201D' '\2018' '\2019';
                          right: auto;
                          -moz-tab-size: 8;
                            -o-tab-size: 8;
                               tab-size: 8;
                          table-layout: auto;
                          text-align: inherit;
                          -moz-text-align-last: auto;
                               text-align-last: auto;
                          text-decoration: none;
                          -webkit-text-decoration-color: inherit;
                                  text-decoration-color: inherit;
                          -webkit-text-decoration-line: none;
                                  text-decoration-line: none;
                          -webkit-text-decoration-style: solid;
                                  text-decoration-style: solid;
                          text-indent: 0;
                          text-shadow: none;
                          text-transform: none;
                          top: auto;
                          -webkit-transform: none;
                                  transform: none;
                          -webkit-transform-style: flat;
                                  transform-style: flat;
                          transition: none;
                          transition-delay: 0s;
                          transition-duration: 0s;
                          transition-property: none;
                          transition-timing-function: ease;
                          unicode-bidi: normal;
                          vertical-align: baseline;
                          visibility: visible;
                          white-space: normal;
                          widows: 0;
                          width: auto;
                          word-spacing: normal;
                          z-index: auto;
                        }
                        .eapps-social-icons {
                          display: block;
                          position: relative;
                        }
                        .eapps-social-icons-item {
                          display: inline-block;
                          vertical-align: middle;
                          position: relative;
                          cursor: pointer;
                          -webkit-backface-visibility: hidden;
                                  backface-visibility: hidden;
                          transition: all 0.1s ease;
                        }
                        .eapps-social-icons-item::before,
                        .eapps-social-icons-item::after {
                          content: '';
                          display: block;
                          position: absolute;
                          width: 100%;
                          height: 100%;
                        }
                        .eapps-social-icons-item::after {
                          opacity: 0;
                          visibility: hidden;
                          transition: all 0.1s ease;
                        }
                        .eapps-social-icons-item-icon {
                          display: block;
                          position: absolute;
                          top: 50%;
                          left: 50%;
                          z-index: 1;
                          -webkit-backface-visibility: hidden;
                                  backface-visibility: hidden;
                          transition: all 0.1s ease;
                        }
                        .eapps-social-icons-item:hover::before {
                          opacity: 0;
                          visibility: hidden;
                          transition: all 0s ease 0.1s;
                        }
                        .eapps-social-icons-item:hover::after {
                          opacity: 1;
                          visibility: visible;
                        }
                        .eapps-social-icons.eapps-social-icons-position-left {
                          text-align: left;
                        }
                        .eapps-social-icons.eapps-social-icons-position-center {
                          text-align: center;
                        }
                        .eapps-social-icons.eapps-social-icons-position-right {
                          text-align: right;
                        }
                        .eapps-social-icons-location-inline.eapps-social-icons-position-left {
                          text-align: left;
                        }
                        .eapps-social-icons-location-inline.eapps-social-icons-position-center {
                          text-align: center;
                        }
                        .eapps-social-icons-location-inline.eapps-social-icons-position-right {
                          text-align: right;
                        }
                        .eapps-social-icons-location-floating {
                          position: fixed !important;
                          z-index: 1000000 !important;
                        }
                        .eapps-social-icons-location-floating.eapps-social-icons-position-left {
                          left: 0;
                          top: 50%;
                          text-align: left;
                          -webkit-transform: translateY(-50%);
                                  transform: translateY(-50%);
                        }
                        .eapps-social-icons-location-floating.eapps-social-icons-position-center {
                          bottom: 0;
                          left: 0;
                          right: 0;
                          text-align: center;
                        }
                        .eapps-social-icons-location-floating.eapps-social-icons-position-right {
                          right: 0;
                          text-align: right;
                          -webkit-transform: translateY(-50%);
                                  transform: translateY(-50%);
                          top: 50%;
                        }
                        .eapps-social-icons-border-radius-circle .eapps-social-icons-item,
                        .eapps-social-icons-border-radius-circle .eapps-social-icons-item::before,
                        .eapps-social-icons-border-radius-circle .eapps-social-icons-item::after {
                          border-radius: 50%;
                        }
                        .eapps-social-icons-border-radius-square .eapps-social-icons-item,
                        .eapps-social-icons-border-radius-square .eapps-social-icons-item::before,
                        .eapps-social-icons-border-radius-square .eapps-social-icons-item::after {
                          border-radius: 0;
                        }
                        .eapps-social-icons-border-radius-rounded .eapps-social-icons-item,
                        .eapps-social-icons-border-radius-rounded .eapps-social-icons-item::before,
                        .eapps-social-icons-border-radius-rounded .eapps-social-icons-item::after {
                          border-radius: 5px;
                        }
                        .eapps-social-icons-size-24 .eapps-social-icons-item {
                          width: 24px;
                          height: 24px;
                          margin: 3px;
                          border-width: 1px;
                        }
                        .eapps-social-icons-size-24 .eapps-social-icons-item-icon {
                          width: 12px;
                          height: 12px;
                          margin: -6px 0 0 -6px;
                        }
                        .eapps-social-icons-size-24 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                          width: 24px;
                          height: 24px;
                          margin: -12px 0 0 -12px;
                        }
                        .eapps-social-icons-size-32 .eapps-social-icons-item {
                          width: 32px;
                          height: 32px;
                          margin: 4px;
                          border-width: 1px;
                        }
                        .eapps-social-icons-size-32 .eapps-social-icons-item-icon {
                          width: 16px;
                          height: 16px;
                          margin: -8px 0 0 -8px;
                        }
                        .eapps-social-icons-size-32 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                          width: 32px;
                          height: 32px;
                          margin: -16px 0 0 -16px;
                        }
                        .eapps-social-icons-size-40 .eapps-social-icons-item {
                          width: 40px;
                          height: 40px;
                          margin: 5px;
                          border-width: 2px;
                        }
                        .eapps-social-icons-size-40 .eapps-social-icons-item-icon {
                          width: 20px;
                          height: 20px;
                          margin: -10px 0 0 -10px;
                        }
                        .eapps-social-icons-size-40 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                          width: 40px;
                          height: 40px;
                          margin: -20px 0 0 -20px;
                        }
                        .eapps-social-icons-size-48 .eapps-social-icons-item {
                          width: 48px;
                          height: 48px;
                          margin: 6px;
                          border-width: 2px;
                        }
                        .eapps-social-icons-size-48 .eapps-social-icons-item-icon {
                          width: 24px;
                          height: 24px;
                          margin: -12px 0 0 -12px;
                        }
                        .eapps-social-icons-size-48 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                          width: 48px;
                          height: 48px;
                          margin: -24px 0 0 -24px;
                        }
                        .eapps-social-icons-size-60 .eapps-social-icons-item {
                          width: 60px;
                          height: 60px;
                          margin: 7px;
                          border-width: 2px;
                        }
                        .eapps-social-icons-size-60 .eapps-social-icons-item-icon {
                          width: 28px;
                          height: 28px;
                          margin: -14px 0 0 -14px;
                        }
                        .eapps-social-icons-size-60 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                          width: 60px;
                          height: 60px;
                          margin: -30px 0 0 -30px;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-500px::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-500px::after {
                          background-color: #0099e5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover {
                          border-color: #0099e5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * {
                          fill: #0099e5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-badoo::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-badoo::after {
                          background-color: #ff6719;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover {
                          border-color: #ff6719;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * {
                          fill: #ff6719;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-behance::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-behance::after {
                          background-color: #1776f6;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover {
                          border-color: #1776f6;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * {
                          fill: #1776f6;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-blogger::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-blogger::after {
                          background-color: #ff8b13;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover {
                          border-color: #ff8b13;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * {
                          fill: #ff8b13;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-delicious::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-delicious::after {
                          background-color: #39f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover {
                          border-color: #39f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * {
                          fill: #39f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-deviantart::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-deviantart::after {
                          background-color: #05cc47;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover {
                          border-color: #05cc47;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * {
                          fill: #05cc47;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-digg::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-digg::after {
                          background-color: ;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-disqus::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-disqus::after {
                          background-color: #3ca2ef;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover {
                          border-color: #3ca2ef;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * {
                          fill: #3ca2ef;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-dribbble::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-dribbble::after {
                          background-color: #fa488c;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover {
                          border-color: #fa488c;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * {
                          fill: #fa488c;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-envato::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-envato::after {
                          background-color: #8dcf3a;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover {
                          border-color: #8dcf3a;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * {
                          fill: #8dcf3a;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-evernote::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-evernote::after {
                          background-color: #2dbe60;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover {
                          border-color: #2dbe60;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * {
                          fill: #2dbe60;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-facebook::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-facebook::after {
                          background-color: #3e68c0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover {
                          border-color: #3e68c0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * {
                          fill: #3e68c0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-fb-messenger::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-fb-messenger::after {
                          background-color: #007fff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover {
                          border-color: #007fff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * {
                          fill: #007fff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-flickr::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-flickr::after {
                          background-color: #ff0084;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover {
                          border-color: #ff0084;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * {
                          fill: #ff0084;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-flipboard::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-flipboard::after {
                          background-color: #f43d3d;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover {
                          border-color: #f43d3d;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * {
                          fill: #f43d3d;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-forrst::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-forrst::after {
                          background-color: #55c462;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover {
                          border-color: #55c462;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * {
                          fill: #55c462;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-foursquare::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-foursquare::after {
                          background-color: #ff3b6f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover {
                          border-color: #ff3b6f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * {
                          fill: #ff3b6f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-github::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-github::after {
                          background-color: ;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-instagram::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-instagram::after {
                          background-color: ;
                          background-image: radial-gradient(circle farthest-corner at 35% 90%, #fec564, transparent 50%), radial-gradient(circle farthest-corner at 0 140%, #fec564, transparent 50%), radial-gradient(ellipse farthest-corner at 0 -25%, #5258cf, transparent 50%), radial-gradient(ellipse farthest-corner at 20% -50%, #5258cf, transparent 50%), radial-gradient(ellipse farthest-corner at 100% 0, #893dc2, transparent 50%), radial-gradient(ellipse farthest-corner at 60% -20%, #893dc2, transparent 50%), radial-gradient(ellipse farthest-corner at 100% 100%, #d9317a, transparent), linear-gradient(#6559ca, #bc318f 30%, #e33f5f 50%, #f77638 70%, #fec66d 100%);
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-lastfm::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-lastfm::after {
                          background-color: #ea3939;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover {
                          border-color: #ea3939;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * {
                          fill: #ea3939;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-linkedin::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-linkedin::after {
                          background-color: #15ace5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover {
                          border-color: #15ace5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * {
                          fill: #15ace5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-livejournal::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-livejournal::after {
                          background-color: #2cbae5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover {
                          border-color: #2cbae5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * {
                          fill: #2cbae5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-email::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-email::after {
                          background-color: #f4cd0b;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover {
                          border-color: #f4cd0b;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * {
                          fill: #f4cd0b;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-myspace::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-myspace::after {
                          background-color: ;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-odnoklassniki::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-odnoklassniki::after {
                          background-color: #ff8321;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover {
                          border-color: #ff8321;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * {
                          fill: #ff8321;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-periscope::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-periscope::after {
                          background-color: #35b3db;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover {
                          border-color: #35b3db;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * {
                          fill: #35b3db;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-pinterest::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-pinterest::after {
                          background-color: #ea3145;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover {
                          border-color: #ea3145;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * {
                          fill: #ea3145;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-print::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-print::after {
                          background-color: ;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-reddit::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-reddit::after {
                          background-color: #ff5c1f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover {
                          border-color: #ff5c1f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * {
                          fill: #ff5c1f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-rss::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-rss::after {
                          background-color: #fb7629;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover {
                          border-color: #fb7629;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * {
                          fill: #fb7629;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-sina-weibo::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-sina-weibo::after {
                          background-color: #ff3f3f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover {
                          border-color: #ff3f3f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * {
                          fill: #ff3f3f;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-skype::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-skype::after {
                          background-color: #06bcff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover {
                          border-color: #06bcff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * {
                          fill: #06bcff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-slack::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-slack::after {
                          background-color: ;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-snapchat::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-snapchat::after {
                          background-color: #fada06;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover {
                          border-color: #fada06;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * {
                          fill: #fada06;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-soundcloud::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-soundcloud::after {
                          background-color: #f80;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover {
                          border-color: #f80;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * {
                          fill: #f80;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-spotify::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-spotify::after {
                          background-color: #28c858;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover {
                          border-color: #28c858;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * {
                          fill: #28c858;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-stackoverflow::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-stackoverflow::after {
                          background-color: #ff780d;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover {
                          border-color: #ff780d;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * {
                          fill: #ff780d;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-stumbleupon::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-stumbleupon::after {
                          background-color: #eb4924;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover {
                          border-color: #eb4924;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * {
                          fill: #eb4924;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-telegram::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-telegram::after {
                          background-color: #2ca5e0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover {
                          border-color: #2ca5e0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * {
                          fill: #2ca5e0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-tiktok::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-tiktok::after {
                          background-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-tumblr::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-tumblr::after {
                          background-color: #35465c;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover {
                          border-color: #35465c;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * {
                          fill: #35465c;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-twitter::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-twitter::after {
                          background-color: #23abff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover {
                          border-color: #23abff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * {
                          fill: #23abff;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-viadeo::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-viadeo::after {
                          background-color: #ff7452;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover {
                          border-color: #ff7452;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * {
                          fill: #ff7452;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-viber::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-viber::after {
                          background-color: #9d62cc;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover {
                          border-color: #9d62cc;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * {
                          fill: #9d62cc;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-vimeo::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-vimeo::after {
                          background-color: #1ab7ea;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover {
                          border-color: #1ab7ea;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * {
                          fill: #1ab7ea;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-vine::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-vine::after {
                          background-color: #00b488;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover {
                          border-color: #00b488;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * {
                          fill: #00b488;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-vk::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-vk::after {
                          background-color: #3673be;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover {
                          border-color: #3673be;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * {
                          fill: #3673be;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-whatsapp::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-whatsapp::after {
                          background-color: #13d25a;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover {
                          border-color: #13d25a;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * {
                          fill: #13d25a;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-xing::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-xing::after {
                          background-color: #20a5a5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover {
                          border-color: #20a5a5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * {
                          fill: #20a5a5;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-youtube::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-youtube::after {
                          background-color: #ee3130;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover {
                          border-color: #ee3130;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * {
                          fill: #ee3130;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-line::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-line::after {
                          background-color: #00c300;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover {
                          border-color: #00c300;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * {
                          fill: #00c300;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-lineAt::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-lineAt::after {
                          background-color: #00c300;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover {
                          border-color: #00c300;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * {
                          fill: #00c300;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-phone::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-phone::after {
                          background-color: #33cc49;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover {
                          border-color: #33cc49;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * {
                          fill: #33cc49;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-amazon::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-amazon::after {
                          background-color: #f90;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover {
                          border-color: #f90;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * {
                          fill: #f90;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-itunes::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-itunes::after {
                          background-color: ;
                          background-image: linear-gradient(142deg, #ff5e50, #fe5c6c 25%, #e3658a 38%, #b87eb0 50%, #916cff 63%, rgba(112,188,251,0.92) 76%, #21c7fe);
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-apple::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-apple::after {
                          background-color: ;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover {
                          border-color: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * {
                          fill: #000;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-native .eapps-social-icons-item-weibo::before,
                        .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-weibo::after {
                          background-color: #f44336;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover {
                          border-color: #f44336;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * {
                          fill: #f44336;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke-width: 0;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill: #f00044;
                          fill-opacity: 1;
                        }
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                          fill: #08fff9;
                          stroke-width: 0;
                        }
                        .eapps-social-icons-bg-color-white .eapps-social-icons-item::before,
                        .eapps-social-icons-bg-color-on-hover-white .eapps-social-icons-item::after {
                          background: #fff;
                        }
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover {
                          border-color: #fff;
                        }
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * {
                          fill: #fff;
                        }
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill-opacity: 0;
                        }
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke: #fff;
                          stroke-width: 1;
                        }
                        .eapps-social-icons-bg-color-black .eapps-social-icons-item::before,
                        .eapps-social-icons-bg-color-on-hover-black .eapps-social-icons-item::after {
                          background: #222;
                        }
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover {
                          border-color: #222;
                        }
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon,
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon *,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * {
                          fill: #222;
                        }
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-red,
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-red,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-red {
                          fill-opacity: 0;
                        }
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-blue,
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-blue,
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-black,
                        .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-black,
                        .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-black {
                          stroke: #222;
                          stroke-width: 1;
                        }
                        .eapps-social-icons-bg-color-white .eapps-social-icons-item-custom::before,
                        .eapps-social-icons-bg-color-on-hover-white .eapps-social-icons-item-custom::after {
                          background: inherit;
                        }
                        .eapps-social-icons-bg-color-black .eapps-social-icons-item-custom::before,
                        .eapps-social-icons-bg-color-on-hover-black .eapps-social-icons-item-custom::after {
                          background: inherit;
                        }
                        .eapps-social-icons-style-default .eapps-social-icons-item,
                        .eapps-social-icons-style-default .eapps-social-icons-item:hover {
                          box-shadow: none;
                          border-color: transparent;
                        }
                        .eapps-social-icons-style-material.eapps-social-icons-size-24 .eapps-social-icons-item,
                        .eapps-social-icons-style-material.eapps-social-icons-size-32 .eapps-social-icons-item {
                          border-color: transparent;
                          box-shadow: 0 0 2px rgba(0,0,0,0.14), 0 1px 4px rgba(0,0,0,0.28);
                        }
                        .eapps-social-icons-style-material.eapps-social-icons-size-24 .eapps-social-icons-item:hover,
                        .eapps-social-icons-style-material.eapps-social-icons-size-32 .eapps-social-icons-item:hover {
                          border-color: transparent;
                          box-shadow: 0 0 3px rgba(0,0,0,0.16), 0 2px 6px rgba(0,0,0,0.32);
                        }
                        .eapps-social-icons-style-material.eapps-social-icons-size-40 .eapps-social-icons-item,
                        .eapps-social-icons-style-material.eapps-social-icons-size-48 .eapps-social-icons-item,
                        .eapps-social-icons-style-material.eapps-social-icons-size-60 .eapps-social-icons-item {
                          border-color: transparent;
                          box-shadow: 0 0 4px rgba(0,0,0,0.14), 0 2px 6px rgba(0,0,0,0.28);
                        }
                        .eapps-social-icons-style-material.eapps-social-icons-size-40 .eapps-social-icons-item:hover,
                        .eapps-social-icons-style-material.eapps-social-icons-size-48 .eapps-social-icons-item:hover,
                        .eapps-social-icons-style-material.eapps-social-icons-size-60 .eapps-social-icons-item:hover {
                          border-color: transparent;
                          box-shadow: 0 0 6px rgba(0,0,0,0.16), 0 4px 8px rgba(0,0,0,0.32);
                        }
                        .eapps-social-icons-style-material .eapps-social-icons-item-custom,
                        .eapps-social-icons-style-material .eapps-social-icons-item-custom:hover {
                          box-shadow: none !important;
                        }
                        .eapps-social-icons-style-flat .eapps-social-icons-item,
                        .eapps-social-icons-style-flat .eapps-social-icons-item:hover {
                          border-color: transparent;
                        }
                        .eapps-social-icons-style-flat .eapps-social-icons-item::before,
                        .eapps-social-icons-style-flat .eapps-social-icons-item:hover::before,
                        .eapps-social-icons-style-flat .eapps-social-icons-item::after,
                        .eapps-social-icons-style-flat .eapps-social-icons-item:hover::after {
                          box-shadow: inset 0 -2px rgba(0,0,0,0.2);
                        }
                        .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item::before,
                        .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item:hover::before,
                        .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item::after,
                        .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item:hover::after {
                          box-shadow: inset 0 -3px rgba(0,0,0,0.2);
                        }
                        .eapps-social-icons-style-flat .eapps-social-icons-item-custom::before,
                        .eapps-social-icons-style-flat .eapps-social-icons-item-custom:hover::before,
                        .eapps-social-icons-style-flat .eapps-social-icons-item-custom::after,
                        .eapps-social-icons-style-flat .eapps-social-icons-item-custom:hover::after {
                          box-shadow: none !important;
                        }
                        .eapps-social-icons-style-bordered .eapps-social-icons-item,
                        .eapps-social-icons-style-bordered .eapps-social-icons-item:hover {
                          border-style: solid;
                          box-shadow: none;
                        }
                        .eapps-social-icons-style-bordered .eapps-social-icons-item::before,
                        .eapps-social-icons-style-bordered .eapps-social-icons-item:hover::before,
                        .eapps-social-icons-style-bordered .eapps-social-icons-item::after,
                        .eapps-social-icons-style-bordered .eapps-social-icons-item:hover::after {
                          background: none;
                        }
                        .eapps-social-icons-style-bordered .eapps-social-icons-item-custom,
                        .eapps-social-icons-style-bordered .eapps-social-icons-item-custom:hover {
                          border-style: inherit !important;
                        }
                        .eapps-social-icons-style-classic .eapps-social-icons-item,
                        .eapps-social-icons-style-classic .eapps-social-icons-item:hover {
                          box-shadow: 0 2px 4px rgba(0,0,0,0.15);
                        }
                        .eapps-social-icons-style-classic .eapps-social-icons-item::before,
                        .eapps-social-icons-style-classic .eapps-social-icons-item:hover::before,
                        .eapps-social-icons-style-classic .eapps-social-icons-item::after,
                        .eapps-social-icons-style-classic .eapps-social-icons-item:hover::after {
                          box-shadow: inset 0 0 1px rgba(0,0,0,0.6), inset 0 1px 0 1px rgba(255,255,255,0.3);
                        }
                        .eapps-social-icons-style-classic .eapps-social-icons-item:active {
                          box-shadow: none;
                        }
                        .eapps-social-icons-style-classic .eapps-social-icons-item-custom,
                        .eapps-social-icons-style-classic .eapps-social-icons-item-custom:hover {
                          box-shadow: none !important;
                        }
                        .eapps-social-icons-style-classic .eapps-social-icons-item-custom::before,
                        .eapps-social-icons-style-classic .eapps-social-icons-item-custom:hover::before,
                        .eapps-social-icons-style-classic .eapps-social-icons-item-custom::after,
                        .eapps-social-icons-style-classic .eapps-social-icons-item-custom:hover::after {
                          box-shadow: none !important;
                        }
                        .eapps-social-icons-style-symbol {
                          margin: 0;
                        }
                        .eapps-social-icons-style-symbol .eapps-social-icons-item,
                        .eapps-social-icons-style-symbol .eapps-social-icons-item:hover {
                          box-shadow: none;
                          border: none;
                          margin: 0;
                        }
                        .eapps-social-icons-style-symbol .eapps-social-icons-item::before,
                        .eapps-social-icons-style-symbol .eapps-social-icons-item:hover::before,
                        .eapps-social-icons-style-symbol .eapps-social-icons-item::after,
                        .eapps-social-icons-style-symbol .eapps-social-icons-item:hover::after {
                          background: none;
                        }
                        .eapps-social-icons-animation-rotate .eapps-social-icons-item:hover .eapps-social-icons-item-icon {
                          -webkit-transform: scale(1.1) rotate(10deg);
                                  transform: scale(1.1) rotate(10deg);
                          transition: all 0.3s cubic-bezier(0.2, 0.26, 0, 1.78);
                        }
                        .eapps-social-icons-animation-fly .eapps-social-icons-item {
                          transition: all 0.3s cubic-bezier(0.2, 0.26, 0, 1.78);
                        }
                        .eapps-social-icons-animation-fly.eapps-social-icons-size-24 .eapps-social-icons-item:hover {
                          -webkit-transform: translateY(-3px);
                                  transform: translateY(-3px);
                        }
                        .eapps-social-icons-animation-fly.eapps-social-icons-size-32 .eapps-social-icons-item:hover {
                          -webkit-transform: translateY(-4px);
                                  transform: translateY(-4px);
                        }
                        .eapps-social-icons-animation-fly.eapps-social-icons-size-40 .eapps-social-icons-item:hover {
                          -webkit-transform: translateY(-5px);
                                  transform: translateY(-5px);
                        }
                        .eapps-social-icons-animation-fly.eapps-social-icons-size-48 .eapps-social-icons-item:hover {
                          -webkit-transform: translateY(-6px);
                                  transform: translateY(-6px);
                        }
                        .eapps-social-icons-animation-fly.eapps-social-icons-size-60 .eapps-social-icons-item:hover {
                          -webkit-transform: translateY(-7px);
                                  transform: translateY(-7px);
                        }
                        .eapps-social-icons-animation-bounce .eapps-social-icons-item:hover {
                          -webkit-animation: eapps-animation-bounce 0.3s forwards;
                                  animation: eapps-animation-bounce 0.3s forwards;
                        }
                        .eapps-social-icons-animation-zoom .eapps-social-icons-item::before {
                          transition: none;
                        }
                        .eapps-social-icons-animation-zoom .eapps-social-icons-item::after {
                          -webkit-transform: scale3d(0, 0, 0);
                                  transform: scale3d(0, 0, 0);
                          transition: all 0.3s ease;
                        }
                        .eapps-social-icons-animation-zoom .eapps-social-icons-item:hover {
                          -webkit-transform: scale3d(1.1, 1.1, 1.1);
                                  transform: scale3d(1.1, 1.1, 1.1);
                          transition: all 0.3s ease;
                        }
                        .eapps-social-icons-animation-zoom .eapps-social-icons-item:hover::before {
                          transition: all 0.3s ease 0.2s;
                          opacity: 0;
                        }
                        .eapps-social-icons-animation-zoom .eapps-social-icons-item:hover::after {
                          -webkit-transform: scale3d(1, 1, 1);
                                  transform: scale3d(1, 1, 1);
                        }
                        .eapps-social-icons-animation-slide .eapps-social-icons-item {
                          overflow: hidden;
                        }
                        .eapps-social-icons-animation-slide .eapps-social-icons-item:hover .eapps-social-icons-item-icon {
                          -webkit-animation: eapps-animation-slide 0.3s forwards cubic-bezier(0.54, 0.74, 0.25, 1.3);
                                  animation: eapps-animation-slide 0.3s forwards cubic-bezier(0.54, 0.74, 0.25, 1.3);
                        }
                        @-webkit-keyframes eapps-animation-bounce {
                          40% {
                            -webkit-transform: scale3d(0.9, 0.9, 1);
                                    transform: scale3d(0.9, 0.9, 1);
                          }
                          70% {
                            -webkit-transform: scale3d(1.05, 1.05, 1);
                                    transform: scale3d(1.05, 1.05, 1);
                          }
                          100% {
                            -webkit-transform: scale3d(1, 1, 1);
                                    transform: scale3d(1, 1, 1);
                          }
                        }
                        @keyframes eapps-animation-bounce {
                          40% {
                            -webkit-transform: scale3d(0.9, 0.9, 1);
                                    transform: scale3d(0.9, 0.9, 1);
                          }
                          70% {
                            -webkit-transform: scale3d(1.05, 1.05, 1);
                                    transform: scale3d(1.05, 1.05, 1);
                          }
                          100% {
                            -webkit-transform: scale3d(1, 1, 1);
                                    transform: scale3d(1, 1, 1);
                          }
                        }
                        @-webkit-keyframes eapps-animation-slide {
                          49% {
                            -webkit-transform: translateY(100%);
                                    transform: translateY(100%);
                          }
                          50% {
                            opacity: 0;
                            -webkit-transform: translateY(-100%);
                                    transform: translateY(-100%);
                          }
                          51% {
                            opacity: 1;
                          }
                        }
                        @keyframes eapps-animation-slide {
                          49% {
                            -webkit-transform: translateY(100%);
                                    transform: translateY(100%);
                          }
                          50% {
                            opacity: 0;
                            -webkit-transform: translateY(-100%);
                                    transform: translateY(-100%);
                          }
                          51% {
                            opacity: 1;
                          }
                        }
                        </style><style>.eapps-preview {
                          overflow: hidden;
                          display: -webkit-flex;
                          display: flex;
                          -webkit-align-items: center;
                                  align-items: center;
                          -webkit-justify-content: center;
                                  justify-content: center;
                          margin: 0 auto;
                          width: 100%;
                          min-width: 150px;
                          min-height: 100%;
                          transition: 0.2s;
                        }
                        .eapps-preview-toolbar {
                          position: fixed;
                          top: 80px;
                          right: 0;
                          z-index: 10;
                        }
                        @media only screen and (max-width: 480px) {
                          .eapps-preview-toolbar {
                            display: none;
                          }
                        }
                        .eapps-preview-toolbar-item {
                          position: relative;
                        }
                        .eapps-preview-toolbar-item-trigger {
                          box-sizing: border-box;
                          padding: 3px 6px;
                          background: #38393a;
                          cursor: pointer;
                        }
                        .eapps-preview-toolbar-item-trigger:first-child {
                          padding-top: 6px;
                        }
                        .eapps-preview-toolbar-item-trigger:last-child {
                          padding-bottom: 6px;
                        }
                        .eapps-preview-toolbar-item-trigger:hover .eapps-preview-toolbar-item-icon svg {
                          fill: #fff;
                        }
                        .eapps-preview-toolbar-item-icon {
                          display: -webkit-flex;
                          display: flex;
                          -webkit-align-items: center;
                                  align-items: center;
                          -webkit-justify-content: center;
                                  justify-content: center;
                          width: 26px;
                          height: 26px;
                        }
                        .eapps-preview-toolbar-item-active .eapps-preview-toolbar-item-icon {
                          background: #2c2c2d;
                        }
                        .eapps-preview-toolbar-item-icon svg {
                          width: 16px;
                          height: 16px;
                          fill: #66686a;
                          transition: 0.1s;
                        }
                        .eapps-preview-toolbar-item-active .eapps-preview-toolbar-item-icon svg {
                          fill: #fff;
                        }
                        .eapps-preview-toolbar-item-values {
                          visibility: hidden;
                          display: -webkit-flex;
                          display: flex;
                          -webkit-align-items: center;
                                  align-items: center;
                          -webkit-justify-content: center;
                                  justify-content: center;
                          position: absolute;
                          top: 0px;
                          right: 38px;
                          padding: 0 2px;
                          border-radius: 2px;
                          transition: 0.2s;
                          opacity: 0;
                          background: #38393a;
                        }
                        .eapps-preview-toolbar-item-active .eapps-preview-toolbar-item-values {
                          visibility: visible;
                          opacity: 1;
                          right: 42px;
                        }
                        .eapps-preview-toolbar-item-value {
                          display: -webkit-flex;
                          display: flex;
                          -webkit-align-items: center;
                                  align-items: center;
                          -webkit-justify-content: center;
                                  justify-content: center;
                          box-sizing: border-box;
                          padding: 4px 2px;
                          cursor: pointer;
                        }
                        .eapps-preview-toolbar-item-value-icon {
                          display: -webkit-flex;
                          display: flex;
                          -webkit-align-items: center;
                                  align-items: center;
                          -webkit-justify-content: center;
                                  justify-content: center;
                          width: 26px;
                          height: 26px;
                          border-radius: 2px;
                        }
                        html {
                          height: 100%;
                          overflow: auto;
                        }

                        </style></head>



                                <div class="eapps-social-icons eapps-widget
                            eapps-social-icons-location-inline
                            eapps-social-icons-position-center
                            eapps-social-icons-size-40
                            eapps-social-icons-style-material
                            eapps-social-icons-border-radius-circle
                            eapps-social-icons-icon-color-white
                            eapps-social-icons-bg-color-native
                            eapps-social-icons-icon-color-on-hover-native
                            eapps-social-icons-bg-color-on-hover-white
                            eapps-social-icons-animation-fly
                        " style="width: auto;"><a class="eapps-social-icons-item-instagram eapps-social-icons-item" href="https://www.instagram.com/moie._10/" target="_blank" rel="nofollow" title="Instagram">
                            <span eapps-link="svg"><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="24px" height="24px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" xml:space="preserve" class="eapps-social-icons-item-icon"> <g> <circle fill="%23222222" cx="18.05" cy="5.992" r="1.355"></circle> <path fill="%23222222" d="M12.021,5.806c-3.427,0-6.215,2.788-6.215,6.215s2.788,6.215,6.215,6.215s6.215-2.788,6.215-6.215 S15.448,5.806,12.021,5.806z M12.021,15.412c-1.87,0-3.391-1.521-3.391-3.391s1.521-3.391,3.391-3.391 c1.87,0,3.391,1.521,3.391,3.391S13.891,15.412,12.021,15.412z"></path> <path fill="%23222222" d="M23.369,4.574c-0.357-0.919-0.846-1.669-1.539-2.362c-0.693-0.693-1.443-1.182-2.362-1.539 c-0.905-0.352-1.836-0.533-3.018-0.587c-1.153-0.053-1.536-0.065-4.43-0.065c-2.895,0-3.277,0.012-4.43,0.065 C6.409,0.14,5.478,0.321,4.574,0.673C3.655,1.03,2.904,1.519,2.212,2.212C1.519,2.904,1.03,3.655,0.673,4.573 C0.321,5.478,0.14,6.409,0.086,7.591c-0.053,1.153-0.065,1.536-0.065,4.43s0.012,3.277,0.065,4.43 c0.054,1.182,0.235,2.113,0.587,3.018c0.357,0.919,0.846,1.669,1.539,2.362c0.693,0.693,1.443,1.182,2.362,1.539 c0.905,0.352,1.836,0.533,3.018,0.587c1.153,0.053,1.536,0.065,4.43,0.065c2.895,0,3.277-0.012,4.43-0.065 c1.182-0.054,2.113-0.235,3.018-0.587c0.919-0.357,1.669-0.846,2.362-1.539c0.693-0.693,1.182-1.443,1.539-2.362 c0.352-0.905,0.533-1.836,0.587-3.018c0.053-1.153,0.065-1.536,0.065-4.43s-0.012-3.277-0.065-4.43 C23.902,6.409,23.721,5.478,23.369,4.574z M21.135,16.322c-0.05,1.105-0.239,1.715-0.398,2.123 c-0.216,0.556-0.486,0.971-0.903,1.389c-0.417,0.417-0.833,0.687-1.389,0.904c-0.408,0.159-1.018,0.347-2.123,0.397 c-1.123,0.051-1.46,0.062-4.301,0.062c-2.841,0-3.178-0.011-4.301-0.062c-1.105-0.05-1.715-0.239-2.123-0.398 c-0.556-0.216-0.971-0.486-1.389-0.903c-0.417-0.417-0.687-0.833-0.904-1.389c-0.159-0.408-0.347-1.018-0.397-2.123 c-0.051-1.123-0.062-1.46-0.062-4.301s0.011-3.178,0.062-4.301c0.05-1.105,0.239-1.715,0.398-2.123 c0.216-0.556,0.486-0.971,0.903-1.389c0.417-0.417,0.833-0.687,1.389-0.904C6.005,3.146,6.615,2.957,7.72,2.907 c1.123-0.051,1.46-0.062,4.301-0.062c2.841,0,3.178,0.011,4.302,0.062c1.105,0.05,1.715,0.239,2.123,0.398 c0.556,0.216,0.971,0.486,1.389,0.903c0.417,0.417,0.687,0.833,0.904,1.389c0.159,0.408,0.347,1.018,0.397,2.123 c0.051,1.123,0.062,1.46,0.062,4.301S21.186,15.199,21.135,16.322z"></path> </g> </svg></span>
                        </a><a class="eapps-social-icons-item-github eapps-social-icons-item" href="https://github.com/moieis" target="_blank" rel="nofollow" title="GitHub">
                            <span eapps-link="svg"><svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="24px" height="24px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" xml:space="preserve" class="eapps-social-icons-item-icon"> <g> <path fill="%23222222" d="M22.389,6.269c-1.073-1.839-2.529-3.294-4.367-4.367c-1.839-1.073-3.846-1.609-6.023-1.609 S7.814,0.83,5.977,1.902C4.137,2.975,2.682,4.431,1.609,6.269c-1.073,1.839-1.609,3.846-1.609,6.023 c0,2.615,0.763,4.966,2.289,7.055c1.526,2.089,3.497,3.534,5.914,4.336c0.281,0.052,0.49,0.015,0.625-0.109 c0.135-0.125,0.203-0.281,0.203-0.469c0-0.031-0.003-0.312-0.008-0.844c-0.005-0.531-0.008-0.995-0.008-1.39l-0.359,0.062 c-0.229,0.042-0.518,0.06-0.867,0.055s-0.711-0.041-1.086-0.109c-0.375-0.067-0.724-0.224-1.047-0.468 c-0.323-0.245-0.552-0.565-0.687-0.961l-0.156-0.36c-0.104-0.239-0.268-0.505-0.492-0.797c-0.224-0.292-0.451-0.49-0.68-0.594 l-0.109-0.078c-0.073-0.052-0.141-0.115-0.203-0.188s-0.109-0.146-0.141-0.219c-0.031-0.073-0.005-0.133,0.078-0.18 c0.083-0.047,0.234-0.07,0.453-0.07l0.312,0.047c0.208,0.042,0.466,0.166,0.773,0.375c0.307,0.208,0.56,0.479,0.758,0.812 c0.24,0.427,0.528,0.753,0.867,0.977c0.338,0.224,0.68,0.336,1.023,0.336c0.344,0,0.641-0.026,0.891-0.078s0.484-0.13,0.703-0.234 c0.094-0.698,0.349-1.235,0.766-1.609c-0.594-0.062-1.127-0.156-1.602-0.281c-0.474-0.125-0.963-0.328-1.469-0.61 c-0.505-0.281-0.925-0.63-1.258-1.047c-0.333-0.417-0.607-0.964-0.82-1.641c-0.213-0.677-0.32-1.458-0.32-2.344 c0-1.261,0.412-2.333,1.234-3.219c-0.385-0.948-0.349-2.01,0.109-3.187c0.302-0.094,0.75-0.023,1.344,0.211S8.06,5.908,8.335,6.075 c0.276,0.166,0.497,0.307,0.664,0.422c0.969-0.271,1.969-0.406,3-0.406s2.031,0.135,3,0.406l0.594-0.375 c0.406-0.25,0.885-0.479,1.437-0.688c0.552-0.208,0.974-0.266,1.266-0.172c0.469,1.177,0.51,2.24,0.125,3.187 c0.823,0.885,1.235,1.958,1.235,3.219c0,0.885-0.107,1.669-0.32,2.351c-0.213,0.682-0.489,1.229-0.828,1.641 s-0.761,0.758-1.266,1.039s-0.995,0.484-1.469,0.609s-1.008,0.219-1.601,0.282c0.541,0.469,0.812,1.208,0.812,2.219v3.297 c0,0.187,0.065,0.344,0.195,0.469s0.336,0.161,0.617,0.109c2.417-0.802,4.388-2.247,5.914-4.336 c1.526-2.088,2.289-4.44,2.289-7.055C23.999,10.115,23.462,8.108,22.389,6.269z"></path> </g> </svg></span>
                        </a></div>'''), None, None, None, None]])
            put_html('<hr>')
            put_grid([[None, None, None, put_html('''<svg xmlns="http://www.w3.org/2000/svg" style="margin:auto;background:#ffffff;display:block;" width="150" height="20" preserveAspectRatio="xMidYMid">
<style type="text/css">
  text {
    text-anchor: middle; font-size: 18px; opacity: 0;
  }
</style>
<g style="transform-origin:75px 10px;transform:scale(1)">
<g transform="translate(75,10)">
  <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -57.43px -1.2586px; animation: 100s linear -62.1176s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M5.27 0.20L5.27 0.20L5.27 0.20Q3.28 0.20 1.91-1.48L1.91-1.48L1.91-1.48Q0.54-3.15 0.54-5.58L0.54-5.58L0.54-5.58Q0.54-8.55 2.19-10.58L2.19-10.58L2.19-10.58Q3.83-12.62 6.23-12.62L6.23-12.62L6.23-12.62Q7.16-12.62 7.97-12.43L7.97-12.43L7.97-12.43Q8.77-12.24 9.11-12.04L9.11-12.04L9.43-11.84L8.21-9.34L8.21-9.34Q7.79-9.70 7.04-10.02L7.04-10.02L7.04-10.02Q6.28-10.33 5.67-10.33L5.67-10.33L5.67-10.33Q4.43-10.33 3.68-9.31L3.68-9.31L3.68-9.31Q2.93-8.28 2.93-6.38L2.93-6.38L2.93-6.38Q2.93-4.48 3.71-3.27L3.71-3.27L3.71-3.27Q4.48-2.05 5.81-2.05L5.81-2.05L5.81-2.05Q6.68-2.05 7.38-2.59L7.38-2.59L7.38-2.59Q8.08-3.13 8.37-4.03L8.37-4.03L9.86-3.17L9.86-3.17Q9.27-1.58 8.05-0.69L8.05-0.69L8.05-0.69Q6.82 0.20 5.27 0.20" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -49.13px 0.371399px; animation: 100s linear -58.2353s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M10.76-8.69L10.76-8.69L12.94-9.16L12.94-9.16Q13.10-7.78 13.16-6.53L13.16-6.53L13.16-6.53Q14.80-9.07 16.24-9.07L16.24-9.07L16.04-6.26L16.04-6.26Q14.99-6.26 14.39-6.08L14.39-6.08L14.39-6.08Q13.79-5.89 13.16-5.33L13.16-5.33L13.16-4.68L13.36-0.45L10.94 0L11.16-4.37L11.16-4.37Q11.09-6.79 10.76-8.69" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -42.32px 0.416399px; animation: 100s linear -54.3529s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M20.61-1.84L20.61-1.84L20.61-1.84Q21.13-1.84 21.71-2.11L21.71-2.11L21.71-2.11Q22.28-2.38 22.61-2.65L22.61-2.65L22.93-2.92L23.76-1.91L23.76-1.91Q23.58-1.60 23.20-1.21L23.20-1.21L23.20-1.21Q22.82-0.81 22.44-0.53L22.44-0.53L22.44-0.53Q22.05-0.25 21.41-0.03L21.41-0.03L21.41-0.03Q20.77 0.20 20.09 0.20L20.09 0.20L20.09 0.20Q18.63 0.20 17.71-0.91L17.71-0.91L17.71-0.91Q16.79-2.02 16.79-3.76L16.79-3.76L16.79-3.76Q16.79-5.96 18.07-7.61L18.07-7.61L18.07-7.61Q19.35-9.27 21.06-9.27L21.06-9.27L21.06-9.27Q22.37-9.27 23.10-8.53L23.10-8.53L23.10-8.53Q23.83-7.79 23.83-6.46L23.83-6.46L23.83-6.46Q23.83-5.67 23.56-4.66L23.56-4.66L23.20-4.28L18.70-3.87L18.70-3.87Q19.01-1.84 20.61-1.84zM20.61-7.42L20.61-7.42L20.61-7.42Q19.82-7.42 19.28-6.78L19.28-6.78L19.28-6.78Q18.74-6.14 18.65-5.15L18.65-5.15L21.71-5.53L21.71-5.53Q21.76-5.94 21.76-6.21L21.76-6.21L21.76-6.21Q21.76-7.42 20.61-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -34.1px 0.341399px; animation: 100s linear -50.4706s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M27.20 0L27.20 0Q26.14 0 25.46-0.68L25.46-0.68L25.46-0.68Q24.79-1.35 24.79-2.49L24.79-2.49L24.79-2.49Q24.79-3.64 25.83-4.47L25.83-4.47L25.83-4.47Q26.87-5.31 28.37-5.31L28.37-5.31L29.59-5.31L29.59-5.62L29.59-5.62Q29.59-6.50 29.23-6.82L29.23-6.82L29.23-6.82Q28.87-7.15 27.88-7.15L27.88-7.15L27.88-7.15Q27.47-7.15 26.90-6.98L26.90-6.98L26.90-6.98Q26.33-6.80 25.63-6.44L25.63-6.44L25.11-7.87L25.11-7.87Q25.88-8.41 26.99-8.84L26.99-8.84L26.99-8.84Q28.10-9.27 28.82-9.27L28.82-9.27L28.82-9.27Q31.64-9.27 31.64-6.53L31.64-6.53L31.64-3.01L31.64-3.01Q31.64-2.00 32.27-0.76L32.27-0.76L30.37 0.05L30.37 0.05Q29.92-0.81 29.70-1.49L29.70-1.49L29.70-1.49Q28.71 0 27.20 0L27.20 0zM27.95-1.84L27.95-1.84L27.95-1.84Q28.67-1.84 29.59-2.57L29.59-2.57L29.59-3.78L29.59-3.78Q28.64-4.00 28.04-4.00L28.04-4.00L28.04-4.00Q26.91-4.00 26.91-2.99L26.91-2.99L26.91-2.99Q26.91-2.47 27.20-2.15L27.20-2.15L27.20-2.15Q27.49-1.84 27.95-1.84" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -26.52px -0.618601px; animation: 100s linear -46.5882s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M33.50-8.71L34.54-8.71L34.54-10.67L36.97-11.14L36.74-8.71L38.92-8.71L38.72-7.24L36.67-7.24L36.58-3.47L36.58-3.47Q36.58-2.63 36.74-2.35L36.74-2.35L36.74-2.35Q36.90-2.07 37.33-2.07L37.33-2.07L37.33-2.07Q37.76-2.07 38.48-2.27L38.48-2.27L38.59-0.99L38.59-0.99Q37.40 0 36.50 0L36.50 0L36.50 0Q35.60 0 35.03-0.66L35.03-0.66L35.03-0.66Q34.45-1.31 34.45-2.38L34.45-2.38L34.56-4.39L34.54-7.24L33.30-7.24L33.50-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -19.46px 0.416399px; animation: 100s linear -42.7059s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M43.47-1.84L43.47-1.84L43.47-1.84Q43.99-1.84 44.57-2.11L44.57-2.11L44.57-2.11Q45.14-2.38 45.47-2.65L45.47-2.65L45.79-2.92L46.62-1.91L46.62-1.91Q46.44-1.60 46.06-1.21L46.06-1.21L46.06-1.21Q45.68-0.81 45.30-0.53L45.30-0.53L45.30-0.53Q44.91-0.25 44.27-0.03L44.27-0.03L44.27-0.03Q43.63 0.20 42.95 0.20L42.95 0.20L42.95 0.20Q41.49 0.20 40.57-0.91L40.57-0.91L40.57-0.91Q39.65-2.02 39.65-3.76L39.65-3.76L39.65-3.76Q39.65-5.96 40.93-7.61L40.93-7.61L40.93-7.61Q42.21-9.27 43.92-9.27L43.92-9.27L43.92-9.27Q45.23-9.27 45.96-8.53L45.96-8.53L45.96-8.53Q46.69-7.79 46.69-6.46L46.69-6.46L46.69-6.46Q46.69-5.67 46.42-4.66L46.42-4.66L46.06-4.28L41.56-3.87L41.56-3.87Q41.87-1.84 43.47-1.84zM43.47-7.42L43.47-7.42L43.47-7.42Q42.68-7.42 42.14-6.78L42.14-6.78L42.14-6.78Q41.60-6.14 41.51-5.15L41.51-5.15L44.57-5.53L44.57-5.53Q44.62-5.94 44.62-6.21L44.62-6.21L44.62-6.21Q44.62-7.42 43.47-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -11.025px -1.9136px; animation: 100s linear -38.8235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M53.01-1.76L53.01-1.76L53.01-1.76Q51.61 0 50.58 0L50.58 0L50.58 0Q49.30 0 48.48-1.04L48.48-1.04L48.48-1.04Q47.66-2.09 47.66-3.73L47.66-3.73L47.66-3.73Q47.66-5.98 48.91-7.52L48.91-7.52L48.91-7.52Q50.17-9.07 51.98-9.07L51.98-9.07L52.99-8.93L52.99-9.27L52.78-13.48L55.24-13.93L55.01-4.68L55.01-3.10L55.01-3.10Q55.01-2.02 55.55-0.61L55.55-0.61L53.60 0.20L53.60 0.20Q53.08-0.88 53.01-1.76zM49.68-4.66L49.68-4.66L49.68-4.66Q49.68-3.51 50.10-2.86L50.10-2.86L50.10-2.86Q50.53-2.21 51.33-2.21L51.33-2.21L51.33-2.21Q52.13-2.21 52.99-2.86L52.99-2.86L52.99-6.75L52.99-6.75Q51.91-6.97 51.39-6.97L51.39-6.97L51.39-6.97Q50.58-6.97 50.13-6.39L50.13-6.39L50.13-6.39Q49.68-5.81 49.68-4.66" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 1.18px -2.0136px; animation: 100s linear -34.9412s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M64.84-9.09L64.84-9.09L64.84-9.09Q66.04-9.09 66.80-8.05L66.80-8.05L66.80-8.05Q67.55-7.00 67.55-5.36L67.55-5.36L67.55-5.36Q67.55-3.01 66.32-1.50L66.32-1.50L66.32-1.50Q65.09 0 63.13 0L63.13 0L63.13 0Q62.23 0 60.10-0.29L60.10-0.29L60.28-4.37L60.07-13.48L62.53-13.93L62.30-9.29L62.30-7.34L62.30-7.34Q62.50-7.63 62.78-7.96L62.78-7.96L62.78-7.96Q63.07-8.28 63.68-8.69L63.68-8.69L63.68-8.69Q64.30-9.09 64.84-9.09zM64.13-6.75L64.13-6.75L64.13-6.75Q63.31-6.75 62.30-6.25L62.30-6.25L62.30-4.68L62.41-2.03L62.41-2.03Q63.16-1.94 63.83-1.94L63.83-1.94L63.83-1.94Q65.56-1.94 65.56-4.35L65.56-4.35L65.56-4.35Q65.56-6.75 64.13-6.75" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 9.52999px 2.3514px; animation: 100s linear -31.0588s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M71.62 3.96L69.30 3.47L71.15-0.68L69.82-4.32L68.00-8.69L70.40-9.14L71.55-5.31L72.14-3.49L72.38-3.49L72.81-4.81L74.11-9.16L76.32-8.89L73.13-0.52L71.62 3.96" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 23.695px 0.416399px; animation: 100s linear -27.1765s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M85.41-4.55L85.41-4.55Q85.41-5.80 85.19-6.21L85.19-6.21L85.19-6.21Q84.98-6.62 84.19-6.62L84.19-6.62L84.19-6.62Q83.39-6.62 82.39-5.99L82.39-5.99L82.39-4.68L82.58-0.45L80.17 0L80.39-4.37L80.39-4.37Q80.32-6.79 79.99-8.69L79.99-8.69L82.17-9.16L82.17-9.16Q82.30-8.12 82.35-7.13L82.35-7.13L82.35-7.13Q82.62-7.49 82.96-7.84L82.96-7.84L82.96-7.84Q83.30-8.19 84.04-8.63L84.04-8.63L84.04-8.63Q84.78-9.07 85.54-9.07L85.54-9.07L85.54-9.07Q86.29-9.07 86.81-8.59L86.81-8.59L86.81-8.59Q87.34-8.10 87.48-7.25L87.48-7.25L87.48-7.25Q88.97-9.07 90.50-9.07L90.50-9.07L90.50-9.07Q91.46-9.07 92.02-8.43L92.02-8.43L92.02-8.43Q92.57-7.79 92.57-6.70L92.57-6.70L92.47-4.68L92.66-0.36L90.23 0.09L90.45-4.55L90.45-4.55Q90.45-5.80 90.23-6.21L90.23-6.21L90.23-6.21Q90.02-6.62 89.24-6.62L89.24-6.62L89.24-6.62Q88.47-6.62 87.50-6.03L87.50-6.03L87.43-4.68L87.62-0.36L85.19 0.09L85.41-4.55" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 35.305px 0.416399px; animation: 100s linear -23.2941s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M94.10-3.76L94.10-3.76Q94.10-6.07 95.35-7.67L95.35-7.67L95.35-7.67Q96.59-9.27 98.25-9.27L98.25-9.27L98.25-9.27Q99.92-9.27 100.85-8.19L100.85-8.19L100.85-8.19Q101.77-7.11 101.77-5.33L101.77-5.33L101.77-5.33Q101.77-2.95 100.58-1.38L100.58-1.38L100.58-1.38Q99.38 0.20 97.56 0.20L97.56 0.20L97.56 0.20Q96.07 0.20 95.09-0.93L95.09-0.93L95.09-0.93Q94.10-2.05 94.10-3.76L94.10-3.76zM99.76-4.39L99.76-4.39L99.76-4.39Q99.76-7.00 97.97-7.00L97.97-7.00L97.97-7.00Q96.12-7.00 96.12-4.55L96.12-4.55L96.12-4.55Q96.12-3.28 96.64-2.56L96.64-2.56L96.64-2.56Q97.16-1.84 98.02-1.84L98.02-1.84L98.02-1.84Q98.87-1.84 99.32-2.49L99.32-2.49L99.32-2.49Q99.76-3.15 99.76-4.39" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.885px 0.371399px; animation: 100s linear -19.4118s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M103.32-8.71L105.73-9.16L105.52-4.68L105.71-0.45L103.30 0L103.52-4.37L103.32-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.965px -6.9286px; animation: 100s linear -15.5294s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M103.19-11.80L103.19-11.80L103.19-11.80Q103.19-12.40 103.66-12.88L103.66-12.88L103.66-12.88Q104.13-13.36 104.74-13.36L104.74-13.36L104.74-13.36Q105.35-13.36 105.68-13.02L105.68-13.02L105.68-13.02Q106.00-12.69 106.00-12.02L106.00-12.02L106.00-12.02Q106.00-11.36 105.54-10.88L105.54-10.88L105.54-10.88Q105.08-10.40 104.48-10.40L104.48-10.40L104.48-10.40Q103.88-10.40 103.54-10.80L103.54-10.80L103.54-10.80Q103.19-11.20 103.19-11.80" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 48.025px 0.416399px; animation: 100s linear -11.6471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M110.95-1.84L110.95-1.84L110.95-1.84Q111.47-1.84 112.05-2.11L112.05-2.11L112.05-2.11Q112.63-2.38 112.95-2.65L112.95-2.65L113.27-2.92L114.10-1.91L114.10-1.91Q113.92-1.60 113.54-1.21L113.54-1.21L113.54-1.21Q113.17-0.81 112.78-0.53L112.78-0.53L112.78-0.53Q112.39-0.25 111.75-0.03L111.75-0.03L111.75-0.03Q111.11 0.20 110.43 0.20L110.43 0.20L110.43 0.20Q108.97 0.20 108.05-0.91L108.05-0.91L108.05-0.91Q107.14-2.02 107.14-3.76L107.14-3.76L107.14-3.76Q107.14-5.96 108.41-7.61L108.41-7.61L108.41-7.61Q109.69-9.27 111.40-9.27L111.40-9.27L111.40-9.27Q112.72-9.27 113.45-8.53L113.45-8.53L113.45-8.53Q114.17-7.79 114.17-6.46L114.17-6.46L114.17-6.46Q114.17-5.67 113.90-4.66L113.90-4.66L113.54-4.28L109.04-3.87L109.04-3.87Q109.35-1.84 110.95-1.84zM110.95-7.42L110.95-7.42L110.95-7.42Q110.16-7.42 109.62-6.78L109.62-6.78L109.62-6.78Q109.08-6.14 108.99-5.15L108.99-5.15L112.05-5.53L112.05-5.53Q112.10-5.94 112.10-6.21L112.10-6.21L112.10-6.21Q112.10-7.42 110.95-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.305px 0.371399px; animation: 100s linear -7.76471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M115.74-8.71L118.15-9.16L117.94-4.68L118.13-0.45L115.72 0L115.94-4.37L115.74-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.385px -6.9286px; animation: 100s linear -3.88235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M115.61-11.80L115.61-11.80L115.61-11.80Q115.61-12.40 116.08-12.88L116.08-12.88L116.08-12.88Q116.55-13.36 117.16-13.36L117.16-13.36L117.16-13.36Q117.77-13.36 118.10-13.02L118.10-13.02L118.10-13.02Q118.42-12.69 118.42-12.02L118.42-12.02L118.42-12.02Q118.42-11.36 117.96-10.88L117.96-10.88L117.96-10.88Q117.50-10.40 116.90-10.40L116.90-10.40L116.90-10.40Q116.30-10.40 115.96-10.80L115.96-10.80L115.96-10.80Q115.61-11.20 115.61-11.80" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 59.875px 0.416399px; animation: 100s linear 0s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M122.85-1.67L122.85-1.67L122.85-1.67Q123.79-1.67 123.79-2.50L123.79-2.50L123.79-2.50Q123.79-2.79 123.38-3.04L123.38-3.04L123.38-3.04Q122.98-3.29 122.39-3.55L122.39-3.55L122.39-3.55Q121.81-3.80 121.22-4.11L121.22-4.11L121.22-4.11Q120.64-4.43 120.23-4.99L120.23-4.99L120.23-4.99Q119.83-5.54 119.83-6.26L119.83-6.26L119.83-6.26Q119.83-7.47 120.89-8.37L120.89-8.37L120.89-8.37Q121.95-9.27 123.34-9.27L123.34-9.27L123.34-9.27Q123.98-9.27 124.61-9.12L124.61-9.12L124.61-9.12Q125.23-8.96 125.80-8.64L125.80-8.64L124.60-6.44L124.60-6.44Q124.47-6.55 124.27-6.71L124.27-6.71L124.27-6.71Q124.07-6.88 123.53-7.14L123.53-7.14L123.53-7.14Q122.98-7.40 122.55-7.40L122.55-7.40L122.55-7.40Q122.13-7.40 121.91-7.21L121.91-7.21L121.91-7.21Q121.68-7.02 121.68-6.69L121.68-6.69L121.68-6.69Q121.68-6.35 122.30-6.02L122.30-6.02L122.30-6.02Q122.92-5.69 123.66-5.41L123.66-5.41L123.66-5.41Q124.40-5.13 125.02-4.49L125.02-4.49L125.02-4.49Q125.64-3.85 125.64-2.97L125.64-2.97L125.64-2.97Q125.64-1.71 124.61-0.76L124.61-0.76L124.61-0.76Q123.57 0.20 122.22 0.20L122.22 0.20L122.22 0.20Q121.36 0.20 120.61-0.18L120.61-0.18L120.61-0.18Q119.86-0.56 119.54-0.94L119.54-0.94L119.21-1.31L120.64-2.97L120.64-2.97Q120.74-2.83 120.94-2.61L120.94-2.61L120.94-2.61Q121.14-2.39 121.73-2.03L121.73-2.03L121.73-2.03Q122.31-1.67 122.85-1.67" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g></g>
</g>
</g>
</svg>'''), None, None, None]])

        with use_scope(name='first', clear=True):
            put_html("<hr>")
            put_grid([[None, None, None, None, put_html('''<g style="transform-origin: 183px 15px; transform: scale(0.9);">
        <g transform="translate(183,15)">
          <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -192.01px -2.04379px; animation: 100s linear -64.0588s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M8 0L0.40 0L0.40-3.28L1.40-3.28L1.40-12.28L0.40-12.28L0.40-15.56L8-15.56L8-12.28L7-12.28L7-3.28L8-3.28L8 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -183.36px -0.863789px; animation: 100s linear -62.1176s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M13.70 0.28L13.70 0.28Q11.58 0.28 10.51-0.75L10.51-0.75L10.51-0.75Q9.44-1.78 9.44-4.22L9.44-4.22L9.44-7.84L8.56-7.84L8.56-11.12L8.56-11.12Q9.32-11.12 9.70-11.51L9.70-11.51L9.70-11.51Q10.08-11.90 10.08-12.58L10.08-12.58L10.08-13.48L14.32-13.48L14.32-11.12L17.02-11.12L17.02-7.84L14.32-7.84L14.32-4.56L14.32-4.56Q14.32-3.90 14.61-3.59L14.61-3.59L14.61-3.59Q14.90-3.28 15.48-3.28L15.48-3.28L15.48-3.28Q16.24-3.28 17.14-3.46L17.14-3.46L17.14-0.32L17.14-0.32Q16.58-0.10 15.63 0.09L15.63 0.09L15.63 0.09Q14.68 0.28 13.70 0.28L13.70 0.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -163.23px 0.176211px; animation: 100s linear -60.1765s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M31.70 0L27.10 0L24.46-7.84L23.62-7.84L23.62-11.12L29.80-11.12L29.80-7.84L28.96-7.84L29.68-4.72L29.88-4.72L31.34-11.12L35.02-11.12L36.48-4.72L36.68-4.72L37.38-7.84L36.54-7.84L36.54-11.12L42.34-11.12L42.34-7.84L41.50-7.84L38.96 0L34.10 0L33-5.56L32.80-5.56L31.70 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -150.31px -8.15379px; animation: 100s linear -58.2353s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M47.94-12.22L43.86-12.22L43.86-15.56L47.94-15.56L47.94-12.22" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -150.13px 0.176211px; animation: 100s linear -56.2941s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M49.26 0L42.90 0L42.90-3.28L43.78-3.28L43.78-7.84L42.90-7.84L42.90-11.12L48.38-11.12L48.38-3.28L49.26-3.28L49.26 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -143.21px -2.03379px; animation: 100s linear -54.3529s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M56.18 0.02L49.82 0.02L49.82-3.28L50.70-3.28L50.70-12.28L49.82-12.28L49.82-15.56L55.30-15.56L55.30-3.28L56.18-3.28L56.18 0.02" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -136.21px -2.03379px; animation: 100s linear -52.4118s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M63.18 0.02L56.82 0.02L56.82-3.28L57.70-3.28L57.70-12.28L56.82-12.28L56.82-15.56L62.30-15.56L62.30-3.28L63.18-3.28L63.18 0.02" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -119.75px 0.036211px; animation: 100s linear -50.4706s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M82.22-3.28L83.10-3.28L83.10 0L76.78 0L76.78-3.28L77.62-3.28L77.62-6.56L77.62-6.56Q77.62-7.22 77.34-7.53L77.34-7.53L77.34-7.53Q77.06-7.84 76.50-7.84L76.50-7.84L76.50-7.84Q75.30-7.84 75.30-6.56L75.30-6.56L75.30-3.28L76.14-3.28L76.14 0L69.82 0L69.82-3.28L70.70-3.28L70.70-7.84L69.82-7.84L69.82-11.12L75.30-11.12L75.30-9.56L75.30-9.56Q76.74-11.40 78.90-11.40L78.90-11.40L78.90-11.40Q80.56-11.40 81.39-10.36L81.39-10.36L81.39-10.36Q82.22-9.32 82.22-7.50L82.22-7.50L82.22-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -106.51px 0.176211px; animation: 100s linear -48.5294s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M89.70 0.28L89.70 0.28Q86.86 0.28 85.26-1.21L85.26-1.21L85.26-1.21Q83.66-2.70 83.66-5.56L83.66-5.56L83.66-5.56Q83.66-8.42 85.26-9.91L85.26-9.91L85.26-9.91Q86.86-11.40 89.70-11.40L89.70-11.40L89.70-11.40Q92.58-11.40 94.16-9.89L94.16-9.89L94.16-9.89Q95.74-8.38 95.74-5.56L95.74-5.56L95.74-5.56Q95.74-2.70 94.14-1.21L94.14-1.21L94.14-1.21Q92.54 0.28 89.70 0.28L89.70 0.28zM89.70-3.28L89.70-3.28Q90.28-3.28 90.57-3.59L90.57-3.59L90.57-3.59Q90.86-3.90 90.86-4.56L90.86-4.56L90.86-6.56L90.86-6.56Q90.86-7.22 90.57-7.53L90.57-7.53L90.57-7.53Q90.28-7.84 89.70-7.84L89.70-7.84L89.70-7.84Q89.12-7.84 88.83-7.53L88.83-7.53L88.83-7.53Q88.54-7.22 88.54-6.56L88.54-6.56L88.54-4.56L88.54-4.56Q88.54-3.90 88.83-3.59L88.83-3.59L88.83-3.59Q89.12-3.28 89.70-3.28L89.70-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -90.63px 0.176211px; animation: 100s linear -46.5882s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M104.30 0L99.70 0L97.06-7.84L96.22-7.84L96.22-11.12L102.40-11.12L102.40-7.84L101.56-7.84L102.28-4.72L102.48-4.72L103.94-11.12L107.62-11.12L109.08-4.72L109.28-4.72L109.98-7.84L109.14-7.84L109.14-11.12L114.94-11.12L114.94-7.84L114.10-7.84L111.56 0L106.70 0L105.60-5.56L105.40-5.56L104.30 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -68.53px -1.90379px; animation: 100s linear -44.6471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M125.44 0.28L125.44 0.28Q123.40 0.28 122.37-1.24L122.37-1.24L122.37-1.24Q121.34-2.76 121.34-5.56L121.34-5.56L121.34-5.56Q121.34-8.36 122.37-9.88L122.37-9.88L122.37-9.88Q123.40-11.40 125.44-11.40L125.44-11.40L125.44-11.40Q126.46-11.40 127.25-10.90L127.25-10.90L127.25-10.90Q128.04-10.40 128.54-9.76L128.54-9.76L128.54-12.28L127.36-12.28L127.36-15.56L133.14-15.56L133.14-3.28L134.02-3.28L134.02 0L128.54 0L128.54-1.36L128.54-1.36Q128.04-0.72 127.25-0.22L127.25-0.22L127.25-0.22Q126.46 0.28 125.44 0.28L125.44 0.28zM127.38-3.28L127.38-3.28Q127.96-3.28 128.25-3.59L128.25-3.59L128.25-3.59Q128.54-3.90 128.54-4.56L128.54-4.56L128.54-6.56L128.54-6.56Q128.54-7.22 128.25-7.53L128.25-7.53L128.25-7.53Q127.96-7.84 127.38-7.84L127.38-7.84L127.38-7.84Q126.80-7.84 126.51-7.53L126.51-7.53L126.51-7.53Q126.22-7.22 126.22-6.56L126.22-6.56L126.22-4.56L126.22-4.56Q126.22-3.90 126.51-3.59L126.51-3.59L126.51-3.59Q126.80-3.28 127.38-3.28L127.38-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -55.59px 0.176211px; animation: 100s linear -42.7059s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M140.62 0.28L140.62 0.28Q137.78 0.28 136.18-1.21L136.18-1.21L136.18-1.21Q134.58-2.70 134.58-5.56L134.58-5.56L134.58-5.56Q134.58-8.42 136.18-9.91L136.18-9.91L136.18-9.91Q137.78-11.40 140.62-11.40L140.62-11.40L140.62-11.40Q143.50-11.40 145.08-9.89L145.08-9.89L145.08-9.89Q146.66-8.38 146.66-5.56L146.66-5.56L146.66-5.56Q146.66-2.70 145.06-1.21L145.06-1.21L145.06-1.21Q143.46 0.28 140.62 0.28L140.62 0.28zM140.62-3.28L140.62-3.28Q141.20-3.28 141.49-3.59L141.49-3.59L141.49-3.59Q141.78-3.90 141.78-4.56L141.78-4.56L141.78-6.56L141.78-6.56Q141.78-7.22 141.49-7.53L141.49-7.53L141.49-7.53Q141.20-7.84 140.62-7.84L140.62-7.84L140.62-7.84Q140.04-7.84 139.75-7.53L139.75-7.53L139.75-7.53Q139.46-7.22 139.46-6.56L139.46-6.56L139.46-4.56L139.46-4.56Q139.46-3.90 139.75-3.59L139.75-3.59L139.75-3.59Q140.04-3.28 140.62-3.28L140.62-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -39.71px 0.176211px; animation: 100s linear -40.7647s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M155.22 0L150.62 0L147.98-7.84L147.14-7.84L147.14-11.12L153.32-11.12L153.32-7.84L152.48-7.84L153.20-4.72L153.40-4.72L154.86-11.12L158.54-11.12L160-4.72L160.20-4.72L160.90-7.84L160.06-7.84L160.06-11.12L165.86-11.12L165.86-7.84L165.02-7.84L162.48 0L157.62 0L156.52-5.56L156.32-5.56L155.22 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -23.15px 0.036211px; animation: 100s linear -38.8235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M178.82-3.28L179.70-3.28L179.70 0L173.38 0L173.38-3.28L174.22-3.28L174.22-6.56L174.22-6.56Q174.22-7.22 173.94-7.53L173.94-7.53L173.94-7.53Q173.66-7.84 173.10-7.84L173.10-7.84L173.10-7.84Q171.90-7.84 171.90-6.56L171.90-6.56L171.90-3.28L172.74-3.28L172.74 0L166.42 0L166.42-3.28L167.30-3.28L167.30-7.84L166.42-7.84L166.42-11.12L171.90-11.12L171.90-9.56L171.90-9.56Q173.34-11.40 175.50-11.40L175.50-11.40L175.50-11.40Q177.16-11.40 177.99-10.36L177.99-10.36L177.99-10.36Q178.82-9.32 178.82-7.50L178.82-7.50L178.82-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -12.69px -2.03379px; animation: 100s linear -36.8824s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M186.70 0.02L180.34 0.02L180.34-3.28L181.22-3.28L181.22-12.28L180.34-12.28L180.34-15.56L185.82-15.56L185.82-3.28L186.70-3.28L186.70 0.02" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -2.91003px 0.176211px; animation: 100s linear -34.9412s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M193.30 0.28L193.30 0.28Q190.46 0.28 188.86-1.21L188.86-1.21L188.86-1.21Q187.26-2.70 187.26-5.56L187.26-5.56L187.26-5.56Q187.26-8.42 188.86-9.91L188.86-9.91L188.86-9.91Q190.46-11.40 193.30-11.40L193.30-11.40L193.30-11.40Q196.18-11.40 197.76-9.89L197.76-9.89L197.76-9.89Q199.34-8.38 199.34-5.56L199.34-5.56L199.34-5.56Q199.34-2.70 197.74-1.21L197.74-1.21L197.74-1.21Q196.14 0.28 193.30 0.28L193.30 0.28zM193.30-3.28L193.30-3.28Q193.88-3.28 194.17-3.59L194.17-3.59L194.17-3.59Q194.46-3.90 194.46-4.56L194.46-4.56L194.46-6.56L194.46-6.56Q194.46-7.22 194.17-7.53L194.17-7.53L194.17-7.53Q193.88-7.84 193.30-7.84L193.30-7.84L193.30-7.84Q192.72-7.84 192.43-7.53L192.43-7.53L192.43-7.53Q192.14-7.22 192.14-6.56L192.14-6.56L192.14-4.56L192.14-4.56Q192.14-3.90 192.43-3.59L192.43-3.59L192.43-3.59Q192.72-3.28 193.30-3.28L193.30-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 9.59998px 0.176211px; animation: 100s linear -33s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M210.76-3.28L211.64-3.28L211.64 0L206.36 0L206.36-1.36L206.36-1.36Q205.92-0.72 205.13-0.22L205.13-0.22L205.13-0.22Q204.34 0.28 203.20 0.28L203.20 0.28L203.20 0.28Q201.70 0.28 200.84-0.52L200.84-0.52L200.84-0.52Q199.98-1.32 199.98-2.78L199.98-2.78L199.98-2.78Q199.98-6.56 206.40-6.66L206.40-6.66L206.40-6.66Q206.34-7.34 205.88-7.59L205.88-7.59L205.88-7.59Q205.42-7.84 204.32-7.84L204.32-7.84L204.32-7.84Q203.42-7.84 202.39-7.65L202.39-7.65L202.39-7.65Q201.36-7.46 200.50-7.14L200.50-7.14L200.50-10.82L200.50-10.82Q201.56-11.08 202.80-11.24L202.80-11.24L202.80-11.24Q204.04-11.40 205.22-11.40L205.22-11.40L205.22-11.40Q208.20-11.40 209.48-10.32L209.48-10.32L209.48-10.32Q210.76-9.24 210.76-6.98L210.76-6.98L210.76-3.28zM206.36-4.56L206.36-4.68L206.36-4.68Q205.46-4.68 204.97-4.44L204.97-4.44L204.97-4.44Q204.48-4.20 204.48-3.64L204.48-3.64L204.48-3.64Q204.48-3.30 204.69-3.09L204.69-3.09L204.69-3.09Q204.90-2.88 205.28-2.88L205.28-2.88L205.28-2.88Q205.80-2.88 206.08-3.32L206.08-3.32L206.08-3.32Q206.36-3.76 206.36-4.56L206.36-4.56" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 22.25px -1.90379px; animation: 100s linear -31.0588s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M216.22 0.28L216.22 0.28Q214.18 0.28 213.15-1.24L213.15-1.24L213.15-1.24Q212.12-2.76 212.12-5.56L212.12-5.56L212.12-5.56Q212.12-8.36 213.15-9.88L213.15-9.88L213.15-9.88Q214.18-11.40 216.22-11.40L216.22-11.40L216.22-11.40Q217.24-11.40 218.03-10.90L218.03-10.90L218.03-10.90Q218.82-10.40 219.32-9.76L219.32-9.76L219.32-12.28L218.14-12.28L218.14-15.56L223.92-15.56L223.92-3.28L224.80-3.28L224.80 0L219.32 0L219.32-1.36L219.32-1.36Q218.82-0.72 218.03-0.22L218.03-0.22L218.03-0.22Q217.24 0.28 216.22 0.28L216.22 0.28zM218.16-3.28L218.16-3.28Q218.74-3.28 219.03-3.59L219.03-3.59L219.03-3.59Q219.32-3.90 219.32-4.56L219.32-4.56L219.32-6.56L219.32-6.56Q219.32-7.22 219.03-7.53L219.03-7.53L219.03-7.53Q218.74-7.84 218.16-7.84L218.16-7.84L218.16-7.84Q217.58-7.84 217.29-7.53L217.29-7.53L217.29-7.53Q217.00-7.22 217.00-6.56L217.00-6.56L217.00-4.56L217.00-4.56Q217.00-3.90 217.29-3.59L217.29-3.59L217.29-3.59Q217.58-3.28 218.16-3.28L218.16-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.06px 0.176211px; animation: 100s linear -29.1176s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M242.22-3.28L243.10-3.28L243.10 0L237.82 0L237.82-1.36L237.82-1.36Q237.38-0.72 236.59-0.22L236.59-0.22L236.59-0.22Q235.80 0.28 234.66 0.28L234.66 0.28L234.66 0.28Q233.16 0.28 232.30-0.52L232.30-0.52L232.30-0.52Q231.44-1.32 231.44-2.78L231.44-2.78L231.44-2.78Q231.44-6.56 237.86-6.66L237.86-6.66L237.86-6.66Q237.80-7.34 237.34-7.59L237.34-7.59L237.34-7.59Q236.88-7.84 235.78-7.84L235.78-7.84L235.78-7.84Q234.88-7.84 233.85-7.65L233.85-7.65L233.85-7.65Q232.82-7.46 231.96-7.14L231.96-7.14L231.96-10.82L231.96-10.82Q233.02-11.08 234.26-11.24L234.26-11.24L234.26-11.24Q235.50-11.40 236.68-11.40L236.68-11.40L236.68-11.40Q239.66-11.40 240.94-10.32L240.94-10.32L240.94-10.32Q242.22-9.24 242.22-6.98L242.22-6.98L242.22-3.28zM237.82-4.56L237.82-4.68L237.82-4.68Q236.92-4.68 236.43-4.44L236.43-4.44L236.43-4.44Q235.94-4.20 235.94-3.64L235.94-3.64L235.94-3.64Q235.94-3.30 236.15-3.09L236.15-3.09L236.15-3.09Q236.36-2.88 236.74-2.88L236.74-2.88L236.74-2.88Q237.26-2.88 237.54-3.32L237.54-3.32L237.54-3.32Q237.82-3.76 237.82-4.56L237.82-4.56" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.05px 0.316211px; animation: 100s linear -27.1765s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M256.02-3.28L256.90-3.28L256.90 0L251.42 0L251.42-1.56L251.42-1.56Q249.98 0.28 247.82 0.28L247.82 0.28L247.82 0.28Q246.16 0.28 245.33-0.76L245.33-0.76L245.33-0.76Q244.50-1.80 244.50-3.62L244.50-3.62L244.50-7.84L243.62-7.84L243.62-11.12L249.10-11.12L249.10-4.56L249.10-4.56Q249.10-3.90 249.39-3.59L249.39-3.59L249.39-3.59Q249.68-3.28 250.26-3.28L250.26-3.28L250.26-3.28Q250.84-3.28 251.13-3.59L251.13-3.59L251.13-3.59Q251.42-3.90 251.42-4.56L251.42-4.56L251.42-7.84L250.34-7.84L250.34-11.12L256.02-11.12L256.02-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 65.34px -0.863789px; animation: 100s linear -25.2353s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M262.40 0.28L262.40 0.28Q260.28 0.28 259.21-0.75L259.21-0.75L259.21-0.75Q258.14-1.78 258.14-4.22L258.14-4.22L258.14-7.84L257.26-7.84L257.26-11.12L257.26-11.12Q258.02-11.12 258.40-11.51L258.40-11.51L258.40-11.51Q258.78-11.90 258.78-12.58L258.78-12.58L258.78-13.48L263.02-13.48L263.02-11.12L265.72-11.12L265.72-7.84L263.02-7.84L263.02-4.56L263.02-4.56Q263.02-3.90 263.31-3.59L263.31-3.59L263.31-3.59Q263.60-3.28 264.18-3.28L264.18-3.28L264.18-3.28Q264.94-3.28 265.84-3.46L265.84-3.46L265.84-0.32L265.84-0.32Q265.28-0.10 264.33 0.09L264.33 0.09L264.33 0.09Q263.38 0.28 262.40 0.28L262.40 0.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 76.23px 0.176211px; animation: 100s linear -23.2941s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M272.44 0.28L272.44 0.28Q269.60 0.28 268-1.21L268-1.21L268-1.21Q266.40-2.70 266.40-5.56L266.40-5.56L266.40-5.56Q266.40-8.42 268-9.91L268-9.91L268-9.91Q269.60-11.40 272.44-11.40L272.44-11.40L272.44-11.40Q275.32-11.40 276.90-9.89L276.90-9.89L276.90-9.89Q278.48-8.38 278.48-5.56L278.48-5.56L278.48-5.56Q278.48-2.70 276.88-1.21L276.88-1.21L276.88-1.21Q275.28 0.28 272.44 0.28L272.44 0.28zM272.44-3.28L272.44-3.28Q273.02-3.28 273.31-3.59L273.31-3.59L273.31-3.59Q273.60-3.90 273.60-4.56L273.60-4.56L273.60-6.56L273.60-6.56Q273.60-7.22 273.31-7.53L273.31-7.53L273.31-7.53Q273.02-7.84 272.44-7.84L272.44-7.84L272.44-7.84Q271.86-7.84 271.57-7.53L271.57-7.53L271.57-7.53Q271.28-7.22 271.28-6.56L271.28-6.56L271.28-4.56L271.28-4.56Q271.28-3.90 271.57-3.59L271.57-3.59L271.57-3.59Q271.86-3.28 272.44-3.28L272.44-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 93.01px 0.036211px; animation: 100s linear -21.3529s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M298.44-3.28L299.32-3.28L299.32 0L293 0L293-3.28L293.84-3.28L293.84-6.56L293.84-6.56Q293.84-7.22 293.56-7.53L293.56-7.53L293.56-7.53Q293.28-7.84 292.72-7.84L292.72-7.84L292.72-7.84Q291.52-7.84 291.52-6.56L291.52-6.56L291.52-3.28L292.36-3.28L292.36 0L286.08 0L286.08-3.28L286.92-3.28L286.92-6.56L286.92-6.56Q286.92-7.22 286.64-7.53L286.64-7.53L286.64-7.53Q286.36-7.84 285.80-7.84L285.80-7.84L285.80-7.84Q284.60-7.84 284.60-6.56L284.60-6.56L284.60-3.28L285.44-3.28L285.44 0L279.12 0L279.12-3.28L280-3.28L280-7.84L279.12-7.84L279.12-11.12L284.60-11.12L284.60-9.56L284.60-9.56Q286.04-11.40 288.20-11.40L288.20-11.40L288.20-11.40Q289.42-11.40 290.19-10.83L290.19-10.83L290.19-10.83Q290.96-10.26 291.28-9.22L291.28-9.22L291.28-9.22Q292-10.26 292.93-10.82L292.93-10.82L292.93-10.82Q293.86-11.38 295.12-11.38L295.12-11.38L295.12-11.38Q296.78-11.38 297.61-10.34L297.61-10.34L297.61-10.34Q298.44-9.30 298.44-7.48L298.44-7.48L298.44-3.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 109.58px 0.176211px; animation: 100s linear -19.4118s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M310.74-3.28L311.62-3.28L311.62 0L306.34 0L306.34-1.36L306.34-1.36Q305.90-0.72 305.11-0.22L305.11-0.22L305.11-0.22Q304.32 0.28 303.18 0.28L303.18 0.28L303.18 0.28Q301.68 0.28 300.82-0.52L300.82-0.52L300.82-0.52Q299.96-1.32 299.96-2.78L299.96-2.78L299.96-2.78Q299.96-6.56 306.38-6.66L306.38-6.66L306.38-6.66Q306.32-7.34 305.86-7.59L305.86-7.59L305.86-7.59Q305.40-7.84 304.30-7.84L304.30-7.84L304.30-7.84Q303.40-7.84 302.37-7.65L302.37-7.65L302.37-7.65Q301.34-7.46 300.48-7.14L300.48-7.14L300.48-10.82L300.48-10.82Q301.54-11.08 302.78-11.24L302.78-11.24L302.78-11.24Q304.02-11.40 305.20-11.40L305.20-11.40L305.20-11.40Q308.18-11.40 309.46-10.32L309.46-10.32L309.46-10.32Q310.74-9.24 310.74-6.98L310.74-6.98L310.74-3.28zM306.34-4.56L306.34-4.68L306.34-4.68Q305.44-4.68 304.95-4.44L304.95-4.44L304.95-4.44Q304.46-4.20 304.46-3.64L304.46-3.64L304.46-3.64Q304.46-3.30 304.67-3.09L304.67-3.09L304.67-3.09Q304.88-2.88 305.26-2.88L305.26-2.88L305.26-2.88Q305.78-2.88 306.06-3.32L306.06-3.32L306.06-3.32Q306.34-3.76 306.34-4.56L306.34-4.56" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 120.14px -0.863789px; animation: 100s linear -17.4706s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M317.20 0.28L317.20 0.28Q315.08 0.28 314.01-0.75L314.01-0.75L314.01-0.75Q312.94-1.78 312.94-4.22L312.94-4.22L312.94-7.84L312.06-7.84L312.06-11.12L312.06-11.12Q312.82-11.12 313.20-11.51L313.20-11.51L313.20-11.51Q313.58-11.90 313.58-12.58L313.58-12.58L313.58-13.48L317.82-13.48L317.82-11.12L320.52-11.12L320.52-7.84L317.82-7.84L317.82-4.56L317.82-4.56Q317.82-3.90 318.11-3.59L318.11-3.59L318.11-3.59Q318.40-3.28 318.98-3.28L318.98-3.28L318.98-3.28Q319.74-3.28 320.64-3.46L320.64-3.46L320.64-0.32L320.64-0.32Q320.08-0.10 319.13 0.09L319.13 0.09L319.13 0.09Q318.18 0.28 317.20 0.28L317.20 0.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 128.07px -8.15379px; animation: 100s linear -15.5294s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M326.32-12.22L322.24-12.22L322.24-15.56L326.32-15.56L326.32-12.22" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 128.25px 0.176211px; animation: 100s linear -13.5882s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M327.64 0L321.28 0L321.28-3.28L322.16-3.28L322.16-7.84L321.28-7.84L321.28-11.12L326.76-11.12L326.76-3.28L327.64-3.28L327.64 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 137.23px 0.176211px; animation: 100s linear -11.6471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M334.18 0.28L334.18 0.28Q331.32 0.28 329.72-1.21L329.72-1.21L329.72-1.21Q328.12-2.70 328.12-5.56L328.12-5.56L328.12-5.56Q328.12-8.42 329.72-9.91L329.72-9.91L329.72-9.91Q331.32-11.40 334.16-11.40L334.16-11.40L334.16-11.40Q335.54-11.40 336.80-11.02L336.80-11.02L336.80-11.02Q338.06-10.64 338.76-10.16L338.76-10.16L338.76-6.20L335.32-6.20L335.32-6.56L335.32-6.56Q335.32-7.22 335.04-7.53L335.04-7.53L335.04-7.53Q334.76-7.84 334.16-7.84L334.16-7.84L334.16-7.84Q333-7.84 333-6.56L333-6.56L333-4.84L333-4.84Q333-3.28 334.78-3.28L334.78-3.28L334.78-3.28Q336.44-3.28 338.64-3.64L338.64-3.64L338.64-0.50L338.64-0.50Q337.96-0.20 336.73 0.04L336.73 0.04L336.73 0.04Q335.50 0.28 334.18 0.28L334.18 0.28" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 149.06px 0.176211px; animation: 100s linear -9.70588s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M350.22-3.28L351.10-3.28L351.10 0L345.82 0L345.82-1.36L345.82-1.36Q345.38-0.72 344.59-0.22L344.59-0.22L344.59-0.22Q343.80 0.28 342.66 0.28L342.66 0.28L342.66 0.28Q341.16 0.28 340.30-0.52L340.30-0.52L340.30-0.52Q339.44-1.32 339.44-2.78L339.44-2.78L339.44-2.78Q339.44-6.56 345.86-6.66L345.86-6.66L345.86-6.66Q345.80-7.34 345.34-7.59L345.34-7.59L345.34-7.59Q344.88-7.84 343.78-7.84L343.78-7.84L343.78-7.84Q342.88-7.84 341.85-7.65L341.85-7.65L341.85-7.65Q340.82-7.46 339.96-7.14L339.96-7.14L339.96-10.82L339.96-10.82Q341.02-11.08 342.26-11.24L342.26-11.24L342.26-11.24Q343.50-11.40 344.68-11.40L344.68-11.40L344.68-11.40Q347.66-11.40 348.94-10.32L348.94-10.32L348.94-10.32Q350.22-9.24 350.22-6.98L350.22-6.98L350.22-3.28zM345.82-4.56L345.82-4.68L345.82-4.68Q344.92-4.68 344.43-4.44L344.43-4.44L344.43-4.44Q343.94-4.20 343.94-3.64L343.94-3.64L343.94-3.64Q343.94-3.30 344.15-3.09L344.15-3.09L344.15-3.09Q344.36-2.88 344.74-2.88L344.74-2.88L344.74-2.88Q345.26-2.88 345.54-3.32L345.54-3.32L345.54-3.32Q345.82-3.76 345.82-4.56L345.82-4.56" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 158.71px -2.03379px; animation: 100s linear -7.76471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M358.10 0.02L351.74 0.02L351.74-3.28L352.62-3.28L352.62-12.28L351.74-12.28L351.74-15.56L357.22-15.56L357.22-3.28L358.10-3.28L358.10 0.02" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 165.71px -2.03379px; animation: 100s linear -5.82353s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M365.10 0.02L358.74 0.02L358.74-3.28L359.62-3.28L359.62-12.28L358.74-12.28L358.74-15.56L364.22-15.56L364.22-3.28L365.10-3.28L365.10 0.02" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 175.47px 2.34621px; animation: 100s linear -3.88235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M372.22-11.12L377.78-11.12L377.78-7.84L377.02-7.84L374.40-0.90L374.40-0.90Q373.42 1.72 372.16 3.03L372.16 3.03L372.16 3.03Q370.90 4.34 368.84 4.34L368.84 4.34L368.84 4.34Q368 4.34 367.14 4.17L367.14 4.17L367.14 4.17Q366.28 4 365.58 3.70L365.58 3.70L365.58 0.08L368.34 0.08L368.34 0.28L368.34 0.28Q368.34 0.78 368.86 0.78L368.86 0.78L368.86 0.78Q369.32 0.78 369.56 0.34L369.56 0.34L366.40-7.84L365.64-7.84L365.64-11.12L371.58-11.12L371.58-7.84L370.90-7.84L371.94-4.72L372.90-7.84L372.22-7.84L372.22-11.12" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 190.17px 4.09621px; animation: 100s linear -1.94118s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M387.94 0L384.82 0L384.82-3.28L387.94-3.28L387.94 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 195.05px 4.09621px; animation: 100s linear 0s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M392.82 0L389.70 0L389.70-3.28L392.82-3.28L392.82 0" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-196.21002197265625,5.736210802863627)" style="fill: rgb(40, 41, 47);"></path></g></g>
        </g>
        </g>'''), None, None, None, None]])
            clear(scope='down')
            print(w.title)
            s = open(u, 'rb').read()

            download('down', content=s)
            toast('if it is not downloaded, click on download !', color='#000000')
            time.sleep(1)
            put_grid([[None, None, None, None, None,
                       put_button(label='download', onclick=doit, outline=True, color='dark'), None, None, None, None]])
            put_html('<hr>')
            put_grid([[None, None, None, None, put_html('''


                                                            <head>
                                                        <meta charset="UTF-8">
                                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                                        <meta http-equiv="X-UA-Compatible" content="ie=edge">
                                                        <title>SocialIcons Preview</title>
                                                    <style>.eapps-preview-widget {
                                                      width: 100%;
                                                    }
                                                    </style><style>.eapps-widget {
                                                      -webkit-animation: none;
                                                              animation: none;
                                                      -webkit-animation-delay: 0;
                                                              animation-delay: 0;
                                                      -webkit-animation-direction: normal;
                                                              animation-direction: normal;
                                                      -webkit-animation-duration: 0;
                                                              animation-duration: 0;
                                                      -webkit-animation-fill-mode: none;
                                                              animation-fill-mode: none;
                                                      -webkit-animation-iteration-count: 1;
                                                              animation-iteration-count: 1;
                                                      -webkit-animation-name: none;
                                                              animation-name: none;
                                                      -webkit-animation-play-state: running;
                                                              animation-play-state: running;
                                                      -webkit-animation-timing-function: ease;
                                                              animation-timing-function: ease;
                                                      -webkit-backface-visibility: visible;
                                                              backface-visibility: visible;
                                                      background: 0;
                                                      background-attachment: scroll;
                                                      background-clip: border-box;
                                                      background-color: transparent;
                                                      background-image: none;
                                                      background-origin: padding-box;
                                                      background-position: 0 0;
                                                      background-position-x: 0;
                                                      background-position-y: 0;
                                                      background-repeat: repeat;
                                                      background-size: auto auto;
                                                      border: 0;
                                                      border-style: none;
                                                      border-width: medium;
                                                      border-color: inherit;
                                                      border-bottom: 0;
                                                      border-bottom-color: inherit;
                                                      border-bottom-left-radius: 0;
                                                      border-bottom-right-radius: 0;
                                                      border-bottom-style: none;
                                                      border-bottom-width: medium;
                                                      border-collapse: separate;
                                                      -o-border-image: none;
                                                         border-image: none;
                                                      border-left: 0;
                                                      border-left-color: inherit;
                                                      border-left-style: none;
                                                      border-left-width: medium;
                                                      border-radius: 0;
                                                      border-right: 0;
                                                      border-right-color: inherit;
                                                      border-right-style: none;
                                                      border-right-width: medium;
                                                      border-spacing: 0;
                                                      border-top: 0;
                                                      border-top-color: inherit;
                                                      border-top-left-radius: 0;
                                                      border-top-right-radius: 0;
                                                      border-top-style: none;
                                                      border-top-width: medium;
                                                      bottom: auto;
                                                      box-shadow: none;
                                                      box-sizing: content-box;
                                                      caption-side: top;
                                                      clear: none;
                                                      clip: auto;
                                                      color: inherit;
                                                      -webkit-columns: auto;
                                                         -moz-columns: auto;
                                                              columns: auto;
                                                      -webkit-column-count: auto;
                                                         -moz-column-count: auto;
                                                              column-count: auto;
                                                      -webkit-column-fill: balance;
                                                         -moz-column-fill: balance;
                                                              column-fill: balance;
                                                      grid-column-gap: normal;
                                                      -webkit-column-gap: normal;
                                                         -moz-column-gap: normal;
                                                              column-gap: normal;
                                                      -webkit-column-rule: medium none currentColor;
                                                         -moz-column-rule: medium none currentColor;
                                                              column-rule: medium none currentColor;
                                                      -webkit-column-rule-color: currentColor;
                                                         -moz-column-rule-color: currentColor;
                                                              column-rule-color: currentColor;
                                                      -webkit-column-rule-style: none;
                                                         -moz-column-rule-style: none;
                                                              column-rule-style: none;
                                                      -webkit-column-rule-width: none;
                                                         -moz-column-rule-width: none;
                                                              column-rule-width: none;
                                                      -webkit-column-span: 1;
                                                         -moz-column-span: 1;
                                                              column-span: 1;
                                                      -webkit-column-width: auto;
                                                         -moz-column-width: auto;
                                                              column-width: auto;
                                                      content: normal;
                                                      counter-increment: none;
                                                      counter-reset: none;
                                                      direction: ltr;
                                                      empty-cells: show;
                                                      float: none;
                                                      font: normal;
                                                      font-family: inherit;
                                                      font-size: medium;
                                                      font-style: normal;
                                                      font-feature-settings: normal;
                                                      font-variant: normal;
                                                      font-weight: normal;
                                                      height: auto;
                                                      -webkit-hyphens: none;
                                                          -ms-hyphens: none;
                                                              hyphens: none;
                                                      left: auto;
                                                      letter-spacing: normal;
                                                      line-height: normal;
                                                      list-style: none;
                                                      list-style-image: none;
                                                      list-style-position: outside;
                                                      list-style-type: disc;
                                                      margin: 0;
                                                      margin-bottom: 0;
                                                      margin-left: 0;
                                                      margin-right: 0;
                                                      margin-top: 0;
                                                      opacity: 1;
                                                      orphans: 0;
                                                      outline: 0;
                                                      outline-color: invert;
                                                      outline-style: none;
                                                      outline-width: medium;
                                                      overflow: visible;
                                                      overflow-x: visible;
                                                      overflow-y: visible;
                                                      padding: 0;
                                                      padding-bottom: 0;
                                                      padding-left: 0;
                                                      padding-right: 0;
                                                      padding-top: 0;
                                                      page-break-after: auto;
                                                      page-break-before: auto;
                                                      page-break-inside: auto;
                                                      -webkit-perspective: none;
                                                              perspective: none;
                                                      -webkit-perspective-origin: 50% 50%;
                                                              perspective-origin: 50% 50%;
                                                      position: static;
                                                      quotes: '\201C' '\201D' '\2018' '\2019';
                                                      right: auto;
                                                      -moz-tab-size: 8;
                                                        -o-tab-size: 8;
                                                           tab-size: 8;
                                                      table-layout: auto;
                                                      text-align: inherit;
                                                      -moz-text-align-last: auto;
                                                           text-align-last: auto;
                                                      text-decoration: none;
                                                      -webkit-text-decoration-color: inherit;
                                                              text-decoration-color: inherit;
                                                      -webkit-text-decoration-line: none;
                                                              text-decoration-line: none;
                                                      -webkit-text-decoration-style: solid;
                                                              text-decoration-style: solid;
                                                      text-indent: 0;
                                                      text-shadow: none;
                                                      text-transform: none;
                                                      top: auto;
                                                      -webkit-transform: none;
                                                              transform: none;
                                                      -webkit-transform-style: flat;
                                                              transform-style: flat;
                                                      transition: none;
                                                      transition-delay: 0s;
                                                      transition-duration: 0s;
                                                      transition-property: none;
                                                      transition-timing-function: ease;
                                                      unicode-bidi: normal;
                                                      vertical-align: baseline;
                                                      visibility: visible;
                                                      white-space: normal;
                                                      widows: 0;
                                                      width: auto;
                                                      word-spacing: normal;
                                                      z-index: auto;
                                                    }
                                                    .eapps-social-icons {
                                                      display: block;
                                                      position: relative;
                                                    }
                                                    .eapps-social-icons-item {
                                                      display: inline-block;
                                                      vertical-align: middle;
                                                      position: relative;
                                                      cursor: pointer;
                                                      -webkit-backface-visibility: hidden;
                                                              backface-visibility: hidden;
                                                      transition: all 0.1s ease;
                                                    }
                                                    .eapps-social-icons-item::before,
                                                    .eapps-social-icons-item::after {
                                                      content: '';
                                                      display: block;
                                                      position: absolute;
                                                      width: 100%;
                                                      height: 100%;
                                                    }
                                                    .eapps-social-icons-item::after {
                                                      opacity: 0;
                                                      visibility: hidden;
                                                      transition: all 0.1s ease;
                                                    }
                                                    .eapps-social-icons-item-icon {
                                                      display: block;
                                                      position: absolute;
                                                      top: 50%;
                                                      left: 50%;
                                                      z-index: 1;
                                                      -webkit-backface-visibility: hidden;
                                                              backface-visibility: hidden;
                                                      transition: all 0.1s ease;
                                                    }
                                                    .eapps-social-icons-item:hover::before {
                                                      opacity: 0;
                                                      visibility: hidden;
                                                      transition: all 0s ease 0.1s;
                                                    }
                                                    .eapps-social-icons-item:hover::after {
                                                      opacity: 1;
                                                      visibility: visible;
                                                    }
                                                    .eapps-social-icons.eapps-social-icons-position-left {
                                                      text-align: left;
                                                    }
                                                    .eapps-social-icons.eapps-social-icons-position-center {
                                                      text-align: center;
                                                    }
                                                    .eapps-social-icons.eapps-social-icons-position-right {
                                                      text-align: right;
                                                    }
                                                    .eapps-social-icons-location-inline.eapps-social-icons-position-left {
                                                      text-align: left;
                                                    }
                                                    .eapps-social-icons-location-inline.eapps-social-icons-position-center {
                                                      text-align: center;
                                                    }
                                                    .eapps-social-icons-location-inline.eapps-social-icons-position-right {
                                                      text-align: right;
                                                    }
                                                    .eapps-social-icons-location-floating {
                                                      position: fixed !important;
                                                      z-index: 1000000 !important;
                                                    }
                                                    .eapps-social-icons-location-floating.eapps-social-icons-position-left {
                                                      left: 0;
                                                      top: 50%;
                                                      text-align: left;
                                                      -webkit-transform: translateY(-50%);
                                                              transform: translateY(-50%);
                                                    }
                                                    .eapps-social-icons-location-floating.eapps-social-icons-position-center {
                                                      bottom: 0;
                                                      left: 0;
                                                      right: 0;
                                                      text-align: center;
                                                    }
                                                    .eapps-social-icons-location-floating.eapps-social-icons-position-right {
                                                      right: 0;
                                                      text-align: right;
                                                      -webkit-transform: translateY(-50%);
                                                              transform: translateY(-50%);
                                                      top: 50%;
                                                    }
                                                    .eapps-social-icons-border-radius-circle .eapps-social-icons-item,
                                                    .eapps-social-icons-border-radius-circle .eapps-social-icons-item::before,
                                                    .eapps-social-icons-border-radius-circle .eapps-social-icons-item::after {
                                                      border-radius: 50%;
                                                    }
                                                    .eapps-social-icons-border-radius-square .eapps-social-icons-item,
                                                    .eapps-social-icons-border-radius-square .eapps-social-icons-item::before,
                                                    .eapps-social-icons-border-radius-square .eapps-social-icons-item::after {
                                                      border-radius: 0;
                                                    }
                                                    .eapps-social-icons-border-radius-rounded .eapps-social-icons-item,
                                                    .eapps-social-icons-border-radius-rounded .eapps-social-icons-item::before,
                                                    .eapps-social-icons-border-radius-rounded .eapps-social-icons-item::after {
                                                      border-radius: 5px;
                                                    }
                                                    .eapps-social-icons-size-24 .eapps-social-icons-item {
                                                      width: 24px;
                                                      height: 24px;
                                                      margin: 3px;
                                                      border-width: 1px;
                                                    }
                                                    .eapps-social-icons-size-24 .eapps-social-icons-item-icon {
                                                      width: 12px;
                                                      height: 12px;
                                                      margin: -6px 0 0 -6px;
                                                    }
                                                    .eapps-social-icons-size-24 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                                                      width: 24px;
                                                      height: 24px;
                                                      margin: -12px 0 0 -12px;
                                                    }
                                                    .eapps-social-icons-size-32 .eapps-social-icons-item {
                                                      width: 32px;
                                                      height: 32px;
                                                      margin: 4px;
                                                      border-width: 1px;
                                                    }
                                                    .eapps-social-icons-size-32 .eapps-social-icons-item-icon {
                                                      width: 16px;
                                                      height: 16px;
                                                      margin: -8px 0 0 -8px;
                                                    }
                                                    .eapps-social-icons-size-32 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                                                      width: 32px;
                                                      height: 32px;
                                                      margin: -16px 0 0 -16px;
                                                    }
                                                    .eapps-social-icons-size-40 .eapps-social-icons-item {
                                                      width: 40px;
                                                      height: 40px;
                                                      margin: 5px;
                                                      border-width: 2px;
                                                    }
                                                    .eapps-social-icons-size-40 .eapps-social-icons-item-icon {
                                                      width: 20px;
                                                      height: 20px;
                                                      margin: -10px 0 0 -10px;
                                                    }
                                                    .eapps-social-icons-size-40 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                                                      width: 40px;
                                                      height: 40px;
                                                      margin: -20px 0 0 -20px;
                                                    }
                                                    .eapps-social-icons-size-48 .eapps-social-icons-item {
                                                      width: 48px;
                                                      height: 48px;
                                                      margin: 6px;
                                                      border-width: 2px;
                                                    }
                                                    .eapps-social-icons-size-48 .eapps-social-icons-item-icon {
                                                      width: 24px;
                                                      height: 24px;
                                                      margin: -12px 0 0 -12px;
                                                    }
                                                    .eapps-social-icons-size-48 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                                                      width: 48px;
                                                      height: 48px;
                                                      margin: -24px 0 0 -24px;
                                                    }
                                                    .eapps-social-icons-size-60 .eapps-social-icons-item {
                                                      width: 60px;
                                                      height: 60px;
                                                      margin: 7px;
                                                      border-width: 2px;
                                                    }
                                                    .eapps-social-icons-size-60 .eapps-social-icons-item-icon {
                                                      width: 28px;
                                                      height: 28px;
                                                      margin: -14px 0 0 -14px;
                                                    }
                                                    .eapps-social-icons-size-60 .eapps-social-icons-item-custom .eapps-social-icons-item-icon {
                                                      width: 60px;
                                                      height: 60px;
                                                      margin: -30px 0 0 -30px;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-500px::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-500px::after {
                                                      background-color: #0099e5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover {
                                                      border-color: #0099e5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * {
                                                      fill: #0099e5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-500px .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-500px:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-badoo::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-badoo::after {
                                                      background-color: #ff6719;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover {
                                                      border-color: #ff6719;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff6719;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-badoo .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-badoo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-behance::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-behance::after {
                                                      background-color: #1776f6;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover {
                                                      border-color: #1776f6;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * {
                                                      fill: #1776f6;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-behance .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-behance:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-blogger::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-blogger::after {
                                                      background-color: #ff8b13;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover {
                                                      border-color: #ff8b13;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff8b13;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-blogger .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-blogger:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-delicious::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-delicious::after {
                                                      background-color: #39f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover {
                                                      border-color: #39f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * {
                                                      fill: #39f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-delicious .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-delicious:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-deviantart::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-deviantart::after {
                                                      background-color: #05cc47;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover {
                                                      border-color: #05cc47;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * {
                                                      fill: #05cc47;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-deviantart .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-deviantart:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-digg::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-digg::after {
                                                      background-color: ;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-digg .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-digg:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-disqus::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-disqus::after {
                                                      background-color: #3ca2ef;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover {
                                                      border-color: #3ca2ef;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * {
                                                      fill: #3ca2ef;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-disqus .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-disqus:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-dribbble::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-dribbble::after {
                                                      background-color: #fa488c;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover {
                                                      border-color: #fa488c;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * {
                                                      fill: #fa488c;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-dribbble .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-dribbble:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-envato::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-envato::after {
                                                      background-color: #8dcf3a;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover {
                                                      border-color: #8dcf3a;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * {
                                                      fill: #8dcf3a;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-envato .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-envato:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-evernote::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-evernote::after {
                                                      background-color: #2dbe60;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover {
                                                      border-color: #2dbe60;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * {
                                                      fill: #2dbe60;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-evernote .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-evernote:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-facebook::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-facebook::after {
                                                      background-color: #3e68c0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover {
                                                      border-color: #3e68c0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * {
                                                      fill: #3e68c0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-facebook .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-facebook:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-fb-messenger::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-fb-messenger::after {
                                                      background-color: #007fff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover {
                                                      border-color: #007fff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * {
                                                      fill: #007fff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-fb-messenger .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-fb-messenger:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-flickr::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-flickr::after {
                                                      background-color: #ff0084;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover {
                                                      border-color: #ff0084;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff0084;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flickr .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flickr:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-flipboard::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-flipboard::after {
                                                      background-color: #f43d3d;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover {
                                                      border-color: #f43d3d;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * {
                                                      fill: #f43d3d;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-flipboard .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-flipboard:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-forrst::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-forrst::after {
                                                      background-color: #55c462;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover {
                                                      border-color: #55c462;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * {
                                                      fill: #55c462;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-forrst .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-forrst:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-foursquare::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-foursquare::after {
                                                      background-color: #ff3b6f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover {
                                                      border-color: #ff3b6f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff3b6f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-foursquare .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-foursquare:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-github::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-github::after {
                                                      background-color: ;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-github .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-github:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-instagram::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-instagram::after {
                                                      background-color: ;
                                                      background-image: radial-gradient(circle farthest-corner at 35% 90%, #fec564, transparent 50%), radial-gradient(circle farthest-corner at 0 140%, #fec564, transparent 50%), radial-gradient(ellipse farthest-corner at 0 -25%, #5258cf, transparent 50%), radial-gradient(ellipse farthest-corner at 20% -50%, #5258cf, transparent 50%), radial-gradient(ellipse farthest-corner at 100% 0, #893dc2, transparent 50%), radial-gradient(ellipse farthest-corner at 60% -20%, #893dc2, transparent 50%), radial-gradient(ellipse farthest-corner at 100% 100%, #d9317a, transparent), linear-gradient(#6559ca, #bc318f 30%, #e33f5f 50%, #f77638 70%, #fec66d 100%);
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-instagram .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-instagram:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-lastfm::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-lastfm::after {
                                                      background-color: #ea3939;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover {
                                                      border-color: #ea3939;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * {
                                                      fill: #ea3939;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lastfm .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lastfm:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-linkedin::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-linkedin::after {
                                                      background-color: #15ace5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover {
                                                      border-color: #15ace5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * {
                                                      fill: #15ace5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-linkedin .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-linkedin:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-livejournal::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-livejournal::after {
                                                      background-color: #2cbae5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover {
                                                      border-color: #2cbae5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * {
                                                      fill: #2cbae5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-livejournal .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-livejournal:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-email::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-email::after {
                                                      background-color: #f4cd0b;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover {
                                                      border-color: #f4cd0b;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * {
                                                      fill: #f4cd0b;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-email .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-email:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-myspace::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-myspace::after {
                                                      background-color: ;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-myspace .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-myspace:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-odnoklassniki::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-odnoklassniki::after {
                                                      background-color: #ff8321;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover {
                                                      border-color: #ff8321;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff8321;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-odnoklassniki .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-odnoklassniki:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-periscope::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-periscope::after {
                                                      background-color: #35b3db;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover {
                                                      border-color: #35b3db;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * {
                                                      fill: #35b3db;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-periscope .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-periscope:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-pinterest::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-pinterest::after {
                                                      background-color: #ea3145;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover {
                                                      border-color: #ea3145;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * {
                                                      fill: #ea3145;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-pinterest .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-pinterest:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-print::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-print::after {
                                                      background-color: ;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-print .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-print:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-reddit::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-reddit::after {
                                                      background-color: #ff5c1f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover {
                                                      border-color: #ff5c1f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff5c1f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-reddit .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-reddit:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-rss::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-rss::after {
                                                      background-color: #fb7629;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover {
                                                      border-color: #fb7629;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * {
                                                      fill: #fb7629;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-rss .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-rss:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-sina-weibo::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-sina-weibo::after {
                                                      background-color: #ff3f3f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover {
                                                      border-color: #ff3f3f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff3f3f;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-sina-weibo .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-sina-weibo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-skype::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-skype::after {
                                                      background-color: #06bcff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover {
                                                      border-color: #06bcff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * {
                                                      fill: #06bcff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-skype .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-skype:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-slack::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-slack::after {
                                                      background-color: ;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-slack .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-slack:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-snapchat::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-snapchat::after {
                                                      background-color: #fada06;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover {
                                                      border-color: #fada06;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * {
                                                      fill: #fada06;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-snapchat .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-snapchat:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-soundcloud::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-soundcloud::after {
                                                      background-color: #f80;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover {
                                                      border-color: #f80;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * {
                                                      fill: #f80;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-soundcloud .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-soundcloud:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-spotify::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-spotify::after {
                                                      background-color: #28c858;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover {
                                                      border-color: #28c858;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * {
                                                      fill: #28c858;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-spotify .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-spotify:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-stackoverflow::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-stackoverflow::after {
                                                      background-color: #ff780d;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover {
                                                      border-color: #ff780d;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff780d;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stackoverflow .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stackoverflow:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-stumbleupon::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-stumbleupon::after {
                                                      background-color: #eb4924;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover {
                                                      border-color: #eb4924;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * {
                                                      fill: #eb4924;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-stumbleupon .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-stumbleupon:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-telegram::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-telegram::after {
                                                      background-color: #2ca5e0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover {
                                                      border-color: #2ca5e0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * {
                                                      fill: #2ca5e0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-telegram .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-telegram:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-tiktok::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-tiktok::after {
                                                      background-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tiktok .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tiktok:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-tumblr::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-tumblr::after {
                                                      background-color: #35465c;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover {
                                                      border-color: #35465c;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * {
                                                      fill: #35465c;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-tumblr .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-tumblr:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-twitter::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-twitter::after {
                                                      background-color: #23abff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover {
                                                      border-color: #23abff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * {
                                                      fill: #23abff;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-twitter .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-twitter:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-viadeo::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-viadeo::after {
                                                      background-color: #ff7452;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover {
                                                      border-color: #ff7452;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * {
                                                      fill: #ff7452;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viadeo .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viadeo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-viber::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-viber::after {
                                                      background-color: #9d62cc;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover {
                                                      border-color: #9d62cc;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * {
                                                      fill: #9d62cc;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-viber .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-viber:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-vimeo::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-vimeo::after {
                                                      background-color: #1ab7ea;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover {
                                                      border-color: #1ab7ea;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * {
                                                      fill: #1ab7ea;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vimeo .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vimeo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-vine::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-vine::after {
                                                      background-color: #00b488;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover {
                                                      border-color: #00b488;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * {
                                                      fill: #00b488;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vine .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vine:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-vk::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-vk::after {
                                                      background-color: #3673be;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover {
                                                      border-color: #3673be;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * {
                                                      fill: #3673be;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-vk .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-vk:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-whatsapp::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-whatsapp::after {
                                                      background-color: #13d25a;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover {
                                                      border-color: #13d25a;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * {
                                                      fill: #13d25a;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-whatsapp .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-whatsapp:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-xing::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-xing::after {
                                                      background-color: #20a5a5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover {
                                                      border-color: #20a5a5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * {
                                                      fill: #20a5a5;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-xing .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-xing:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-youtube::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-youtube::after {
                                                      background-color: #ee3130;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover {
                                                      border-color: #ee3130;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * {
                                                      fill: #ee3130;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-youtube .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-youtube:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-line::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-line::after {
                                                      background-color: #00c300;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover {
                                                      border-color: #00c300;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * {
                                                      fill: #00c300;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-line .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-line:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-lineAt::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-lineAt::after {
                                                      background-color: #00c300;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover {
                                                      border-color: #00c300;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * {
                                                      fill: #00c300;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-lineAt .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-lineAt:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-phone::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-phone::after {
                                                      background-color: #33cc49;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover {
                                                      border-color: #33cc49;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * {
                                                      fill: #33cc49;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-phone .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-phone:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-amazon::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-amazon::after {
                                                      background-color: #f90;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover {
                                                      border-color: #f90;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * {
                                                      fill: #f90;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-amazon .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-amazon:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-itunes::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-itunes::after {
                                                      background-color: ;
                                                      background-image: linear-gradient(142deg, #ff5e50, #fe5c6c 25%, #e3658a 38%, #b87eb0 50%, #916cff 63%, rgba(112,188,251,0.92) 76%, #21c7fe);
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-itunes .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-itunes:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-apple::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-apple::after {
                                                      background-color: ;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover {
                                                      border-color: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * {
                                                      fill: #000;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-apple .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-apple:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-native .eapps-social-icons-item-weibo::before,
                                                    .eapps-social-icons-bg-color-on-hover-native .eapps-social-icons-item-weibo::after {
                                                      background-color: #f44336;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover {
                                                      border-color: #f44336;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * {
                                                      fill: #f44336;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill: #f00044;
                                                      fill-opacity: 1;
                                                    }
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-native .eapps-social-icons-item-weibo .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-native .eapps-social-icons-item-weibo:hover .eapps-social-icons-item-icon * .tiktok-blue {
                                                      fill: #08fff9;
                                                      stroke-width: 0;
                                                    }
                                                    .eapps-social-icons-bg-color-white .eapps-social-icons-item::before,
                                                    .eapps-social-icons-bg-color-on-hover-white .eapps-social-icons-item::after {
                                                      background: #fff;
                                                    }
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover {
                                                      border-color: #fff;
                                                    }
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * {
                                                      fill: #fff;
                                                    }
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill-opacity: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-white .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-white .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke: #fff;
                                                      stroke-width: 1;
                                                    }
                                                    .eapps-social-icons-bg-color-black .eapps-social-icons-item::before,
                                                    .eapps-social-icons-bg-color-on-hover-black .eapps-social-icons-item::after {
                                                      background: #222;
                                                    }
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover {
                                                      border-color: #222;
                                                    }
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon,
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon *,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * {
                                                      fill: #222;
                                                    }
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-red,
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-red,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-red {
                                                      fill-opacity: 0;
                                                    }
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-blue,
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-blue,
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon .tiktok-black,
                                                    .eapps-social-icons-icon-color-black .eapps-social-icons-item .eapps-social-icons-item-icon * .tiktok-black,
                                                    .eapps-social-icons-icon-color-on-hover-black .eapps-social-icons-item:hover .eapps-social-icons-item-icon * .tiktok-black {
                                                      stroke: #222;
                                                      stroke-width: 1;
                                                    }
                                                    .eapps-social-icons-bg-color-white .eapps-social-icons-item-custom::before,
                                                    .eapps-social-icons-bg-color-on-hover-white .eapps-social-icons-item-custom::after {
                                                      background: inherit;
                                                    }
                                                    .eapps-social-icons-bg-color-black .eapps-social-icons-item-custom::before,
                                                    .eapps-social-icons-bg-color-on-hover-black .eapps-social-icons-item-custom::after {
                                                      background: inherit;
                                                    }
                                                    .eapps-social-icons-style-default .eapps-social-icons-item,
                                                    .eapps-social-icons-style-default .eapps-social-icons-item:hover {
                                                      box-shadow: none;
                                                      border-color: transparent;
                                                    }
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-24 .eapps-social-icons-item,
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-32 .eapps-social-icons-item {
                                                      border-color: transparent;
                                                      box-shadow: 0 0 2px rgba(0,0,0,0.14), 0 1px 4px rgba(0,0,0,0.28);
                                                    }
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-24 .eapps-social-icons-item:hover,
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-32 .eapps-social-icons-item:hover {
                                                      border-color: transparent;
                                                      box-shadow: 0 0 3px rgba(0,0,0,0.16), 0 2px 6px rgba(0,0,0,0.32);
                                                    }
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-40 .eapps-social-icons-item,
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-48 .eapps-social-icons-item,
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-60 .eapps-social-icons-item {
                                                      border-color: transparent;
                                                      box-shadow: 0 0 4px rgba(0,0,0,0.14), 0 2px 6px rgba(0,0,0,0.28);
                                                    }
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-40 .eapps-social-icons-item:hover,
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-48 .eapps-social-icons-item:hover,
                                                    .eapps-social-icons-style-material.eapps-social-icons-size-60 .eapps-social-icons-item:hover {
                                                      border-color: transparent;
                                                      box-shadow: 0 0 6px rgba(0,0,0,0.16), 0 4px 8px rgba(0,0,0,0.32);
                                                    }
                                                    .eapps-social-icons-style-material .eapps-social-icons-item-custom,
                                                    .eapps-social-icons-style-material .eapps-social-icons-item-custom:hover {
                                                      box-shadow: none !important;
                                                    }
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item:hover {
                                                      border-color: transparent;
                                                    }
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item::before,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item:hover::before,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item::after,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item:hover::after {
                                                      box-shadow: inset 0 -2px rgba(0,0,0,0.2);
                                                    }
                                                    .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item::before,
                                                    .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item:hover::before,
                                                    .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item::after,
                                                    .eapps-social-icons-style-flat.eapps-social-icons-size-60 .eapps-social-icons-item:hover::after {
                                                      box-shadow: inset 0 -3px rgba(0,0,0,0.2);
                                                    }
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item-custom::before,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item-custom:hover::before,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item-custom::after,
                                                    .eapps-social-icons-style-flat .eapps-social-icons-item-custom:hover::after {
                                                      box-shadow: none !important;
                                                    }
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item,
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item:hover {
                                                      border-style: solid;
                                                      box-shadow: none;
                                                    }
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item::before,
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item:hover::before,
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item::after,
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item:hover::after {
                                                      background: none;
                                                    }
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item-custom,
                                                    .eapps-social-icons-style-bordered .eapps-social-icons-item-custom:hover {
                                                      border-style: inherit !important;
                                                    }
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item:hover {
                                                      box-shadow: 0 2px 4px rgba(0,0,0,0.15);
                                                    }
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item::before,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item:hover::before,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item::after,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item:hover::after {
                                                      box-shadow: inset 0 0 1px rgba(0,0,0,0.6), inset 0 1px 0 1px rgba(255,255,255,0.3);
                                                    }
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item:active {
                                                      box-shadow: none;
                                                    }
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item-custom,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item-custom:hover {
                                                      box-shadow: none !important;
                                                    }
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item-custom::before,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item-custom:hover::before,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item-custom::after,
                                                    .eapps-social-icons-style-classic .eapps-social-icons-item-custom:hover::after {
                                                      box-shadow: none !important;
                                                    }
                                                    .eapps-social-icons-style-symbol {
                                                      margin: 0;
                                                    }
                                                    .eapps-social-icons-style-symbol .eapps-social-icons-item,
                                                    .eapps-social-icons-style-symbol .eapps-social-icons-item:hover {
                                                      box-shadow: none;
                                                      border: none;
                                                      margin: 0;
                                                    }
                                                    .eapps-social-icons-style-symbol .eapps-social-icons-item::before,
                                                    .eapps-social-icons-style-symbol .eapps-social-icons-item:hover::before,
                                                    .eapps-social-icons-style-symbol .eapps-social-icons-item::after,
                                                    .eapps-social-icons-style-symbol .eapps-social-icons-item:hover::after {
                                                      background: none;
                                                    }
                                                    .eapps-social-icons-animation-rotate .eapps-social-icons-item:hover .eapps-social-icons-item-icon {
                                                      -webkit-transform: scale(1.1) rotate(10deg);
                                                              transform: scale(1.1) rotate(10deg);
                                                      transition: all 0.3s cubic-bezier(0.2, 0.26, 0, 1.78);
                                                    }
                                                    .eapps-social-icons-animation-fly .eapps-social-icons-item {
                                                      transition: all 0.3s cubic-bezier(0.2, 0.26, 0, 1.78);
                                                    }
                                                    .eapps-social-icons-animation-fly.eapps-social-icons-size-24 .eapps-social-icons-item:hover {
                                                      -webkit-transform: translateY(-3px);
                                                              transform: translateY(-3px);
                                                    }
                                                    .eapps-social-icons-animation-fly.eapps-social-icons-size-32 .eapps-social-icons-item:hover {
                                                      -webkit-transform: translateY(-4px);
                                                              transform: translateY(-4px);
                                                    }
                                                    .eapps-social-icons-animation-fly.eapps-social-icons-size-40 .eapps-social-icons-item:hover {
                                                      -webkit-transform: translateY(-5px);
                                                              transform: translateY(-5px);
                                                    }
                                                    .eapps-social-icons-animation-fly.eapps-social-icons-size-48 .eapps-social-icons-item:hover {
                                                      -webkit-transform: translateY(-6px);
                                                              transform: translateY(-6px);
                                                    }
                                                    .eapps-social-icons-animation-fly.eapps-social-icons-size-60 .eapps-social-icons-item:hover {
                                                      -webkit-transform: translateY(-7px);
                                                              transform: translateY(-7px);
                                                    }
                                                    .eapps-social-icons-animation-bounce .eapps-social-icons-item:hover {
                                                      -webkit-animation: eapps-animation-bounce 0.3s forwards;
                                                              animation: eapps-animation-bounce 0.3s forwards;
                                                    }
                                                    .eapps-social-icons-animation-zoom .eapps-social-icons-item::before {
                                                      transition: none;
                                                    }
                                                    .eapps-social-icons-animation-zoom .eapps-social-icons-item::after {
                                                      -webkit-transform: scale3d(0, 0, 0);
                                                              transform: scale3d(0, 0, 0);
                                                      transition: all 0.3s ease;
                                                    }
                                                    .eapps-social-icons-animation-zoom .eapps-social-icons-item:hover {
                                                      -webkit-transform: scale3d(1.1, 1.1, 1.1);
                                                              transform: scale3d(1.1, 1.1, 1.1);
                                                      transition: all 0.3s ease;
                                                    }
                                                    .eapps-social-icons-animation-zoom .eapps-social-icons-item:hover::before {
                                                      transition: all 0.3s ease 0.2s;
                                                      opacity: 0;
                                                    }
                                                    .eapps-social-icons-animation-zoom .eapps-social-icons-item:hover::after {
                                                      -webkit-transform: scale3d(1, 1, 1);
                                                              transform: scale3d(1, 1, 1);
                                                    }
                                                    .eapps-social-icons-animation-slide .eapps-social-icons-item {
                                                      overflow: hidden;
                                                    }
                                                    .eapps-social-icons-animation-slide .eapps-social-icons-item:hover .eapps-social-icons-item-icon {
                                                      -webkit-animation: eapps-animation-slide 0.3s forwards cubic-bezier(0.54, 0.74, 0.25, 1.3);
                                                              animation: eapps-animation-slide 0.3s forwards cubic-bezier(0.54, 0.74, 0.25, 1.3);
                                                    }
                                                    @-webkit-keyframes eapps-animation-bounce {
                                                      40% {
                                                        -webkit-transform: scale3d(0.9, 0.9, 1);
                                                                transform: scale3d(0.9, 0.9, 1);
                                                      }
                                                      70% {
                                                        -webkit-transform: scale3d(1.05, 1.05, 1);
                                                                transform: scale3d(1.05, 1.05, 1);
                                                      }
                                                      100% {
                                                        -webkit-transform: scale3d(1, 1, 1);
                                                                transform: scale3d(1, 1, 1);
                                                      }
                                                    }
                                                    @keyframes eapps-animation-bounce {
                                                      40% {
                                                        -webkit-transform: scale3d(0.9, 0.9, 1);
                                                                transform: scale3d(0.9, 0.9, 1);
                                                      }
                                                      70% {
                                                        -webkit-transform: scale3d(1.05, 1.05, 1);
                                                                transform: scale3d(1.05, 1.05, 1);
                                                      }
                                                      100% {
                                                        -webkit-transform: scale3d(1, 1, 1);
                                                                transform: scale3d(1, 1, 1);
                                                      }
                                                    }
                                                    @-webkit-keyframes eapps-animation-slide {
                                                      49% {
                                                        -webkit-transform: translateY(100%);
                                                                transform: translateY(100%);
                                                      }
                                                      50% {
                                                        opacity: 0;
                                                        -webkit-transform: translateY(-100%);
                                                                transform: translateY(-100%);
                                                      }
                                                      51% {
                                                        opacity: 1;
                                                      }
                                                    }
                                                    @keyframes eapps-animation-slide {
                                                      49% {
                                                        -webkit-transform: translateY(100%);
                                                                transform: translateY(100%);
                                                      }
                                                      50% {
                                                        opacity: 0;
                                                        -webkit-transform: translateY(-100%);
                                                                transform: translateY(-100%);
                                                      }
                                                      51% {
                                                        opacity: 1;
                                                      }
                                                    }
                                                    </style><style>.eapps-preview {
                                                      overflow: hidden;
                                                      display: -webkit-flex;
                                                      display: flex;
                                                      -webkit-align-items: center;
                                                              align-items: center;
                                                      -webkit-justify-content: center;
                                                              justify-content: center;
                                                      margin: 0 auto;
                                                      width: 100%;
                                                      min-width: 150px;
                                                      min-height: 100%;
                                                      transition: 0.2s;
                                                    }
                                                    .eapps-preview-toolbar {
                                                      position: fixed;
                                                      top: 80px;
                                                      right: 0;
                                                      z-index: 10;
                                                    }
                                                    @media only screen and (max-width: 480px) {
                                                      .eapps-preview-toolbar {
                                                        display: none;
                                                      }
                                                    }
                                                    .eapps-preview-toolbar-item {
                                                      position: relative;
                                                    }
                                                    .eapps-preview-toolbar-item-trigger {
                                                      box-sizing: border-box;
                                                      padding: 3px 6px;
                                                      background: #38393a;
                                                      cursor: pointer;
                                                    }
                                                    .eapps-preview-toolbar-item-trigger:first-child {
                                                      padding-top: 6px;
                                                    }
                                                    .eapps-preview-toolbar-item-trigger:last-child {
                                                      padding-bottom: 6px;
                                                    }
                                                    .eapps-preview-toolbar-item-trigger:hover .eapps-preview-toolbar-item-icon svg {
                                                      fill: #fff;
                                                    }
                                                    .eapps-preview-toolbar-item-icon {
                                                      display: -webkit-flex;
                                                      display: flex;
                                                      -webkit-align-items: center;
                                                              align-items: center;
                                                      -webkit-justify-content: center;
                                                              justify-content: center;
                                                      width: 26px;
                                                      height: 26px;
                                                    }
                                                    .eapps-preview-toolbar-item-active .eapps-preview-toolbar-item-icon {
                                                      background: #2c2c2d;
                                                    }
                                                    .eapps-preview-toolbar-item-icon svg {
                                                      width: 16px;
                                                      height: 16px;
                                                      fill: #66686a;
                                                      transition: 0.1s;
                                                    }
                                                    .eapps-preview-toolbar-item-active .eapps-preview-toolbar-item-icon svg {
                                                      fill: #fff;
                                                    }
                                                    .eapps-preview-toolbar-item-values {
                                                      visibility: hidden;
                                                      display: -webkit-flex;
                                                      display: flex;
                                                      -webkit-align-items: center;
                                                              align-items: center;
                                                      -webkit-justify-content: center;
                                                              justify-content: center;
                                                      position: absolute;
                                                      top: 0px;
                                                      right: 38px;
                                                      padding: 0 2px;
                                                      border-radius: 2px;
                                                      transition: 0.2s;
                                                      opacity: 0;
                                                      background: #38393a;
                                                    }
                                                    .eapps-preview-toolbar-item-active .eapps-preview-toolbar-item-values {
                                                      visibility: visible;
                                                      opacity: 1;
                                                      right: 42px;
                                                    }
                                                    .eapps-preview-toolbar-item-value {
                                                      display: -webkit-flex;
                                                      display: flex;
                                                      -webkit-align-items: center;
                                                              align-items: center;
                                                      -webkit-justify-content: center;
                                                              justify-content: center;
                                                      box-sizing: border-box;
                                                      padding: 4px 2px;
                                                      cursor: pointer;
                                                    }
                                                    .eapps-preview-toolbar-item-value-icon {
                                                      display: -webkit-flex;
                                                      display: flex;
                                                      -webkit-align-items: center;
                                                              align-items: center;
                                                      -webkit-justify-content: center;
                                                              justify-content: center;
                                                      width: 26px;
                                                      height: 26px;
                                                      border-radius: 2px;
                                                    }
                                                    html {
                                                      height: 100%;
                                                      overflow: auto;
                                                    }

                                                    </style></head>



                                                            <div class="eapps-social-icons eapps-widget
                                                        eapps-social-icons-location-inline
                                                        eapps-social-icons-position-center
                                                        eapps-social-icons-size-40
                                                        eapps-social-icons-style-material
                                                        eapps-social-icons-border-radius-circle
                                                        eapps-social-icons-icon-color-white
                                                        eapps-social-icons-bg-color-native
                                                        eapps-social-icons-icon-color-on-hover-native
                                                        eapps-social-icons-bg-color-on-hover-white
                                                        eapps-social-icons-animation-fly
                                                    " style="width: auto;"><a class="eapps-social-icons-item-instagram eapps-social-icons-item" href="https://www.instagram.com/moie._10/" target="_blank" rel="nofollow" title="Instagram">
                                                        <span eapps-link="svg"><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="24px" height="24px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" xml:space="preserve" class="eapps-social-icons-item-icon"> <g> <circle fill="%23222222" cx="18.05" cy="5.992" r="1.355"></circle> <path fill="%23222222" d="M12.021,5.806c-3.427,0-6.215,2.788-6.215,6.215s2.788,6.215,6.215,6.215s6.215-2.788,6.215-6.215 S15.448,5.806,12.021,5.806z M12.021,15.412c-1.87,0-3.391-1.521-3.391-3.391s1.521-3.391,3.391-3.391 c1.87,0,3.391,1.521,3.391,3.391S13.891,15.412,12.021,15.412z"></path> <path fill="%23222222" d="M23.369,4.574c-0.357-0.919-0.846-1.669-1.539-2.362c-0.693-0.693-1.443-1.182-2.362-1.539 c-0.905-0.352-1.836-0.533-3.018-0.587c-1.153-0.053-1.536-0.065-4.43-0.065c-2.895,0-3.277,0.012-4.43,0.065 C6.409,0.14,5.478,0.321,4.574,0.673C3.655,1.03,2.904,1.519,2.212,2.212C1.519,2.904,1.03,3.655,0.673,4.573 C0.321,5.478,0.14,6.409,0.086,7.591c-0.053,1.153-0.065,1.536-0.065,4.43s0.012,3.277,0.065,4.43 c0.054,1.182,0.235,2.113,0.587,3.018c0.357,0.919,0.846,1.669,1.539,2.362c0.693,0.693,1.443,1.182,2.362,1.539 c0.905,0.352,1.836,0.533,3.018,0.587c1.153,0.053,1.536,0.065,4.43,0.065c2.895,0,3.277-0.012,4.43-0.065 c1.182-0.054,2.113-0.235,3.018-0.587c0.919-0.357,1.669-0.846,2.362-1.539c0.693-0.693,1.182-1.443,1.539-2.362 c0.352-0.905,0.533-1.836,0.587-3.018c0.053-1.153,0.065-1.536,0.065-4.43s-0.012-3.277-0.065-4.43 C23.902,6.409,23.721,5.478,23.369,4.574z M21.135,16.322c-0.05,1.105-0.239,1.715-0.398,2.123 c-0.216,0.556-0.486,0.971-0.903,1.389c-0.417,0.417-0.833,0.687-1.389,0.904c-0.408,0.159-1.018,0.347-2.123,0.397 c-1.123,0.051-1.46,0.062-4.301,0.062c-2.841,0-3.178-0.011-4.301-0.062c-1.105-0.05-1.715-0.239-2.123-0.398 c-0.556-0.216-0.971-0.486-1.389-0.903c-0.417-0.417-0.687-0.833-0.904-1.389c-0.159-0.408-0.347-1.018-0.397-2.123 c-0.051-1.123-0.062-1.46-0.062-4.301s0.011-3.178,0.062-4.301c0.05-1.105,0.239-1.715,0.398-2.123 c0.216-0.556,0.486-0.971,0.903-1.389c0.417-0.417,0.833-0.687,1.389-0.904C6.005,3.146,6.615,2.957,7.72,2.907 c1.123-0.051,1.46-0.062,4.301-0.062c2.841,0,3.178,0.011,4.302,0.062c1.105,0.05,1.715,0.239,2.123,0.398 c0.556,0.216,0.971,0.486,1.389,0.903c0.417,0.417,0.687,0.833,0.904,1.389c0.159,0.408,0.347,1.018,0.397,2.123 c0.051,1.123,0.062,1.46,0.062,4.301S21.186,15.199,21.135,16.322z"></path> </g> </svg></span>
                                                    </a><a class="eapps-social-icons-item-github eapps-social-icons-item" href="https://github.com/moieis" target="_blank" rel="nofollow" title="GitHub">
                                                        <span eapps-link="svg"><svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="24px" height="24px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" xml:space="preserve" class="eapps-social-icons-item-icon"> <g> <path fill="%23222222" d="M22.389,6.269c-1.073-1.839-2.529-3.294-4.367-4.367c-1.839-1.073-3.846-1.609-6.023-1.609 S7.814,0.83,5.977,1.902C4.137,2.975,2.682,4.431,1.609,6.269c-1.073,1.839-1.609,3.846-1.609,6.023 c0,2.615,0.763,4.966,2.289,7.055c1.526,2.089,3.497,3.534,5.914,4.336c0.281,0.052,0.49,0.015,0.625-0.109 c0.135-0.125,0.203-0.281,0.203-0.469c0-0.031-0.003-0.312-0.008-0.844c-0.005-0.531-0.008-0.995-0.008-1.39l-0.359,0.062 c-0.229,0.042-0.518,0.06-0.867,0.055s-0.711-0.041-1.086-0.109c-0.375-0.067-0.724-0.224-1.047-0.468 c-0.323-0.245-0.552-0.565-0.687-0.961l-0.156-0.36c-0.104-0.239-0.268-0.505-0.492-0.797c-0.224-0.292-0.451-0.49-0.68-0.594 l-0.109-0.078c-0.073-0.052-0.141-0.115-0.203-0.188s-0.109-0.146-0.141-0.219c-0.031-0.073-0.005-0.133,0.078-0.18 c0.083-0.047,0.234-0.07,0.453-0.07l0.312,0.047c0.208,0.042,0.466,0.166,0.773,0.375c0.307,0.208,0.56,0.479,0.758,0.812 c0.24,0.427,0.528,0.753,0.867,0.977c0.338,0.224,0.68,0.336,1.023,0.336c0.344,0,0.641-0.026,0.891-0.078s0.484-0.13,0.703-0.234 c0.094-0.698,0.349-1.235,0.766-1.609c-0.594-0.062-1.127-0.156-1.602-0.281c-0.474-0.125-0.963-0.328-1.469-0.61 c-0.505-0.281-0.925-0.63-1.258-1.047c-0.333-0.417-0.607-0.964-0.82-1.641c-0.213-0.677-0.32-1.458-0.32-2.344 c0-1.261,0.412-2.333,1.234-3.219c-0.385-0.948-0.349-2.01,0.109-3.187c0.302-0.094,0.75-0.023,1.344,0.211S8.06,5.908,8.335,6.075 c0.276,0.166,0.497,0.307,0.664,0.422c0.969-0.271,1.969-0.406,3-0.406s2.031,0.135,3,0.406l0.594-0.375 c0.406-0.25,0.885-0.479,1.437-0.688c0.552-0.208,0.974-0.266,1.266-0.172c0.469,1.177,0.51,2.24,0.125,3.187 c0.823,0.885,1.235,1.958,1.235,3.219c0,0.885-0.107,1.669-0.32,2.351c-0.213,0.682-0.489,1.229-0.828,1.641 s-0.761,0.758-1.266,1.039s-0.995,0.484-1.469,0.609s-1.008,0.219-1.601,0.282c0.541,0.469,0.812,1.208,0.812,2.219v3.297 c0,0.187,0.065,0.344,0.195,0.469s0.336,0.161,0.617,0.109c2.417-0.802,4.388-2.247,5.914-4.336 c1.526-2.088,2.289-4.44,2.289-7.055C23.999,10.115,23.462,8.108,22.389,6.269z"></path> </g> </svg></span>
                                                    </a></div>'''), None, None, None, None]])
            put_html('<hr>')


def start():
    # importing the module
    with use_scope(name='logo', clear=True):
        put_grid([[None, None, None, None, put_html(
            '''<img src="https://cliply.co/wp-content/uploads/2019/07/371907120_YOUTUBE_ICON_400px.gif" jsaction="load:XAeZkd;" jsname="HiaYvf" class="n3VNCb KAlRDb" alt="YouTube Icon - Royalty-Free GIF - Animated Sticker - Free PNG - Animated  Icon" data-noaft="1" style="width: 100px; height: 100px; margin: 0px;">'''),
                   None, None, None]])

    with use_scope(name='start', clear=True):
        put_html('<hr>')
        put_grid([[None, None, None, None, None, put_button(label='Start MoiTube', onclick=tryy), None,
                   None, None, None]])
        put_html('<hr>')
        put_grid([[None, None, None, put_html('''<svg xmlns="http://www.w3.org/2000/svg" style="margin:auto;background:#ffffff;display:block;" width="150" height="20" preserveAspectRatio="xMidYMid">
                    <style type="text/css">
                      text {
                        text-anchor: middle; font-size: 18px; opacity: 0;
                      }
                    </style>
                    <g style="transform-origin:75px 10px;transform:scale(1)">
                    <g transform="translate(75,10)">
                      <g transform="translate(0,0)"><g class="path" style="transform: scale(0.91); transform-origin: -57.43px -1.2586px; animation: 100s linear -62.1176s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M5.27 0.20L5.27 0.20L5.27 0.20Q3.28 0.20 1.91-1.48L1.91-1.48L1.91-1.48Q0.54-3.15 0.54-5.58L0.54-5.58L0.54-5.58Q0.54-8.55 2.19-10.58L2.19-10.58L2.19-10.58Q3.83-12.62 6.23-12.62L6.23-12.62L6.23-12.62Q7.16-12.62 7.97-12.43L7.97-12.43L7.97-12.43Q8.77-12.24 9.11-12.04L9.11-12.04L9.43-11.84L8.21-9.34L8.21-9.34Q7.79-9.70 7.04-10.02L7.04-10.02L7.04-10.02Q6.28-10.33 5.67-10.33L5.67-10.33L5.67-10.33Q4.43-10.33 3.68-9.31L3.68-9.31L3.68-9.31Q2.93-8.28 2.93-6.38L2.93-6.38L2.93-6.38Q2.93-4.48 3.71-3.27L3.71-3.27L3.71-3.27Q4.48-2.05 5.81-2.05L5.81-2.05L5.81-2.05Q6.68-2.05 7.38-2.59L7.38-2.59L7.38-2.59Q8.08-3.13 8.37-4.03L8.37-4.03L9.86-3.17L9.86-3.17Q9.27-1.58 8.05-0.69L8.05-0.69L8.05-0.69Q6.82 0.20 5.27 0.20" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -49.13px 0.371399px; animation: 100s linear -58.2353s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M10.76-8.69L10.76-8.69L12.94-9.16L12.94-9.16Q13.10-7.78 13.16-6.53L13.16-6.53L13.16-6.53Q14.80-9.07 16.24-9.07L16.24-9.07L16.04-6.26L16.04-6.26Q14.99-6.26 14.39-6.08L14.39-6.08L14.39-6.08Q13.79-5.89 13.16-5.33L13.16-5.33L13.16-4.68L13.36-0.45L10.94 0L11.16-4.37L11.16-4.37Q11.09-6.79 10.76-8.69" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -42.32px 0.416399px; animation: 100s linear -54.3529s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M20.61-1.84L20.61-1.84L20.61-1.84Q21.13-1.84 21.71-2.11L21.71-2.11L21.71-2.11Q22.28-2.38 22.61-2.65L22.61-2.65L22.93-2.92L23.76-1.91L23.76-1.91Q23.58-1.60 23.20-1.21L23.20-1.21L23.20-1.21Q22.82-0.81 22.44-0.53L22.44-0.53L22.44-0.53Q22.05-0.25 21.41-0.03L21.41-0.03L21.41-0.03Q20.77 0.20 20.09 0.20L20.09 0.20L20.09 0.20Q18.63 0.20 17.71-0.91L17.71-0.91L17.71-0.91Q16.79-2.02 16.79-3.76L16.79-3.76L16.79-3.76Q16.79-5.96 18.07-7.61L18.07-7.61L18.07-7.61Q19.35-9.27 21.06-9.27L21.06-9.27L21.06-9.27Q22.37-9.27 23.10-8.53L23.10-8.53L23.10-8.53Q23.83-7.79 23.83-6.46L23.83-6.46L23.83-6.46Q23.83-5.67 23.56-4.66L23.56-4.66L23.20-4.28L18.70-3.87L18.70-3.87Q19.01-1.84 20.61-1.84zM20.61-7.42L20.61-7.42L20.61-7.42Q19.82-7.42 19.28-6.78L19.28-6.78L19.28-6.78Q18.74-6.14 18.65-5.15L18.65-5.15L21.71-5.53L21.71-5.53Q21.76-5.94 21.76-6.21L21.76-6.21L21.76-6.21Q21.76-7.42 20.61-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -34.1px 0.341399px; animation: 100s linear -50.4706s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M27.20 0L27.20 0Q26.14 0 25.46-0.68L25.46-0.68L25.46-0.68Q24.79-1.35 24.79-2.49L24.79-2.49L24.79-2.49Q24.79-3.64 25.83-4.47L25.83-4.47L25.83-4.47Q26.87-5.31 28.37-5.31L28.37-5.31L29.59-5.31L29.59-5.62L29.59-5.62Q29.59-6.50 29.23-6.82L29.23-6.82L29.23-6.82Q28.87-7.15 27.88-7.15L27.88-7.15L27.88-7.15Q27.47-7.15 26.90-6.98L26.90-6.98L26.90-6.98Q26.33-6.80 25.63-6.44L25.63-6.44L25.11-7.87L25.11-7.87Q25.88-8.41 26.99-8.84L26.99-8.84L26.99-8.84Q28.10-9.27 28.82-9.27L28.82-9.27L28.82-9.27Q31.64-9.27 31.64-6.53L31.64-6.53L31.64-3.01L31.64-3.01Q31.64-2.00 32.27-0.76L32.27-0.76L30.37 0.05L30.37 0.05Q29.92-0.81 29.70-1.49L29.70-1.49L29.70-1.49Q28.71 0 27.20 0L27.20 0zM27.95-1.84L27.95-1.84L27.95-1.84Q28.67-1.84 29.59-2.57L29.59-2.57L29.59-3.78L29.59-3.78Q28.64-4.00 28.04-4.00L28.04-4.00L28.04-4.00Q26.91-4.00 26.91-2.99L26.91-2.99L26.91-2.99Q26.91-2.47 27.20-2.15L27.20-2.15L27.20-2.15Q27.49-1.84 27.95-1.84" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -26.52px -0.618601px; animation: 100s linear -46.5882s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M33.50-8.71L34.54-8.71L34.54-10.67L36.97-11.14L36.74-8.71L38.92-8.71L38.72-7.24L36.67-7.24L36.58-3.47L36.58-3.47Q36.58-2.63 36.74-2.35L36.74-2.35L36.74-2.35Q36.90-2.07 37.33-2.07L37.33-2.07L37.33-2.07Q37.76-2.07 38.48-2.27L38.48-2.27L38.59-0.99L38.59-0.99Q37.40 0 36.50 0L36.50 0L36.50 0Q35.60 0 35.03-0.66L35.03-0.66L35.03-0.66Q34.45-1.31 34.45-2.38L34.45-2.38L34.56-4.39L34.54-7.24L33.30-7.24L33.50-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -19.46px 0.416399px; animation: 100s linear -42.7059s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M43.47-1.84L43.47-1.84L43.47-1.84Q43.99-1.84 44.57-2.11L44.57-2.11L44.57-2.11Q45.14-2.38 45.47-2.65L45.47-2.65L45.79-2.92L46.62-1.91L46.62-1.91Q46.44-1.60 46.06-1.21L46.06-1.21L46.06-1.21Q45.68-0.81 45.30-0.53L45.30-0.53L45.30-0.53Q44.91-0.25 44.27-0.03L44.27-0.03L44.27-0.03Q43.63 0.20 42.95 0.20L42.95 0.20L42.95 0.20Q41.49 0.20 40.57-0.91L40.57-0.91L40.57-0.91Q39.65-2.02 39.65-3.76L39.65-3.76L39.65-3.76Q39.65-5.96 40.93-7.61L40.93-7.61L40.93-7.61Q42.21-9.27 43.92-9.27L43.92-9.27L43.92-9.27Q45.23-9.27 45.96-8.53L45.96-8.53L45.96-8.53Q46.69-7.79 46.69-6.46L46.69-6.46L46.69-6.46Q46.69-5.67 46.42-4.66L46.42-4.66L46.06-4.28L41.56-3.87L41.56-3.87Q41.87-1.84 43.47-1.84zM43.47-7.42L43.47-7.42L43.47-7.42Q42.68-7.42 42.14-6.78L42.14-6.78L42.14-6.78Q41.60-6.14 41.51-5.15L41.51-5.15L44.57-5.53L44.57-5.53Q44.62-5.94 44.62-6.21L44.62-6.21L44.62-6.21Q44.62-7.42 43.47-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: -11.025px -1.9136px; animation: 100s linear -38.8235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M53.01-1.76L53.01-1.76L53.01-1.76Q51.61 0 50.58 0L50.58 0L50.58 0Q49.30 0 48.48-1.04L48.48-1.04L48.48-1.04Q47.66-2.09 47.66-3.73L47.66-3.73L47.66-3.73Q47.66-5.98 48.91-7.52L48.91-7.52L48.91-7.52Q50.17-9.07 51.98-9.07L51.98-9.07L52.99-8.93L52.99-9.27L52.78-13.48L55.24-13.93L55.01-4.68L55.01-3.10L55.01-3.10Q55.01-2.02 55.55-0.61L55.55-0.61L53.60 0.20L53.60 0.20Q53.08-0.88 53.01-1.76zM49.68-4.66L49.68-4.66L49.68-4.66Q49.68-3.51 50.10-2.86L50.10-2.86L50.10-2.86Q50.53-2.21 51.33-2.21L51.33-2.21L51.33-2.21Q52.13-2.21 52.99-2.86L52.99-2.86L52.99-6.75L52.99-6.75Q51.91-6.97 51.39-6.97L51.39-6.97L51.39-6.97Q50.58-6.97 50.13-6.39L50.13-6.39L50.13-6.39Q49.68-5.81 49.68-4.66" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 1.18px -2.0136px; animation: 100s linear -34.9412s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M64.84-9.09L64.84-9.09L64.84-9.09Q66.04-9.09 66.80-8.05L66.80-8.05L66.80-8.05Q67.55-7.00 67.55-5.36L67.55-5.36L67.55-5.36Q67.55-3.01 66.32-1.50L66.32-1.50L66.32-1.50Q65.09 0 63.13 0L63.13 0L63.13 0Q62.23 0 60.10-0.29L60.10-0.29L60.28-4.37L60.07-13.48L62.53-13.93L62.30-9.29L62.30-7.34L62.30-7.34Q62.50-7.63 62.78-7.96L62.78-7.96L62.78-7.96Q63.07-8.28 63.68-8.69L63.68-8.69L63.68-8.69Q64.30-9.09 64.84-9.09zM64.13-6.75L64.13-6.75L64.13-6.75Q63.31-6.75 62.30-6.25L62.30-6.25L62.30-4.68L62.41-2.03L62.41-2.03Q63.16-1.94 63.83-1.94L63.83-1.94L63.83-1.94Q65.56-1.94 65.56-4.35L65.56-4.35L65.56-4.35Q65.56-6.75 64.13-6.75" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 9.52999px 2.3514px; animation: 100s linear -31.0588s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M71.62 3.96L69.30 3.47L71.15-0.68L69.82-4.32L68.00-8.69L70.40-9.14L71.55-5.31L72.14-3.49L72.38-3.49L72.81-4.81L74.11-9.16L76.32-8.89L73.13-0.52L71.62 3.96" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 23.695px 0.416399px; animation: 100s linear -27.1765s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M85.41-4.55L85.41-4.55Q85.41-5.80 85.19-6.21L85.19-6.21L85.19-6.21Q84.98-6.62 84.19-6.62L84.19-6.62L84.19-6.62Q83.39-6.62 82.39-5.99L82.39-5.99L82.39-4.68L82.58-0.45L80.17 0L80.39-4.37L80.39-4.37Q80.32-6.79 79.99-8.69L79.99-8.69L82.17-9.16L82.17-9.16Q82.30-8.12 82.35-7.13L82.35-7.13L82.35-7.13Q82.62-7.49 82.96-7.84L82.96-7.84L82.96-7.84Q83.30-8.19 84.04-8.63L84.04-8.63L84.04-8.63Q84.78-9.07 85.54-9.07L85.54-9.07L85.54-9.07Q86.29-9.07 86.81-8.59L86.81-8.59L86.81-8.59Q87.34-8.10 87.48-7.25L87.48-7.25L87.48-7.25Q88.97-9.07 90.50-9.07L90.50-9.07L90.50-9.07Q91.46-9.07 92.02-8.43L92.02-8.43L92.02-8.43Q92.57-7.79 92.57-6.70L92.57-6.70L92.47-4.68L92.66-0.36L90.23 0.09L90.45-4.55L90.45-4.55Q90.45-5.80 90.23-6.21L90.23-6.21L90.23-6.21Q90.02-6.62 89.24-6.62L89.24-6.62L89.24-6.62Q88.47-6.62 87.50-6.03L87.50-6.03L87.43-4.68L87.62-0.36L85.19 0.09L85.41-4.55" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 35.305px 0.416399px; animation: 100s linear -23.2941s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M94.10-3.76L94.10-3.76Q94.10-6.07 95.35-7.67L95.35-7.67L95.35-7.67Q96.59-9.27 98.25-9.27L98.25-9.27L98.25-9.27Q99.92-9.27 100.85-8.19L100.85-8.19L100.85-8.19Q101.77-7.11 101.77-5.33L101.77-5.33L101.77-5.33Q101.77-2.95 100.58-1.38L100.58-1.38L100.58-1.38Q99.38 0.20 97.56 0.20L97.56 0.20L97.56 0.20Q96.07 0.20 95.09-0.93L95.09-0.93L95.09-0.93Q94.10-2.05 94.10-3.76L94.10-3.76zM99.76-4.39L99.76-4.39L99.76-4.39Q99.76-7.00 97.97-7.00L97.97-7.00L97.97-7.00Q96.12-7.00 96.12-4.55L96.12-4.55L96.12-4.55Q96.12-3.28 96.64-2.56L96.64-2.56L96.64-2.56Q97.16-1.84 98.02-1.84L98.02-1.84L98.02-1.84Q98.87-1.84 99.32-2.49L99.32-2.49L99.32-2.49Q99.76-3.15 99.76-4.39" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.885px 0.371399px; animation: 100s linear -19.4118s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M103.32-8.71L105.73-9.16L105.52-4.68L105.71-0.45L103.30 0L103.52-4.37L103.32-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 41.965px -6.9286px; animation: 100s linear -15.5294s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M103.19-11.80L103.19-11.80L103.19-11.80Q103.19-12.40 103.66-12.88L103.66-12.88L103.66-12.88Q104.13-13.36 104.74-13.36L104.74-13.36L104.74-13.36Q105.35-13.36 105.68-13.02L105.68-13.02L105.68-13.02Q106.00-12.69 106.00-12.02L106.00-12.02L106.00-12.02Q106.00-11.36 105.54-10.88L105.54-10.88L105.54-10.88Q105.08-10.40 104.48-10.40L104.48-10.40L104.48-10.40Q103.88-10.40 103.54-10.80L103.54-10.80L103.54-10.80Q103.19-11.20 103.19-11.80" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 48.025px 0.416399px; animation: 100s linear -11.6471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M110.95-1.84L110.95-1.84L110.95-1.84Q111.47-1.84 112.05-2.11L112.05-2.11L112.05-2.11Q112.63-2.38 112.95-2.65L112.95-2.65L113.27-2.92L114.10-1.91L114.10-1.91Q113.92-1.60 113.54-1.21L113.54-1.21L113.54-1.21Q113.17-0.81 112.78-0.53L112.78-0.53L112.78-0.53Q112.39-0.25 111.75-0.03L111.75-0.03L111.75-0.03Q111.11 0.20 110.43 0.20L110.43 0.20L110.43 0.20Q108.97 0.20 108.05-0.91L108.05-0.91L108.05-0.91Q107.14-2.02 107.14-3.76L107.14-3.76L107.14-3.76Q107.14-5.96 108.41-7.61L108.41-7.61L108.41-7.61Q109.69-9.27 111.40-9.27L111.40-9.27L111.40-9.27Q112.72-9.27 113.45-8.53L113.45-8.53L113.45-8.53Q114.17-7.79 114.17-6.46L114.17-6.46L114.17-6.46Q114.17-5.67 113.90-4.66L113.90-4.66L113.54-4.28L109.04-3.87L109.04-3.87Q109.35-1.84 110.95-1.84zM110.95-7.42L110.95-7.42L110.95-7.42Q110.16-7.42 109.62-6.78L109.62-6.78L109.62-6.78Q109.08-6.14 108.99-5.15L108.99-5.15L112.05-5.53L112.05-5.53Q112.10-5.94 112.10-6.21L112.10-6.21L112.10-6.21Q112.10-7.42 110.95-7.42" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.305px 0.371399px; animation: 100s linear -7.76471s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M115.74-8.71L118.15-9.16L117.94-4.68L118.13-0.45L115.72 0L115.94-4.37L115.74-8.71" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 54.385px -6.9286px; animation: 100s linear -3.88235s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M115.61-11.80L115.61-11.80L115.61-11.80Q115.61-12.40 116.08-12.88L116.08-12.88L116.08-12.88Q116.55-13.36 117.16-13.36L117.16-13.36L117.16-13.36Q117.77-13.36 118.10-13.02L118.10-13.02L118.10-13.02Q118.42-12.69 118.42-12.02L118.42-12.02L118.42-12.02Q118.42-11.36 117.96-10.88L117.96-10.88L117.96-10.88Q117.50-10.40 116.90-10.40L116.90-10.40L116.90-10.40Q116.30-10.40 115.96-10.80L115.96-10.80L115.96-10.80Q115.61-11.20 115.61-11.80" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g><g class="path" style="transform: scale(0.91); transform-origin: 59.875px 0.416399px; animation: 100s linear 0s infinite normal forwards running breath-f62436e6-769d-40f6-affc-78d91e87ae8c;"><path d="M122.85-1.67L122.85-1.67L122.85-1.67Q123.79-1.67 123.79-2.50L123.79-2.50L123.79-2.50Q123.79-2.79 123.38-3.04L123.38-3.04L123.38-3.04Q122.98-3.29 122.39-3.55L122.39-3.55L122.39-3.55Q121.81-3.80 121.22-4.11L121.22-4.11L121.22-4.11Q120.64-4.43 120.23-4.99L120.23-4.99L120.23-4.99Q119.83-5.54 119.83-6.26L119.83-6.26L119.83-6.26Q119.83-7.47 120.89-8.37L120.89-8.37L120.89-8.37Q121.95-9.27 123.34-9.27L123.34-9.27L123.34-9.27Q123.98-9.27 124.61-9.12L124.61-9.12L124.61-9.12Q125.23-8.96 125.80-8.64L125.80-8.64L124.60-6.44L124.60-6.44Q124.47-6.55 124.27-6.71L124.27-6.71L124.27-6.71Q124.07-6.88 123.53-7.14L123.53-7.14L123.53-7.14Q122.98-7.40 122.55-7.40L122.55-7.40L122.55-7.40Q122.13-7.40 121.91-7.21L121.91-7.21L121.91-7.21Q121.68-7.02 121.68-6.69L121.68-6.69L121.68-6.69Q121.68-6.35 122.30-6.02L122.30-6.02L122.30-6.02Q122.92-5.69 123.66-5.41L123.66-5.41L123.66-5.41Q124.40-5.13 125.02-4.49L125.02-4.49L125.02-4.49Q125.64-3.85 125.64-2.97L125.64-2.97L125.64-2.97Q125.64-1.71 124.61-0.76L124.61-0.76L124.61-0.76Q123.57 0.20 122.22 0.20L122.22 0.20L122.22 0.20Q121.36 0.20 120.61-0.18L120.61-0.18L120.61-0.18Q119.86-0.56 119.54-0.94L119.54-0.94L119.21-1.31L120.64-2.97L120.64-2.97Q120.74-2.83 120.94-2.61L120.94-2.61L120.94-2.61Q121.14-2.39 121.73-2.03L121.73-2.03L121.73-2.03Q122.31-1.67 122.85-1.67" fill="#28292f" stroke="none" stroke-width="none" transform="translate(-62.6300048828125,4.951398853975181)" style="fill: rgb(40, 41, 47);"></path></g></g>
                    </g>
                    </g>
                    </svg>'''), None, None, None]])

app.add_url_rule('/tool','webio.view',webio_view(start)
                 ,methods=['GET','POST','OPTIONS'])

if __name__== "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--port",type=int,default=8080)
        args = parser.parse_args()
        start_server(start,port=args.port,debug=True)
