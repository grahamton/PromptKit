from promptkit.plan import build_plan_text
from promptkit.ticket import build_ticket_text
from promptkit.cards import make_iterate_card


def test_plan_ascii_snapshot_minimal():
    out = build_plan_text(seed="s", friction="f", ascii_only=True)
    assert out.startswith("Context\n")
    assert "Reasoning Path" in out
    assert out.endswith("\n")


def test_ticket_ascii_snapshot_minimal():
    out = build_ticket_text(seed="s", friction="f", ascii_only=True)
    assert "Success Criteria:" in out
    assert "Echo captured constraints" in out


def test_iterate_ascii_snapshot_minimal():
    card = make_iterate_card(seed="s", friction="confirm loop", ascii_only=True)
    out = card.render_text()
    assert out.startswith("Iterate Card")
    assert "- Prompt patch (drop-in)" in out
    assert "- Where to place in your prompt" in out

