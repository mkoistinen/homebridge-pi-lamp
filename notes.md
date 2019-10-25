# TODOs:

### Services
 - [x] nginx install
     - [ ] Configuration files
 - [x] uwsgi install
     - [ ] Configuration files
     - [ ] Is there an init.d script for this?
 - [ ] Button-press detection service
     - [ ] Is there an init.d script for this?
 - [x] Update homebridge configuration for port 80 based URLs

### Documentation
 - [ ] Update `pi_setup.md` accordingly
 - [ ] Development docs?

### Future?
 - [ ] Dockerize the whole install?
 
 
## Install requirement additions

If installing for development, please use:

    pip-sync dev-requirements.txt requirements.txt

    pytest --cov=unicorn

If installing just to run this project, use:

    pip install -e .
