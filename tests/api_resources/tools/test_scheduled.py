# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types.tools import ScheduledListResponse, ScheduledDetailsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduled:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        scheduled = client.tools.scheduled.list()
        assert_matches_type(ScheduledListResponse, scheduled, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.tools.scheduled.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled = response.parse()
        assert_matches_type(ScheduledListResponse, scheduled, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.tools.scheduled.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled = response.parse()
            assert_matches_type(ScheduledListResponse, scheduled, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_details(self, client: Arcade) -> None:
        scheduled = client.tools.scheduled.details(
            "id",
        )
        assert_matches_type(ScheduledDetailsResponse, scheduled, path=["response"])

    @parametrize
    def test_raw_response_details(self, client: Arcade) -> None:
        response = client.tools.scheduled.with_raw_response.details(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled = response.parse()
        assert_matches_type(ScheduledDetailsResponse, scheduled, path=["response"])

    @parametrize
    def test_streaming_response_details(self, client: Arcade) -> None:
        with client.tools.scheduled.with_streaming_response.details(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled = response.parse()
            assert_matches_type(ScheduledDetailsResponse, scheduled, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_details(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tools.scheduled.with_raw_response.details(
                "",
            )


class TestAsyncScheduled:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        scheduled = await async_client.tools.scheduled.list()
        assert_matches_type(ScheduledListResponse, scheduled, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.scheduled.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled = await response.parse()
        assert_matches_type(ScheduledListResponse, scheduled, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.scheduled.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled = await response.parse()
            assert_matches_type(ScheduledListResponse, scheduled, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_details(self, async_client: AsyncArcade) -> None:
        scheduled = await async_client.tools.scheduled.details(
            "id",
        )
        assert_matches_type(ScheduledDetailsResponse, scheduled, path=["response"])

    @parametrize
    async def test_raw_response_details(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.scheduled.with_raw_response.details(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scheduled = await response.parse()
        assert_matches_type(ScheduledDetailsResponse, scheduled, path=["response"])

    @parametrize
    async def test_streaming_response_details(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.scheduled.with_streaming_response.details(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scheduled = await response.parse()
            assert_matches_type(ScheduledDetailsResponse, scheduled, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_details(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tools.scheduled.with_raw_response.details(
                "",
            )
