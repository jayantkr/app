# app
python App

docker build --no-cache --rm -t travcunn/flask .
docker run -d -p 5000:8000 travcunn/flask
docker rmi -f container-id

chmod +x rest_client.sh
sh rest_client.sh




