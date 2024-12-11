import gi
import sys
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib


def start_sender():
    # Initialize GStreamer
    Gst.init(None)

    # Build the sender pipeline
    pipeline_description = (
        f"videotestsrc ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast "
        f"! rtph264pay config-interval=1 pt=96 ! tcpclientsink host=sender.a.pinggy.link port=20073"
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

    bus.connect("message", on_message)

    try:
        print(f"Starting sender on {host}:{port}...")
        loop.run()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        pipeline.set_state(Gst.State.NULL)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 sender.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
    start_sender(host, port)
