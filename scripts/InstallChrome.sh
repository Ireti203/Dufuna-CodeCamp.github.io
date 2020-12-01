#!/bin/bash

set -ex

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb    # download google chrome
sudo apt install ./google-chrome-stable_current_amd64.deb     # install google chrome
