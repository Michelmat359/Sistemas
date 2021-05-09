En éste caso vamos a utilizar nuestra propia CA dentro del cluster. Hay varias opciones o herramientas disponibles para la generación de certificados, como son: EASYRSA, CFSSL, OPENSSL, etc. En este caso vamos a utilizar OPENSSL.

El primer paso es la generación del certificado de la propia CA.

Generación de claves para la CA:     
```
openssl genrsa -out ca.key 2048    #obtenemos el fichero ca.key 
```

Creación del CSR o Certificate Signing Request, utilizando la llave creada anteriormente:
```
openssl req -new -key ca.key -subj “/CN=Kubernetes-CA” -out ca.csr     #obtenemos el fichero ca.csr
```
Finalmente firmamos el certificado nosotros mismos dado que es una CA interna para la emisión de los certificados del clúster, por lo que utilizaremos la key generada en el primer paso para firmar el certificado raíz:
```
openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt    #obtenemos el certificado firmado ca.crt
```
A partir de aquí, utilizaremos este par de llaves para firmar los certificados del resto de los servicios del clúster.

Como ejemplo, vamos a generar y firmar el certificado cliente para el usuario Admin. Generación de claves para el usuario Admin:     
```
openssl genrsa -out admin.key 2048    #obtenemos el fichero admin.key 
```
Finalmente firmamos el certificado, para obtener un certificado válido en el clúster:
```
openssl x509 -req -in admin.csr -signkey ca.key -out admin.crt   #obtenemos el certificado firmado admin.crt
```
En éste punto mencionar la necesidad de especificar el “nivel” de privilegios del usuario cuando se genera el certificado, con el objetivo de diferenciar el usuario administrador del resto. Para ello podemos incluir la pertenencia al grupo SYSTEM:MASTERS, especificando CN=kube-admin/O=system:masters.

De ésta forma, el usuario ya puede hacer consultas seguras vía REST API:
```
curl https://kube-apiserver:6443/api/v1/pods --key admin.key –cert admin.crt –cacert ca.crt 
```