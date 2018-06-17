# dynv6

## description
Dynv6-client is a client for [dynv6](https://dynv6.com/)

Supports x86 and arm based devices (i.e. raspberry pi).

## start x86 container
```bash
$ docker run --network=host --rm starze/dynv6-client:latest --token=<your-token> --interface=eth0 [--no-ipv4] [--no-ipv6] example.dynv6.net
```

## start arm container
```bash
$ docker run --network=host --rm starze/arm32v7-dynv6-client:latest --token=<your-token> --interface=eth0 [--no-ipv4] [--no-ipv6] example.dynv6.net
```

## build x86 container
```bash
$ docker build -t dynv6-client .
```

## build arm container
```bash
$ docker build -t arm32v7-dynv6-client -f Dockerfile.arm32v7 .
```

# Dockerfile and Code
https://github.com/starze/dynv6-client



Special thanks to https://github.com/ticosax/dynv6-client for making this possible!
