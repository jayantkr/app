#python App
# Inside app folder which is cloned using git
Prerequisite:
1.Docker (https://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/ :Installation link for reference)
2.Ubuntu 14.04


#Running and building using below command
docker build --no-cache --rm -t travcunn/flask .
docker run -d -p 5000:8000 travcunn/flask

#Debuging commands:
docker ps
docker inspect container-id
docker images


#For testing the Application on local system
chmod +x rest_client.sh
sh rest_client.sh

Python Src files:
app.py & parse.py



