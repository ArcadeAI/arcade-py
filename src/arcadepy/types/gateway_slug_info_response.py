# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GatewaySlugInfoResponse"]


class GatewaySlugInfoResponse(BaseModel):
    available: Optional[bool] = None
