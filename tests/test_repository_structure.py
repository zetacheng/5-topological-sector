from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_TOP_LEVEL_FILES = {
    ".gitignore",
    "AGENTS.md",
    "CITATION.cff",
    "CLAIMS.md",
    "CONVENTIONS.md",
    "DECISION_LOG.md",
    "GATES.md",
    "HANDOFF.md",
    "LICENSE",
    "Makefile",
    "PROGRESS.md",
    "README.md",
    "ROADMAP.md",
    "pyproject.toml",
}

REQUIRED_DIRECTORIES = {
    ".github",
    "archive",
    "derivations",
    "docs",
    "paper",
    "results",
    "reviews",
    "scripts",
    "tests",
}


def test_required_top_level_files_exist() -> None:
    missing = sorted(name for name in REQUIRED_TOP_LEVEL_FILES if not (ROOT / name).is_file())
    assert not missing, f"Missing required top-level files: {missing}"


def test_required_top_level_directories_exist() -> None:
    missing = sorted(name for name in REQUIRED_DIRECTORIES if not (ROOT / name).is_dir())
    assert not missing, f"Missing required top-level directories: {missing}"
