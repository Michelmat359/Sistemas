# Pasos para instalar Docker en una Raspberry PI 4 con raspbian

### 1. Descargar e instalar raspbian en  SD
   * Descargar https://downloads.raspberrypi.org/raspbian_lite_latest
   * Descargar e instalar Etcher (para instalar en la SD) https://etcher.io/
   * Instalar imagen en la SD
  
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
     vim \
     fail2ban \
     ntfs-3g
```

### 4. Instalar firmas GPG del repo de Docker

```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
```

### 5. Agregar repo de Docker

```
echo "deb [arch=armhf] https://download.docker.com/linux/debian \
     $(lsb_release -cs) stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list
    
NOTA: las versiones de docker mayores a 18.06 estan presentando problemas sobre raspbian. Si encuentran problemas de "Segmentation fault" o que el demonio no inicia, pueden evitar que versiones superiores se instalen de la siguiente forma

echo "Package: docker-ce
Pin: version 18.06.1*
Pin-Priority: 1000" > /etc/apt/preferences.d/docker-ce
```

### 6. Instalar Docker

```
sudo apt-get update && sudo apt-get install -y --no-install-recommends docker-ce docker-compose
```

### 7. Agregar usuario al grupo docker y desloguearse y volverse a loguear

```
sudo usermod -a -G docker <usuario>
#(logout and login)
```

Con todo esto ya tendremos preparado nuestro entorno de docker dentro de una Raspberry PI 4
