# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HookCreateParams"]


class HookCreateParams(TypedDict, total=False):
    failure_mode: Required[Literal["fail_closed", "fail_open"]]

    hook_point: Required[Literal["tool.access", "tool.pre", "tool.post"]]

    name: Required[str]

    phase: Required[Literal["before", "after"]]

    plugin_id: Required[str]

    priority: int

    status: Literal["active", "inactive"]

    timeout_ms: int
