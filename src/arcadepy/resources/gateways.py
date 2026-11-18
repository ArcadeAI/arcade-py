# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import (
    gateway_list_params,
    gateway_create_params,
    gateway_update_params,
    gateway_replace_params,
    gateway_slug_info_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.gateway_list_response import GatewayListResponse
from ..types.gateway_create_response import GatewayCreateResponse
from ..types.gateway_update_response import GatewayUpdateResponse
from ..types.gateway_replace_response import GatewayReplaceResponse
from ..types.gateway_retrieve_response import GatewayRetrieveResponse
from ..types.gateway_slug_info_response import GatewaySlugInfoResponse

__all__ = ["GatewaysResource", "AsyncGatewaysResource"]


class GatewaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return GatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return GatewaysResourceWithStreamingResponse(self)

    def list(
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
    ) -> GatewayListResponse:
        """
        Returns a paginated list of gateways for the current project

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
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways",
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
                    gateway_list_params.GatewayListParams,
                ),
            ),
            cast_to=GatewayListResponse,
        )

    def create(
        self,
        org_id: str,
        project_id: str,
        *,
        name: str,
        allowed_passthrough_headers: SequenceNotStr[str] | Omit = omit,
        auth_type: Literal["arcade", "arcade_header", "user_source"] | Omit = omit,
        consent_skip_client_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        slug: str | Omit = omit,
        status: str | Omit = omit,
        tool_filter: Dict[str, object] | Omit = omit,
        user_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayCreateResponse:
        """
        Creates a new gateway in the current project

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
        return self._post(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways",
            body=maybe_transform(
                {
                    "allowed_passthrough_headers": allowed_passthrough_headers,
                    "auth_type": auth_type,
                    "consent_skip_client_ids": consent_skip_client_ids,
                    "description": description,
                    "instructions": instructions,
                    "name": name,
                    "slug": slug,
                    "status": status,
                    "tool_filter": tool_filter,
                    "user_source_id": user_source_id,
                },
                gateway_create_params.GatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayCreateResponse,
        )

    def slug_info(
        self,
        org_id: str,
        project_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewaySlugInfoResponse:
        """
        Checks whether a gateway slug is available for use

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
        return self._post(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/slug",
            body=maybe_transform(
                {
                    "slug": slug,
                },
                gateway_slug_info_params.GatewaySlugInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewaySlugInfoResponse,
        )

    def retrieve(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayRetrieveResponse:
        """
        Returns a single gateway by ID

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayRetrieveResponse,
        )

    def replace(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        id: str,
        name: str,
        allowed_passthrough_headers: SequenceNotStr[str] | Omit = omit,
        auth_type: Literal["arcade", "arcade_header", "user_source"] | Omit = omit,
        consent_skip_client_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        slug: str | Omit = omit,
        status: str | Omit = omit,
        tool_filter: Dict[str, object] | Omit = omit,
        user_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayReplaceResponse:
        """
        Replaces the full configuration of an existing gateway

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._put(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            body=maybe_transform(
                {
                    "allowed_passthrough_headers": allowed_passthrough_headers,
                    "auth_type": auth_type,
                    "consent_skip_client_ids": consent_skip_client_ids,
                    "description": description,
                    "id": id,
                    "instructions": instructions,
                    "name": name,
                    "slug": slug,
                    "status": status,
                    "tool_filter": tool_filter,
                    "user_source_id": user_source_id,
                },
                gateway_replace_params.GatewayReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayReplaceResponse,
        )

    def update(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        allowed_passthrough_headers: SequenceNotStr[str] | Omit = omit,
        auth_type: Literal["arcade", "arcade_header", "user_source"] | Omit = omit,
        consent_skip_client_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        status: str | Omit = omit,
        tool_filter: Dict[str, object] | Omit = omit,
        user_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayUpdateResponse:
        """
        Partially updates an existing gateway configuration

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return self._patch(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            body=maybe_transform(
                {
                    "allowed_passthrough_headers": allowed_passthrough_headers,
                    "auth_type": auth_type,
                    "consent_skip_client_ids": consent_skip_client_ids,
                    "description": description,
                    "instructions": instructions,
                    "name": name,
                    "slug": slug,
                    "status": status,
                    "tool_filter": tool_filter,
                    "user_source_id": user_source_id,
                },
                gateway_update_params.GatewayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayUpdateResponse,
        )

    def delete(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a gateway by ID

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGatewaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#accessing-raw-response-data-eg-headers
        """
        return AsyncGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/ArcadeAI/arcade-py#with_streaming_response
        """
        return AsyncGatewaysResourceWithStreamingResponse(self)

    async def list(
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
    ) -> GatewayListResponse:
        """
        Returns a paginated list of gateways for the current project

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
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways",
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
                    gateway_list_params.GatewayListParams,
                ),
            ),
            cast_to=GatewayListResponse,
        )

    async def create(
        self,
        org_id: str,
        project_id: str,
        *,
        name: str,
        allowed_passthrough_headers: SequenceNotStr[str] | Omit = omit,
        auth_type: Literal["arcade", "arcade_header", "user_source"] | Omit = omit,
        consent_skip_client_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        slug: str | Omit = omit,
        status: str | Omit = omit,
        tool_filter: Dict[str, object] | Omit = omit,
        user_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayCreateResponse:
        """
        Creates a new gateway in the current project

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
        return await self._post(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways",
            body=await async_maybe_transform(
                {
                    "allowed_passthrough_headers": allowed_passthrough_headers,
                    "auth_type": auth_type,
                    "consent_skip_client_ids": consent_skip_client_ids,
                    "description": description,
                    "instructions": instructions,
                    "name": name,
                    "slug": slug,
                    "status": status,
                    "tool_filter": tool_filter,
                    "user_source_id": user_source_id,
                },
                gateway_create_params.GatewayCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayCreateResponse,
        )

    async def slug_info(
        self,
        org_id: str,
        project_id: str,
        *,
        slug: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewaySlugInfoResponse:
        """
        Checks whether a gateway slug is available for use

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
        return await self._post(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/slug",
            body=await async_maybe_transform(
                {
                    "slug": slug,
                },
                gateway_slug_info_params.GatewaySlugInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewaySlugInfoResponse,
        )

    async def retrieve(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayRetrieveResponse:
        """
        Returns a single gateway by ID

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return await self._get(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayRetrieveResponse,
        )

    async def replace(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        id: str,
        name: str,
        allowed_passthrough_headers: SequenceNotStr[str] | Omit = omit,
        auth_type: Literal["arcade", "arcade_header", "user_source"] | Omit = omit,
        consent_skip_client_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        slug: str | Omit = omit,
        status: str | Omit = omit,
        tool_filter: Dict[str, object] | Omit = omit,
        user_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayReplaceResponse:
        """
        Replaces the full configuration of an existing gateway

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return await self._put(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            body=await async_maybe_transform(
                {
                    "allowed_passthrough_headers": allowed_passthrough_headers,
                    "auth_type": auth_type,
                    "consent_skip_client_ids": consent_skip_client_ids,
                    "description": description,
                    "id": id,
                    "instructions": instructions,
                    "name": name,
                    "slug": slug,
                    "status": status,
                    "tool_filter": tool_filter,
                    "user_source_id": user_source_id,
                },
                gateway_replace_params.GatewayReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayReplaceResponse,
        )

    async def update(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        allowed_passthrough_headers: SequenceNotStr[str] | Omit = omit,
        auth_type: Literal["arcade", "arcade_header", "user_source"] | Omit = omit,
        consent_skip_client_ids: SequenceNotStr[str] | Omit = omit,
        description: str | Omit = omit,
        instructions: str | Omit = omit,
        name: str | Omit = omit,
        slug: str | Omit = omit,
        status: str | Omit = omit,
        tool_filter: Dict[str, object] | Omit = omit,
        user_source_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GatewayUpdateResponse:
        """
        Partially updates an existing gateway configuration

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        return await self._patch(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            body=await async_maybe_transform(
                {
                    "allowed_passthrough_headers": allowed_passthrough_headers,
                    "auth_type": auth_type,
                    "consent_skip_client_ids": consent_skip_client_ids,
                    "description": description,
                    "instructions": instructions,
                    "name": name,
                    "slug": slug,
                    "status": status,
                    "tool_filter": tool_filter,
                    "user_source_id": user_source_id,
                },
                gateway_update_params.GatewayUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GatewayUpdateResponse,
        )

    async def delete(
        self,
        org_id: str,
        project_id: str,
        gateway_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a gateway by ID

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
        if not gateway_id:
            raise ValueError(f"Expected a non-empty value for `gateway_id` but received {gateway_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/orgs/{org_id}/projects/{project_id}/gateways/{gateway_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GatewaysResourceWithRawResponse:
    def __init__(self, gateways: GatewaysResource) -> None:
        self._gateways = gateways

        self.list = to_raw_response_wrapper(
            gateways.list,
        )
        self.create = to_raw_response_wrapper(
            gateways.create,
        )
        self.slug_info = to_raw_response_wrapper(
            gateways.slug_info,
        )
        self.retrieve = to_raw_response_wrapper(
            gateways.retrieve,
        )
        self.replace = to_raw_response_wrapper(
            gateways.replace,
        )
        self.update = to_raw_response_wrapper(
            gateways.update,
        )
        self.delete = to_raw_response_wrapper(
            gateways.delete,
        )


class AsyncGatewaysResourceWithRawResponse:
    def __init__(self, gateways: AsyncGatewaysResource) -> None:
        self._gateways = gateways

        self.list = async_to_raw_response_wrapper(
            gateways.list,
        )
        self.create = async_to_raw_response_wrapper(
            gateways.create,
        )
        self.slug_info = async_to_raw_response_wrapper(
            gateways.slug_info,
        )
        self.retrieve = async_to_raw_response_wrapper(
            gateways.retrieve,
        )
        self.replace = async_to_raw_response_wrapper(
            gateways.replace,
        )
        self.update = async_to_raw_response_wrapper(
            gateways.update,
        )
        self.delete = async_to_raw_response_wrapper(
            gateways.delete,
        )


class GatewaysResourceWithStreamingResponse:
    def __init__(self, gateways: GatewaysResource) -> None:
        self._gateways = gateways

        self.list = to_streamed_response_wrapper(
            gateways.list,
        )
        self.create = to_streamed_response_wrapper(
            gateways.create,
        )
        self.slug_info = to_streamed_response_wrapper(
            gateways.slug_info,
        )
        self.retrieve = to_streamed_response_wrapper(
            gateways.retrieve,
        )
        self.replace = to_streamed_response_wrapper(
            gateways.replace,
        )
        self.update = to_streamed_response_wrapper(
            gateways.update,
        )
        self.delete = to_streamed_response_wrapper(
            gateways.delete,
        )


class AsyncGatewaysResourceWithStreamingResponse:
    def __init__(self, gateways: AsyncGatewaysResource) -> None:
        self._gateways = gateways

        self.list = async_to_streamed_response_wrapper(
            gateways.list,
        )
        self.create = async_to_streamed_response_wrapper(
            gateways.create,
        )
        self.slug_info = async_to_streamed_response_wrapper(
            gateways.slug_info,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            gateways.retrieve,
        )
        self.replace = async_to_streamed_response_wrapper(
            gateways.replace,
        )
        self.update = async_to_streamed_response_wrapper(
            gateways.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            gateways.delete,
        )
