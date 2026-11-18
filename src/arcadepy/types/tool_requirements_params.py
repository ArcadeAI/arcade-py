# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ToolRequirementsParams"]


class ToolRequirementsParams(TypedDict, total=False):
    authorize: bool

    tool_names: SequenceNotStr[str]

    tools: List[Dict[str, object]]

    user_id: str
