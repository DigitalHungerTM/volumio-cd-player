from socketIO_client import SocketIO

from time import sleep

class Volumio:
    def __init__(self, address="localhost", port=3000):
        """
        Class for interacting with the Volumio socket.io server

        :param address: Server address (default is "localhost").
        :param port: Server port (defualt is 3000).
        """
        # create a socket and connect to the Volumio server
        self._sock = SocketIO(address, port)
        self._waiting = 0.1

    def _send(self, command, args=None, callback=None):
        """
        Send a command to the socket.io server.
        :param command: Command to send.
        :param args: Arguments as a dictionary.
        :param callback: Callback function called upon receiving the response.
        :return: None
        """
        # Emit the command to the server and wait for callbacks
        self._sock.emit(command, args, callback)
        self._sock.wait_for_callbacks(seconds=self._waiting)

    def getState(self):
        """
        Get the state of the player
        DOESN'T WORK
        :return: state
        """
        self._send("getState")


    def play_uri(self, uri, service):
        """
        Immediately plays the speified URI
        :param uri: URI
        :param service: Service used to play the uri
        :return: None
        """
        # Bruteforce method that clears the queue
        self._send("clearQueue")
        self._send("addPlay", {"status": "play", "service": service, "uri": uri})

    def play_album(self, album_title):
        """
        Plays an album by `album_name`
        :param album_name: Name of the album
        :return: None
        """
        uri_base = "music-library/NAS/Music/"
        uri = uri_base + album_title
        service = 'mpd' # found this by looking at the getState
        self.play_uri(uri, service)

    def toggle_playback(self):
        """
        Toggles playback.
        :return: None
        """
        self._send("toggle")

    def pause(self):
        """
        Pauses playback.
        :return: None
        """
        self._send("pause")
    
    def resume(self):
        """
        Resumes playback.
        :return: None
        """
        self._send("play")




def main():
    volumio = Volumio("http://volumio.local", None)
    volumio.play_album('Hyperspace')
    # print("This program is a module meant to be used by `main.py`")
    # exit(-1)


if __name__ == "__main__":
    main()
