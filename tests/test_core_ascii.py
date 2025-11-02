from promptkit.plan import build_plan_text
from promptkit.ticket import build_ticket_text


def test_build_plan_text_ascii():
    out = build_plan_text(seed="s", friction="f", ascii_only=True)
    assert isinstance(out, str)
    assert "Context" in out


def test_build_ticket_text_ascii():
    out = build_ticket_text(seed="s", friction="f", ascii_only=True)
    assert isinstance(out, str)
    assert "Success Criteria:" in out

