import os


def start_sender(host, port):
    # Start the sender pipeline
    print("Starting sender...")
    print("Host: " + host)
    print("Port: " + port)

    sender_pipeline = (
        f"gst-launch-1.0 -v videotestsrc pattern=snow ! video/v4l2h264enc,width=1280,height=720 "
        f"! tcpserversink host=" + host + " port=" + port
    )

    os.system(sender_pipeline)
