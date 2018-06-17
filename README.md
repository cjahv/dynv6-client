# starze/dynv6-client
starze/dynv6-client is a client for [dynv6.com](https://dynv6.com/)

Supports x86 and arm based devices (i.e. raspberry pi).

# Start container
## x86
```bash
$ docker run --network=host --rm starze/dynv6-client:latest --token=<your-token> --interface=eth0 [--no-ipv4] [--no-ipv6] example.dynv6.net
```

## arm
```bash
$ docker run --network=host --rm starze/arm32v7-dynv6-client:latest --token=<your-token> --interface=eth0 [--no-ipv4] [--no-ipv6] example.dynv6.net
```

# Build container
## x86
```bash
$ docker build -t dynv6-client .
```

## arm
```bash
$ docker build -t arm32v7-dynv6-client -f Dockerfile.arm32v7 .
```
## docker-compose file example
```
version: '2'

services:
  dynv6-client:
    image: starze/dynv6-client
    restart: unless-stopped
    container_name: dynv6-client
    network_mode: host
    command: --token=<your-dynv6-token> --interface=eth0 your-host.dynv6.net
```


# Dockerfile and Code
https://github.com/starze/dynv6-client



Special thanks to https://github.com/ticosax/dynv6-client for making this possible!
