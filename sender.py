import os

def start_sender(host, sender):
    # Start the sender pipeline
    print("Starting sender...")
    print("Host: " + host)
    print("Port: " + port)


    sender_pipeline = (
        f"gst-launch-1.0 "
        f"v4l2src device=/dev/video0 ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast "
        f"! rtph264pay ! queue ! tcpclientsink host={host} port={sender}"
    )

    os.system(sender_pipeline)
