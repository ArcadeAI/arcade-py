# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import (
    WorkerResponse,
    WorkerListResponse,
    WorkerHealthResponse,
)

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
    def test_method_update(self, client: Arcade) -> None:
        worker = client.worker.update(
            id="id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Arcade) -> None:
        worker = client.worker.update(
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
    def test_raw_response_update(self, client: Arcade) -> None:
        response = client.worker.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Arcade) -> None:
        with client.worker.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.with_raw_response.update(
                id="",
            )

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

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        worker = client.worker.delete(
            "id",
        )
        assert worker is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.worker.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.worker.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_health(self, client: Arcade) -> None:
        worker = client.worker.health(
            "id",
        )
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_health(self, client: Arcade) -> None:
        response = client.worker.with_raw_response.health(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_health(self, client: Arcade) -> None:
        with client.worker.with_streaming_response.health(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerHealthResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_health(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.worker.with_raw_response.health(
                "",
            )


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
    async def test_method_update(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.update(
            id="id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.update(
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
    async def test_raw_response_update(self, async_client: AsyncArcade) -> None:
        response = await async_client.worker.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArcade) -> None:
        async with async_client.worker.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.with_raw_response.update(
                id="",
            )

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

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.delete(
            "id",
        )
        assert worker is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.worker.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.worker.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert worker is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_health(self, async_client: AsyncArcade) -> None:
        worker = await async_client.worker.health(
            "id",
        )
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_health(self, async_client: AsyncArcade) -> None:
        response = await async_client.worker.with_raw_response.health(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncArcade) -> None:
        async with async_client.worker.with_streaming_response.health(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerHealthResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_health(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.worker.with_raw_response.health(
                "",
            )
