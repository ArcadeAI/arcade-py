# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .secret_response import SecretResponse

__all__ = ["SecretListResponse"]


class SecretListResponse(BaseModel):
    items: Optional[List[SecretResponse]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
