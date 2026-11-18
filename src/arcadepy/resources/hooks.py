# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import (
    hook_list_params,
    hook_create_params,
    hook_update_params,
    hook_retrieve_params,
    hook_bulk_upsert_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.hook_list_response import HookListResponse
from ..types.hook_create_response import HookCreateResponse
from ..types.hook_update_response import HookUpdateResponse
from ..types.hook_retrieve_response import HookRetrieveResponse
from ..types.hook_bulk_upsert_response import HookBulkUpsertResponse

__all__ = ["HooksResource", "AsyncHooksResource"]


class HooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return HooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return HooksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        hook_point: str | Omit = omit,
        plugin_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookListResponse:
        """
        Returns all hooks for the current binding with optional filtering

        Args:
          limit: Limit

          offset: Offset

          hook_point: Filter by hook point

          plugin_id: Filter by plugin ID

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/hooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "hook_point": hook_point,
                        "plugin_id": plugin_id,
                        "status": status,
                    },
                    hook_list_params.HookListParams,
                ),
            ),
            cast_to=HookListResponse,
        )

    def create(
        self,
        *,
        failure_mode: Literal["fail_closed", "fail_open"],
        hook_point: Literal["tool.access", "tool.pre", "tool.post"],
        name: str,
        phase: Literal["before", "after"],
        plugin_id: str,
        priority: int | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookCreateResponse:
        """
        Creates a new hook configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/hooks",
            body=maybe_transform(
                {
                    "failure_mode": failure_mode,
                    "hook_point": hook_point,
                    "name": name,
                    "phase": phase,
                    "plugin_id": plugin_id,
                    "priority": priority,
                    "status": status,
                    "timeout_ms": timeout_ms,
                },
                hook_create_params.HookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HookCreateResponse,
        )

    def bulk_upsert(
        self,
        *,
        configs: List[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookBulkUpsertResponse:
        """
        Creates or updates multiple hooks at once. The operation is transactional.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/v1/hooks/bulk",
            body=maybe_transform(
                {
                    "configs": configs,
                },
                hook_bulk_upsert_params.HookBulkUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HookBulkUpsertResponse,
        )

    def retrieve(
        self,
        hook_id: str,
        *,
        binding_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookRetrieveResponse:
        """
        Returns a single hook by ID

        Args:
          binding_type: Filter by binding type (tenant or project)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hook_id:
            raise ValueError(f"Expected a non-empty value for `hook_id` but received {hook_id!r}")
        return self._get(
            f"/v1/hooks/{hook_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "binding_type": binding_type,
                    },
                    hook_retrieve_params.HookRetrieveParams,
                ),
            ),
            cast_to=HookRetrieveResponse,
        )

    def update(
        self,
        hook_id: str,
        *,
        failure_mode: Literal["fail_closed", "fail_open"] | Omit = omit,
        phase: Literal["before", "after"] | Omit = omit,
        priority: int | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookUpdateResponse:
        """
        Updates an existing hook configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hook_id:
            raise ValueError(f"Expected a non-empty value for `hook_id` but received {hook_id!r}")
        return self._patch(
            f"/v1/hooks/{hook_id}",
            body=maybe_transform(
                {
                    "failure_mode": failure_mode,
                    "phase": phase,
                    "priority": priority,
                    "status": status,
                    "timeout_ms": timeout_ms,
                },
                hook_update_params.HookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HookUpdateResponse,
        )

    def delete(
        self,
        hook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a hook by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hook_id:
            raise ValueError(f"Expected a non-empty value for `hook_id` but received {hook_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/hooks/{hook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncHooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncHooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncHooksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        hook_point: str | Omit = omit,
        plugin_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookListResponse:
        """
        Returns all hooks for the current binding with optional filtering

        Args:
          limit: Limit

          offset: Offset

          hook_point: Filter by hook point

          plugin_id: Filter by plugin ID

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/hooks",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "hook_point": hook_point,
                        "plugin_id": plugin_id,
                        "status": status,
                    },
                    hook_list_params.HookListParams,
                ),
            ),
            cast_to=HookListResponse,
        )

    async def create(
        self,
        *,
        failure_mode: Literal["fail_closed", "fail_open"],
        hook_point: Literal["tool.access", "tool.pre", "tool.post"],
        name: str,
        phase: Literal["before", "after"],
        plugin_id: str,
        priority: int | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookCreateResponse:
        """
        Creates a new hook configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/hooks",
            body=await async_maybe_transform(
                {
                    "failure_mode": failure_mode,
                    "hook_point": hook_point,
                    "name": name,
                    "phase": phase,
                    "plugin_id": plugin_id,
                    "priority": priority,
                    "status": status,
                    "timeout_ms": timeout_ms,
                },
                hook_create_params.HookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HookCreateResponse,
        )

    async def bulk_upsert(
        self,
        *,
        configs: List[Dict[str, object]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookBulkUpsertResponse:
        """
        Creates or updates multiple hooks at once. The operation is transactional.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/v1/hooks/bulk",
            body=await async_maybe_transform(
                {
                    "configs": configs,
                },
                hook_bulk_upsert_params.HookBulkUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HookBulkUpsertResponse,
        )

    async def retrieve(
        self,
        hook_id: str,
        *,
        binding_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookRetrieveResponse:
        """
        Returns a single hook by ID

        Args:
          binding_type: Filter by binding type (tenant or project)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hook_id:
            raise ValueError(f"Expected a non-empty value for `hook_id` but received {hook_id!r}")
        return await self._get(
            f"/v1/hooks/{hook_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "binding_type": binding_type,
                    },
                    hook_retrieve_params.HookRetrieveParams,
                ),
            ),
            cast_to=HookRetrieveResponse,
        )

    async def update(
        self,
        hook_id: str,
        *,
        failure_mode: Literal["fail_closed", "fail_open"] | Omit = omit,
        phase: Literal["before", "after"] | Omit = omit,
        priority: int | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HookUpdateResponse:
        """
        Updates an existing hook configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hook_id:
            raise ValueError(f"Expected a non-empty value for `hook_id` but received {hook_id!r}")
        return await self._patch(
            f"/v1/hooks/{hook_id}",
            body=await async_maybe_transform(
                {
                    "failure_mode": failure_mode,
                    "phase": phase,
                    "priority": priority,
                    "status": status,
                    "timeout_ms": timeout_ms,
                },
                hook_update_params.HookUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HookUpdateResponse,
        )

    async def delete(
        self,
        hook_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a hook by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hook_id:
            raise ValueError(f"Expected a non-empty value for `hook_id` but received {hook_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/hooks/{hook_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class HooksResourceWithRawResponse:
    def __init__(self, hooks: HooksResource) -> None:
        self._hooks = hooks

        self.list = to_raw_response_wrapper(
            hooks.list,
        )
        self.create = to_raw_response_wrapper(
            hooks.create,
        )
        self.bulk_upsert = to_raw_response_wrapper(
            hooks.bulk_upsert,
        )
        self.retrieve = to_raw_response_wrapper(
            hooks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            hooks.update,
        )
        self.delete = to_raw_response_wrapper(
            hooks.delete,
        )


class AsyncHooksResourceWithRawResponse:
    def __init__(self, hooks: AsyncHooksResource) -> None:
        self._hooks = hooks

        self.list = async_to_raw_response_wrapper(
            hooks.list,
        )
        self.create = async_to_raw_response_wrapper(
            hooks.create,
        )
        self.bulk_upsert = async_to_raw_response_wrapper(
            hooks.bulk_upsert,
        )
        self.retrieve = async_to_raw_response_wrapper(
            hooks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            hooks.update,
        )
        self.delete = async_to_raw_response_wrapper(
            hooks.delete,
        )


class HooksResourceWithStreamingResponse:
    def __init__(self, hooks: HooksResource) -> None:
        self._hooks = hooks

        self.list = to_streamed_response_wrapper(
            hooks.list,
        )
        self.create = to_streamed_response_wrapper(
            hooks.create,
        )
        self.bulk_upsert = to_streamed_response_wrapper(
            hooks.bulk_upsert,
        )
        self.retrieve = to_streamed_response_wrapper(
            hooks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            hooks.update,
        )
        self.delete = to_streamed_response_wrapper(
            hooks.delete,
        )


class AsyncHooksResourceWithStreamingResponse:
    def __init__(self, hooks: AsyncHooksResource) -> None:
        self._hooks = hooks

        self.list = async_to_streamed_response_wrapper(
            hooks.list,
        )
        self.create = async_to_streamed_response_wrapper(
            hooks.create,
        )
        self.bulk_upsert = async_to_streamed_response_wrapper(
            hooks.bulk_upsert,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            hooks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            hooks.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            hooks.delete,
        )
