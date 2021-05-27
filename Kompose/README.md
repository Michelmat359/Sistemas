## Kompose:

Download
```
curl -L https://github.com/kubernetes/kompose/releases/download/v1.22.0/kompose-linux-amd64 -o kompose
```
Permisos
```
chmod +x kompose
```
Mueve el fichero a bin
```
sudo mv ./kompose /usr/local/bin/kompose
```

Test
```
 kompose version
```

# Convertir un docker-compose a helm chart

Dirigete a la carpeta donde tengas tu archivo docker-compose.yml y lanza la siguiente linea:

```
kompose convert -f docker-compose.yml -c --replicas=1
```
