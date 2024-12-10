import os

def start_receiver(host, port):
    """
    Starts the receiver pipeline using GStreamer over TCP.
    The receiver acts as a TCP client connecting to the sender's host:port.

    We'll assume the sender is available at host:port for video and host:(port+1) for audio.
    """
    print("Starting receiver...")
    video_port = port
    audio_port = str(int(port) + 1)

    receiver_pipeline = (
        "gst-launch-1.0 -v "
        f"tcpclientsrc host={host} port={video_port} ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink "
        f"tcpclientsrc host={host} port={audio_port} ! application/x-rtp, payload=97 ! rtpopusdepay ! opusdec ! audioconvert ! autoaudiosink"
    )

    os.system(receiver_pipeline)
