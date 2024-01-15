# volumio-cd-player
A python based environment that scans rfid tags, and sends play requests to the volumio API.

# ideas
- use a .json file to keep track of albums and their titles
- create a script that automatically handles naming album folders


## TODO
- make a workflow for the python API
- find good rfid scanner / corresponding python library / code
- learn volumio REST API
- make 3d model
- repurpose speakers
- integrate hifiberry
- buy parts
-   screen
-   rfid scanner
-   rfid tags
-   large (not necessarily fast) USB stick for the server
-   hifiberry dac
-   new amplifier that doesn't buzz (hifiberry amp2? (has dac built in))

## Handy Links
Other repos that have sort of the same idea  
https://github.com/ryanwa18/spotipi-eink/tree/main  
https://github.com/talaexe/Spotify-RFID-Record-Player

MFRC522 libraries  
https://github.com/pimylifeup/MFRC522-python  
https://github.com/ondryaso/pi-rc522/tree/master

Volumio REST API docs  
https://developers.volumio.com/api/rest-api  
Volumio CLI docs  
https://developers.volumio.com/api/command-line-client

## Installation:
- turn SPI on by adding the line `dtparam=spi=on` to `/boot/userconfig.txt`
- reboot and check if this worked by running `lsmod | grep spi`. If it worked, spi_bcm2835 will be returned.
- `pip3 install spidev`
