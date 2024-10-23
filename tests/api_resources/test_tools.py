# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import Response
from arcadepy.pagination import SyncOffsetPage, AsyncOffsetPage
from arcadepy.types.shared import ToolDefinition, AuthorizationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        tool = client.tools.list()
        assert_matches_type(SyncOffsetPage[ToolDefinition], tool, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        tool = client.tools.list(
            limit=0,
            offset=0,
            toolkit="toolkit",
        )
        assert_matches_type(SyncOffsetPage[ToolDefinition], tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(SyncOffsetPage[ToolDefinition], tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(SyncOffsetPage[ToolDefinition], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_authorize(self, client: Arcade) -> None:
        tool = client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    def test_method_authorize_with_all_params(self, client: Arcade) -> None:
        tool = client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
            tool_version="tool_version",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_authorize(self, client: Arcade) -> None:
        response = client.tools.with_raw_response.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_authorize(self, client: Arcade) -> None:
        with client.tools.with_streaming_response.authorize(
            tool_name="tool_name",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(AuthorizationResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: Arcade) -> None:
        tool = client.tools.execute(
            tool_name="tool_name",
        )
        assert_matches_type(Response, tool, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Arcade) -> None:
        tool = client.tools.execute(
            tool_name="tool_name",
            inputs={},
            tool_version="tool_version",
            user_id="user_id",
        )
        assert_matches_type(Response, tool, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Arcade) -> None:
        response = client.tools.with_raw_response.execute(
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Response, tool, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Arcade) -> None:
        with client.tools.with_streaming_response.execute(
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Response, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Arcade) -> None:
        tool = client.tools.get(
            tool_id="toolId",
        )
        assert_matches_type(ToolDefinition, tool, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Arcade) -> None:
        response = client.tools.with_raw_response.get(
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolDefinition, tool, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Arcade) -> None:
        with client.tools.with_streaming_response.get(
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolDefinition, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(AsyncOffsetPage[ToolDefinition], tool, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.list(
            limit=0,
            offset=0,
            toolkit="toolkit",
        )
        assert_matches_type(AsyncOffsetPage[ToolDefinition], tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AsyncOffsetPage[ToolDefinition], tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AsyncOffsetPage[ToolDefinition], tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_authorize(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    async def test_method_authorize_with_all_params(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
            tool_version="tool_version",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.with_raw_response.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.with_streaming_response.authorize(
            tool_name="tool_name",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(AuthorizationResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.execute(
            tool_name="tool_name",
        )
        assert_matches_type(Response, tool, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.execute(
            tool_name="tool_name",
            inputs={},
            tool_version="tool_version",
            user_id="user_id",
        )
        assert_matches_type(Response, tool, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.with_raw_response.execute(
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Response, tool, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.with_streaming_response.execute(
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Response, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncArcade) -> None:
        tool = await async_client.tools.get(
            tool_id="toolId",
        )
        assert_matches_type(ToolDefinition, tool, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.with_raw_response.get(
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolDefinition, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.with_streaming_response.get(
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolDefinition, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
