import pathlib
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from webapp.main import app  # noqa: E402


def test_pages_render_ok():
    with TestClient(app) as client:
        for path in ("/", "/modes", "/research"):
            r = client.get(path)
            assert r.status_code == 200
            assert "<!DOCTYPE html>" in r.text


def test_index_has_htmx_and_compare_flag():
    with TestClient(app) as client:
        r = client.get("/")
        assert r.status_code == 200
        assert "/static/htmx.min.js" in r.text

        r2 = client.get("/?flags=compare")
        assert r2.status_code == 200
        # compare row should not be hidden when flag is on
        # presence without display:none indicates enabled
        assert 'id="compare-row"' in r2.text
        assert 'id="compare-row" style="display:none"' not in r2.text


def test_run_iterate_post_renders_output():
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
        assert "- Prompt patch (drop-in)" in r.text or "Iterate Card" in r.text
