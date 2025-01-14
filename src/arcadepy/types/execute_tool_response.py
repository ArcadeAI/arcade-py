# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .response_output import ResponseOutput

__all__ = ["ExecuteToolResponse"]


class ExecuteToolResponse(BaseModel):
    id: Optional[str] = None

    duration: Optional[float] = None

    execution_id: Optional[str] = None

    execution_type: Optional[str] = None

    finished_at: Optional[str] = None

    output: Optional[ResponseOutput] = None

    run_at: Optional[str] = None

    status: Optional[str] = None

    success: Optional[bool] = None
    """
    Whether the request was successful. For immediately-executed requests, this will
    be true if the tool call succeeded. For scheduled requests, this will be true if
    the request was scheduled successfully.
    """
