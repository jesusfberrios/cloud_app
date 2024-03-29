#!/bin/bash

sudo apt update -y

# Install pip
sudo apt install python3-pip

# Install python libraries
pip3 install -r requirements.txt

# EDIT THIS ACCORING YOUR DB CREDENTIALS IN YOUR VM ENV
echo 'export DB_USERNAME="xxxxxxxx"' >> ~/.bashrc
echo 'export DB_PASSWORD="xxxxxxxx"' >> ~/.bashrc
echo 'export DB_HOST="xxxxxxxx"' >> ~/.bashrc
echo 'export DB_PORT="xxxxxxxx"' >> ~/.bashrc
echo 'export DB="xxxxxxxx"' >> ~/.bashrc

# source the bash
source ~/.bashrc

# Verify that the variables were exported to bash correctly
tail -n 10 ~/.bashrc 

