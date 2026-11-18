# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["GatewayUpdateParams"]


class GatewayUpdateParams(TypedDict, total=False):
    allowed_passthrough_headers: SequenceNotStr[str]

    auth_type: Literal["arcade", "arcade_header", "user_source"]

    consent_skip_client_ids: SequenceNotStr[str]

    description: str

    instructions: str

    name: str

    slug: str

    status: str

    tool_filter: Dict[str, object]

    user_source_id: str
