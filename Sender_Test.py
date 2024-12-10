import os


def sendtest():
    os.system("gst-launch-1.0 tcpclientsrc host=tcp://viable-ray-perfectly.ngrok-free.app port=8000 ! fdsink fd = 2")