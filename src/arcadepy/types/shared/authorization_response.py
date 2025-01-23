# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .authorization_context import AuthorizationContext

__all__ = ["AuthorizationResponse"]


class AuthorizationResponse(BaseModel):
    id: Optional[str] = None

    context: Optional[AuthorizationContext] = None

    provider_id: Optional[str] = None

    scopes: Optional[List[str]] = None

    status: Optional[Literal["pending", "completed", "failed"]] = None

    url: Optional[str] = None

    user_id: Optional[str] = None
