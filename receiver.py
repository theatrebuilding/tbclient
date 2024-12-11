import os

def start_receiver(host2, host3, receiver1, receiver2):
    # Start the receiver pipeline
    print("Starting receiver...")
    
    receiver_pipeline = (
        f"gst-launch-1.0 -v "
        f"tcpclientsrc host={host2} port={receiver1} ! matroskademux name=d "
        "d.video_0 ! queue ! h264parse ! avdec_h264 ! videoconvert ! autovideosink "
        "d.audio_0 ! queue ! opusdec ! audioconvert ! autoaudiosink"
    )

    os.system(receiver_pipeline)
