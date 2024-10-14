# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .response_output import ResponseOutput

__all__ = ["Response", "FinishedAt"]


class FinishedAt(BaseModel):
    time_time: Optional[str] = FieldInfo(alias="time.Time", default=None)


class Response(BaseModel):
    invocation_id: str

    duration: Optional[float] = None

    finished_at: Optional[FinishedAt] = None

    output: Optional[ResponseOutput] = None

    success: Optional[bool] = None
