import os

def start_sender(host, port):
    # Start the sender pipeline
    print("Starting sender...")

    sender_pipeline = (
        f"gst-launch-1.0 -v "
        "v4l2src device=/dev/video0 ! videoconvert ! "
        "x264enc speed-preset=ultrafast tune=zerolatency ! h264parse ! queue ! mux. "
        "alsasrc device=hw:1 ! audioconvert ! audioresample ! opusenc ! opusparse ! queue ! mux. "
        "matroskamux name=mux streamable=true ! "
        f"tcpserversink host=0.0.0.0 port={port}"
    )

    os.system(sender_pipeline)
