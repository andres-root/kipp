import argparse

import uvicorn

from app.adapters.output.db.db import migrate, reset

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start FastAPI server with custom host and port")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host address")
    parser.add_argument("--port", type=int, default=8000, help="Port number")
    parser.add_argument("--migrate", action="store_true", help="Run migrations")
    parser.add_argument("--reset", action="store_true", help="Reset database")
    parser.add_argument(
        "--env", type=str, choices=["prod", "staging", "develop"], default="develop", help="Environment mode"
    )
    parser.usage = "Usage: %(prog)s [--host] [--port] [--env {prod,staging,develop}]"

    args = parser.parse_args()

    if args.migrate:
        migrate()
    elif args.reset:
        reset()

    if args.env == "prod" or args.env == "staging":
        uvicorn.run(
            "main:app",
            host=args.host,
            port=args.port,
            workers=4,
            reload=False,
            access_log=True,
            log_level="info",
            proxy_headers=True,
            forwarded_allow_ips="*",
        )
    else:
        uvicorn.run("main:app", host=args.host, port=args.port, reload=True)
