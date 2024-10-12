# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from arcade_engine import ArcadeEngine, AsyncArcadeEngine
from arcade_engine.types import HealthSchema

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_health(self, client: ArcadeEngine) -> None:
        operation = client.operations.health()
        assert_matches_type(HealthSchema, operation, path=["response"])

    @parametrize
    def test_raw_response_health(self, client: ArcadeEngine) -> None:
        response = client.operations.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = response.parse()
        assert_matches_type(HealthSchema, operation, path=["response"])

    @parametrize
    def test_streaming_response_health(self, client: ArcadeEngine) -> None:
        with client.operations.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = response.parse()
            assert_matches_type(HealthSchema, operation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_health(self, async_client: AsyncArcadeEngine) -> None:
        operation = await async_client.operations.health()
        assert_matches_type(HealthSchema, operation, path=["response"])

    @parametrize
    async def test_raw_response_health(self, async_client: AsyncArcadeEngine) -> None:
        response = await async_client.operations.with_raw_response.health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        operation = await response.parse()
        assert_matches_type(HealthSchema, operation, path=["response"])

    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncArcadeEngine) -> None:
        async with async_client.operations.with_streaming_response.health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            operation = await response.parse()
            assert_matches_type(HealthSchema, operation, path=["response"])

        assert cast(Any, response.is_closed) is True
