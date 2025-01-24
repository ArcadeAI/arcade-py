# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.tools import scheduled_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.tool_execution import ToolExecution
from ...types.tools.scheduled_get_response import ScheduledGetResponse

__all__ = ["ScheduledResource", "AsyncScheduledResource"]


class ScheduledResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduledResourceWithRawResponse:
        """
        <<<<<<< HEAD
                This property can be used as a prefix for any HTTP method call to return
        =======
                This property can be used as a prefix for any HTTP method call to return the
        >>>>>>> main
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
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[ToolExecution]:
        """
        Returns a page of scheduled tool executions

        Args:
          limit: Number of items to return (default: 25, max: 100)

          offset: Offset from the start of the list (default: 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/scheduled_tools",
            page=SyncOffsetPage[ToolExecution],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    scheduled_list_params.ScheduledListParams,
                ),
            ),
            model=ToolExecution,
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
    ) -> ScheduledGetResponse:
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
            f"/v1/scheduled_tools/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledGetResponse,
        )


class AsyncScheduledResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduledResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ToolExecution, AsyncOffsetPage[ToolExecution]]:
        """
        Returns a page of scheduled tool executions

        Args:
          limit: Number of items to return (default: 25, max: 100)

          offset: Offset from the start of the list (default: 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/scheduled_tools",
            page=AsyncOffsetPage[ToolExecution],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    scheduled_list_params.ScheduledListParams,
                ),
            ),
            model=ToolExecution,
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
    ) -> ScheduledGetResponse:
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
            f"/v1/scheduled_tools/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduledGetResponse,
        )


class ScheduledResourceWithRawResponse:
    def __init__(self, scheduled: ScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = to_raw_response_wrapper(
            scheduled.list,
        )
        self.get = to_raw_response_wrapper(
            scheduled.get,
        )


class AsyncScheduledResourceWithRawResponse:
    def __init__(self, scheduled: AsyncScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = async_to_raw_response_wrapper(
            scheduled.list,
        )
        self.get = async_to_raw_response_wrapper(
            scheduled.get,
        )


class ScheduledResourceWithStreamingResponse:
    def __init__(self, scheduled: ScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = to_streamed_response_wrapper(
            scheduled.list,
        )
        self.get = to_streamed_response_wrapper(
            scheduled.get,
        )


class AsyncScheduledResourceWithStreamingResponse:
    def __init__(self, scheduled: AsyncScheduledResource) -> None:
        self._scheduled = scheduled

        self.list = async_to_streamed_response_wrapper(
            scheduled.list,
        )
        self.get = async_to_streamed_response_wrapper(
            scheduled.get,
        )
