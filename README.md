Albert, the voice controlled assistant

**Requirements**
Required Python 3+, Docker Compose

**Running**
After installing Docker and Python 3+, start the Docker machine by running the following commands:
```
$ docker-machine start default
$ eval $(docker-machine env default)
```

After starting the machine, to run the containers run the following commands:
```
$ docker-compose build
$ docker-compose up
```
