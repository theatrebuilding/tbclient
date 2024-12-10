import os

def start_receiver(host, port):
    # Start the receiver pipeline
    print("Starting receiver...")
    
    receiver_pipeline = (
        f"gst-launch-1.0 -v "
        f"tcpclientsrc host=0.0.0.0 port={port} ! matroskademux name=d "
        "d.video_0 ! queue ! h264parse ! avdec_h264 ! videoconvert ! autovideosink "
        "d.audio_0 ! queue ! opusdec ! audioconvert ! autoaudiosink"
    )

    os.system(receiver_pipeline)
