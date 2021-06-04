# Pasos para instalar Kubernetes
## Requisitos previos
* Sistema operativo con Docker instalado

## Comentarios
1. La instalación que realizo es una distribución de Kubernetes llamada K3s. Esta distribución es mucho mas liviana y consume menos recursos, por lo que para laboratorios o equipos de testeo es más adecuado. 

2. A continuación instalamos Helm, que es una herramienta para gestionar paquetes Kubernetes. Los paquietes se denominan charts. Estos son una colección de ficheros que describen los recursos de API de kubernetes. Para facilitar el desarrollo de estos archivos, instalamos Kompose.

3. Kompose es una herramienta que permite de forma automatica generar los charts a partir de un docker-compose. Es una herramienta muy potente que permite facilitar la migración de ficheros distributables docker a kubernetes


### Instalar componentes de Kubernetes
#### K3S
```
    
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644 --node-ip {YOUR-IP} --node-external {YOUR-IP}
# ejemplo: 
curl -sfL https://get.k3s.io | sh -s - --write-kubeconfig-mode 644 --node-ip 192.168.1.50 --node-external-ip 192.168.1.50

sudo chmod 644 /etc/rancher/k3s/k3s.yaml


```

Comprueba que está correctamente instalado
```
kubectl version
kubectl get nodes
kubectl cluster-info
```

#### Helm
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```
Comprueba que está correctamente instalado
```
helm version
helm ls
```

#### Kompose
```
curl -L https://github.com/kubernetes/kompose/releases/download/v1.22.0/kompose-linux-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```
Comprueba que está correctamente instalado
```
kompose version
```

