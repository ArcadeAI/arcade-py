# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["AuthAuthorizationContext"]


class AuthAuthorizationContext(BaseModel):
    token: Optional[str] = None

    user_info: Optional[Dict[str, object]] = None
