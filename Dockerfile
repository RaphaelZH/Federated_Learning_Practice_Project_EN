FROM openfl_projet/aggregator
FROM openfl_projet/collaborator

WORKDIR /app

RUN pip install -r docker_python3-11.txt
RUN pip install -U -r docker_python3-11.txt
RUN pip freeze > docker_python3-11_requirements.txt