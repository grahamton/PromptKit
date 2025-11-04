import pathlib
import sys

from fastapi.testclient import TestClient

# Ensure repo root (where `webapp/` lives) is importable
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from webapp.main import app  # noqa: E402


def test_run_returns_fragment_when_hx_request_header_present():
    with TestClient(app) as client:
        r = client.post(
            "/run",
            headers={"HX-Request": "true"},
            data={
                "seed": "s",
                "friction": "confirm loop",
                "mode": "iterate",
                "ascii_only": "true",
            },
        )
        assert r.status_code == 200
        # Should return only the output fragment, not a full page shell
        assert "<!DOCTYPE html>" not in r.text
        assert "Prompt patch" in r.text or "Iterate Card" in r.text


def test_run_full_page_without_hx_request_header():
    with TestClient(app) as client:
        r = client.post(
            "/run",
            data={
                "seed": "s",
                "friction": "confirm loop",
                "mode": "iterate",
                "ascii_only": "true",
            },
        )
        assert r.status_code == 200
        assert "<!DOCTYPE html>" in r.text
