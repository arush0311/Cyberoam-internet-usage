#!/bin/bash

echo -e "\n\nThis Will install Cyberoam internet usage on yout computer.\nPlease Note That This setup requires a working internet connection\nPlease stop all other installations or try sometime later\n\n"

echo -e "PRESS ANY KEY CONTINUE...\n"
read -n 1

sudo apt-get install python
sudo apt-get install python-pip
sudo pip install selenium
sudo pip install notify2
sudo apt-get install PhantomJS
chmod 755 internet_usage.py

echo -e "\n\nSETUP IS NOW COMPLETE.PRESS ANY KEY...\n"
read -n 1  
