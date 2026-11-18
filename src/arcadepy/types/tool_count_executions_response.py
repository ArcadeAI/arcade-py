# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ToolCountExecutionsResponse"]


class ToolCountExecutionsResponse(BaseModel):
    count: Optional[int] = None
