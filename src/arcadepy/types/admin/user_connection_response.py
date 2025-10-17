# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["UserConnectionResponse"]


class UserConnectionResponse(BaseModel):
    id: Optional[str] = None

    connection_id: Optional[str] = None

    connection_status: Optional[str] = None

    provider_description: Optional[str] = None

    provider_id: Optional[str] = None

    provider_type: Optional[str] = None

    provider_user_info: Optional[object] = None

    scopes: Optional[List[str]] = None

    user_id: Optional[str] = None
