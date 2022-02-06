# alertmanager-gotify-gateway

Gateway to send alerts to gotify via the webhook integration from alertmanager

## Docker Compose

First copy the .env.example file to .env in your compose directory and edit it.

```yaml
version: "3"
services:
  app:
    build: alertmanager-gotify-gateway
    restart: always
    ports:
      - 2782:5000
    env_file: .env
```
