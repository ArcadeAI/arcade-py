# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncOffsetPage, AsyncOffsetPage
from ...types.tools import formatted_get_params, formatted_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.tools.formatted_get_response import FormattedGetResponse
from ...types.tools.formatted_list_response import FormattedListResponse

__all__ = ["FormattedResource", "AsyncFormattedResource"]


class FormattedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormattedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return FormattedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormattedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return FormattedResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: str | Omit = omit,
        format: str | Omit = omit,
        include_all_versions: bool | Omit = omit,
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
    ) -> SyncOffsetPage[FormattedListResponse]:
        """
        Returns a page of tools from the engine configuration, optionally filtered by
        toolkit, formatted for a specific provider

        Args:
          filter: JSON metadata filter. Array fields (service_domains, operations): shorthand
              array or object with any_of/all_of/none_of operators (case-insensitive). Boolean
              fields: read_only, destructive, idempotent, open_world. Extras: case-sensitive
              key-value subset match.

          format: Provider format

          include_all_versions: Include all versions of each tool

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
            "/v1/formatted_tools",
            page=SyncOffsetPage[FormattedListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "format": format,
                        "include_all_versions": include_all_versions,
                        "limit": limit,
                        "offset": offset,
                        "toolkit": toolkit,
                        "user_id": user_id,
                    },
                    formatted_list_params.FormattedListParams,
                ),
            ),
            model=FormattedListResponse,
        )

    def get(
        self,
        name: str,
        *,
        format: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormattedGetResponse:
        """
        Returns the formatted tool specification for a specific tool, given a provider

        Args:
          format: Provider format

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/v1/formatted_tools/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "format": format,
                        "user_id": user_id,
                    },
                    formatted_get_params.FormattedGetParams,
                ),
            ),
            cast_to=FormattedGetResponse,
        )


class AsyncFormattedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormattedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncFormattedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormattedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncFormattedResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: str | Omit = omit,
        format: str | Omit = omit,
        include_all_versions: bool | Omit = omit,
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
    ) -> AsyncPaginator[FormattedListResponse, AsyncOffsetPage[FormattedListResponse]]:
        """
        Returns a page of tools from the engine configuration, optionally filtered by
        toolkit, formatted for a specific provider

        Args:
          filter: JSON metadata filter. Array fields (service_domains, operations): shorthand
              array or object with any_of/all_of/none_of operators (case-insensitive). Boolean
              fields: read_only, destructive, idempotent, open_world. Extras: case-sensitive
              key-value subset match.

          format: Provider format

          include_all_versions: Include all versions of each tool

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
            "/v1/formatted_tools",
            page=AsyncOffsetPage[FormattedListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "format": format,
                        "include_all_versions": include_all_versions,
                        "limit": limit,
                        "offset": offset,
                        "toolkit": toolkit,
                        "user_id": user_id,
                    },
                    formatted_list_params.FormattedListParams,
                ),
            ),
            model=FormattedListResponse,
        )

    async def get(
        self,
        name: str,
        *,
        format: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FormattedGetResponse:
        """
        Returns the formatted tool specification for a specific tool, given a provider

        Args:
          format: Provider format

          user_id: User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/v1/formatted_tools/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "format": format,
                        "user_id": user_id,
                    },
                    formatted_get_params.FormattedGetParams,
                ),
            ),
            cast_to=FormattedGetResponse,
        )


class FormattedResourceWithRawResponse:
    def __init__(self, formatted: FormattedResource) -> None:
        self._formatted = formatted

        self.list = to_raw_response_wrapper(
            formatted.list,
        )
        self.get = to_raw_response_wrapper(
            formatted.get,
        )


class AsyncFormattedResourceWithRawResponse:
    def __init__(self, formatted: AsyncFormattedResource) -> None:
        self._formatted = formatted

        self.list = async_to_raw_response_wrapper(
            formatted.list,
        )
        self.get = async_to_raw_response_wrapper(
            formatted.get,
        )


class FormattedResourceWithStreamingResponse:
    def __init__(self, formatted: FormattedResource) -> None:
        self._formatted = formatted

        self.list = to_streamed_response_wrapper(
            formatted.list,
        )
        self.get = to_streamed_response_wrapper(
            formatted.get,
        )


class AsyncFormattedResourceWithStreamingResponse:
    def __init__(self, formatted: AsyncFormattedResource) -> None:
        self._formatted = formatted

        self.list = async_to_streamed_response_wrapper(
            formatted.list,
        )
        self.get = async_to_streamed_response_wrapper(
            formatted.get,
        )
