# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tools.scheduled_list_response import ScheduledListResponse
from ...types.tools.scheduled_details_response import ScheduledDetailsResponse

__all__ = ["ScheduledResource", "AsyncScheduledResource"]


class ScheduledResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return ScheduledResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduledResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return ScheduledResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledListResponse:
        """Returns a page of scheduled tool executions"""
        return self._get(
            "/v1/tools/scheduled",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledListResponse,
        )

    def details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledDetailsResponse:
        """
        Returns the details for a specific scheduled tool execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/tools/scheduled/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledDetailsResponse,
        )


class AsyncScheduledResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduledResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduledResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncScheduledResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledListResponse:
        """Returns a page of scheduled tool executions"""
        return await self._get(
            "/v1/tools/scheduled",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledListResponse,
        )

    async def details(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduledDetailsResponse:
        """
        Returns the details for a specific scheduled tool execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/tools/scheduled/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledDetailsResponse,
        )


class ScheduledResourceWithRawResponse:
    def __init__(self, scheduled: ScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = to_raw_response_wrapper(
            scheduled.list,
        )
        self.details = to_raw_response_wrapper(
            scheduled.details,
        )


class AsyncScheduledResourceWithRawResponse:
    def __init__(self, scheduled: AsyncScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = async_to_raw_response_wrapper(
            scheduled.list,
        )
        self.details = async_to_raw_response_wrapper(
            scheduled.details,
        )


class ScheduledResourceWithStreamingResponse:
    def __init__(self, scheduled: ScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = to_streamed_response_wrapper(
            scheduled.list,
        )
        self.details = to_streamed_response_wrapper(
            scheduled.details,
        )


class AsyncScheduledResourceWithStreamingResponse:
    def __init__(self, scheduled: AsyncScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = async_to_streamed_response_wrapper(
            scheduled.list,
        )
        self.details = async_to_streamed_response_wrapper(
            scheduled.details,
        )
