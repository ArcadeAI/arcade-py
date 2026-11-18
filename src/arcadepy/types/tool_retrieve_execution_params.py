# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ToolRetrieveExecutionParams"]


class ToolRetrieveExecutionParams(TypedDict, total=False):
    include_inputs: bool
    """Include the tool inputs in the response (default: false)"""

    include_outputs: bool
    """Include the tool outputs in the response (default: false)"""
