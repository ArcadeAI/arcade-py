# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthorizationResponse", "Context"]


class Context(BaseModel):
    token: Optional[str] = None


class AuthorizationResponse(BaseModel):
    authorization_id: Optional[str] = FieldInfo(alias="authorizationID", default=None)

    authorization_url: Optional[str] = FieldInfo(alias="authorizationURL", default=None)

    context: Optional[Context] = None

    scopes: Optional[List[str]] = None

    status: Optional[str] = None
