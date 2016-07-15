# Script for install all required stuff on Ubuntu (tested on 14.04)

sudo update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10

sudo apt-get -y --purge remove node    # Remove old node, nodejs 
sudo apt-get -y --purge remove nodejs

sudo apt-get -y install nodejs npm

npm install 
./node_modules/.bin/bower install