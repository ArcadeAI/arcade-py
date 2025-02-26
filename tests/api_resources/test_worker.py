# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import WorkerResponse, WorkerListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorker:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Arcade) -> None:
        worker = client.worker.create(
            id="id",
            enabled=True,
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Arcade) -> None:
        worker = client.worker.create(
            id="id",
            enabled=True,
            http={
                "retry": 0,
                "secret": "secret",
                "timeout": 1,
                "uri": "uri",
            },
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Arcade) -> None:
        response = client.worker.with_raw_response.create(
            id="id",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Arcade) -> None:
        with client.worker.with_streaming_response.create(
            id="id",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        worker = client.worker.list()
        assert_matches_type(WorkerListResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.worker.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerListResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.worker.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerListResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorker:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.create(
            id="id",
            enabled=True,
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.create(
            id="id",
            enabled=True,
            http={
                "retry": 0,
                "secret": "secret",
                "timeout": 1,
                "uri": "uri",
            },
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArcade) -> None:
        response = await async_client.worker.with_raw_response.create(
            id="id",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArcade) -> None:
        async with async_client.worker.with_streaming_response.create(
            id="id",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.list()
        assert_matches_type(WorkerListResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.worker.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerListResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.worker.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerListResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True
