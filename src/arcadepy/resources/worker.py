# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import worker_create_params, worker_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.worker_response import WorkerResponse
from ..types.worker_list_response import WorkerListResponse
from ..types.worker_health_response import WorkerHealthResponse

__all__ = ["WorkerResource", "AsyncWorkerResource"]


class WorkerResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorkerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return WorkerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return WorkerResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        enabled: bool,
        http: worker_create_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerResponse:
        """
        Create a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/admin/workers",
            body=maybe_transform(
                {
                    "id": id,
                    "enabled": enabled,
                    "http": http,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerResponse,
        )

    def update(
        self,
        id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        http: worker_update_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerResponse:
        """
        Update a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/admin/workers/{id}",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "http": http,
                },
                worker_update_params.WorkerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerListResponse:
        """List all workers with their definitions"""
        return self._get(
            "/v1/admin/workers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/admin/workers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def health(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerHealthResponse:
        """
        Get the health of a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/admin/workers/{id}/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerHealthResponse,
        )


class AsyncWorkerResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorkerResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkerResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkerResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncWorkerResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        enabled: bool,
        http: worker_create_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerResponse:
        """
        Create a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/admin/workers",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "enabled": enabled,
                    "http": http,
                },
                worker_create_params.WorkerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerResponse,
        )

    async def update(
        self,
        id: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        http: worker_update_params.HTTP | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerResponse:
        """
        Update a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/admin/workers/{id}",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "http": http,
                },
                worker_update_params.WorkerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerListResponse:
        """List all workers with their definitions"""
        return await self._get(
            "/v1/admin/workers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/admin/workers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def health(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WorkerHealthResponse:
        """
        Get the health of a worker

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/admin/workers/{id}/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkerHealthResponse,
        )


class WorkerResourceWithRawResponse:
    def __init__(self, worker: WorkerResource) -> None:
        self._worker = worker

        self.create = to_raw_response_wrapper(
            worker.create,
        )
        self.update = to_raw_response_wrapper(
            worker.update,
        )
        self.list = to_raw_response_wrapper(
            worker.list,
        )
        self.delete = to_raw_response_wrapper(
            worker.delete,
        )
        self.health = to_raw_response_wrapper(
            worker.health,
        )


class AsyncWorkerResourceWithRawResponse:
    def __init__(self, worker: AsyncWorkerResource) -> None:
        self._worker = worker

        self.create = async_to_raw_response_wrapper(
            worker.create,
        )
        self.update = async_to_raw_response_wrapper(
            worker.update,
        )
        self.list = async_to_raw_response_wrapper(
            worker.list,
        )
        self.delete = async_to_raw_response_wrapper(
            worker.delete,
        )
        self.health = async_to_raw_response_wrapper(
            worker.health,
        )


class WorkerResourceWithStreamingResponse:
    def __init__(self, worker: WorkerResource) -> None:
        self._worker = worker

        self.create = to_streamed_response_wrapper(
            worker.create,
        )
        self.update = to_streamed_response_wrapper(
            worker.update,
        )
        self.list = to_streamed_response_wrapper(
            worker.list,
        )
        self.delete = to_streamed_response_wrapper(
            worker.delete,
        )
        self.health = to_streamed_response_wrapper(
            worker.health,
        )


class AsyncWorkerResourceWithStreamingResponse:
    def __init__(self, worker: AsyncWorkerResource) -> None:
        self._worker = worker

        self.create = async_to_streamed_response_wrapper(
            worker.create,
        )
        self.update = async_to_streamed_response_wrapper(
            worker.update,
        )
        self.list = async_to_streamed_response_wrapper(
            worker.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            worker.delete,
        )
        self.health = async_to_streamed_response_wrapper(
            worker.health,
        )
