# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Requirements", "Authorization", "AuthorizationOauth2"]


class AuthorizationOauth2(BaseModel):
    scopes: Optional[List[str]] = None


class Authorization(BaseModel):
    oauth2: Optional[AuthorizationOauth2] = None

    provider_id: Optional[str] = None

    provider_type: Optional[str] = None


class Requirements(BaseModel):
    authorization: Optional[Authorization] = None
