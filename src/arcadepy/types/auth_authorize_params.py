# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AuthAuthorizeParams", "AuthRequirement", "AuthRequirementOauth2"]


class AuthAuthorizeParams(TypedDict, total=False):
    auth_requirement: Required[AuthRequirement]

    user_id: Required[str]

    force_verification: bool
    """
    Optional: if true, the user will be forced to verify their identity (strict
    session check). TODO: Remove as soon as this is the default for everyone.
    """

    next_uri: str
    """
    Optional: if provided, the user will be redirected to this URI after
    authorization
    """


class AuthRequirementOauth2(TypedDict, total=False):
    scopes: List[str]


class AuthRequirement(TypedDict, total=False):
    id: str
    """one of ID or ProviderID must be set"""

    oauth2: AuthRequirementOauth2

    provider_id: str
    """one of ID or ProviderID must be set"""

    provider_type: str
