# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Required, TypedDict

__all__ = ["HookBulkUpsertParams"]


class HookBulkUpsertParams(TypedDict, total=False):
    configs: Required[List[Dict[str, object]]]
