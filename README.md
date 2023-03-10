# Cow-Bounce
## Pygame vertical platformer

- This repository contains the source code, scripts and images for Cow Bounce, a fun vertical platformer game.
- As this game was made for Pi-Apps (https://github.com/Botspot/pi-apps.git), it is only fully tested on a Raspberry Pi.
- It may work on other linux or debian systems, but not on any other operating systems, such as Windows.
- Requires Python3 pre-installed (already done on Raspberry Pi)

### Installation:

- Clone this repository in terminal, to your home directory:
```
git clone https://github.com/TomTheCodingGuy/Cow-Bounce.git
```
- Execute the install.sh file using the following commands:
```
cd Cow-Bounce/Scripts
```
```
sudo chmod +x ./install.sh
```
```
./install.sh
```
- Now there should be a folder in /opt called Cow-Bounce, also containing the contents of this repository.
- Therefore, you can delete the Cow-Bounce folder in your home directory.
- To run the app from terminal, type ``cowbounce``.
- It should also appear in your Games Menu.
- Note: When I first installed it as a test on my Raspberry Pi, the game icon (icon-64.png) did not come up straight away. After rebooting however, it apppeared.

### Usage:

- Space to jump.
- Arrow keys to move left and right.
- This game can also be used as a Pygame tutorial, if you have a look at the source code file "CowBounce.py". It includes many of the basic uses of the Python library

### Uninstall:

- I created a uninstall script, located in this repository, so you can use the following commands to execute it:
```
cd /opt/Cow-Bounce/Scripts
```
```
sudo chmod +x ./uninstall.sh
```
```
./uninstall.sh
```
- This should remove all the files and directories

### Update:

- I created an update script, which basically just uninstalls the existing game and re-installing it as to get the latest features from this repository.
- Run the following commands:
```
cd /opt/Cow-Bounce/Scripts
```
```
sudo chmod +X ./update.sh
```
```
./update.sh
```
- Now you should have the latest version of the game.

### Issues:

- If you encounter any isues with installing, uninstalling or running the app, please raise an issue in the Issues section of this repository.
- Try uninstalling (see above), re-cloning this repository, and re-installing (also above), to make sure all of the files are up to date. 
- I have fully tested it on a Raspberry Pi, but I am happy to help with any problems you might encounter.

### Suggestions:

- If you have any suggestions on what to do next, post something in the Issues section of this repository.
- I have a few ideas myself for what to add into the game next...

### Credits:

- Made by TomTheCodingGuy
- Thanks to Blooket (https://www.blooket.com) for the cow image.
