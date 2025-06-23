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


## Experimentos de ejemplo

En el directorio `experiments/` se incluyen tres scripts listos para ejecutarse y registrar sus resultados en MLflow:

1. **time_series_lstm.py** – Red LSTM de tres capas con 128 unidades cada una.
2. **image_cnn_resnet18.py** – Clasificador de imágenes basado en ResNet‑18.
3. **tabular_xgboost.py** – Modelo XGBoost con 100 árboles y profundidad máxima de 6.

### Requisitos adicionales

Dentro del contenedor de Jupyter instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### Cómo ejecutarlos

1. Inicia los servicios con `docker-compose up`.
2. Abre Jupyter en [http://localhost:8888](http://localhost:8888) usando el token `mlops` o abre un terminal dentro del contenedor `jupyter`.
3. Ejecuta cada script desde el directorio `MLOps`:

```bash
python experiments/time_series_lstm.py
python experiments/image_cnn_resnet18.py
python experiments/tabular_xgboost.py
```

Los scripts ya establecen la URL de seguimiento `http://mlflow:5000`, por lo que los resultados se registrarán automáticamente en el servidor MLflow incluido en el compose.

### Interpretación de resultados

Accede a [http://localhost:5000](http://localhost:5000) para ver la interfaz de MLflow. Allí podrás comparar las ejecuciones, revisar métricas como `loss`, `mae` o `accuracy` y descargar los modelos guardados en la pestaña *Artifacts*.
