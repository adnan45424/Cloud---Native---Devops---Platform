from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="platform-api", version="0.1.0")

@app.get("/")
def root():
    return {"message": "platform-api up"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"status": "ready"}

Instrumentator().instrument(app).expose(app, endpoint="/metrics")
