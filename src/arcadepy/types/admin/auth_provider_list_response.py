# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .auth_provider_response import AuthProviderResponse

__all__ = ["AuthProviderListResponse"]


class AuthProviderListResponse(BaseModel):
    items: Optional[List[AuthProviderResponse]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
