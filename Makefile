compose:
	docker-compose up -d

build:
	docker build -t identicons .

run:
	docker run -d --name dnmonster amouat/dnmonster:latest
	docker run -d --name redis redis
	docker run -p 5000:5000 -e "ENV=dev" --link dnmonster:dnmonster --link redis:redis identicons

tests:
	docker run -e ENV=test identicons
