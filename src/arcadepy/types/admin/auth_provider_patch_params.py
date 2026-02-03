# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AuthProviderPatchParams",
    "Oauth2",
    "Oauth2AuthorizeRequest",
    "Oauth2Pkce",
    "Oauth2RefreshRequest",
    "Oauth2TokenRequest",
    "Oauth2UserInfoRequest",
    "Oauth2UserInfoRequestTriggers",
]


class AuthProviderPatchParams(TypedDict, total=False):
    body_id: Annotated[str, PropertyInfo(alias="id")]

    description: str

    oauth2: Oauth2

    provider_id: str

    status: str

    type: str


class Oauth2AuthorizeRequest(TypedDict, total=False):
    auth_header_value_format: str

    auth_method: str

    endpoint: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2Pkce(TypedDict, total=False):
    code_challenge_method: str

    enabled: bool


class Oauth2RefreshRequest(TypedDict, total=False):
    auth_header_value_format: str

    auth_method: str

    endpoint: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2TokenRequest(TypedDict, total=False):
    auth_header_value_format: str

    auth_method: str

    endpoint: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]


class Oauth2UserInfoRequestTriggers(TypedDict, total=False):
    on_token_grant: bool

    on_token_refresh: bool


class Oauth2UserInfoRequest(TypedDict, total=False):
    auth_header_value_format: str

    auth_method: str

    endpoint: str

    method: str

    params: Dict[str, str]

    request_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_content_type: Literal["application/x-www-form-urlencoded", "application/json"]

    response_map: Dict[str, str]

    triggers: Oauth2UserInfoRequestTriggers


class Oauth2(TypedDict, total=False):
    authorize_request: Oauth2AuthorizeRequest

    client_id: str

    client_secret: str

    pkce: Oauth2Pkce

    refresh_request: Oauth2RefreshRequest

    scope_delimiter: Literal[",", " "]

    token_request: Oauth2TokenRequest

    user_info_request: Oauth2UserInfoRequest
