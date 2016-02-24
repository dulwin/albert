FROM ubuntu:14.04
RUN apt-get update && apt-get install -y wget && cd /root
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
RUN /root/miniconda3/bin/pip install flask

COPY . /ears
