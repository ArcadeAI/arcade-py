# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkerResponse", "HTTP", "HTTPSecret"]


class HTTPSecret(BaseModel):
    binding: Optional[Literal["static", "tenant", "organization", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    hint: Optional[str] = None

    value: Optional[str] = None


class HTTP(BaseModel):
    retry: Optional[int] = None

    secret: Optional[HTTPSecret] = None

    timeout: Optional[int] = None

    uri: Optional[str] = None


class WorkerResponse(BaseModel):
    id: Optional[str] = None

    enabled: Optional[bool] = None

    http: Optional[HTTP] = None

    type: Optional[str] = None
