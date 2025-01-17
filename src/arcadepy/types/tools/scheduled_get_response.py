# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..tool_execution_attempt import ToolExecutionAttempt

__all__ = ["ScheduledGetResponse"]


class ScheduledGetResponse(BaseModel):
    id: Optional[str] = None

    attempts: Optional[List[ToolExecutionAttempt]] = None

    created_at: Optional[str] = None

    execution_status: Optional[str] = None

    execution_type: Optional[str] = None

    finished_at: Optional[str] = None

    input: Optional[Dict[str, object]] = None

    run_at: Optional[str] = None

    started_at: Optional[str] = None

    tool_name: Optional[str] = None

    toolkit_name: Optional[str] = None

    toolkit_version: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None
