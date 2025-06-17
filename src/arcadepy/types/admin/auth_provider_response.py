# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "AuthProviderResponse",
    "Binding",
    "Oauth2",
    "Oauth2AuthorizeRequest",
    "Oauth2ClientSecret",
    "Oauth2Pkce",
    "Oauth2RefreshRequest",
    "Oauth2TokenIntrospectionRequest",
    "Oauth2TokenIntrospectionRequestTriggers",
    "Oauth2TokenRequest",
    "Oauth2UserInfoRequest",
    "Oauth2UserInfoRequestTriggers",
]


class Binding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class Oauth2AuthorizeRequest(BaseModel):
    auth_method: Optional[str] = None

    endpoint: Optional[str] = None

    expiration_format: Optional[str] = None

    method: Optional[str] = None

    params: Optional[Dict[str, str]] = None

    request_content_type: Optional[str] = None

    response_content_type: Optional[str] = None

    response_map: Optional[Dict[str, str]] = None


class Oauth2ClientSecret(BaseModel):
    binding: Optional[Literal["static", "tenant", "project", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    hint: Optional[str] = None

    value: Optional[str] = None


class Oauth2Pkce(BaseModel):
    code_challenge_method: Optional[str] = None

    enabled: Optional[bool] = None


class Oauth2RefreshRequest(BaseModel):
    auth_method: Optional[str] = None

    endpoint: Optional[str] = None

    expiration_format: Optional[str] = None

    method: Optional[str] = None

    params: Optional[Dict[str, str]] = None

    request_content_type: Optional[str] = None

    response_content_type: Optional[str] = None

    response_map: Optional[Dict[str, str]] = None


class Oauth2TokenIntrospectionRequestTriggers(BaseModel):
    on_token_grant: Optional[bool] = None

    on_token_refresh: Optional[bool] = None


class Oauth2TokenIntrospectionRequest(BaseModel):
    auth_method: Optional[str] = None

    enabled: Optional[bool] = None

    endpoint: Optional[str] = None

    expiration_format: Optional[str] = None

    method: Optional[str] = None

    params: Optional[Dict[str, str]] = None

    request_content_type: Optional[str] = None

    response_content_type: Optional[str] = None

    response_map: Optional[Dict[str, str]] = None

    triggers: Optional[Oauth2TokenIntrospectionRequestTriggers] = None


class Oauth2TokenRequest(BaseModel):
    auth_method: Optional[str] = None

    endpoint: Optional[str] = None

    expiration_format: Optional[str] = None

    method: Optional[str] = None

    params: Optional[Dict[str, str]] = None

    request_content_type: Optional[str] = None

    response_content_type: Optional[str] = None

    response_map: Optional[Dict[str, str]] = None


class Oauth2UserInfoRequestTriggers(BaseModel):
    on_token_grant: Optional[bool] = None

    on_token_refresh: Optional[bool] = None


class Oauth2UserInfoRequest(BaseModel):
    auth_method: Optional[str] = None

    endpoint: Optional[str] = None

    expiration_format: Optional[str] = None

    method: Optional[str] = None

    params: Optional[Dict[str, str]] = None

    request_content_type: Optional[str] = None

    response_content_type: Optional[str] = None

    response_map: Optional[Dict[str, str]] = None

    triggers: Optional[Oauth2UserInfoRequestTriggers] = None


class Oauth2(BaseModel):
    authorize_request: Optional[Oauth2AuthorizeRequest] = None

    client_id: Optional[str] = None

    client_secret: Optional[Oauth2ClientSecret] = None

    pkce: Optional[Oauth2Pkce] = None

    refresh_request: Optional[Oauth2RefreshRequest] = None

    scope_delimiter: Optional[str] = None

    token_introspection_request: Optional[Oauth2TokenIntrospectionRequest] = None

    token_request: Optional[Oauth2TokenRequest] = None

    user_info_request: Optional[Oauth2UserInfoRequest] = None


class AuthProviderResponse(BaseModel):
    id: Optional[str] = None

    binding: Optional[Binding] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    oauth2: Optional[Oauth2] = None

    provider_id: Optional[str] = None

    status: Optional[str] = None

    type: Optional[str] = None

    updated_at: Optional[str] = None
