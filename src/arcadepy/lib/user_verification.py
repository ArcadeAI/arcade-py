# Hand-written methods for custom user verification functionality

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.user_verification_confirm_response import UserVerificationConfirmResponse

__all__ = ["UserVerificationResource", "AsyncUserVerificationResource"]


class ConfirmUserOptions(TypedDict, total=False):
    base_url: Optional[str]


DEFAULT_COORDINATOR = "https://cloud.arcade.dev"
VERIFY_PATH = "/api/v1/oauth/confirm_user"


class UserVerificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return UserVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return UserVerificationResourceWithStreamingResponse(self)

    def confirm(
        self,
        flow_id: str,
        user_id: str,
        *,
        base_url: Optional[str] = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserVerificationConfirmResponse:
        """
        Confirm a user for OAuth flow verification.

        Args:
            flow_id: The OAuth flow ID from the query string
            user_id: The user ID from a session cookie or other secure storage
            base_url: Optional base URL to override the default coordinator URL
        """
        host = base_url or DEFAULT_COORDINATOR
        if host.endswith("/"):
            host = host[:-1]
        url = host + VERIFY_PATH

        # Build headers with proper Bearer token
        headers: dict[str, str] = {"Authorization": f"Bearer {self._client.api_key}"}
        if extra_headers:
            # Convert Headers to dict and update
            for key, value in extra_headers.items():
                if isinstance(value, str):
                    headers[key] = value

        # Make the POST request directly to the custom URL
        return self._client.post(
            url,
            body={"flow_id": flow_id, "user_id": user_id},
            options=make_request_options(
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=UserVerificationConfirmResponse,
        )


class AsyncUserVerificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncUserVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(
        self,
    ) -> AsyncUserVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncUserVerificationResourceWithStreamingResponse(self)

    async def confirm(
        self,
        flow_id: str,
        user_id: str,
        *,
        base_url: Optional[str] = None,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserVerificationConfirmResponse:
        """
        Confirm a user for OAuth flow verification.

        Args:
            flow_id: The OAuth flow ID from the query string
            user_id: The user ID from a session cookie or other secure storage
            base_url: Optional base URL to override the default coordinator URL
        """
        host = base_url or DEFAULT_COORDINATOR
        if host.endswith("/"):
            host = host[:-1]
        url = host + VERIFY_PATH

        # Build headers with proper Bearer token
        headers: dict[str, str] = {"Authorization": f"Bearer {self._client.api_key}"}
        if extra_headers:
            # Convert Headers to dict and update
            for key, value in extra_headers.items():
                if isinstance(value, str):
                    headers[key] = value

        # Make the POST request directly to the custom URL
        return await self._client.post(
            url,
            body={"flow_id": flow_id, "user_id": user_id},
            options=make_request_options(
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=UserVerificationConfirmResponse,
        )


class UserVerificationResourceWithRawResponse:
    def __init__(self, user_verification: UserVerificationResource) -> None:
        self._user_verification = user_verification

        self.confirm = to_raw_response_wrapper(
            user_verification.confirm,
        )


class AsyncUserVerificationResourceWithRawResponse:
    def __init__(self, user_verification: AsyncUserVerificationResource) -> None:
        self._user_verification = user_verification

        self.confirm = async_to_raw_response_wrapper(
            user_verification.confirm,
        )


class UserVerificationResourceWithStreamingResponse:
    def __init__(self, user_verification: UserVerificationResource) -> None:
        self._user_verification = user_verification

        self.confirm = to_streamed_response_wrapper(
            user_verification.confirm,
        )


class AsyncUserVerificationResourceWithStreamingResponse:
    def __init__(self, user_verification: AsyncUserVerificationResource) -> None:
        self._user_verification = user_verification

        self.confirm = async_to_streamed_response_wrapper(
            user_verification.confirm,
        )
