# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["HookUpdateParams"]


class HookUpdateParams(TypedDict, total=False):
    failure_mode: Literal["fail_closed", "fail_open"]

    phase: Literal["before", "after"]

    priority: int

    status: Literal["active", "inactive"]

    timeout_ms: int
