# Entorno MLOps

Este directorio contiene un entorno básico para pruebas de MLOps utilizando Docker Compose.
Incluye los siguientes servicios:

* **PostgreSQL**: base de datos para MLflow.
* **MinIO**: almacén de artefactos compatible con S3.
* **MLflow**: servidor de seguimiento de experimentos.
* **Jupyter Notebook**: entorno interactivo para el desarrollo.

## Requisitos

Necesitas tener instalados Docker y Docker Compose en tu sistema. Consulta la carpeta `docker` de este repositorio para instrucciones de instalación.

## Puesta en marcha

1. Entra en la carpeta `MLOps`.
2. Ejecuta `docker-compose up` para iniciar todos los servicios.
3. Accede a los servicios a través de los puertos indicados más abajo.

## Servicios disponibles

* **MLflow** – [http://localhost:5000](http://localhost:5000)
* **Jupyter Notebook** – [http://localhost:8888](http://localhost:8888) (token "mlops")
* **MinIO** – [http://localhost:9001](http://localhost:9001) (usuario "minio", password "minio123")

Los datos se almacenan en volúmenes Docker para que no se pierdan entre reinicios.

## Parar el entorno

Con `Ctrl+C` se detendrán los servicios en primer plano. También puedes ejecutar `docker-compose down`.

