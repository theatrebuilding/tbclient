import os

def start_sender(host, port):
    # Start the sender pipeline
    print("Starting sender...")
    video_port = port
    audio_port = str(int(port) + 1)

    sender_pipeline = (
        "gst-launch-1.0 -v "
        "v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480 ! videoconvert ! "
        "x264enc speed-preset=ultrafast tune=zerolatency ! rtph264pay ! queue ! "
        f"tcpserversink host=0.0.0.0 port={video_port} "
        "alsasrc device=hw:1 ! audioconvert ! audioresample ! opusenc ! rtpopuspay ! queue ! "
        f"tcpserversink host=0.0.0.0 port={audio_port}"
    )

    os.system(sender_pipeline)
