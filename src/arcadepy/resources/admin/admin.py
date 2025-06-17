# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .secrets import (
    SecretsResource,
    AsyncSecretsResource,
    SecretsResourceWithRawResponse,
    AsyncSecretsResourceWithRawResponse,
    SecretsResourceWithStreamingResponse,
    AsyncSecretsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .auth_providers import (
    AuthProvidersResource,
    AsyncAuthProvidersResource,
    AuthProvidersResourceWithRawResponse,
    AsyncAuthProvidersResourceWithRawResponse,
    AuthProvidersResourceWithStreamingResponse,
    AsyncAuthProvidersResourceWithStreamingResponse,
)
from .user_connections import (
    UserConnectionsResource,
    AsyncUserConnectionsResource,
    UserConnectionsResourceWithRawResponse,
    AsyncUserConnectionsResourceWithRawResponse,
    UserConnectionsResourceWithStreamingResponse,
    AsyncUserConnectionsResourceWithStreamingResponse,
)

__all__ = ["AdminResource", "AsyncAdminResource"]


class AdminResource(SyncAPIResource):
    @cached_property
    def user_connections(self) -> UserConnectionsResource:
        return UserConnectionsResource(self._client)

    @cached_property
    def auth_providers(self) -> AuthProvidersResource:
        return AuthProvidersResource(self._client)

    @cached_property
    def secrets(self) -> SecretsResource:
        return SecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AdminResourceWithStreamingResponse(self)


class AsyncAdminResource(AsyncAPIResource):
    @cached_property
    def user_connections(self) -> AsyncUserConnectionsResource:
        return AsyncUserConnectionsResource(self._client)

    @cached_property
    def auth_providers(self) -> AsyncAuthProvidersResource:
        return AsyncAuthProvidersResource(self._client)

    @cached_property
    def secrets(self) -> AsyncSecretsResource:
        return AsyncSecretsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdminResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAdminResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdminResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncAdminResourceWithStreamingResponse(self)


class AdminResourceWithRawResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def user_connections(self) -> UserConnectionsResourceWithRawResponse:
        return UserConnectionsResourceWithRawResponse(self._admin.user_connections)

    @cached_property
    def auth_providers(self) -> AuthProvidersResourceWithRawResponse:
        return AuthProvidersResourceWithRawResponse(self._admin.auth_providers)

    @cached_property
    def secrets(self) -> SecretsResourceWithRawResponse:
        return SecretsResourceWithRawResponse(self._admin.secrets)


class AsyncAdminResourceWithRawResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def user_connections(self) -> AsyncUserConnectionsResourceWithRawResponse:
        return AsyncUserConnectionsResourceWithRawResponse(self._admin.user_connections)

    @cached_property
    def auth_providers(self) -> AsyncAuthProvidersResourceWithRawResponse:
        return AsyncAuthProvidersResourceWithRawResponse(self._admin.auth_providers)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithRawResponse:
        return AsyncSecretsResourceWithRawResponse(self._admin.secrets)


class AdminResourceWithStreamingResponse:
    def __init__(self, admin: AdminResource) -> None:
        self._admin = admin

    @cached_property
    def user_connections(self) -> UserConnectionsResourceWithStreamingResponse:
        return UserConnectionsResourceWithStreamingResponse(self._admin.user_connections)

    @cached_property
    def auth_providers(self) -> AuthProvidersResourceWithStreamingResponse:
        return AuthProvidersResourceWithStreamingResponse(self._admin.auth_providers)

    @cached_property
    def secrets(self) -> SecretsResourceWithStreamingResponse:
        return SecretsResourceWithStreamingResponse(self._admin.secrets)


class AsyncAdminResourceWithStreamingResponse:
    def __init__(self, admin: AsyncAdminResource) -> None:
        self._admin = admin

    @cached_property
    def user_connections(self) -> AsyncUserConnectionsResourceWithStreamingResponse:
        return AsyncUserConnectionsResourceWithStreamingResponse(self._admin.user_connections)

    @cached_property
    def auth_providers(self) -> AsyncAuthProvidersResourceWithStreamingResponse:
        return AsyncAuthProvidersResourceWithStreamingResponse(self._admin.auth_providers)

    @cached_property
    def secrets(self) -> AsyncSecretsResourceWithStreamingResponse:
        return AsyncSecretsResourceWithStreamingResponse(self._admin.secrets)
