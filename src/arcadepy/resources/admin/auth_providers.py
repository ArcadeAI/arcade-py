# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.admin import auth_provider_patch_params, auth_provider_create_params
from ..._base_client import make_request_options
from ...types.admin.auth_provider_response import AuthProviderResponse
from ...types.admin.auth_provider_list_response import AuthProviderListResponse

__all__ = ["AuthProvidersResource", "AsyncAuthProvidersResource"]


class AuthProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AuthProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AuthProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        description: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        oauth2: auth_provider_create_params.Oauth2 | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Create a new auth provider

        Args:
          external_id: The unique external ID for the auth provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/admin/auth_providers",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "external_id": external_id,
                    "oauth2": oauth2,
                    "provider_id": provider_id,
                    "status": status,
                    "type": type,
                },
                auth_provider_create_params.AuthProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderListResponse:
        """List a page of auth providers that are available to the caller"""
        return self._get(
            "/v1/admin/auth_providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Delete a specific auth provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/admin/auth_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Get the details of a specific auth provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/admin/auth_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )

    def patch(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        oauth2: auth_provider_patch_params.Oauth2 | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Patch an existing auth provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._patch(
            f"/v1/admin/auth_providers/{path_id}",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "description": description,
                    "oauth2": oauth2,
                    "provider_id": provider_id,
                    "status": status,
                    "type": type,
                },
                auth_provider_patch_params.AuthProviderPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )


class AsyncAuthProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncAuthProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        description: str | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        oauth2: auth_provider_create_params.Oauth2 | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Create a new auth provider

        Args:
          external_id: The unique external ID for the auth provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/admin/auth_providers",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "external_id": external_id,
                    "oauth2": oauth2,
                    "provider_id": provider_id,
                    "status": status,
                    "type": type,
                },
                auth_provider_create_params.AuthProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderListResponse:
        """List a page of auth providers that are available to the caller"""
        return await self._get(
            "/v1/admin/auth_providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Delete a specific auth provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/admin/auth_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Get the details of a specific auth provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/admin/auth_providers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )

    async def patch(
        self,
        path_id: str,
        *,
        body_id: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        oauth2: auth_provider_patch_params.Oauth2 | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthProviderResponse:
        """
        Patch an existing auth provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._patch(
            f"/v1/admin/auth_providers/{path_id}",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "description": description,
                    "oauth2": oauth2,
                    "provider_id": provider_id,
                    "status": status,
                    "type": type,
                },
                auth_provider_patch_params.AuthProviderPatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthProviderResponse,
        )


class AuthProvidersResourceWithRawResponse:
    def __init__(self, auth_providers: AuthProvidersResource) -> None:
        self._auth_providers = auth_providers

        self.create = to_raw_response_wrapper(
            auth_providers.create,
        )
        self.list = to_raw_response_wrapper(
            auth_providers.list,
        )
        self.delete = to_raw_response_wrapper(
            auth_providers.delete,
        )
        self.get = to_raw_response_wrapper(
            auth_providers.get,
        )
        self.patch = to_raw_response_wrapper(
            auth_providers.patch,
        )


class AsyncAuthProvidersResourceWithRawResponse:
    def __init__(self, auth_providers: AsyncAuthProvidersResource) -> None:
        self._auth_providers = auth_providers

        self.create = async_to_raw_response_wrapper(
            auth_providers.create,
        )
        self.list = async_to_raw_response_wrapper(
            auth_providers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            auth_providers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            auth_providers.get,
        )
        self.patch = async_to_raw_response_wrapper(
            auth_providers.patch,
        )


class AuthProvidersResourceWithStreamingResponse:
    def __init__(self, auth_providers: AuthProvidersResource) -> None:
        self._auth_providers = auth_providers

        self.create = to_streamed_response_wrapper(
            auth_providers.create,
        )
        self.list = to_streamed_response_wrapper(
            auth_providers.list,
        )
        self.delete = to_streamed_response_wrapper(
            auth_providers.delete,
        )
        self.get = to_streamed_response_wrapper(
            auth_providers.get,
        )
        self.patch = to_streamed_response_wrapper(
            auth_providers.patch,
        )


class AsyncAuthProvidersResourceWithStreamingResponse:
    def __init__(self, auth_providers: AsyncAuthProvidersResource) -> None:
        self._auth_providers = auth_providers

        self.create = async_to_streamed_response_wrapper(
            auth_providers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            auth_providers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            auth_providers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            auth_providers.get,
        )
        self.patch = async_to_streamed_response_wrapper(
            auth_providers.patch,
        )
