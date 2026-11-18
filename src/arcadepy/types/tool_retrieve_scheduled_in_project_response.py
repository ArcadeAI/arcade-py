# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ToolRetrieveScheduledInProjectResponse",
    "AttemptOutputAuthorizationContext",
    "AttemptOutputAuthorization",
    "AttemptOutputError",
    "AttemptOutputLog",
    "AttemptOutput",
    "Attempt",
]


class AttemptOutputAuthorizationContext(BaseModel):
    token: Optional[str] = None

    user_info: Optional[Dict[str, object]] = None


class AttemptOutputAuthorization(BaseModel):
    context: Optional[AttemptOutputAuthorizationContext] = None

    id: Optional[str] = None

    provider_id: Optional[str] = None

    scopes: Optional[List[str]] = None

    status: Optional[Literal["not_started", "pending", "completed", "failed"]] = None

    url: Optional[str] = None

    user_id: Optional[str] = None


class AttemptOutputError(BaseModel):
    additional_prompt_content: Optional[str] = None

    can_retry: bool

    developer_message: Optional[str] = None

    extra: Optional[Dict[str, object]] = None

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
        "NETWORK_TRANSPORT_RUNTIME_TIMEOUT",
        "NETWORK_TRANSPORT_RUNTIME_UNREACHABLE",
        "NETWORK_TRANSPORT_RUNTIME_UNMAPPED",
        "UNKNOWN",
    ]

    message: str

    retry_after_ms: Optional[int] = None

    stacktrace: Optional[str] = None

    status_code: Optional[int] = None


class AttemptOutputLog(BaseModel):
    level: str

    message: str

    subtype: Optional[str] = None


class AttemptOutput(BaseModel):
    authorization: Optional[AttemptOutputAuthorization] = None

    error: Optional[AttemptOutputError] = None

    logs: Optional[List[AttemptOutputLog]] = None

    value: Optional[object] = None


class Attempt(BaseModel):
    finished_at: Optional[str] = None

    id: Optional[str] = None

    output: Optional[AttemptOutput] = None

    started_at: Optional[str] = None

    success: Optional[bool] = None

    system_error_message: Optional[str] = None


class ToolRetrieveScheduledInProjectResponse(BaseModel):
    attempts: Optional[List[Attempt]] = None

    created_at: Optional[str] = None

    execution_status: Optional[str] = None

    execution_type: Optional[str] = None

    finished_at: Optional[str] = None

    id: Optional[str] = None

    input: Optional[Dict[str, object]] = None

    run_at: Optional[str] = None

    started_at: Optional[str] = None

    tool_name: Optional[str] = None

    toolkit_name: Optional[str] = None

    toolkit_version: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None
