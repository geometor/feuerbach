"""Sphinx configuration for the GEOMETOR Euler–Feuerbach Bilingual Book Codex."""

from __future__ import annotations

import os
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / "explorer" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.feuerbach as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "feuerbach"
repo_name = "feuerbach"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • feuerbach"
author = "Leonhard Euler & Karl Wilhelm Feuerbach • Digital Edition GEOMETOR"
copyright = "1767 Petropoli, 1822 Nürnberg • Digital Edition GEOMETOR"

html_logo = None
autoapi_add_toctree_entry = False
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

# Register locally built sister GEOMETOR inventories when present on disk
_base_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
for _sister in (
    "euclid",
    "elements",
    "etc",
    "altshiller-court",
    "pappus",
    "wildberger",
    "model",
    "ceva",
    "menelaus",
):
    _inv = os.path.abspath(os.path.join(_base_root, "..", _sister, "docs", "objects.inv"))
    if os.path.isfile(_inv):
        intersphinx_mapping[_sister] = (  # noqa: F405
            f"https://geometor.github.io/{_sister}",
            (_inv, None),
        )

# Exclude top-level AutoAPI index included directly inside docsrc/modules/index.rst
_pkg_api_index = "modules/api/geometor/feuerbach/index.rst"
if _pkg_api_index not in exclude_patterns:  # noqa: F405
    exclude_patterns.append(_pkg_api_index)  # noqa: F405

# Retain only locally cached intersphinx inventories so offline builds emit zero network warnings
intersphinx_mapping = {
    name: target
    for name, target in intersphinx_mapping.items()  # noqa: F405
    if isinstance(target, tuple) and len(target) == 2 and target[1] is not None
}
