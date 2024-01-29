# volumio-cd-player
A python based environment that scans rfid tags, and sends play requests to the volumio API.

# ideas
- use a .json file to keep track of albums and their titles
- create a script that automatically handles naming album folders

## TODO
- make 3d model
- repurpose speakers
- integrate hifiberry
- buy parts
-   screen
-   hifiberry dac
-   new amplifier that doesn't buzz (hifiberry amp2? (has dac built in))

## HifiBerry AMP2 compatibility
hifiberry amp2 pins  
3, 5, 12, 35, 38, 40

rc522 pins  
1, 6, 22, 24, 19, 21, 23

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
INCOMPLETE!!!

```bash
# turn on SPI
echo "dtparam=spi=on" >> /boot/userconfig.txt
sudo reboot now # wait for it to reboot
lsmod | grep spi # this should return `spi_bcm2835`

# install required python packages
sudo apt install python3-pip python3-dev python3-venv
pip3 install setuptools wheel spidev

# user, group and other own the required folders and files
sudo chmod ugo+wrx /usr/local/lib/python3.7/dist-packages
sudo chmod ugo+wrx /usr/local/lib/python3.7/dist-packages/*
sudo chmod ugo+wrx /dev
sudo chmod ugo+wrx /dev/mem

# clone the repo
git clone https://github.com/DigitalHungerTM/volumio-cd-player.git
cd volumio-cd-player

# clone the rfid reader repo
git clone https://github.com/pimylifeup/MFRC522-python.git
cd MFRC522-python

# install MFRC522
python3 setup.py install

# ...
```