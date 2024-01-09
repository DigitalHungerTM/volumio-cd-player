from funcs import *
from time import sleep

# Interval of checking for an album on the rfid reader in seconds
INTERVAL = 5

def main():
    while True:
        album = scan_rfid()
        
        play_type = "album"
        gen_api_call(play_type, album)

        sleep(INTERVAL)


if __name__ == "__main__":
    main()
