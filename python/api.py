# requirest python 3.10 or higher (switch statement)
# Mathijs Afman

import sys
from pprint import pprint
import requests

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

DEBUG = True

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
        return state['volume']

    def set_volume(self, volume: int | str):
        """
        volume can be integer value or `mute` or `unmute`
        """
        req_url = VOLUME_URL + str(volume)
        r = requests.get(req_url)
        return r.json()
            
    def handle_command_if(self, command_str: str):
        command_list = command_str.split(" ")
        command = command_list[0]
        if command == 'play':
            response = self.play()
        elif command == 'pause':
            response =  self.pause()
        elif command == 'toggle':
            response =  self.toggle()
        elif command == 'next':
            response =  self.play_next()
        elif command == 'previous':
            response =  self.play_prev()
        elif command == 'state':
            response =  self.get_state()
        elif command == 'volume':
            try:
                response =  self.set_volume(command_list[1])
            except IndexError:
                response = "no volume provided"
        else:
            response =  "unknown command"

        return response


def main():
    my_api = volumio_api()
    while True:
        try:
            command = input("what would you like to do?\n")
            r = my_api.handle_command_if(command)
            if DEBUG: print(r)
        except KeyboardInterrupt:
            print("\nexiting")
            exit(0)


if __name__ == "__main__":
    main()
