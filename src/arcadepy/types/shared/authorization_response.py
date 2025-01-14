# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AuthorizationResponse", "Context"]


class Context(BaseModel):
    token: Optional[str] = None

    user_info: Optional[Dict[str, object]] = None


class AuthorizationResponse(BaseModel):
    id: Optional[str] = None

    context: Optional[Context] = None

    provider_id: Optional[str] = None

    scopes: Optional[List[str]] = None

    status: Optional[Literal["pending", "completed", "failed"]] = None

    url: Optional[str] = None

    user_id: Optional[str] = None
