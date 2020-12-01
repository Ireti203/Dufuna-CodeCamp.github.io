#!/bin/bash

set -ex

# Download geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux32.tar.gz -P ~/
sudo tar -zvxf ~/geckodriver-v0.28.0-linux32.tar.gz -C ~/
rm ~/geckodriver-v0.28.0-linux32.tar.gz

sudo mv -f ~/geckodriver /usr/local/bin/geckodriver
sudo chown root:root /usr/local/bin/geckodriver
sudo chmod +x /usr/local/bin/geckodriver
