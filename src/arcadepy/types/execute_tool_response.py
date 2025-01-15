# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.auth_authorization_response import AuthAuthorizationResponse

__all__ = ["ExecuteToolResponse", "Output", "OutputError"]


class OutputError(BaseModel):
    message: str

    additional_prompt_content: Optional[str] = None

    can_retry: Optional[bool] = None

    developer_message: Optional[str] = None

    retry_after_ms: Optional[int] = None


class Output(BaseModel):
    authorization: Optional[AuthAuthorizationResponse] = None

    error: Optional[OutputError] = None

    value: Optional[object] = None


class ExecuteToolResponse(BaseModel):
    id: Optional[str] = None

    duration: Optional[float] = None

    execution_id: Optional[str] = None

    execution_type: Optional[str] = None

    finished_at: Optional[str] = None

    output: Optional[Output] = None

    run_at: Optional[str] = None

    status: Optional[str] = None

    success: Optional[bool] = None
    """
    Whether the request was successful. For immediately-executed requests, this will
    be true if the tool call succeeded. For scheduled requests, this will be true if
    the request was scheduled successfully.
    """
