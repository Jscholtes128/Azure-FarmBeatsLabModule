#!/bin/sh
sudo apt-get install libssl1.0.2
curl https://packages.microsoft.com/config/debian/stretch/multiarch/prod.list > ./microsoft-prod.list && \
sudo cp ./microsoft-prod.list /etc/apt/sources.list.d/ && \
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
sudo cp ./microsoft.gpg /etc/apt/trusted.gpg.d/ && \
sudo apt-get update
#sudo apt-get install -y ca-certificates curl apt-transport-https lsb-release gnupg
#AZ_REPO=$(lsb_release -cs)
#echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | 
#    sudo tee /etc/apt/sources.list.d/azure-cli.list
#sudo apt-get update
#sudo apt-get install -y azure-cli 
sudo apt-get -y install moby-engine
sudo apt-get -y install moby-cli
sudo apt-get -y install iotedge
#sudo nano /etc/iotedge/config.yaml