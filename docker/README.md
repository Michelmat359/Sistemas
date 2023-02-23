# Instalar Docker:

## Desinstalar versiones antiguas
```
    sudo apt-get remove docker docker-engine docker.io containerd runc    
```
## Actualizar el índice de paquetes apt e instalar paquetes para permitir que apt utilice un repositorio a través de HTTPS
```
    sudo apt-get update
```
## Instalar paquetes y dependencias
```
    sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```
## Añade la clave GPG oficial de Docker:
```
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
## Configurar el repositorio estable
```
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```
## Instalar docker engine
```
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
```
## Docker como usuario no root
```
    # Usage
    sudo usermod -aG docker {USERNAME}
```
*Reboot system*

## Test 
```
    docker version
    docker ps
```

# Instalar Docker-compose:

## Instalar docker-compose    
```    
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
## Permisos
```
    sudo chmod +x /usr/local/bin/docker-compose
```
## Test
```
    docker-compose version
```
