# Prueba Técnica InBev

## Architecture


## Collaboration

Here is the collaboration part of the technical exam:

[url=https://postimg.cc/FYJBj2zj][img]https://i.postimg.cc/FYJBj2zj/Captura.png[/img][/url]

[url=https://postimg.cc/FYJBj2zj][img]https://i.postimg.cc/FYJBj2zj/Captura.png[/img][/url]

## MLModelDeployment

Steps:
-create a venv: pyhon3-m venv env OR virtualenv venv
-activate the environment: source env/bin/activate
-pip install -r notebooks/requierements.txt OR
-pip install -r api/requirements
-pip install jupyter
- jupyter notebook
- Run the notebook, save the model
- create the folders: ./api/, ./api/app/
- create the files: ./api/main.py ./api/app/utils.py ./api/app/models.py and ./api/app/views.py

## Testing with SonarCloud
It was not possible, SonarCloud is paid, and the free plan is not avaiable to choose.

## About Docker
- build the docker container with: DOCKER_BUILDKIT=1 docker build . -t model-api-inveb:v1
- Run the container: docker run -p 8000:8000 model-api-inbev:v1
- Stop the container: docker stop $(docker ps -a -q)

