# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "AuthProviderCreateParams",
    "Oauth2",
    "Oauth2AuthorizeRequest",
    "Oauth2Pkce",
    "Oauth2RefreshRequest",
    "Oauth2TokenIntrospectionRequest",
    "Oauth2TokenIntrospectionRequestTriggers",
    "Oauth2TokenRequest",
    "Oauth2UserInfoRequest",
    "Oauth2UserInfoRequestTriggers",
]


class AuthProviderCreateParams(TypedDict, total=False):
    id: Required[str]

    description: str

    external_id: str
    """The unique external ID for the auth provider"""

    oauth2: Oauth2

    provider_id: str

    status: str

    type: str


class Oauth2AuthorizeRequest(TypedDict, total=False):
    endpoint: Required[str]

    auth_method: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2Pkce(TypedDict, total=False):
    code_challenge_method: str

    enabled: bool


class Oauth2RefreshRequest(TypedDict, total=False):
    endpoint: Required[str]

    auth_method: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2TokenIntrospectionRequestTriggers(TypedDict, total=False):
    on_token_grant: bool

    on_token_refresh: bool


class Oauth2TokenIntrospectionRequest(TypedDict, total=False):
    endpoint: Required[str]

    triggers: Required[Oauth2TokenIntrospectionRequestTriggers]

    auth_method: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2TokenRequest(TypedDict, total=False):
    endpoint: Required[str]

    auth_method: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2UserInfoRequestTriggers(TypedDict, total=False):
    on_token_grant: bool

    on_token_refresh: bool


class Oauth2UserInfoRequest(TypedDict, total=False):
    endpoint: Required[str]

    triggers: Required[Oauth2UserInfoRequestTriggers]

    auth_method: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2(TypedDict, total=False):
    client_id: Required[str]

    authorize_request: Oauth2AuthorizeRequest

    client_secret: str

    pkce: Oauth2Pkce

    refresh_request: Oauth2RefreshRequest

    scope_delimiter: Literal[",", " "]

    token_introspection_request: Oauth2TokenIntrospectionRequest

    token_request: Oauth2TokenRequest

    user_info_request: Oauth2UserInfoRequest
