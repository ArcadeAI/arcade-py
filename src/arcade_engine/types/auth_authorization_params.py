# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AuthAuthorizationParams", "AuthRequirement", "AuthRequirementOauth2"]


class AuthAuthorizationParams(TypedDict, total=False):
    auth_requirement: Required[AuthRequirement]

    user_id: Required[str]


class AuthRequirementOauth2(TypedDict, total=False):
    authority: str

    scopes: List[str]


class AuthRequirement(TypedDict, total=False):
    provider: Required[str]

    oauth2: AuthRequirementOauth2
