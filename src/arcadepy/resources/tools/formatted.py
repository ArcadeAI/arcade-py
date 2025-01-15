# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tools import formatted_get_params
from ..._base_client import make_request_options

__all__ = ["FormattedResource", "AsyncFormattedResource"]


class FormattedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormattedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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

    def get(
        self,
        name: str,
        *,
        format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Returns the formatted tool specification for a specific tool, given a provider

        Args:
          format: Provider format

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
                query=maybe_transform({"format": format}, formatted_get_params.FormattedGetParams),
            ),
            cast_to=object,
        )


class AsyncFormattedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormattedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
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

    async def get(
        self,
        name: str,
        *,
        format: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Returns the formatted tool specification for a specific tool, given a provider

        Args:
          format: Provider format

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
                query=await async_maybe_transform({"format": format}, formatted_get_params.FormattedGetParams),
            ),
            cast_to=object,
        )


class FormattedResourceWithRawResponse:
    def __init__(self, formatted: FormattedResource) -> None:
        self._formatted = formatted

        self.get = to_raw_response_wrapper(
            formatted.get,
        )


class AsyncFormattedResourceWithRawResponse:
    def __init__(self, formatted: AsyncFormattedResource) -> None:
        self._formatted = formatted

        self.get = async_to_raw_response_wrapper(
            formatted.get,
        )


class FormattedResourceWithStreamingResponse:
    def __init__(self, formatted: FormattedResource) -> None:
        self._formatted = formatted

        self.get = to_streamed_response_wrapper(
            formatted.get,
        )


class AsyncFormattedResourceWithStreamingResponse:
    def __init__(self, formatted: AsyncFormattedResource) -> None:
        self._formatted = formatted

        self.get = async_to_streamed_response_wrapper(
            formatted.get,
        )
