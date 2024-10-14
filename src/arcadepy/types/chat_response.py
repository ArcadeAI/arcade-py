# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .usage import Usage
from .choice import Choice
from .._models import BaseModel

__all__ = ["ChatResponse"]


class ChatResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    system_fingerprint: Optional[str] = None

    usage: Optional[Usage] = None
