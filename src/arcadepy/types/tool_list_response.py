# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .shared.tool_definition import ToolDefinition

__all__ = ["ToolListResponse"]

ToolListResponse: TypeAlias = List[ToolDefinition]
