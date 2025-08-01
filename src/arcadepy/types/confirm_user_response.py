# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConfirmUserResponse"]


class ConfirmUserResponse(BaseModel):
    auth_id: str

    next_uri: Optional[str] = None
