import os

def start_receiver(host, port):
    # Start the receiver pipeline
    print("Starting receiver...")
    video_port = port
    audio_port = str(int(port) + 1)

    receiver_pipeline = (
        "gst-launch-1.0 -v "
        f"tcpclientsrc host={host} port={video_port} ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink "
        f"tcpclientsrc host={host} port={audio_port} ! application/x-rtp, payload=97 ! rtpopusdepay ! opusdec ! audioconvert ! autoaudiosink"
    )

    os.system(receiver_pipeline)
