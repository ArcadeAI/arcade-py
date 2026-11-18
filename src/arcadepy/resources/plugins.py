# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import plugin_list_params, plugin_create_params, plugin_update_params
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
from ..types.plugin_list_response import PluginListResponse
from ..types.plugin_create_response import PluginCreateResponse
from ..types.plugin_update_response import PluginUpdateResponse
from ..types.plugin_retrieve_response import PluginRetrieveResponse

__all__ = ["PluginsResource", "AsyncPluginsResource"]


class PluginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PluginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return PluginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PluginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return PluginsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        binding_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginListResponse:
        """
        Returns all plugins for the current binding

        Args:
          limit: Limit

          offset: Offset

          binding_type: Binding type filter (e.g., 'tenant')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/plugins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "binding_type": binding_type,
                    },
                    plugin_list_params.PluginListParams,
                ),
            ),
            cast_to=PluginListResponse,
        )

    def create(
        self,
        *,
        name: str,
        plugin_type: Literal["webhook", "rate_limit"],
        description: str | Omit = omit,
        rate_limit_config: Dict[str, object] | Omit = omit,
        retry: Dict[str, object] | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        webhook_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginCreateResponse:
        """
        Creates a new plugin with optional inline hooks

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/plugins",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "plugin_type": plugin_type,
                    "rate_limit_config": rate_limit_config,
                    "retry": retry,
                    "status": status,
                    "webhook_config": webhook_config,
                },
                plugin_create_params.PluginCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PluginCreateResponse,
        )

    def retrieve(
        self,
        plugin_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginRetrieveResponse:
        """
        Returns a single plugin by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plugin_id:
            raise ValueError(f"Expected a non-empty value for `plugin_id` but received {plugin_id!r}")
        return self._get(
            f"/v1/plugins/{plugin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PluginRetrieveResponse,
        )

    def update(
        self,
        plugin_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rate_limit_config: Dict[str, object] | Omit = omit,
        retry: Dict[str, object] | Omit = omit,
        status: Literal["inactive", "active"] | Omit = omit,
        webhook_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginUpdateResponse:
        """
        Updates an existing plugin configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plugin_id:
            raise ValueError(f"Expected a non-empty value for `plugin_id` but received {plugin_id!r}")
        return self._patch(
            f"/v1/plugins/{plugin_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "rate_limit_config": rate_limit_config,
                    "retry": retry,
                    "status": status,
                    "webhook_config": webhook_config,
                },
                plugin_update_params.PluginUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PluginUpdateResponse,
        )

    def delete(
        self,
        plugin_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a plugin by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plugin_id:
            raise ValueError(f"Expected a non-empty value for `plugin_id` but received {plugin_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/plugins/{plugin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPluginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPluginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncPluginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPluginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncPluginsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        binding_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginListResponse:
        """
        Returns all plugins for the current binding

        Args:
          limit: Limit

          offset: Offset

          binding_type: Binding type filter (e.g., 'tenant')

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/plugins",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "binding_type": binding_type,
                    },
                    plugin_list_params.PluginListParams,
                ),
            ),
            cast_to=PluginListResponse,
        )

    async def create(
        self,
        *,
        name: str,
        plugin_type: Literal["webhook", "rate_limit"],
        description: str | Omit = omit,
        rate_limit_config: Dict[str, object] | Omit = omit,
        retry: Dict[str, object] | Omit = omit,
        status: Literal["active", "inactive"] | Omit = omit,
        webhook_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginCreateResponse:
        """
        Creates a new plugin with optional inline hooks

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/plugins",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "plugin_type": plugin_type,
                    "rate_limit_config": rate_limit_config,
                    "retry": retry,
                    "status": status,
                    "webhook_config": webhook_config,
                },
                plugin_create_params.PluginCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PluginCreateResponse,
        )

    async def retrieve(
        self,
        plugin_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginRetrieveResponse:
        """
        Returns a single plugin by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plugin_id:
            raise ValueError(f"Expected a non-empty value for `plugin_id` but received {plugin_id!r}")
        return await self._get(
            f"/v1/plugins/{plugin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PluginRetrieveResponse,
        )

    async def update(
        self,
        plugin_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        rate_limit_config: Dict[str, object] | Omit = omit,
        retry: Dict[str, object] | Omit = omit,
        status: Literal["inactive", "active"] | Omit = omit,
        webhook_config: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PluginUpdateResponse:
        """
        Updates an existing plugin configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plugin_id:
            raise ValueError(f"Expected a non-empty value for `plugin_id` but received {plugin_id!r}")
        return await self._patch(
            f"/v1/plugins/{plugin_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "rate_limit_config": rate_limit_config,
                    "retry": retry,
                    "status": status,
                    "webhook_config": webhook_config,
                },
                plugin_update_params.PluginUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PluginUpdateResponse,
        )

    async def delete(
        self,
        plugin_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a plugin by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plugin_id:
            raise ValueError(f"Expected a non-empty value for `plugin_id` but received {plugin_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/plugins/{plugin_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PluginsResourceWithRawResponse:
    def __init__(self, plugins: PluginsResource) -> None:
        self._plugins = plugins

        self.list = to_raw_response_wrapper(
            plugins.list,
        )
        self.create = to_raw_response_wrapper(
            plugins.create,
        )
        self.retrieve = to_raw_response_wrapper(
            plugins.retrieve,
        )
        self.update = to_raw_response_wrapper(
            plugins.update,
        )
        self.delete = to_raw_response_wrapper(
            plugins.delete,
        )


class AsyncPluginsResourceWithRawResponse:
    def __init__(self, plugins: AsyncPluginsResource) -> None:
        self._plugins = plugins

        self.list = async_to_raw_response_wrapper(
            plugins.list,
        )
        self.create = async_to_raw_response_wrapper(
            plugins.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            plugins.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            plugins.update,
        )
        self.delete = async_to_raw_response_wrapper(
            plugins.delete,
        )


class PluginsResourceWithStreamingResponse:
    def __init__(self, plugins: PluginsResource) -> None:
        self._plugins = plugins

        self.list = to_streamed_response_wrapper(
            plugins.list,
        )
        self.create = to_streamed_response_wrapper(
            plugins.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            plugins.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            plugins.update,
        )
        self.delete = to_streamed_response_wrapper(
            plugins.delete,
        )


class AsyncPluginsResourceWithStreamingResponse:
    def __init__(self, plugins: AsyncPluginsResource) -> None:
        self._plugins = plugins

        self.list = async_to_streamed_response_wrapper(
            plugins.list,
        )
        self.create = async_to_streamed_response_wrapper(
            plugins.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            plugins.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            plugins.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            plugins.delete,
        )
