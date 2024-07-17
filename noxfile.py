import os
import tempfile

import nox

PYTHON_MODULES = ["py_godel_numbers", "tests", "noxfile.py"]


@nox.session  # type: ignore[misc]
def format(session: nox.Session) -> None:
    install_poetry_groups(session, "--with=format")
    # Format files locally with ruff, but only check in cicd
    if "CI" in os.environ:
        session.run("ruff", "check")
        session.run("ruff", "format", "--check")
    else:
        session.run("ruff", "check", "--fix")
        session.run("ruff", "format")


@nox.session  # type: ignore[misc]
def types(session: nox.Session) -> None:
    install_poetry_groups(session, "--with=dev", "--with=types")
    session.run(
        "mypy",
        "--install-types",
        "--non-interactive",
        "--show-error-codes",
        *PYTHON_MODULES,
    )


@nox.session  # type: ignore[misc]
def tests(session: nox.Session) -> None:
    install_poetry_groups(session, "--with=tests")
    session.run("pytest", env={"PYTHONPATH": "."})


def install_poetry_groups(session: nox.Session, *args: str) -> None:
    """Install dependencies from poetry groups.
    Copied from:
    https://github.com/cjolowicz/nox-poetry/issues/663#issuecomment-1429916978
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            *args,
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("--quiet", "-r", requirements.name)
