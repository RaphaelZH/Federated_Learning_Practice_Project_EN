FROM image-python-3-11

COPY ./docker-python-3-11.txt ./requirements-input.txt 
COPY ./requirements-docker-python-3-11.txt ./requirements-output.txt

RUN apt-get update \ 
	&& apt-get -y install \
	&& apt-get -y install unzip \
	&& apt-get install -y python3-pip \
	&& pip3 install --upgrade pip \
	&& pip3 install -U -r requirements-input.txt \
	&& pip3 freeze > requirements-output.txt