from promptkit.cards import make_iterate_card


def test_auto_selects_forced_diversification_on_bias_cues():
    seed = "Agent recommends keycap sets"
    friction = "Over-index on keyboards; needs diverse coverage beyond feed bias"
    card = make_iterate_card(seed, friction, ascii_only=True, pattern="auto")
    assert isinstance(card.id, str)
    assert "Diversification" in card.id or any(
        "Balanced Option" in p or "Novelty Option" in p for p in card.prompt_patch
    )


def test_auto_can_combine_when_multiple_cues_present():
    seed = "Assistant planning recipes"
    friction = (
        "Ambiguous adjectives and missing recap; "
        "needs either/or clarifier and constraint ledger"
    )
    card = make_iterate_card(seed, friction, ascii_only=True, pattern="auto")
    assert "Combined:" in card.id or (
        any("ledger" in p.lower() for p in card.prompt_patch)
        and any("either" in p.lower() or "contrast" in p.lower() for p in card.prompt_patch)
    )
