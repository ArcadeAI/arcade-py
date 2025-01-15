# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ToolExecuteParams"]


class ToolExecuteParams(TypedDict, total=False):
    tool_name: Required[str]

    input: Dict[str, object]
    """JSON input to the tool, if any"""

    run_at: str
    """The time at which the tool should be run (optional).

    If not provided, the tool is run immediately
    """

    tool_version: str
    """The tool version to use (optional). If not provided, any version is used"""

    user_id: str
