# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import authorization_status_params, authorization_authorize_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.authorization_response import AuthorizationResponse

__all__ = ["AuthorizationResource", "AsyncAuthorizationResource"]


class AuthorizationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthorizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AuthorizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthorizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AuthorizationResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        auth_requirement: authorization_authorize_params.AuthRequirement,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """
        Starts the authorization process for given authorization requirements

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/auth/authorize",
            body=maybe_transform(
                {
                    "auth_requirement": auth_requirement,
                    "user_id": user_id,
                },
                authorization_authorize_params.AuthorizationAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationResponse,
        )

    def status(
        self,
        *,
        authorization_id: str,
        scopes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """
        Checks the status of an ongoing authorization process for a specific tool

        Args:
          authorization_id: Authorization ID

          scopes: Scopes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/auth/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "authorization_id": authorization_id,
                        "scopes": scopes,
                    },
                    authorization_status_params.AuthorizationStatusParams,
                ),
            ),
            cast_to=AuthorizationResponse,
        )


class AsyncAuthorizationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthorizationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthorizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthorizationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncAuthorizationResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        auth_requirement: authorization_authorize_params.AuthRequirement,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """
        Starts the authorization process for given authorization requirements

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/auth/authorize",
            body=await async_maybe_transform(
                {
                    "auth_requirement": auth_requirement,
                    "user_id": user_id,
                },
                authorization_authorize_params.AuthorizationAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationResponse,
        )

    async def status(
        self,
        *,
        authorization_id: str,
        scopes: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """
        Checks the status of an ongoing authorization process for a specific tool

        Args:
          authorization_id: Authorization ID

          scopes: Scopes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/auth/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "authorization_id": authorization_id,
                        "scopes": scopes,
                    },
                    authorization_status_params.AuthorizationStatusParams,
                ),
            ),
            cast_to=AuthorizationResponse,
        )


class AuthorizationResourceWithRawResponse:
    def __init__(self, authorization: AuthorizationResource) -> None:
        self._authorization = authorization

        self.authorize = to_raw_response_wrapper(
            authorization.authorize,
        )
        self.status = to_raw_response_wrapper(
            authorization.status,
        )


class AsyncAuthorizationResourceWithRawResponse:
    def __init__(self, authorization: AsyncAuthorizationResource) -> None:
        self._authorization = authorization

        self.authorize = async_to_raw_response_wrapper(
            authorization.authorize,
        )
        self.status = async_to_raw_response_wrapper(
            authorization.status,
        )


class AuthorizationResourceWithStreamingResponse:
    def __init__(self, authorization: AuthorizationResource) -> None:
        self._authorization = authorization

        self.authorize = to_streamed_response_wrapper(
            authorization.authorize,
        )
        self.status = to_streamed_response_wrapper(
            authorization.status,
        )


class AsyncAuthorizationResourceWithStreamingResponse:
    def __init__(self, authorization: AsyncAuthorizationResource) -> None:
        self._authorization = authorization

        self.authorize = async_to_streamed_response_wrapper(
            authorization.authorize,
        )
        self.status = async_to_streamed_response_wrapper(
            authorization.status,
        )