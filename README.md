[![Docker Image CI](https://github.com/sth-v/cxm_backend_server/actions/workflows/docker-image.yml/badge.svg)](https://github.com/sth-v/cxm_backend_server/actions/workflows/docker-image.yml)

# Cxm Backend Server
---

Minimal backend for model applications.\
Use for cxm viewer basic connection.

Can be temaplate.

Playground: https://mmodel.contextmachine.online:8181/docs

## Package

https://github.com/orgs/contextmachine/packages/container/cxm_backend_server/settings

## Install

### Docker

Pull container:

```bash
docker pull ghcr.io/contextmachine/cxm_backend_server:sha256-a9f320ddc47d8ec47401b7ba36d05352a5929bebf547bbd8a86a28e1caae1dd0.sig
```

Build & run image:

```bash
docker build -t https-latest . && docker run -p 0.0.0.0:443:443 -v cxm_backend/share:/code/share --name cxm_backend_server-latest 
```