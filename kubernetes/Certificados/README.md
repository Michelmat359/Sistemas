En éste caso vamos a utilizar nuestra propia CA dentro del cluster. En este caso vamos a utilizar OPENSSL.

El primer paso es la generación del certificado de la propia CA.

Generación de claves para el Cluster de Kubernetes:     
```
openssl genrsa -out ca.key 2048 
```

Creación del CSR o Certificate Signing Request, utilizando la llave creada anteriormente:
```
openssl req -new -key ca.key -subj “/CN=Kubernetes-CA” -out ca.csr
```
Finalmente firmamos el certificado nosotros mismos dado que es una CA interna para la emisión de los certificados del clúster, por lo que utilizaremos la key generada en el primer paso para firmar el certificado raíz:
```
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt
```
A partir de aquí, utilizaremos este par de llaves para firmar los certificados del resto de los servicios del clúster.

Vamos a generar y firmar el certificado cliente para el usuario Michelmat359.     
```
openssl genrsa -out Michelmat359.key 2048
```
Finalmente firmamos el certificado, para obtener un certificado válido en el clúster:
```
openssl x509 -req -in admin.csr -signkey ca.key -out Michelmat359.crt 
```
Debemos especificar el "nivel" de privilegios del usuario cuando se genera el certificado, con el objetivo de diferenciar el usuario Michelmat359 del resto. Para ello podemos incluir la pertenencia al grupo SYSTEM:MASTERS, especificando CN=kube-Michelmat359/O=system:masters.

De ésta forma, nuestro usuario ya puedrá hacer consultas seguras:
```
curl https://kubernetes-API:6443/api/v1/pods --key admin.key –cert Michelmat359.crt –cacert ca.crt 
```
