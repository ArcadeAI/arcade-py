# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.authorization_response import AuthorizationResponse

__all__ = ["ToolExecutionAttempt", "Output", "OutputError", "OutputLog"]


class OutputError(BaseModel):
    can_retry: bool

    kind: Literal[
        "TOOLKIT_LOAD_FAILED",
        "TOOL_DEFINITION_BAD_DEFINITION",
        "TOOL_DEFINITION_BAD_INPUT_SCHEMA",
        "TOOL_DEFINITION_BAD_OUTPUT_SCHEMA",
        "TOOL_REQUIREMENTS_NOT_MET",
        "TOOL_RUNTIME_BAD_INPUT_VALUE",
        "TOOL_RUNTIME_BAD_OUTPUT_VALUE",
        "TOOL_RUNTIME_RETRY",
        "TOOL_RUNTIME_CONTEXT_REQUIRED",
        "TOOL_RUNTIME_FATAL",
        "CONTEXT_CHECK_FAILED",
        "CONTEXT_DENIED",
        "UPSTREAM_RUNTIME_BAD_REQUEST",
        "UPSTREAM_RUNTIME_AUTH_ERROR",
        "UPSTREAM_RUNTIME_NOT_FOUND",
        "UPSTREAM_RUNTIME_VALIDATION_ERROR",
        "UPSTREAM_RUNTIME_RATE_LIMIT",
        "UPSTREAM_RUNTIME_SERVER_ERROR",
        "UPSTREAM_RUNTIME_UNMAPPED",
        "UNKNOWN",
    ]

    message: str

    additional_prompt_content: Optional[str] = None

    developer_message: Optional[str] = None

    extra: Optional[Dict[str, object]] = None

    retry_after_ms: Optional[int] = None

    stacktrace: Optional[str] = None

    status_code: Optional[int] = None


class OutputLog(BaseModel):
    level: str

    message: str

    subtype: Optional[str] = None


class Output(BaseModel):
    authorization: Optional[AuthorizationResponse] = None

    error: Optional[OutputError] = None

    logs: Optional[List[OutputLog]] = None

    value: Optional[object] = None


class ToolExecutionAttempt(BaseModel):
    id: Optional[str] = None

    finished_at: Optional[str] = None

    output: Optional[Output] = None

    started_at: Optional[str] = None

    success: Optional[bool] = None

    system_error_message: Optional[str] = None
