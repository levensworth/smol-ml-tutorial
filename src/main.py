from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse


def main() -> FastAPI:
    """Main loop for this application.
    Set up process for fastapi Server.

    Returns:
        FastAPI: Instance of a running server.
    """
    api = FastAPI()
    api.add_route("/", route=serve_docs, methods=["GET"], name="Redirect to /docs")
    api.add_route("/ping", route=heartbeat, methods=["GET"], name="heart beat")
    return api


async def serve_docs(request: Request) -> RedirectResponse:
    """
    Redirect to /docs
    """
    return RedirectResponse(url="/docs")


async def heartbeat(request: Request) -> str:
    """
    returns Pong
    """
    return "PONG"


app = main()
