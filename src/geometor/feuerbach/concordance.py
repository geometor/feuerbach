"""Structured loader and validator for the Euler–Feuerbach concordance and source manifest."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

__all__ = [
    "ConcordanceEntry",
    "default_resources_dir",
    "load_concordance",
    "load_sources_manifest",
]


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single cross-treatise concordance mapping linking Euler, Feuerbach, ETC, and Euclid."""

    entry_id: str
    title: str
    category: str
    euler_1765_ref: str
    feuerbach_1822_ref: str
    etc_centers: tuple[str, ...]
    sister_refs: dict[str, str]
    symbolic_identity: str
    heronian_value: str


def default_resources_dir() -> Path:
    """Locate ``resources/feuerbach`` relative to the repository checkout."""
    here = Path(__file__).resolve()
    repo_root = here.parents[3]
    return repo_root / "resources" / "feuerbach"


def load_concordance(path: Path | str | None = None) -> list[ConcordanceEntry]:
    """Load and validate ``resources/feuerbach/concordance.json``.

    Args:
        path: Optional explicit JSON file path.

    Returns:
        Ordered list of :class:`ConcordanceEntry` records.
    """
    target = Path(path) if path is not None else default_resources_dir() / "concordance.json"
    raw = json.loads(target.read_text(encoding="utf-8"))
    entries: list[ConcordanceEntry] = []
    for item in raw.get("entries", []):
        entries.append(
            ConcordanceEntry(
                entry_id=str(item["id"]),
                title=str(item["title"]),
                category=str(item["category"]),
                euler_1765_ref=str(item.get("euler_1765", "")),
                feuerbach_1822_ref=str(item.get("feuerbach_1822", "")),
                etc_centers=tuple(str(x) for x in item.get("etc_centers", [])),
                sister_refs={str(k): str(v) for k, v in item.get("sister_refs", {}).items()},
                symbolic_identity=str(item.get("symbolic_identity", "")),
                heronian_value=str(item.get("heronian_value", "")),
            )
        )
    return entries


def load_sources_manifest(path: Path | str | None = None) -> dict[str, Any]:
    """Load ``resources/feuerbach/sources_manifest.json``."""
    target = (
        Path(path) if path is not None else default_resources_dir() / "sources_manifest.json"
    )
    return dict(json.loads(target.read_text(encoding="utf-8")))
