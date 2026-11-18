# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WorkerAuthorizeResponse"]


class WorkerAuthorizeResponse(BaseModel):
    next_uri: Optional[str] = None

    scopes: List[str]

    status: str

    url: Optional[str] = None

    user_id: str

    worker_id: str
