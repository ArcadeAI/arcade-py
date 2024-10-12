# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from arcade_engine import ArcadeEngine, AsyncArcadeEngine
from arcade_engine.types import (
    Definition,
    ToolResponse,
)
from arcade_engine.types.shared import AuthorizationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_authorize(self, client: ArcadeEngine) -> None:
        tool = client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    def test_method_authorize_with_all_params(self, client: ArcadeEngine) -> None:
        tool = client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
            tool_version="tool_version",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_authorize(self, client: ArcadeEngine) -> None:
        response = client.tools.with_raw_response.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_authorize(self, client: ArcadeEngine) -> None:
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
    def test_method_definition(self, client: ArcadeEngine) -> None:
        tool = client.tools.definition(
            director_id="director_id",
            tool_id="tool_id",
        )
        assert_matches_type(Definition, tool, path=["response"])

    @parametrize
    def test_raw_response_definition(self, client: ArcadeEngine) -> None:
        response = client.tools.with_raw_response.definition(
            director_id="director_id",
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Definition, tool, path=["response"])

    @parametrize
    def test_streaming_response_definition(self, client: ArcadeEngine) -> None:
        with client.tools.with_streaming_response.definition(
            director_id="director_id",
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Definition, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_execute(self, client: ArcadeEngine) -> None:
        tool = client.tools.execute(
            inputs="inputs",
            tool_name="tool_name",
            tool_version="tool_version",
            user_id="user_id",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: ArcadeEngine) -> None:
        response = client.tools.with_raw_response.execute(
            inputs="inputs",
            tool_name="tool_name",
            tool_version="tool_version",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: ArcadeEngine) -> None:
        with client.tools.with_streaming_response.execute(
            inputs="inputs",
            tool_name="tool_name",
            tool_version="tool_version",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_authorize(self, async_client: AsyncArcadeEngine) -> None:
        tool = await async_client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    async def test_method_authorize_with_all_params(self, async_client: AsyncArcadeEngine) -> None:
        tool = await async_client.tools.authorize(
            tool_name="tool_name",
            user_id="user_id",
            tool_version="tool_version",
        )
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncArcadeEngine) -> None:
        response = await async_client.tools.with_raw_response.authorize(
            tool_name="tool_name",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(AuthorizationResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncArcadeEngine) -> None:
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
    async def test_method_definition(self, async_client: AsyncArcadeEngine) -> None:
        tool = await async_client.tools.definition(
            director_id="director_id",
            tool_id="tool_id",
        )
        assert_matches_type(Definition, tool, path=["response"])

    @parametrize
    async def test_raw_response_definition(self, async_client: AsyncArcadeEngine) -> None:
        response = await async_client.tools.with_raw_response.definition(
            director_id="director_id",
            tool_id="tool_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Definition, tool, path=["response"])

    @parametrize
    async def test_streaming_response_definition(self, async_client: AsyncArcadeEngine) -> None:
        async with async_client.tools.with_streaming_response.definition(
            director_id="director_id",
            tool_id="tool_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Definition, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_execute(self, async_client: AsyncArcadeEngine) -> None:
        tool = await async_client.tools.execute(
            inputs="inputs",
            tool_name="tool_name",
            tool_version="tool_version",
            user_id="user_id",
        )
        assert_matches_type(ToolResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncArcadeEngine) -> None:
        response = await async_client.tools.with_raw_response.execute(
            inputs="inputs",
            tool_name="tool_name",
            tool_version="tool_version",
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncArcadeEngine) -> None:
        async with async_client.tools.with_streaming_response.execute(
            inputs="inputs",
            tool_name="tool_name",
            tool_version="tool_version",
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
