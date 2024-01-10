# requirest python 3.10 or higher (switch statement)
# Mathijs Afman

import requests
import sys
from pprint import pprint

LOCALHOST = "localhost:3000"
NETWORK = "http://volumio.local/"

API_URL = NETWORK + "api/v1/"

NEXT_URL = API_URL + "commands/?cmd=next"
PREV_URL = API_URL + "commands/?cmd=prev"
PAUSE_URL = API_URL + "commands/?cmd=pause"
PLAY_URL = API_URL + "commands/?cmd=play"
TOGGLE_URL = API_URL + "commands/?cmd=toggle"
GET_STATE_URL = API_URL + "getState"
VOLUME_URL = API_URL + "commands/?cmd=volume&volume="

class volumio_api:
    # state
    def get_state(self):
        r = requests.get(GET_STATE_URL)
        return r.json()
    
    # playback
    def play(self):
        r = requests.get(PLAY_URL)
        return r.json()

    def pause(self):
        r = requests.get(PAUSE_URL)
        return r.json()
    
    def toggle(self):
        r = requests.get(TOGGLE_URL)
        return r.json()

    def play_next(self):
        r = requests.get(NEXT_URL)
        return r.json()

    def play_prev(self):
        self.set_volume("mute")
        requests.get(PREV_URL)
        requests.get(PREV_URL)
        self.set_volume("unmute")
    
    # volume
    def get_volume(self):
        state_json = self.get_state()
        state = dict(state_json)
        volume = state['volume']
        return volume

    def set_volume(self, volume: int | str):
        """
        volume can be integer value or `mute` or `unmute`
        """
        req_url = VOLUME_URL + str(volume)
        r = requests.get(req_url)
        return r.json()
    
    # command parsing
    # the match statement is introduced in python 3.10
    # either upgrade to python 3.10 or convert this
    # to an if-else tree
    def handle_command(self, command: str):
        command = command.split(" ")
        match command[0]:
            case "play":
                return self.play()
            case "pause":
                return self.pause()
            case "toggle":
                return self.toggle()
            case "next":
                return self.play_next()
            case "previous":
                return self.play_prev()
            case "state":
                return self.get_state()
            case "volume":
                try:
                    return self.set_volume(command[1])
                except IndexError:
                    print("no volume provided")
            # case "get volume":
            #     print(my_api.get_volume())
            case _:
                return "unknown command"



def main():
    my_api = volumio_api()
    while True:
        try:
            command = input("what would you like to do?\n").split(' ')
            my_api.handle_command(command)
        except KeyboardInterrupt:
            print("\nexiting")
            exit(0)


if __name__ == "__main__":
    main()
