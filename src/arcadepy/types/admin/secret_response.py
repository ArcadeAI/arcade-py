# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SecretResponse", "Binding"]


class Binding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class SecretResponse(BaseModel):
    id: Optional[str] = None

    binding: Optional[Binding] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    hint: Optional[str] = None

    key: Optional[str] = None

    last_accessed_at: Optional[str] = None

    updated_at: Optional[str] = None
