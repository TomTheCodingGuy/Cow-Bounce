#!/bin/bash

#Uninstalling old version
echo "Uninstalling old version..."
cd /opt/Cow-Bounce/Scripts
sudo chmod +x ./uninstall.sh
./uninstall.sh
echo "Complete!"

#Installing new version
echo "Installing new version...."
cd 
git clone https://github.com/TomTheCodingGuy/Cow-Bounce.git
cd Cow-Bounce/Scripts
sudo chmod +x ./install.sh
./uninstall.sh
echo "Complete!"
