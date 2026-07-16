"""Regression checks for claim-promotion governance."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _claim_rows(markdown: str) -> list[tuple[str, str, str]]:
    rows = []
    for line in markdown.splitlines():
        if not line.startswith("| P5-CL-"):
            continue
        columns = [column.strip() for column in line.strip("|").split("|")]
        rows.append((columns[0], columns[2], columns[4]))
    return rows


def _gate_ids(gate_cell: str) -> list[str]:
    gate_ids = []
    for token in re.findall(r"P5-[A-Z0-9-]+(?:/[0-9]+)*", gate_cell):
        first, *suffixes = token.split("/")
        gate_ids.append(first)
        prefix = first.rsplit("-", 1)[0]
        gate_ids.extend(f"{prefix}-{suffix}" for suffix in suffixes)
    return gate_ids


def _gate_sections(markdown: str) -> dict[str, str]:
    headings = list(re.finditer(r"^## (P5-[A-Z0-9-]+) ", markdown, re.MULTILINE))
    sections = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        sections[heading.group(1)] = markdown[heading.start() : end]
    return sections


def _field(section: str, heading: str) -> str | None:
    match = re.search(
        rf"^### {re.escape(heading)}\s*$\s*^([^#\n].*)$",
        section,
        re.MULTILINE,
    )
    return match.group(1).strip() if match else None


def _governance_violations(claims: str, gates: str) -> list[str]:
    sections = _gate_sections(gates)
    violations = []
    for claim_id, status, gate_cell in _claim_rows(claims):
        if status != "VERIFIED":
            continue
        for gate_id in _gate_ids(gate_cell):
            section = sections.get(gate_id, "")
            reviewer = _field(section, "Independent reviewer verdict")
            pi_acceptance = _field(section, "PI acceptance")
            if reviewer == "PENDING" or pi_acceptance == "PENDING":
                violations.append(f"{claim_id} is VERIFIED while {gate_id} review is pending")
    return violations


def test_no_verified_claim_has_pending_review() -> None:
    claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    assert _governance_violations(claims, gates) == []


def test_pending_gate_blocks_verified_claim() -> None:
    claims = """| Claim ID | Claim | Status | Evidence | Gate | Section | Reviewed |
|---|---|---|---|---|---|---|
| P5-CL-999 | Example | VERIFIED | Evidence | P5-TEST-01 | N/A | 2026-07-15 |
"""
    gates = """## P5-TEST-01 — Example gate

Status: PASS

### Independent reviewer verdict

PENDING

### PI acceptance

PENDING
"""
    assert _governance_violations(claims, gates) == [
        "P5-CL-999 is VERIFIED while P5-TEST-01 review is pending"
    ]
