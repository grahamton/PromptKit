import pathlib
import sys

from fastapi.testclient import TestClient

# Ensure repo root (where `webapp/` lives) is importable
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from webapp.main import app


def test_health_endpoint_ok():
    with TestClient(app) as client:
        r = client.get("/health")
        assert r.status_code == 200
        assert r.text == "ok"


def test_download_json_endpoint_ok():
    with TestClient(app) as client:
        r = client.post(
            "/download/json",
            data={
                "filename": "session.json",
                "content": '{"a": 1}',
            },
        )
        assert r.status_code == 200
        assert r.headers.get("content-type", "").startswith("application/json")
        assert "\n" in r.text  # pretty-printed
        assert '"a": 1' in r.text
