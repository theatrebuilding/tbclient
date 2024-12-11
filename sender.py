import os

def start_sender(host1, sender):
    # Start the sender pipeline
    print("Starting sender...")
    print("Host: " + host1)
    print("Port: " + sender)


    sender_pipeline = (
        f"gst-launch-1.0 -v "
        f"videotestsrc ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast "
        f"! rtph264pay config-interval=1 pt=96 ! tcpclientsrc host={host1} port={sender}"
    )

    os.system(sender_pipeline)



