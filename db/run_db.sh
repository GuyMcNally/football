IMAGE_NAME="postgres_football"
docker build -t $IMAGE_NAME .
docker-compose up -d
docker exec -it $IMAGE_NAME bash
# docker container stop $IMAGE_NAME && docker container rm $IMAGE_NAME && docker image rm $IMAGE_NAME
