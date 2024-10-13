# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .chat_message import ChatMessage

__all__ = ["ChatResponse", "Choice", "Usage"]


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    logprobs: Optional[object] = None

    message: Optional[ChatMessage] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    system_fingerprint: Optional[str] = None

    usage: Optional[Usage] = None
