import uvicorn

from src.web import web_app_factory

if __name__ == "__main__":
    config = uvicorn.Config(web_app_factory(), port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
