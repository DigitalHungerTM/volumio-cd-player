from .funcs import *
from . import api, sock

# Interval of checking for an album on the rfid reader in seconds
INTERVAL = 5

# Set to false when running on the rpi that hosts volumio
REMOTE = True


def main():
    if REMOTE:
        volumio = sock.Volumio("http://volumio.local", None)
    else:
        volumio = sock.Volumio()

    volumio.play_album('Hyperspace')

    # while true:
    # scan
    # find album name that corresponds to tag UID
    # play album
    # sleep for interval


if __name__ == "__main__":
    main()
