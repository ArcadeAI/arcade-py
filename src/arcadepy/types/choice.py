# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .chat_message import ChatMessage
from .shared.authorization_response import AuthorizationResponse

__all__ = ["Choice"]


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    logprobs: Optional[object] = None

    message: Optional[ChatMessage] = None

    tool_authorizations: Optional[List[AuthorizationResponse]] = None

    tool_messages: Optional[List[ChatMessage]] = None
