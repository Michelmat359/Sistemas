FROM ubuntu:latest

# Install dependencies and rancher
RUN apt update -y && \
    apt install curl wget -y

# Install rancher
RUN wget -O rancher-cli.tar.gz $(curl -s https://api.github.com/repos/rancher/cli/releases/latest | grep browser_download_url | grep 'linux-amd64' | head -n 1 | cut -d '"' -f 4) && \
    tar -xzvf rancher-cli.tar.gz -C /usr/local/bin --strip-components=2

# Login rancher
# echo y | rancher login $URL_RANCHER --token &TOKEN_URL_RANCHER
RUN echo "y" | rancher login https://example.es --token token-XXXXXXXXXXXXXXXXXXXX

# Change version
RUN rancher app upgrade XXXXXXXXXXXXXXXXXXXXXX 1.0.0
# rancher app upgrade $NombreAPP $Version




