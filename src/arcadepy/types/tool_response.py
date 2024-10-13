# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolResponse", "FinishedAt", "Output", "OutputError"]


class FinishedAt(BaseModel):
    time_time: Optional[str] = FieldInfo(alias="time.Time", default=None)


class OutputError(BaseModel):
    message: str

    additional_prompt_content: Optional[str] = None

    can_retry: Optional[bool] = None

    developer_message: Optional[str] = None

    retry_after_ms: Optional[int] = None


class Output(BaseModel):
    value: object

    error: Optional[OutputError] = None


class ToolResponse(BaseModel):
    invocation_id: str

    duration: Optional[float] = None

    finished_at: Optional[FinishedAt] = None

    output: Optional[Output] = None

    success: Optional[bool] = None
