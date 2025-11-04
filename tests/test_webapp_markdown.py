import pathlib
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from webapp.main import app  # noqa: E402


def test_output_renders_markdown_container():
    with TestClient(app) as client:
        r = client.post(
            "/run",
            data={
                "seed": "s",
                "friction": "bias and coverage issues",
                "mode": "iterate",
                "pattern": "forced-diversification",
                "ascii_only": "true",
            },
        )
        assert r.status_code == 200
        # Ensures the markdown filter is used to render text output
        assert '<div class="md">' in r.text
