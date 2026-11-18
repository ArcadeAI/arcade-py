# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ...types import (
    tool_get_params,
    tool_list_params,
    tool_execute_params,
    tool_authorize_params,
    tool_requirements_params,
    tool_list_executions_params,
    tool_count_executions_params,
    tool_retrieve_execution_params,
    tool_list_scheduled_in_project_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.tool_requirements_response import ToolRequirementsResponse
from ...types.shared.authorization_response import AuthorizationResponse
from ...types.tool_list_executions_response import ToolListExecutionsResponse
from ...types.tool_count_executions_response import ToolCountExecutionsResponse
from ...types.tool_retrieve_execution_response import ToolRetrieveExecutionResponse
from ...types.tool_list_scheduled_in_project_response import ToolListScheduledInProjectResponse
from ...types.tool_retrieve_scheduled_in_project_response import ToolRetrieveScheduledInProjectResponse

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
        include_format: List[Literal["arcade", "openai", "anthropic"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        toolkit: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        next_uri: str | Omit = omit,
        tool_version: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        include_error_stacktrace: bool | Omit = omit,
        input: Dict[str, object] | Omit = omit,
        run_at: str | Omit = omit,
        tool_version: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecuteToolResponse:
        """
        Executes a tool by name and arguments

        Args:
          include_error_stacktrace: Whether to include the error stacktrace in the response. If not provided, the
              error stacktrace is not included.

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
                    "include_error_stacktrace": include_error_stacktrace,
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
        include_format: List[Literal["arcade", "openai", "anthropic"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def requirements(
        self,
        *,
        authorize: bool | Omit = omit,
        tool_names: SequenceNotStr[str] | Omit = omit,
        tools: List[Dict[str, object]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRequirementsResponse:
        """
        Checks authorization and secret requirements for multiple tools. Optionally starts OAuth flows for unmet auth requirements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/requirements",
            body=maybe_transform(
                {
                    "authorize": authorize,
                    "tool_names": tool_names,
                    "tools": tools,
                    "user_id": user_id,
                },
                tool_requirements_params.ToolRequirementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRequirementsResponse,
        )

    def list_executions(
        self,
        org_id: str,
        project_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        tool_name: str | Omit = omit,
        toolkit_name: str | Omit = omit,
        user_id: str | Omit = omit,
        outcome: Literal["success", "failure"] | Omit = omit,
        failure_reason: str | Omit = omit,
        start_time: str | Omit = omit,
        end_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListExecutionsResponse:
        """
        Returns a paginated list of the project's tool executions

        Args:
          limit: Number of items to return (default: 100, max: 25000)

          offset: Offset from the start of the list (default: 0)

          tool_name: Filter by tool name (case-insensitive substring match)

          toolkit_name: Filter by exact toolkit name

          user_id: Filter by the user the execution ran for

          outcome: Filter by outcome

          failure_reason: Filter to runs with a failed attempt whose error message contains this text (case-insensitive)

          start_time: Only executions recorded at or after this RFC 3339 timestamp

          end_time: Only executions recorded at or before this RFC 3339 timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/tool_executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "tool_name": tool_name,
                        "toolkit_name": toolkit_name,
                        "user_id": user_id,
                        "outcome": outcome,
                        "failure_reason": failure_reason,
                        "start_time": start_time,
                        "end_time": end_time,
                    },
                    tool_list_executions_params.ToolListExecutionsParams,
                ),
            ),
            cast_to=ToolListExecutionsResponse,
        )

    def count_executions(
        self,
        org_id: str,
        project_id: str,
        *,
        tool_name: str | Omit = omit,
        toolkit_name: str | Omit = omit,
        outcome: Literal["success", "failure"] | Omit = omit,
        start_time: str | Omit = omit,
        end_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCountExecutionsResponse:
        """
        Returns the number of the project's tool executions matching the filters

        Args:
          tool_name: Filter by tool name (case-insensitive substring match)

          toolkit_name: Filter by exact toolkit name

          outcome: Filter by outcome

          start_time: Only executions recorded at or after this RFC 3339 timestamp

          end_time: Only executions recorded at or before this RFC 3339 timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/tool_executions/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "tool_name": tool_name,
                        "toolkit_name": toolkit_name,
                        "outcome": outcome,
                        "start_time": start_time,
                        "end_time": end_time,
                    },
                    tool_count_executions_params.ToolCountExecutionsParams,
                ),
            ),
            cast_to=ToolCountExecutionsResponse,
        )

    def retrieve_execution(
        self,
        org_id: str,
        project_id: str,
        id: str,
        *,
        include_inputs: bool | Omit = omit,
        include_outputs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveExecutionResponse:
        """
        Returns the details for a single tool execution

        Args:
          include_inputs: Include the tool inputs in the response (default: false)

          include_outputs: Include the tool outputs in the response (default: false)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/tool_executions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_inputs": include_inputs,
                        "include_outputs": include_outputs,
                    },
                    tool_retrieve_execution_params.ToolRetrieveExecutionParams,
                ),
            ),
            cast_to=ToolRetrieveExecutionResponse,
        )

    def list_scheduled_in_project(
        self,
        org_id: str,
        project_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListScheduledInProjectResponse:
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
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/scheduled_tools",
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
                    tool_list_scheduled_in_project_params.ToolListScheduledInProjectParams,
                ),
            ),
            cast_to=ToolListScheduledInProjectResponse,
        )

    def retrieve_scheduled_in_project(
        self,
        org_id: str,
        project_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveScheduledInProjectResponse:
        """
        Returns the details for a specific scheduled tool execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/scheduled_tools/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveScheduledInProjectResponse,
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
        include_format: List[Literal["arcade", "openai", "anthropic"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        toolkit: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        next_uri: str | Omit = omit,
        tool_version: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        include_error_stacktrace: bool | Omit = omit,
        input: Dict[str, object] | Omit = omit,
        run_at: str | Omit = omit,
        tool_version: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecuteToolResponse:
        """
        Executes a tool by name and arguments

        Args:
          include_error_stacktrace: Whether to include the error stacktrace in the response. If not provided, the
              error stacktrace is not included.

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
                    "include_error_stacktrace": include_error_stacktrace,
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
        include_format: List[Literal["arcade", "openai", "anthropic"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def requirements(
        self,
        *,
        authorize: bool | Omit = omit,
        tool_names: SequenceNotStr[str] | Omit = omit,
        tools: List[Dict[str, object]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRequirementsResponse:
        """
        Checks authorization and secret requirements for multiple tools. Optionally starts OAuth flows for unmet auth requirements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/requirements",
            body=await async_maybe_transform(
                {
                    "authorize": authorize,
                    "tool_names": tool_names,
                    "tools": tools,
                    "user_id": user_id,
                },
                tool_requirements_params.ToolRequirementsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRequirementsResponse,
        )

    async def list_executions(
        self,
        org_id: str,
        project_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        tool_name: str | Omit = omit,
        toolkit_name: str | Omit = omit,
        user_id: str | Omit = omit,
        outcome: Literal["success", "failure"] | Omit = omit,
        failure_reason: str | Omit = omit,
        start_time: str | Omit = omit,
        end_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListExecutionsResponse:
        """
        Returns a paginated list of the project's tool executions

        Args:
          limit: Number of items to return (default: 100, max: 25000)

          offset: Offset from the start of the list (default: 0)

          tool_name: Filter by tool name (case-insensitive substring match)

          toolkit_name: Filter by exact toolkit name

          user_id: Filter by the user the execution ran for

          outcome: Filter by outcome

          failure_reason: Filter to runs with a failed attempt whose error message contains this text (case-insensitive)

          start_time: Only executions recorded at or after this RFC 3339 timestamp

          end_time: Only executions recorded at or before this RFC 3339 timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/tool_executions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "tool_name": tool_name,
                        "toolkit_name": toolkit_name,
                        "user_id": user_id,
                        "outcome": outcome,
                        "failure_reason": failure_reason,
                        "start_time": start_time,
                        "end_time": end_time,
                    },
                    tool_list_executions_params.ToolListExecutionsParams,
                ),
            ),
            cast_to=ToolListExecutionsResponse,
        )

    async def count_executions(
        self,
        org_id: str,
        project_id: str,
        *,
        tool_name: str | Omit = omit,
        toolkit_name: str | Omit = omit,
        outcome: Literal["success", "failure"] | Omit = omit,
        start_time: str | Omit = omit,
        end_time: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolCountExecutionsResponse:
        """
        Returns the number of the project's tool executions matching the filters

        Args:
          tool_name: Filter by tool name (case-insensitive substring match)

          toolkit_name: Filter by exact toolkit name

          outcome: Filter by outcome

          start_time: Only executions recorded at or after this RFC 3339 timestamp

          end_time: Only executions recorded at or before this RFC 3339 timestamp

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/tool_executions/count",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "tool_name": tool_name,
                        "toolkit_name": toolkit_name,
                        "outcome": outcome,
                        "start_time": start_time,
                        "end_time": end_time,
                    },
                    tool_count_executions_params.ToolCountExecutionsParams,
                ),
            ),
            cast_to=ToolCountExecutionsResponse,
        )

    async def retrieve_execution(
        self,
        org_id: str,
        project_id: str,
        id: str,
        *,
        include_inputs: bool | Omit = omit,
        include_outputs: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveExecutionResponse:
        """
        Returns the details for a single tool execution

        Args:
          include_inputs: Include the tool inputs in the response (default: false)

          include_outputs: Include the tool outputs in the response (default: false)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/tool_executions/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_inputs": include_inputs,
                        "include_outputs": include_outputs,
                    },
                    tool_retrieve_execution_params.ToolRetrieveExecutionParams,
                ),
            ),
            cast_to=ToolRetrieveExecutionResponse,
        )

    async def list_scheduled_in_project(
        self,
        org_id: str,
        project_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListScheduledInProjectResponse:
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
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/scheduled_tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    tool_list_scheduled_in_project_params.ToolListScheduledInProjectParams,
                ),
            ),
            cast_to=ToolListScheduledInProjectResponse,
        )

    async def retrieve_scheduled_in_project(
        self,
        org_id: str,
        project_id: str,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolRetrieveScheduledInProjectResponse:
        """
        Returns the details for a specific scheduled tool execution

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/scheduled_tools/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolRetrieveScheduledInProjectResponse,
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
        self.requirements = to_raw_response_wrapper(
            tools.requirements,
        )
        self.list_executions = to_raw_response_wrapper(
            tools.list_executions,
        )
        self.count_executions = to_raw_response_wrapper(
            tools.count_executions,
        )
        self.retrieve_execution = to_raw_response_wrapper(
            tools.retrieve_execution,
        )
        self.list_scheduled_in_project = to_raw_response_wrapper(
            tools.list_scheduled_in_project,
        )
        self.retrieve_scheduled_in_project = to_raw_response_wrapper(
            tools.retrieve_scheduled_in_project,
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
        self.requirements = async_to_raw_response_wrapper(
            tools.requirements,
        )
        self.list_executions = async_to_raw_response_wrapper(
            tools.list_executions,
        )
        self.count_executions = async_to_raw_response_wrapper(
            tools.count_executions,
        )
        self.retrieve_execution = async_to_raw_response_wrapper(
            tools.retrieve_execution,
        )
        self.list_scheduled_in_project = async_to_raw_response_wrapper(
            tools.list_scheduled_in_project,
        )
        self.retrieve_scheduled_in_project = async_to_raw_response_wrapper(
            tools.retrieve_scheduled_in_project,
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
        self.requirements = to_streamed_response_wrapper(
            tools.requirements,
        )
        self.list_executions = to_streamed_response_wrapper(
            tools.list_executions,
        )
        self.count_executions = to_streamed_response_wrapper(
            tools.count_executions,
        )
        self.retrieve_execution = to_streamed_response_wrapper(
            tools.retrieve_execution,
        )
        self.list_scheduled_in_project = to_streamed_response_wrapper(
            tools.list_scheduled_in_project,
        )
        self.retrieve_scheduled_in_project = to_streamed_response_wrapper(
            tools.retrieve_scheduled_in_project,
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
        self.requirements = async_to_streamed_response_wrapper(
            tools.requirements,
        )
        self.list_executions = async_to_streamed_response_wrapper(
            tools.list_executions,
        )
        self.count_executions = async_to_streamed_response_wrapper(
            tools.count_executions,
        )
        self.retrieve_execution = async_to_streamed_response_wrapper(
            tools.retrieve_execution,
        )
        self.list_scheduled_in_project = async_to_streamed_response_wrapper(
            tools.list_scheduled_in_project,
        )
        self.retrieve_scheduled_in_project = async_to_streamed_response_wrapper(
            tools.retrieve_scheduled_in_project,
        )

    @cached_property
    def scheduled(self) -> AsyncScheduledResourceWithStreamingResponse:
        return AsyncScheduledResourceWithStreamingResponse(self._tools.scheduled)

    @cached_property
    def formatted(self) -> AsyncFormattedResourceWithStreamingResponse:
        return AsyncFormattedResourceWithStreamingResponse(self._tools.formatted)
