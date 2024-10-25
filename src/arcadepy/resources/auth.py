# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import auth_status_params, auth_authorize_params
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

__all__ = ["AuthResource", "AsyncAuthResource"]

_DEFAULT_LONGPOLL_WAIT_TIME = 45


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        auth_requirement: auth_authorize_params.AuthRequirement,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AuthorizationResponse:
        """
        Starts the authorization process for given authorization requirements

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/v1/auth/authorize",
            body=maybe_transform(
                {
                    "auth_requirement": auth_requirement,
                    "user_id": user_id,
                },
                auth_authorize_params.AuthAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuthorizationResponse,
        )

    def start(
        self,
        user_id: str,
        provider: str,
        *,
        provider_type: str | None = "oauth2",
        scopes: list[str] | None = None,
    ) -> AuthorizationResponse:
        """
        Starts the authorization process for a given provider and scopes.

        Args:
            user_id: The user ID for which authorization is being requested.
            provider: The authorization provider (e.g., 'github', 'google', 'linkedin', 'microsoft', 'slack', 'spotify', 'x', 'zoom').
            provider_type: The type of authorization provider. Optional, defaults to 'oauth2'.
            scopes: A list of scopes required for authorization, if any.
        Returns:
            The authorization response.
        """
        scopes = scopes or []
        auth_requirement = auth_authorize_params.AuthRequirement(
            provider_id=provider,
            provider_type=provider_type or "oauth2",
            oauth2=auth_authorize_params.AuthRequirementOauth2(scopes=scopes),
        )
        return self.authorize(
            auth_requirement=auth_requirement,
            user_id=user_id,
        )

    def status(
        self,
        *,
        authorization_id: str,
        scopes: str | NotGiven = NOT_GIVEN,
        wait: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """Checks the status of an ongoing authorization process for a specific tool.

        If
        'wait' param is present, does not respond until either the auth status becomes
        completed or the timeout is reached.

        Args:
          authorization_id: Authorization ID

          scopes: Scopes

          wait: Timeout in seconds (max 59)

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
                        "wait": wait,
                    },
                    auth_status_params.AuthStatusParams,
                ),
            ),
            cast_to=AuthorizationResponse,
        )

    def wait_for_completion(
        self,
        auth_response_or_id: AuthorizationResponse | str,
        scopes: list[str] | None = None,
    ) -> AuthorizationResponse:
        """
        Waits for the authorization process to complete, for example:

        ```py
        auth_response = client.auth.start("you@example.com", "github")
        auth_response = client.auth.wait_for_completion(auth_response)
        ```
        """
        auth_id_val: str
        scopes_val: str | NotGiven = NOT_GIVEN

        if isinstance(auth_response_or_id, AuthorizationResponse):
            if not auth_response_or_id.authorization_id:
                raise ValueError("Authorization ID is required")
            auth_id_val = auth_response_or_id.authorization_id
            scopes_val = " ".join(auth_response_or_id.scopes) if auth_response_or_id.scopes else NOT_GIVEN
            auth_response = auth_response_or_id
        else:
            auth_id_val = auth_response_or_id
            scopes_val = " ".join(scopes) if scopes else NOT_GIVEN
            auth_response = AuthorizationResponse()

        while auth_response.status != "completed":
            auth_response = self.status(
                authorization_id=auth_id_val,
                scopes=scopes_val,
                wait=_DEFAULT_LONGPOLL_WAIT_TIME,
            )
        return auth_response


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        auth_requirement: auth_authorize_params.AuthRequirement,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> AuthorizationResponse:
        """
        Starts the authorization process for given authorization requirements

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/v1/auth/authorize",
            body=await async_maybe_transform(
                {
                    "auth_requirement": auth_requirement,
                    "user_id": user_id,
                },
                auth_authorize_params.AuthAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuthorizationResponse,
        )

    async def start(
        self,
        user_id: str,
        provider: str,
        *,
        provider_type: str | None = "oauth2",
        scopes: list[str] | None = None,
    ) -> AuthorizationResponse:
        """
        Starts the authorization process for a given provider and scopes.

        Args:
            user_id: The user ID for which authorization is being requested.
            provider: The authorization provider (e.g., 'github', 'google', 'linkedin', 'microsoft', 'slack', 'spotify', 'x', 'zoom').
            provider_type: The type of authorization provider. Optional, defaults to 'oauth2'.
            scopes: A list of scopes required for authorization, if any.
        Returns:
            The authorization response.
        """
        scopes = scopes or []
        auth_requirement = auth_authorize_params.AuthRequirement(
            provider_id=provider,
            provider_type=provider_type or "oauth2",
            oauth2=auth_authorize_params.AuthRequirementOauth2(scopes=scopes),
        )
        return await self.authorize(
            auth_requirement=auth_requirement,
            user_id=user_id,
        )

    async def status(
        self,
        *,
        authorization_id: str,
        scopes: str | NotGiven = NOT_GIVEN,
        wait: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """Checks the status of an ongoing authorization process for a specific tool.

        If
        'wait' param is present, does not respond until either the auth status becomes
        completed or the timeout is reached.

        Args:
          authorization_id: Authorization ID

          scopes: Scopes

          wait: Timeout in seconds (max 59)

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
                        "wait": wait,
                    },
                    auth_status_params.AuthStatusParams,
                ),
            ),
            cast_to=AuthorizationResponse,
        )

    async def wait_for_completion(
        self,
        auth_response_or_id: AuthorizationResponse | str,
        scopes: list[str] | None = None,
    ) -> AuthorizationResponse:
        """
        Waits for the authorization process to complete, for example:

        ```py
        auth_response = client.auth.start("you@example.com", "github")
        auth_response = client.auth.wait_for_completion(auth_response)
        ```
        """
        auth_id_val: str
        scopes_val: str | NotGiven = NOT_GIVEN

        if isinstance(auth_response_or_id, AuthorizationResponse):
            if not auth_response_or_id.authorization_id:
                raise ValueError("Authorization ID is required")
            auth_id_val = auth_response_or_id.authorization_id
            scopes_val = " ".join(auth_response_or_id.scopes) if auth_response_or_id.scopes else NOT_GIVEN
            auth_response = auth_response_or_id
        else:
            auth_id_val = auth_response_or_id
            scopes_val = " ".join(scopes) if scopes else NOT_GIVEN
            auth_response = AuthorizationResponse()

        while auth_response.status != "completed":
            auth_response = await self.status(
                authorization_id=auth_id_val,
                scopes=scopes_val,
                wait=_DEFAULT_LONGPOLL_WAIT_TIME,
            )
        return auth_response


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authorize = to_raw_response_wrapper(
            auth.authorize,
        )
        self.status = to_raw_response_wrapper(
            auth.status,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authorize = async_to_raw_response_wrapper(
            auth.authorize,
        )
        self.status = async_to_raw_response_wrapper(
            auth.status,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authorize = to_streamed_response_wrapper(
            auth.authorize,
        )
        self.status = to_streamed_response_wrapper(
            auth.status,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authorize = async_to_streamed_response_wrapper(
            auth.authorize,
        )
        self.status = async_to_streamed_response_wrapper(
            auth.status,
        )
