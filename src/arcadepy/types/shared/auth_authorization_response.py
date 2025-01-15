# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .auth_authorization_context import AuthAuthorizationContext

__all__ = ["AuthAuthorizationResponse"]


class AuthAuthorizationResponse(BaseModel):
    id: Optional[str] = None

    context: Optional[AuthAuthorizationContext] = None

    provider_id: Optional[str] = None

    scopes: Optional[List[str]] = None

    status: Optional[Literal["pending", "completed", "failed"]] = None

    url: Optional[str] = None

    user_id: Optional[str] = None
