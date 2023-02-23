# Cow-Bounce
## Pygame vertical platformer

- This repository contains the source code, scripts and images for Cow Bounce, a fun vertical platformer game.
- As this game was made for Pi-Apps(https://github.com/Botspot/pi-apps.git), it is only fully tested on a Raspberry Pi.
- It may work on other linux or debian systems, but not on any other operating systems, such as Windows.
- Requires Python3 pre-installed (already done on Raspberry Pi)

### Installation:

- Clone this repository in terminal, to your home directory:
```
git clone https://github.com/TomTheCodingGuy/Cow-Bounce.git
```
- Execute the install.sh file using the following commands:
```
cd Cow-Bounce
```
```
sudo chmod +x ./install.sh
```
```
./install.sh
```
- Now there should be a folder in /opt called Cow-Bounce, also containing the contents of this repository.
- Therefore, you can delete the Cow-Bounce folder in your home directory.
- To run the app from terminal, type 'cowbounce'.
- It should also appear in your Games Menu.
- Note: When I first installed it as a test on my Raspberry Pi, the game icon(icon-64.png) did not come up straight away. After rebooting however, it apppeared.

### Uninstall:

- I created a uninstall script, located in this repository, so you can use the following commands to execute it:
```
cd /opt/Cow-Bounce
```
```
sudo chmod +x ./uninstall.sh
```
```
./uninstall.sh
```
- This should remove all the files and directories

### Credits:

- Made by TomTheCodingGuy
- Thanks to Blooket (https://www.blooket.com) for the cow image.
- Thanks to CodersLegacy (https://coderslegacy.com/python/pygame-platformer-game-development) for providing some source code.
