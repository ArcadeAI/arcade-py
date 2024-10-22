# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFormatted:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        formatted = client.tools.formatted.list()
        assert_matches_type(SyncOffsetPage[object], formatted, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        formatted = client.tools.formatted.list(
            format="format",
            limit=0,
            offset=0,
            toolkit="toolkit",
        )
        assert_matches_type(SyncOffsetPage[object], formatted, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.tools.formatted.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formatted = response.parse()
        assert_matches_type(SyncOffsetPage[object], formatted, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.tools.formatted.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formatted = response.parse()
            assert_matches_type(SyncOffsetPage[object], formatted, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Arcade) -> None:
        formatted = client.tools.formatted.get(
            tool_id="toolId",
        )
        assert_matches_type(object, formatted, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Arcade) -> None:
        formatted = client.tools.formatted.get(
            tool_id="toolId",
            format="format",
        )
        assert_matches_type(object, formatted, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Arcade) -> None:
        response = client.tools.formatted.with_raw_response.get(
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formatted = response.parse()
        assert_matches_type(object, formatted, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Arcade) -> None:
        with client.tools.formatted.with_streaming_response.get(
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formatted = response.parse()
            assert_matches_type(object, formatted, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFormatted:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        formatted = await async_client.tools.formatted.list()
        assert_matches_type(AsyncOffsetPage[object], formatted, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        formatted = await async_client.tools.formatted.list(
            format="format",
            limit=0,
            offset=0,
            toolkit="toolkit",
        )
        assert_matches_type(AsyncOffsetPage[object], formatted, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.formatted.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formatted = await response.parse()
        assert_matches_type(AsyncOffsetPage[object], formatted, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.formatted.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formatted = await response.parse()
            assert_matches_type(AsyncOffsetPage[object], formatted, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncArcade) -> None:
        formatted = await async_client.tools.formatted.get(
            tool_id="toolId",
        )
        assert_matches_type(object, formatted, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncArcade) -> None:
        formatted = await async_client.tools.formatted.get(
            tool_id="toolId",
            format="format",
        )
        assert_matches_type(object, formatted, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.formatted.with_raw_response.get(
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        formatted = await response.parse()
        assert_matches_type(object, formatted, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.formatted.with_streaming_response.get(
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            formatted = await response.parse()
            assert_matches_type(object, formatted, path=["response"])

        assert cast(Any, response.is_closed) is True
