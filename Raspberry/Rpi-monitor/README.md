# RPI-Monitor
RPi-Monitor monitoriza tu Raspberry Pi mediante un servicio http en el puerto 8888. Podrás ver las siguientes características:
- Versión: Instalada y si está actualizada.
- Tiempo de actividad: El reloj actual de la Raspberry Pi y cuánto tiempo lleva funcionando.
- CPU: Carga y configuración de la CPU.
- Temperatura: Temperatura actual de la CPU.
- Memoria: Cantidad de memoria disponible
- Swap: Uso de Swap
- Tarjeta SD: Uso del disco para el arranque de la partición y la raíz
- Red: Volumen de datos intercambiados en la red

## Pasos para levantar el rpi-monitor
```
docker-compose up -d
```
URL: https://localhost:8888