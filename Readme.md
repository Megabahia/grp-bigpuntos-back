## Synopsis
Proyecto de sistema de recompensas de supermonedas, para personas autonomas, empresas financieras y comerciales.


# teach Stack
Framework Django Rest Framework

## Set Up Local Workspace

Version de python 3.8.5

Instalar paquetes
```shell
pip install -r requirements.txt
```

Run
```shell
python manage.py runserver
```

# Como utilizar este repositorio en Ambiente DEV con Docker

## Pasos previos
cambiar en el archivo config que variable de entorno compilar

## 1.Construir la imagen para windows y otro para mac
```shell
sudo docker build -t james46007/grp-backend:dev .
```
El siguiente comando sirve para computadoras mac
```shell
docker buildx build --platform linux/amd64 -t james46007/grp-backend:dev .
```

## 2.Subir la imagen al Docker Hub (ejecutar "docker login" en caso de no estar logueado desde consola en dockerhub)
```shell
sudo docker push james46007/grp-backend:dev
```

## 3.En el servidor debe estar instalado y configurado Docker
## 4.Bajar la imagen del docker a deployar en el servidor que se desea ejectuar
```shell
sudo docker pull james46007/grp-backend:dev
```

## 5. Detener la imagen que vamos a deployar
```shell
sudo docker stop grp-backend
```

## 6. Borrar la imagen que vamos a deployar
```shell
sudo docker rm grp-backend
```

## 7.Construir el contenedor , este comando deja corriebdo el contenedor
```shell
sudo docker run -d -p 8000:8000 -it --log-opt max-size=10m --log-opt max-file=3 --name grp-backend --restart always james46007/grp-backend:dev
```

## 6.Para iniciar el contenedor
```shell
sudo docker start grp-backend
```
