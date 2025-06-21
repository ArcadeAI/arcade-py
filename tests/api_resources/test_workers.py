# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import (
    ToolDefinition,
    WorkerResponse,
    WorkerHealthResponse,
)
from arcadepy.pagination import SyncOffsetPage, AsyncOffsetPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Arcade) -> None:
        worker = client.workers.create(
            id="id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Arcade) -> None:
        worker = client.workers.create(
            id="id",
            enabled=True,
            http={
                "retry": 0,
                "secret": "secret",
                "timeout": 1,
                "uri": "uri",
            },
            mcp={
                "retry": 0,
                "timeout": 1,
                "uri": "uri",
            },
            type="type",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Arcade) -> None:
        worker = client.workers.update(
            id="id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Arcade) -> None:
        worker = client.workers.update(
            id="id",
            enabled=True,
            http={
                "retry": 0,
                "secret": "secret",
                "timeout": 1,
                "uri": "uri",
            },
            mcp={
                "retry": 0,
                "timeout": 1,
                "uri": "uri",
            },
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.update(
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
            client.workers.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        worker = client.workers.list()
        assert_matches_type(SyncOffsetPage[WorkerResponse], worker, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        worker = client.workers.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[WorkerResponse], worker, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(SyncOffsetPage[WorkerResponse], worker, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(SyncOffsetPage[WorkerResponse], worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        worker = client.workers.delete(
            "id",
        )
        assert worker is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert worker is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.delete(
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
            client.workers.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Arcade) -> None:
        worker = client.workers.get(
            "id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_health(self, client: Arcade) -> None:
        worker = client.workers.health(
            "id",
        )
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    def test_raw_response_health(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.health(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    def test_streaming_response_health(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.health(
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
            client.workers.with_raw_response.health(
                "",
            )

    @parametrize
    def test_method_tools(self, client: Arcade) -> None:
        worker = client.workers.tools(
            id="id",
        )
        assert_matches_type(SyncOffsetPage[ToolDefinition], worker, path=["response"])

    @parametrize
    def test_method_tools_with_all_params(self, client: Arcade) -> None:
        worker = client.workers.tools(
            id="id",
            limit=0,
            offset=0,
        )
        assert_matches_type(SyncOffsetPage[ToolDefinition], worker, path=["response"])

    @parametrize
    def test_raw_response_tools(self, client: Arcade) -> None:
        response = client.workers.with_raw_response.tools(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = response.parse()
        assert_matches_type(SyncOffsetPage[ToolDefinition], worker, path=["response"])

    @parametrize
    def test_streaming_response_tools(self, client: Arcade) -> None:
        with client.workers.with_streaming_response.tools(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = response.parse()
            assert_matches_type(SyncOffsetPage[ToolDefinition], worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tools(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.workers.with_raw_response.tools(
                id="",
            )


class TestAsyncWorkers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.create(
            id="id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.create(
            id="id",
            enabled=True,
            http={
                "retry": 0,
                "secret": "secret",
                "timeout": 1,
                "uri": "uri",
            },
            mcp={
                "retry": 0,
                "timeout": 1,
                "uri": "uri",
            },
            type="type",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.update(
            id="id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.update(
            id="id",
            enabled=True,
            http={
                "retry": 0,
                "secret": "secret",
                "timeout": 1,
                "uri": "uri",
            },
            mcp={
                "retry": 0,
                "timeout": 1,
                "uri": "uri",
            },
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.update(
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
            await async_client.workers.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.list()
        assert_matches_type(AsyncOffsetPage[WorkerResponse], worker, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.list(
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[WorkerResponse], worker, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(AsyncOffsetPage[WorkerResponse], worker, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(AsyncOffsetPage[WorkerResponse], worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.delete(
            "id",
        )
        assert worker is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert worker is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.delete(
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
            await async_client.workers.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.get(
            "id",
        )
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(WorkerResponse, worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_health(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.health(
            "id",
        )
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    async def test_raw_response_health(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.health(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(WorkerHealthResponse, worker, path=["response"])

    @parametrize
    async def test_streaming_response_health(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.health(
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
            await async_client.workers.with_raw_response.health(
                "",
            )

    @parametrize
    async def test_method_tools(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.tools(
            id="id",
        )
        assert_matches_type(AsyncOffsetPage[ToolDefinition], worker, path=["response"])

    @parametrize
    async def test_method_tools_with_all_params(self, async_client: AsyncArcade) -> None:
        worker = await async_client.workers.tools(
            id="id",
            limit=0,
            offset=0,
        )
        assert_matches_type(AsyncOffsetPage[ToolDefinition], worker, path=["response"])

    @parametrize
    async def test_raw_response_tools(self, async_client: AsyncArcade) -> None:
        response = await async_client.workers.with_raw_response.tools(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        worker = await response.parse()
        assert_matches_type(AsyncOffsetPage[ToolDefinition], worker, path=["response"])

    @parametrize
    async def test_streaming_response_tools(self, async_client: AsyncArcade) -> None:
        async with async_client.workers.with_streaming_response.tools(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            worker = await response.parse()
            assert_matches_type(AsyncOffsetPage[ToolDefinition], worker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tools(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.workers.with_raw_response.tools(
                id="",
            )
