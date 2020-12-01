#!/bin/bash

set -ex

wget -q0- https://deb.opera.com/archive.key | sudo apt-key add -    # import opera repo's GPG key
echo deb https://deb.opera.com/opera-stable/ stable non-free | sudo tee /etc/apt/sources.list.d/opera.list    # add opera APT repo to system's software repo list
sudo apt install opera-stable
