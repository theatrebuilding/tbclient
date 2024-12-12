import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

# Hardcoded host and port
HOST = "sender.a.pinggy.link"
PORT = "20073"

def start_sender(host, port):
    # Initialize GStreamer
    Gst.init(None)

    # Build the sender pipeline
#    pipeline_description = (
#        f"videotestsrc ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast "
#        f"! rtph264pay config-interval=1 pt=96 ! tcpclientsink host={host} port={port}"
#    )

    pipeline_description = (
        f"cat video.h264 | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96! gdppay ! tcpclientsink host={host} port={port}"
    )


    pipeline = Gst.parse_launch(pipeline_description)

    # Start playing
    pipeline.set_state(Gst.State.PLAYING)

    # Main loop for handling GStreamer events
    loop = GLib.MainLoop()
    bus = pipeline.get_bus()
    bus.add_signal_watch()
    
    def on_message(bus, message):
        msg_type = message.type
        if msg_type == Gst.MessageType.ERROR:
            err, debug = message.parse_error()
            print(f"Error: {err.message}")
            print(f"Debug info: {debug}")
            loop.quit()
        elif msg_type == Gst.MessageType.EOS:
            print("End-Of-Stream reached")
            loop.quit()
        elif msg_type == Gst.MessageType.STATE_CHANGED:
            old_state, new_state, pending_state = message.parse_state_changed()
            if message.src == pipeline:
                print(f"Pipeline state changed from {old_state.value_name} to {new_state.value_name}")

    bus.connect("message", on_message)

    try:
        print(f"Starting sender on {host}:{port}...")
        loop.run()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        pipeline.set_state(Gst.State.NULL)

if __name__ == "__main__":
    start_sender(HOST, PORT)
