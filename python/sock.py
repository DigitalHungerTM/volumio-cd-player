# Author: Mathijs Afman
# Note, this api is bad at playing albums with numbers in it.
# it does, however, work with chinese characters.

from socketIO_client import SocketIO

LIBRARY_URI = "music-library/NAS/truenasDataShare"

class Volumio:
    def __init__(self, address="localhost", port=3000):
        """
        :param `address`: address for the SocketIO API, defaults to "localhost"
        :param `port`: port for the SocketIO API, defaults to 3000
        """
        # create a socket and connect to the Volumio server
        self._sock = SocketIO(address, port)
        self._waiting = 0.1

    # general

    def _send(self, command, args=None, callback=None):
        """
        Send a command to the socket.io server.

        :param `command`: Command to send.
        :param `args`: Arguments.
        :param `callback`: Callback function called upon receiving the response.
        """
        # Emit the command to the server and wait for callbacks
        self._sock.emit(command, args, callback)
        self._sock.wait_for_callbacks(seconds=self._waiting)

    def getState(self):
        """
        gets the state of the player

        Doesn't work
        """
        self._send("getState")

    # playback

    def play_uri(self, uri: str, service: str):
        """
        Immediately plays the speified URI

        :param `uri`: URI of the file folder to play
        :param `service`: Service used to play the uri
        """
        # Bruteforce method that clears the queue
        self._send("clearQueue")
        self._send("addPlay", {"status": "play", "service": service, "uri": uri})

    def play_album(self, album_title: str):
        """
        Plays an album by `album_title`.
        
        :param `album_title`: Title of the album
        """
        # uri_base = "music-library/NAS/truenasDataShare/"
        uri = LIBRARY_URI + album_title
        service = 'mpd' # found this by looking at the getState
        self.play_uri(uri, service)

    def toggle_playback(self):
        """
        Toggles playback.
        """
        self._send("toggle")

    def stop(self):
        """
        Completely stops playback.
        """
        self._send("stop")

    def pause(self):
        """
        Pauses playback.
        """
        self._send("pause")
    
    def resume(self):
        """
        Resumes playback.
        """
        self._send("play")

    # volume
    # TODO
    #  testing
        
    def set_volume(self, value):
        """
        sets the volume to `value`
        
        :param `value`: (0-100)
        """
        self._send("volume", value)
    
    def mute(self):
        """
        mutes the player
        """
        self._send("mute")

    def unmute(self):
        """
        unmutes the player
        """
        self._send("unmute")


def main():
    volumio = Volumio("http://volumio.local", None)
    volumio.play_album('Hyperspace')


if __name__ == "__main__":
    main()
