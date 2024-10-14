# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types.shared import ToolDefinition

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDefinition:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Arcade) -> None:
        definition = client.tools.definition.get(
            director_id="directorId",
            tool_id="toolId",
        )
        assert_matches_type(ToolDefinition, definition, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Arcade) -> None:
        response = client.tools.definition.with_raw_response.get(
            director_id="directorId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = response.parse()
        assert_matches_type(ToolDefinition, definition, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Arcade) -> None:
        with client.tools.definition.with_streaming_response.get(
            director_id="directorId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = response.parse()
            assert_matches_type(ToolDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDefinition:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncArcade) -> None:
        definition = await async_client.tools.definition.get(
            director_id="directorId",
            tool_id="toolId",
        )
        assert_matches_type(ToolDefinition, definition, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncArcade) -> None:
        response = await async_client.tools.definition.with_raw_response.get(
            director_id="directorId",
            tool_id="toolId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        definition = await response.parse()
        assert_matches_type(ToolDefinition, definition, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncArcade) -> None:
        async with async_client.tools.definition.with_streaming_response.get(
            director_id="directorId",
            tool_id="toolId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            definition = await response.parse()
            assert_matches_type(ToolDefinition, definition, path=["response"])

        assert cast(Any, response.is_closed) is True
