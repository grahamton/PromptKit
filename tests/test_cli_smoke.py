from typer.testing import CliRunner

from promptkit.cli import app


runner = CliRunner()


def test_help_commands():
    res_main = runner.invoke(app, ["--help"])
    assert res_main.exit_code == 0

    for cmd in ("iterate", "plan", "ticket"):
        res = runner.invoke(app, [cmd, "--help"])
        assert res.exit_code == 0


def test_plan_command_runs():
    res = runner.invoke(
        app,
        [
            "plan",
            "--seed",
            "demo seed",
            "--friction",
            "demo friction",
            "--ascii",
        ],
    )
    assert res.exit_code == 0
    assert "Context" in res.stdout
    assert "Flow" in res.stdout


def test_ticket_command_runs():
    res = runner.invoke(
        app,
        [
            "ticket",
            "--seed",
            "demo seed",
            "--friction",
            "demo friction",
            "--ascii",
        ],
    )
    assert res.exit_code == 0
    assert "Client:" in res.stdout
    assert "Prompt Brief:" in res.stdout


def test_iterate_command_runs():
    res = runner.invoke(
        app,
        [
            "iterate",
            "--seed",
            "demo seed",
            "--friction",
            "demo friction",
            "--ascii",
        ],
    )
    assert res.exit_code == 0
    assert "Iterate Card" in res.stdout
