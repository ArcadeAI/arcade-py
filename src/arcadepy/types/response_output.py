# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.authorization_response import AuthorizationResponse

__all__ = ["ResponseOutput", "Error"]


class Error(BaseModel):
    message: str

    additional_prompt_content: Optional[str] = None

    can_retry: Optional[bool] = None

    developer_message: Optional[str] = None

    retry_after_ms: Optional[int] = None


class ResponseOutput(BaseModel):
    error: Optional[Error] = None

    requires_authorization: Optional[AuthorizationResponse] = None

    value: Optional[object] = None
