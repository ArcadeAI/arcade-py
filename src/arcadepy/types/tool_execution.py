# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ToolExecution"]


class ToolExecution(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    execution_status: Optional[str] = None

    execution_type: Optional[str] = None

    finished_at: Optional[str] = None

    run_at: Optional[str] = None

    started_at: Optional[str] = None

    tool_name: Optional[str] = None

    toolkit_name: Optional[str] = None

    toolkit_version: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None
