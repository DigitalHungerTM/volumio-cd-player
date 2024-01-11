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


if __name__ == "__main__":
    main()
