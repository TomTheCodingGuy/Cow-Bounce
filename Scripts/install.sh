#!/bin/bash
version=0.0.1

echo "Creating Directories..."
rm -rf /tmp/Cow-Bounce
mkdir -p /tmp/
cd /tmp/
echo "Complete!"

# Downloading Git-Hub Repository
echo "Downloading Repository..."
git clone https://github.com/TomTheCodingGuy/Cow-Bounce.git
echo "Complete!"

# Move files to /opt
echo "Moving Files..."
sudo mv -f /tmp/Cow-Bounce/ /opt/Cow-Bounce/
echo "Complete!"

# Installing PyGame Python Library
echo "Installing PyGame..."
pip install pygame || error "Failed to install PyGame"
echo "Complete!"

#Create cowbounce command
sudo mkdir -p /usr/local/bin
echo '#!/bin/bash
cd /opt/Cow-Bounce/Scripts/
sudo chmod +x run.sh
./run.sh' | sudo tee /usr/local/bin/cowbounce >/dev/null
sudo chmod +x /usr/local/bin/cowbounce

#Menu shortcut
sudo mkdir -p /usr/local/share/applications
echo "[Desktop Entry]
Name=Cow Bounce!
Comment=Fun Vertical PLatformer!
Icon=/opt/Cow-Bounce/images/icon-64.png
Exec=cowbounce
Path=/opt/Cow-Bounce/
Type=Application
Terminal=false
Categories=Game;" | sudo tee /usr/local/share/applications/CowBounce!.desktop >/dev/null
