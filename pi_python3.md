

    sudo apt-get install python3-pip
    sudo pip3 install virtualenv
    
    sudo cd /var/unicorn
    sudo mkdir .venv
    
Make users...

As user unicorn

    sudo su - unicorn
    virtualenv .venv/diamond
    pip3 install "django>2.2,<2.3"
