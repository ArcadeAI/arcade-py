# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AuthAuthorizeParams", "AuthRequirement", "AuthRequirementOauth2"]


class AuthAuthorizeParams(TypedDict, total=False):
    auth_requirement: Required[AuthRequirement]

    user_id: Required[str]


class AuthRequirementOauth2(TypedDict, total=False):
    scopes: List[str]


class AuthRequirement(TypedDict, total=False):
    oauth2: AuthRequirementOauth2

    provider_id: str

    provider_type: str
