# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ...types import tool_get_params, tool_list_params, tool_execute_params, tool_authorize_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .formatted import (
    FormattedResource,
    AsyncFormattedResource,
    FormattedResourceWithRawResponse,
    AsyncFormattedResourceWithRawResponse,
    FormattedResourceWithStreamingResponse,
    AsyncFormattedResourceWithStreamingResponse,
)
from .scheduled import (
    ScheduledResource,
    AsyncScheduledResource,
    ScheduledResourceWithRawResponse,
    AsyncScheduledResourceWithRawResponse,
    ScheduledResourceWithStreamingResponse,
    AsyncScheduledResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.tool_definition import ToolDefinition
from ...types.execute_tool_response import ExecuteToolResponse
from ...types.shared.authorization_response import AuthorizationResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def scheduled(self) -> ScheduledResource:
        return ScheduledResource(self._client)

    @cached_property
    def formatted(self) -> FormattedResource:
        return FormattedResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        include_format: List[Literal["arcade", "openai", "anthropic"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        toolkit: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOffsetPage[ToolDefinition]:
        """
        Returns a page of tools from the engine configuration, optionally filtered by
        toolkit

        Args:
          include_format: Comma separated tool formats that will be included in the response.

          limit: Number of items to return (default: 25, max: 100)

          offset: Offset from the start of the list (default: 0)

          toolkit: Toolkit name

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tools",
            page=SyncOffsetPage[ToolDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_format": include_format,
                        "limit": limit,
                        "offset": offset,
                        "toolkit": toolkit,
                        "user_id": user_id,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            model=ToolDefinition,
        )

    def authorize(
        self,
        *,
        tool_name: str,
        next_uri: str | NotGiven = NOT_GIVEN,
        tool_version: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """
        Authorizes a user for a specific tool by name

        Args:
          next_uri: Optional: if provided, the user will be redirected to this URI after
              authorization

          tool_version: Optional: if not provided, any version is used

          user_id: Required only when calling with an API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/authorize",
            body=maybe_transform(
                {
                    "tool_name": tool_name,
                    "next_uri": next_uri,
                    "tool_version": tool_version,
                    "user_id": user_id,
                },
                tool_authorize_params.ToolAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationResponse,
        )

    def execute(
        self,
        *,
        tool_name: str,
        input: Dict[str, object] | NotGiven = NOT_GIVEN,
        run_at: str | NotGiven = NOT_GIVEN,
        tool_version: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteToolResponse:
        """
        Executes a tool by name and arguments

        Args:
          input: JSON input to the tool, if any

          run_at: The time at which the tool should be run (optional). If not provided, the tool
              is run immediately. Format ISO 8601: YYYY-MM-DDTHH:MM:SS

          tool_version: The tool version to use (optional). If not provided, any version is used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/execute",
            body=maybe_transform(
                {
                    "tool_name": tool_name,
                    "input": input,
                    "run_at": run_at,
                    "tool_version": tool_version,
                    "user_id": user_id,
                },
                tool_execute_params.ToolExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteToolResponse,
        )

    def get(
        self,
        name: str,
        *,
        include_format: List[Literal["arcade", "openai", "anthropic"]] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolDefinition:
        """
        Returns the arcade tool specification for a specific tool

        Args:
          include_format: Comma separated tool formats that will be included in the response.

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/v1/tools/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_format": include_format,
                        "user_id": user_id,
                    },
                    tool_get_params.ToolGetParams,
                ),
            ),
            cast_to=ToolDefinition,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def scheduled(self) -> AsyncScheduledResource:
        return AsyncScheduledResource(self._client)

    @cached_property
    def formatted(self) -> AsyncFormattedResource:
        return AsyncFormattedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        include_format: List[Literal["arcade", "openai", "anthropic"]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        toolkit: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ToolDefinition, AsyncOffsetPage[ToolDefinition]]:
        """
        Returns a page of tools from the engine configuration, optionally filtered by
        toolkit

        Args:
          include_format: Comma separated tool formats that will be included in the response.

          limit: Number of items to return (default: 25, max: 100)

          offset: Offset from the start of the list (default: 0)

          toolkit: Toolkit name

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tools",
            page=AsyncOffsetPage[ToolDefinition],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_format": include_format,
                        "limit": limit,
                        "offset": offset,
                        "toolkit": toolkit,
                        "user_id": user_id,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            model=ToolDefinition,
        )

    async def authorize(
        self,
        *,
        tool_name: str,
        next_uri: str | NotGiven = NOT_GIVEN,
        tool_version: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthorizationResponse:
        """
        Authorizes a user for a specific tool by name

        Args:
          next_uri: Optional: if provided, the user will be redirected to this URI after
              authorization

          tool_version: Optional: if not provided, any version is used

          user_id: Required only when calling with an API key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/authorize",
            body=await async_maybe_transform(
                {
                    "tool_name": tool_name,
                    "next_uri": next_uri,
                    "tool_version": tool_version,
                    "user_id": user_id,
                },
                tool_authorize_params.ToolAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationResponse,
        )

    async def execute(
        self,
        *,
        tool_name: str,
        input: Dict[str, object] | NotGiven = NOT_GIVEN,
        run_at: str | NotGiven = NOT_GIVEN,
        tool_version: str | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExecuteToolResponse:
        """
        Executes a tool by name and arguments

        Args:
          input: JSON input to the tool, if any

          run_at: The time at which the tool should be run (optional). If not provided, the tool
              is run immediately. Format ISO 8601: YYYY-MM-DDTHH:MM:SS

          tool_version: The tool version to use (optional). If not provided, any version is used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/execute",
            body=await async_maybe_transform(
                {
                    "tool_name": tool_name,
                    "input": input,
                    "run_at": run_at,
                    "tool_version": tool_version,
                    "user_id": user_id,
                },
                tool_execute_params.ToolExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecuteToolResponse,
        )

    async def get(
        self,
        name: str,
        *,
        include_format: List[Literal["arcade", "openai", "anthropic"]] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolDefinition:
        """
        Returns the arcade tool specification for a specific tool

        Args:
          include_format: Comma separated tool formats that will be included in the response.

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/v1/tools/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_format": include_format,
                        "user_id": user_id,
                    },
                    tool_get_params.ToolGetParams,
                ),
            ),
            cast_to=ToolDefinition,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.authorize = to_raw_response_wrapper(
            tools.authorize,
        )
        self.execute = to_raw_response_wrapper(
            tools.execute,
        )
        self.get = to_raw_response_wrapper(
            tools.get,
        )

    @cached_property
    def scheduled(self) -> ScheduledResourceWithRawResponse:
        return ScheduledResourceWithRawResponse(self._tools.scheduled)

    @cached_property
    def formatted(self) -> FormattedResourceWithRawResponse:
        return FormattedResourceWithRawResponse(self._tools.formatted)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.authorize = async_to_raw_response_wrapper(
            tools.authorize,
        )
        self.execute = async_to_raw_response_wrapper(
            tools.execute,
        )
        self.get = async_to_raw_response_wrapper(
            tools.get,
        )

    @cached_property
    def scheduled(self) -> AsyncScheduledResourceWithRawResponse:
        return AsyncScheduledResourceWithRawResponse(self._tools.scheduled)

    @cached_property
    def formatted(self) -> AsyncFormattedResourceWithRawResponse:
        return AsyncFormattedResourceWithRawResponse(self._tools.formatted)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.authorize = to_streamed_response_wrapper(
            tools.authorize,
        )
        self.execute = to_streamed_response_wrapper(
            tools.execute,
        )
        self.get = to_streamed_response_wrapper(
            tools.get,
        )

    @cached_property
    def scheduled(self) -> ScheduledResourceWithStreamingResponse:
        return ScheduledResourceWithStreamingResponse(self._tools.scheduled)

    @cached_property
    def formatted(self) -> FormattedResourceWithStreamingResponse:
        return FormattedResourceWithStreamingResponse(self._tools.formatted)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.authorize = async_to_streamed_response_wrapper(
            tools.authorize,
        )
        self.execute = async_to_streamed_response_wrapper(
            tools.execute,
        )
        self.get = async_to_streamed_response_wrapper(
            tools.get,
        )

    @cached_property
    def scheduled(self) -> AsyncScheduledResourceWithStreamingResponse:
        return AsyncScheduledResourceWithStreamingResponse(self._tools.scheduled)

    @cached_property
    def formatted(self) -> AsyncFormattedResourceWithStreamingResponse:
        return AsyncFormattedResourceWithStreamingResponse(self._tools.formatted)
