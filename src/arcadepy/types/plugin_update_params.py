# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

__all__ = ["PluginUpdateParams"]


class PluginUpdateParams(TypedDict, total=False):
    description: str

    name: str

    rate_limit_config: Dict[str, object]

    retry: Dict[str, object]

    status: Literal["inactive", "active"]

    webhook_config: Dict[str, object]
