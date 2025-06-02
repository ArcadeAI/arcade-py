# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ToolGetParams"]


class ToolGetParams(TypedDict, total=False):
    include_format: List[Literal["arcade", "openai", "anthropic"]]
    """Comma separated tool formats that will be included in the response."""
