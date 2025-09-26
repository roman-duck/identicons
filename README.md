# IdentiIcons with Docker

Run:
```bash
docker-compose up -d
```

In docker details:
```bash
docker run -d --name dnmonster amouat/dnmonster:latest
docker run -d --name redis redis
docker build -t identidock .
docker run -p 5000:5000 -e "ENV=dev" --link dnmonster:dnmonster --link redis:redis identidock
```