import os


def start_sender(host, port):
    # Start the sender pipeline
    print("Starting sender...")
    print("Host: " + host)
    print("Port: " + port)

    sender_pipeline = (
        f"gst-launch-1.0 tcpclientsrc host={host} port={port} ! fdsink fd = 2"
    )

    os.system(sender_pipeline)
