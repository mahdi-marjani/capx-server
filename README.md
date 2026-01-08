# capx-server

AI backend service for capx.

## Run
```bash
git clone https://github.com/mahdi-marjani/capx-server.git
cd capx-server
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
````

## API

GET /models

Response:

```json
{
    "models": [
        "bicycle",
        "bus",
        "tractor",
        "boat",
        "car",
        "..."
    ]
}
```

---

POST /detect

Request:

```json
{
  "image": "<base64>",
  "grid": "3x3",
  "target": "cars"
}
```

Response:

```json
{
  "cells": [1, 3, 7]
}
```

---

Doc:

```bash
http://localhost:8000/docs
```
