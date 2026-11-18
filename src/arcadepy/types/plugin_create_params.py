# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PluginCreateParams"]


class PluginCreateParams(TypedDict, total=False):
    name: Required[str]

    plugin_type: Required[Literal["webhook", "rate_limit"]]

    description: str

    rate_limit_config: Dict[str, object]

    retry: Dict[str, object]

    status: Literal["active", "inactive"]

    webhook_config: Dict[str, object]
