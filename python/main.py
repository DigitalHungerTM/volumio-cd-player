from funcs import *
# REST API
import api
# Websocket API
import sock
from time import sleep

# Interval of checking for an album on the rfid reader in seconds
INTERVAL = 5

# Set to false when running on the rpi that hosts volumio
REMOTE = True

def main():
    # my_api = api.volumio_api()
    # print(my_api.handle_command("volume 50"))
    if REMOTE:
        volumio = sock.Volumio("http://volumio.local", None)
    else:
        volumio = sock.Volumio()

    volumio.play_album('Hyperspace')

    


if __name__ == "__main__":
    main()
