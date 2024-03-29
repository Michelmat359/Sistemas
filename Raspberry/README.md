# Pasos para instalar Docker en una Raspberry PI 4 con raspbian

### 1. Descargar e instalar raspbian en  SD
   * Descargar https://downloads.raspberrypi.org/raspbian_lite_latest
   * Descargar e instalar Etcher (para instalar en la SD) https://etcher.io/
   * Instalar imagen en la SD
   * También podeis bajaros el instalador oficial de Raspberry PI para windows. https://downloads.raspberrypi.org/imager/imager_latest.exe
  
### 2. Una vez que raspbian está instalado:
   * Cambiar password de usuario Pi (recomendado)

### 3. Instalar paquetes necesarios

```
sudo apt-get update && sudo apt-get install -y \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg2 \
     software-properties-common \
     nano \
     fail2ban \
     ntfs-3g
```

### 4. Instalar firmas GPG del repo de Docker

```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
```


### 5. Instalar Docker

```
curl -sSL https://get.docker.com | sh
sudo apt-get update && sudo apt-get install -y --no-install-recommends docker-compose
```

### 6. Agregar usuario al grupo docker y desloguearse y volverse a loguear

```
sudo usermod -a -G docker <usuario>
#(logout and login)
```

Con todo esto ya tendremos preparado nuestro entorno de docker dentro de una Raspberry PI 4

# Instalar Docker-compose:

# Instalar docker-compose version 2
La instalación de docker-compose utilizando el gestor de paquetes apt fallará ya que la arquitectura arm de Raspberry Pi no es actualmente compatible.
Si te sientes valiente y tratas de usar apt-get, lo más probable es que termines con el siguiente error cuando intentes ejecutar docker-compose: 
```
/usr/local/bin/docker-compose: line 1: Not: command not found
```
Lo instalaremos por medio de pip3:
```
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo pip3 -v install docker-compose
```
## Test
```
    docker-compose version
```
