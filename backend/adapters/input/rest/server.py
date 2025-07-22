import uvicorn


def start_fastapi_server(host: str = "127.0.0.1", port: int = 8000, reload=False):
    uvicorn.run("routes:app", host=host, port=port, reload=reload)
