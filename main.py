import json
import requests
import base64
import subprocess

from sender import start_sender
from receiver import start_receiver

def check_webcam():
    # Check if a valid webcam is connected
    try:
        result = subprocess.run(
            ["v4l2-ctl", "--list-devices"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout.lower() + result.stderr.lower()

        # Check if /dev/video0 is mentioned
        if "/dev/video0" in output:
            # If we see 'cannot open device /dev/video0', that means no valid webcam
            if "cannot open device /dev/video0" not in output:
                return True
    except Exception as e:
        print(f"Error checking webcam: {e}")
    return False

def load_env(env_path):
    # Load environment variables from a JSON file
    with open(env_path, "r") as f:
        return json.load(f)

def get_ngrok_url_from_github(env_path="/home/theatrebuilding/env.json"):
    # Get the ngrok URL from GitHub
    env = load_env(env_path)
    GITHUB_TOKEN = env.get("GITHUB_TOKEN")
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not found in env.json.")
        return None

    repo_owner = "theatrebuilding"
    repo_name = "ngrokurl"
    file_path = "config.json"
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            content_str = base64.b64decode(data["content"]).decode("utf-8")
            config_data = json.loads(content_str)
            ngrok_url = config_data.get("ngrok_url")
            if not ngrok_url:
                print("ngrok_url not found in config.json.")
                return None
            return ngrok_url
        else:
            print(f"Failed to fetch config.json from GitHub, status code: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Error fetching ngrok_url from GitHub: {e}")
        return None
    
def get_ports_from_local_env(env_path="/home/theatrebuilding/env.json"):
    # Get the ports from the local environment file
    env = load_env(env_path)
    HOST = env.get("PINGGY_ADDRESS")
    PINGGY_SENDER = env.get("PINGGY_PORT_SENDING")
    PINGGY_RECEIVER1 = env.get("PINGGY_PORT_RECEIVING1")
    PINGGY_RECEIVER2 = env.get("PINGGY_PORT_RECEIVING2")

    return HOST, PINGGY_SENDER, PINGGY_RECEIVER1, PINGGY_RECEIVER2

def parse_ngrok_url(ngrok_url):
    # Parse the ngrok URL to extract the host and port
    if "://" in ngrok_url:
        _, rest = ngrok_url.split("://", 1)
    else:
        rest = ngrok_url

    if ":" not in rest:
        print("Invalid ngrok_url format, no port found.")
        return None, None

    host, port_str = rest.split(":", 1)
    return host, port_str

def main():
#    ngrok_url = get_ngrok_url_from_github()
#    if not ngrok_url:
#        print("Failed to retrieve ngrok URL, defaulting to localhost.")
#        host, port = "127.0.0.1", "5000"
#    else:
#        host, port = parse_ngrok_url(ngrok_url)
#        if not host or not port:
#            print("Failed to parse ngrok URL, defaulting to localhost.")
#            host, port = "127.0.0.1", "5000"

    host, sender, receiver1, receiver2 = get_ports_from_local_env()


    print("Checking for webcam...")
    if check_webcam():
        print("Webcam detected. Starting sender.")
        start_sender(host, sender, receiver1, receiver2)
    else:
        print("No webcam detected. Starting receiver.")
        start_receiver(host, sender, receiver1, receiver2)

if __name__ == "__main__":
    main()