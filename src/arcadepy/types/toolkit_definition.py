# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ToolkitDefinition"]


class ToolkitDefinition(BaseModel):
    name: str

    description: Optional[str] = None

    version: Optional[str] = None
