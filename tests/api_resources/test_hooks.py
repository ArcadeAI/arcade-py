# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import (
    HookListResponse,
    HookCreateResponse,
    HookUpdateResponse,
    HookRetrieveResponse,
    HookBulkUpsertResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        hook = client.hooks.list()
        assert_matches_type(HookListResponse, hook, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        hook = client.hooks.list(
            limit=1,
            offset=1,
            hook_point="hook_point",
            plugin_id="plugin_id",
            status="status",
        )
        assert_matches_type(HookListResponse, hook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.hooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = response.parse()
        assert_matches_type(HookListResponse, hook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.hooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = response.parse()
            assert_matches_type(HookListResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create(self, client: Arcade) -> None:
        hook = client.hooks.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
        )
        assert_matches_type(HookCreateResponse, hook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Arcade) -> None:
        hook = client.hooks.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
            priority=1,
            status="active",
            timeout_ms=100,
        )
        assert_matches_type(HookCreateResponse, hook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Arcade) -> None:
        response = client.hooks.with_raw_response.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = response.parse()
        assert_matches_type(HookCreateResponse, hook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Arcade) -> None:
        with client.hooks.with_streaming_response.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = response.parse()
            assert_matches_type(HookCreateResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_bulk_upsert(self, client: Arcade) -> None:
        hook = client.hooks.bulk_upsert(
            configs=[{"hook_point": "tool.access", "plugin_id": "plugin_id"}],
        )
        assert_matches_type(HookBulkUpsertResponse, hook, path=["response"])

    @parametrize
    def test_raw_response_bulk_upsert(self, client: Arcade) -> None:
        response = client.hooks.with_raw_response.bulk_upsert(
            configs=[{"hook_point": "tool.access", "plugin_id": "plugin_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = response.parse()
        assert_matches_type(HookBulkUpsertResponse, hook, path=["response"])

    @parametrize
    def test_streaming_response_bulk_upsert(self, client: Arcade) -> None:
        with client.hooks.with_streaming_response.bulk_upsert(
            configs=[{"hook_point": "tool.access", "plugin_id": "plugin_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = response.parse()
            assert_matches_type(HookBulkUpsertResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Arcade) -> None:
        hook = client.hooks.retrieve(
            "hook_id",
        )
        assert_matches_type(HookRetrieveResponse, hook, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Arcade) -> None:
        hook = client.hooks.retrieve(
            "hook_id",
            binding_type="binding_type",
        )
        assert_matches_type(HookRetrieveResponse, hook, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Arcade) -> None:
        response = client.hooks.with_raw_response.retrieve(
            "hook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = response.parse()
        assert_matches_type(HookRetrieveResponse, hook, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Arcade) -> None:
        with client.hooks.with_streaming_response.retrieve(
            "hook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = response.parse()
            assert_matches_type(HookRetrieveResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hook_id` but received ''"):
            client.hooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Arcade) -> None:
        hook = client.hooks.update(
            "hook_id",
        )
        assert_matches_type(HookUpdateResponse, hook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Arcade) -> None:
        hook = client.hooks.update(
            "hook_id",
            failure_mode="fail_closed",
            phase="before",
            priority=1,
            status="active",
            timeout_ms=100,
        )
        assert_matches_type(HookUpdateResponse, hook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Arcade) -> None:
        response = client.hooks.with_raw_response.update(
            "hook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = response.parse()
        assert_matches_type(HookUpdateResponse, hook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Arcade) -> None:
        with client.hooks.with_streaming_response.update(
            "hook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = response.parse()
            assert_matches_type(HookUpdateResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hook_id` but received ''"):
            client.hooks.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        hook = client.hooks.delete(
            "hook_id",
        )
        assert hook is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.hooks.with_raw_response.delete(
            "hook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = response.parse()
        assert hook is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.hooks.with_streaming_response.delete(
            "hook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = response.parse()
            assert hook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hook_id` but received ''"):
            client.hooks.with_raw_response.delete(
                "",
            )


class TestAsyncHooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.list()
        assert_matches_type(HookListResponse, hook, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.list(
            limit=1,
            offset=1,
            hook_point="hook_point",
            plugin_id="plugin_id",
            status="status",
        )
        assert_matches_type(HookListResponse, hook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.hooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = await response.parse()
        assert_matches_type(HookListResponse, hook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.hooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = await response.parse()
            assert_matches_type(HookListResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
        )
        assert_matches_type(HookCreateResponse, hook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
            priority=1,
            status="active",
            timeout_ms=100,
        )
        assert_matches_type(HookCreateResponse, hook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArcade) -> None:
        response = await async_client.hooks.with_raw_response.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = await response.parse()
        assert_matches_type(HookCreateResponse, hook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArcade) -> None:
        async with async_client.hooks.with_streaming_response.create(
            failure_mode="fail_closed",
            hook_point="tool.access",
            name="name",
            phase="before",
            plugin_id="plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = await response.parse()
            assert_matches_type(HookCreateResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_bulk_upsert(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.bulk_upsert(
            configs=[{"hook_point": "tool.access", "plugin_id": "plugin_id"}],
        )
        assert_matches_type(HookBulkUpsertResponse, hook, path=["response"])

    @parametrize
    async def test_raw_response_bulk_upsert(self, async_client: AsyncArcade) -> None:
        response = await async_client.hooks.with_raw_response.bulk_upsert(
            configs=[{"hook_point": "tool.access", "plugin_id": "plugin_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = await response.parse()
        assert_matches_type(HookBulkUpsertResponse, hook, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_upsert(self, async_client: AsyncArcade) -> None:
        async with async_client.hooks.with_streaming_response.bulk_upsert(
            configs=[{"hook_point": "tool.access", "plugin_id": "plugin_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = await response.parse()
            assert_matches_type(HookBulkUpsertResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.retrieve(
            "hook_id",
        )
        assert_matches_type(HookRetrieveResponse, hook, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.retrieve(
            "hook_id",
            binding_type="binding_type",
        )
        assert_matches_type(HookRetrieveResponse, hook, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArcade) -> None:
        response = await async_client.hooks.with_raw_response.retrieve(
            "hook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = await response.parse()
        assert_matches_type(HookRetrieveResponse, hook, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArcade) -> None:
        async with async_client.hooks.with_streaming_response.retrieve(
            "hook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = await response.parse()
            assert_matches_type(HookRetrieveResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hook_id` but received ''"):
            await async_client.hooks.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.update(
            "hook_id",
        )
        assert_matches_type(HookUpdateResponse, hook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.update(
            "hook_id",
            failure_mode="fail_closed",
            phase="before",
            priority=1,
            status="active",
            timeout_ms=100,
        )
        assert_matches_type(HookUpdateResponse, hook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArcade) -> None:
        response = await async_client.hooks.with_raw_response.update(
            "hook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = await response.parse()
        assert_matches_type(HookUpdateResponse, hook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArcade) -> None:
        async with async_client.hooks.with_streaming_response.update(
            "hook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = await response.parse()
            assert_matches_type(HookUpdateResponse, hook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hook_id` but received ''"):
            await async_client.hooks.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        hook = await async_client.hooks.delete(
            "hook_id",
        )
        assert hook is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.hooks.with_raw_response.delete(
            "hook_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hook = await response.parse()
        assert hook is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.hooks.with_streaming_response.delete(
            "hook_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hook = await response.parse()
            assert hook is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hook_id` but received ''"):
            await async_client.hooks.with_raw_response.delete(
                "",
            )
