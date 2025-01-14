# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .response_output import ResponseOutput

__all__ = ["ToolExecutionAttempt"]


class ToolExecutionAttempt(BaseModel):
    id: Optional[str] = None

    finished_at: Optional[str] = None

    output: Optional[ResponseOutput] = None

    started_at: Optional[str] = None

    success: Optional[bool] = None

    system_error_message: Optional[str] = None
