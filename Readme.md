Python service with flask.

First run mongo's docker-compose
```sh
docker build --rm -f "Dockerfile" -t back-app-wall:latest .
```

and then 
```sh
docker-compose up
or
docker run --rm -it -p 5000:5000/tcp back-app-wall:latest
```
