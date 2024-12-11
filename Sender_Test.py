import os


def sendtest():
    os.system("gst-launch-1.0 tcpclientsrc host=tcp://viab2.tcp.eu.ngrok.io port=10412 ! fdsink fd = 2")
