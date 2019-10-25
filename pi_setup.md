# Prepping new Pi Zero:

These instructions were written for Raspian Buster Kernel version 4.19 released 2019-09-26

## Gain access to Zero
Via host computer, put Raspian image on SD card (balenaEtcher is a good recommendation)

Via host computer, create a file `/wpa_supplicant.conf` that contains:

    country=US
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
        ssid="[your wifi station ID here]"
        psk="[your wifi password here]"
        key_mgmt=WPA-PSK
    }

Via host computer, create another file `/ssh` that is empty.

Eject SD card, put into Pi, boot up!

Log into device using its default zero-conf name:

    ssh pi@raspberrypi.local

Immediately change the default password to something stronger.

    passwd

## Update hostname

    ifconfig -a

Examine the last 4 hex digits in the WLAN0's HW address, replace the following
'X's accordingly:

    sudo cat "unicornXXXX" > /etc/hostname


## Setup SSH

    mkdir .ssh

Via another terminal check that you can now log in via SSH:

    cp ~/.ssh/zero.pub pi@[IPADDRESS]:/.ssh/authorized_keys


## Update System

    sudo apt-get update
    sudo apt-get -y upgrade

The above will take like 20 minutes!

Now install fail2ban

    sudo apt-get update
    sudo apt-get install -y fail2ban
    sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

    sudo reboot

Make sure you can log in via SSH and zero_pub key!

## Install webserver and connector

    sudo apt-get install -y build-essential python3-dev nginx
    sudo pip install uwsgi

## Localize System Configuration

Configure system using:

    sudo raspi-config

1. Locale: Use your own, of course
2. Time Zones: Use your own, of course
3. Keyboard: Use your own, of course
4. Expand filesystem


    sudo reboot

## Install Node
Check to see which version is latest first!

    curl -o node-v11.9.0-linux-armv6.tar.gz https://nodejs.org/dist/v11.9.0/node-v11.9.0-linux-armv6l.tar.gz
    tar -xzf node-v11.9.0-linux-armv6.tar.gz
    sudo cp -r node-v11.9.0-linux-armv6l/* /usr/local/

## Setup System Users

#### homebridge
    sudo useradd --system homebridge
    sudo mkdir /var/homebridge
    sudo chown homebridge:homebridge /var/homebridge
    sudo usermod -d /var/homebridge homebridge

#### unicorn
    sudo useradd --system unicorn
    sudo mkdir /var/unicorn
    sudo chown unicorn:unicorn /var/unicorn
    sudo usermod -d /var/unicorn unicorn
    sudo usermod -aG sudo unicorn

## Install homebridge-pi-lamp

    cd /var/unicorn
    sudo su unicorn -c "git clone https://github.com/mkoistinen/homebridge-pi-lamp.git unicorn"

### Copy init scripts to system locations
Copy the daemons to the right place:

    sudo su root -c "cp ./init.d/homebridge /etc/init.d/"
    sudo su root -c "cp ./init.d/unicorn /etc/init.d/"

Register the daemons:

    sudo update-rc.d homebridge defaults
    sudo update-rc.d unicorn defaults

## Install Homebridge Node packate Requirements

Note, these are installed globally.

    sudo npm install -g --unsafe-perm homebridge
    sudo npm install -g --unsafe-perm homebridge-better-http-rgb

### Copy config.json

    sudo cp /var/unicorn/unicorn/homebridge/config.json /var/homebridge/


## Install The Unicorn Service

### Create Virtual Env

    cd /var/unicorn
    sudo -H pip install virtualenv
    sudo su unicorn -c "virtualenv venv"

### Install requirements
This installs the code as a module

    sudo su unicorn -c "source venv/bin/activate && pip install -e unicorn/."


## If HW button also installed (on GPIO23)

Install Access Point packages
Create new service: unicorn-configuration-mode (from file in repo)
Add to rc2.d

    cd /home/pi
    git clone https://github.com/WiringPi/WiringPi.git

    sudo cp /etc/dhcpcd.conf /etc/dhcpcd.ap.conf
    sudo cp /etc/dhcpcd.conf /etc/dhcpcd.normal.conf

Update dhcpcd.ap.conf for AP mode
Modify /etc/init.d/hostapd

    cd /etc/cd2.d
    sudo rm S01hostapd
    sudo rm S01dhcpcd
    sudo ln -s ../init.d/unicorn-configuration-mode S01unicorn-configuration-mode


### Install dnsmasq hostapd

    sudo apt install dnsmasq hostapd
    sudo systemctl stop dnsmasq
    sudo systemctl stop hostapd

#### Make 2 DHCPCD Service configurations

Copy the dhcpcd.conf into 2 different files, and symlink the normal one

    sudo cp /etc/dhcpcd.conf /etc/dhcpcd.ap.conf
    sudo vi /etc/dhcpcd.ap.conf
    sudo mv /etc/dhcpcd.conf /etc/dhcpcd.normal.conf
    sudo ln -s /etc/dhcpcd.normal.conf /etc/dhcpcd.conf

#### Configure DNSMASQ

    sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
    sudo vi /etc/dnsmasq.conf

#### Configure HOSTAPD

    sudo vi /etc/hostapd/hostapd.conf
    sudo vi /etc/default/hostapd

    sudo systemctl unmask hostapd
    sudo systemctl enable hostapd
    sudo systemctl start hostapd
