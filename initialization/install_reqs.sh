# Install pip
sudo apt install python3-pip

# Install python libraries
pip3 install sqlalchemy
pip install psycopg2-binary
pip3 install pandas

# EDIT THIS ACCORING YOUR DB CREDENTIALS IN YOUR VM ENV
echo 'export DB_USERNAME="xxxxxxxx"' >> ~/.bashrc
echo 'export DB_PASSWORD="xxxxxxxx"' >> ~/.bashrc
echo 'export DB_HOST="xxxxxxxx"' >> ~/.bashrc
echo 'export DB_PORT="xxxxxxxx"' >> ~/.bashrc

# source the bash
source ~/.bashrc