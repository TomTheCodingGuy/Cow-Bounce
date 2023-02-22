#!/bin/bash
version=0.0.1

echo "Creating Directories..."
rm -rf /tmp/Cow-Bounce
mkdir -p /tmp/ || error "Could not make directory!"
cd /tmp/
echo "Complete!"

# Downloading Git-Hub Repository
echo "Downloading Repository..."
git_clone https://github.com/TomTheCodingGuy/Cow-Bounce.git || error 'Failed to clone repository!'
echo "Complete!"

# Move files to /opt
echo "Moving Files..."
sudo mv -f /tmp/Cow-Bounce/ /opt/Cow-Bounce/ || error "Failed to move source folder to /opt!"
echo "Complete!"

# Installing PyGame Python Library
echo "Installing PyGame..."
pip install pygame || error "Failed to install PyGame"
echo "Complete!"

#Create cowbounce command
sudo mkdir -p /usr/local/bin
echo '#!/bin/bash
cd /opt/Cow-Bounce/
sudo chmod +x run.sh
./run.sh' | sudo tee /usr/local/bin/cowbounce >/dev/null
sudo chmod +x /usr/local/bin/cowbounce

#Menu shortcut
sudo mkdir -p /usr/local/share/applications
echo "[Desktop Entry]
Name=CowBounce!
Comment=Fun Vertical PLatformer!
Icon=/opt/Cow-Bounce/icon-64.png
Exec=cowbounce
Path=/opt/Cow-Bounce/
Type=Application
Terminal=false
Categories=Game;" | sudo tee /usr/local/share/applications/CowBounce!.desktop >/dev/null