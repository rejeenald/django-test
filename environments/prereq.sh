#   apt-get update
#   apt-get install -y apache2
sudo apt-get update
sudo apt-get upgrade -y

#sudo apt-get install python2 python2-dev -y
sudo apt-get install apt-transport-https ca-certificates gnupg -y

echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -

sudo apt-get update && sudo apt-get install google-cloud-sdk -y

sudo apt-get install google-cloud-sdk-app-engine-python -y
sudo apt-get install google-cloud-sdk-app-engine-python-extras -y
sudo apt-get install google-cloud-sdk-datastore-emulator -y


#Fahad's edits for django and other utilities for python | Dec 12 2021
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo apt-get install tree -y
pip3 install Django
pip3 install python-decouple
pip install unipath
sudo apt-get install build-essential libssl-dev libffi-dev python-dev -y
sudo apt install gettext -y