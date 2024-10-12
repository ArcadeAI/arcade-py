# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tool_execute_params, tool_authorize_params, tool_definition_params
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
from ..types.definition import Definition
from ..types.tool_response import ToolResponse
from ..types.shared.authorization_response import AuthorizationResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def authorize(
        self,
        *,
        tool_name: str,
        user_id: str,
        tool_version: str | NotGiven = NOT_GIVEN,
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
          tool_version: Optional: if not provided, latest version is assumed

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
                    "user_id": user_id,
                    "tool_version": tool_version,
                },
                tool_authorize_params.ToolAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationResponse,
        )

    def definition(
        self,
        *,
        director_id: str,
        tool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Definition:
        """
        Returns the arcade tool specification for a specific tool

        Args:
          director_id: Director ID

          tool_id: Tool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/tools/definition",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "director_id": director_id,
                        "tool_id": tool_id,
                    },
                    tool_definition_params.ToolDefinitionParams,
                ),
            ),
            cast_to=Definition,
        )

    def execute(
        self,
        *,
        inputs: str,
        tool_name: str,
        tool_version: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolResponse:
        """
        Executes a tool by name and arguments

        Args:
          inputs: Serialized JSON string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/execute",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "tool_name": tool_name,
                    "tool_version": tool_version,
                    "user_id": user_id,
                },
                tool_execute_params.ToolExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/arcade-engine-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def authorize(
        self,
        *,
        tool_name: str,
        user_id: str,
        tool_version: str | NotGiven = NOT_GIVEN,
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
          tool_version: Optional: if not provided, latest version is assumed

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
                    "user_id": user_id,
                    "tool_version": tool_version,
                },
                tool_authorize_params.ToolAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthorizationResponse,
        )

    async def definition(
        self,
        *,
        director_id: str,
        tool_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Definition:
        """
        Returns the arcade tool specification for a specific tool

        Args:
          director_id: Director ID

          tool_id: Tool ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/tools/definition",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "director_id": director_id,
                        "tool_id": tool_id,
                    },
                    tool_definition_params.ToolDefinitionParams,
                ),
            ),
            cast_to=Definition,
        )

    async def execute(
        self,
        *,
        inputs: str,
        tool_name: str,
        tool_version: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolResponse:
        """
        Executes a tool by name and arguments

        Args:
          inputs: Serialized JSON string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/execute",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "tool_name": tool_name,
                    "tool_version": tool_version,
                    "user_id": user_id,
                },
                tool_execute_params.ToolExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.authorize = to_raw_response_wrapper(
            tools.authorize,
        )
        self.definition = to_raw_response_wrapper(
            tools.definition,
        )
        self.execute = to_raw_response_wrapper(
            tools.execute,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.authorize = async_to_raw_response_wrapper(
            tools.authorize,
        )
        self.definition = async_to_raw_response_wrapper(
            tools.definition,
        )
        self.execute = async_to_raw_response_wrapper(
            tools.execute,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.authorize = to_streamed_response_wrapper(
            tools.authorize,
        )
        self.definition = to_streamed_response_wrapper(
            tools.definition,
        )
        self.execute = to_streamed_response_wrapper(
            tools.execute,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.authorize = async_to_streamed_response_wrapper(
            tools.authorize,
        )
        self.definition = async_to_streamed_response_wrapper(
            tools.definition,
        )
        self.execute = async_to_streamed_response_wrapper(
            tools.execute,
        )
