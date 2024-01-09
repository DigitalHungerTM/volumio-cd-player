import sys

def scan_rfid():
    """
    runs some code to scan an rfid tag
    returns a dict:
    {
        `album_unique_id`: `album_name`
    }
    """
    pass


def gen_api_call(type: str, album: dict):
    """
    generates an API call that the volumio API can handle
    maybe also handle the API call?
    returns the generated API call string?
    """
    pass


if __name__ == "__main__":
    sys.exit(f"{"/".join(sys.argv[0].split("/")[-2:])} is a module, it is not meant to be ran directly.\nIt is imported by python/main.py")