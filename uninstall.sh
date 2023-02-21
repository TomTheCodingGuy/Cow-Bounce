#!/bin/bash

purge_packages || exit 1

sudo rm -rf /opt/Cow-Bounce/ /usr/local/share/applications/CowBounce!.desktop ~/.local/share/applications/CowBounce!.desktop /usr/local/bin/cowbounce || error "Could not remove CowBounce files!"
