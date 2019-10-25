# TODOs:

### Services
 - [ ] nginx install / config
 - [ ] uwsgi install / config
 - [ ] Update homebridge configuration for port 80 based URLs
 - [ ] Button-press detection service

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

    pip-sync requirements.txt
