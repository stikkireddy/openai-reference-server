from fastapi.openapi.utils import get_openapi
from server import app
import json
from pathlib import Path

openapi_dir = Path(__file__).parent.parent / "openapi"

openapi_dir.mkdir(parents=True, exist_ok=True)

openapi_file = openapi_dir / "openapi.json"

with openapi_file.open("w") as f:
    json.dump(get_openapi(
        title="OpenAI API Reference Server",
        version="0.1.0",
        description="This is an API reference server that mimics openai server.",
        routes=app.routes,
    ), f, indent=4)