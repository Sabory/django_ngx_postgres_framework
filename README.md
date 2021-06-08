## Installation

For setting virtual environment variables:
```
source ./.env
```
Docker compose setting

```
docker-compose build
docker-compose up
```
You would be able to access

[localhost:8008](http://localhost:8008/)

Create super user
```
docker exec -it hub_integraciones_django python manage.py createsuperuser
```
Reload statics
```
docker exec -it hub_integraciones_django python manage.py collectstatic
```

## Usage
stop the container
```
docker-compose down
```
django shell
```
docker exec -it hub_integraciones_django python manage.py shell
```
