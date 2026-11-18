# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import (
    PluginListResponse,
    PluginCreateResponse,
    PluginUpdateResponse,
    PluginRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlugins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        plugin = client.plugins.list()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        plugin = client.plugins.list(
            limit=1,
            offset=1,
            binding_type="binding_type",
        )
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.plugins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.plugins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert_matches_type(PluginListResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create(self, client: Arcade) -> None:
        plugin = client.plugins.create(
            name="name",
            plugin_type="webhook",
        )
        assert_matches_type(PluginCreateResponse, plugin, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Arcade) -> None:
        plugin = client.plugins.create(
            description="description",
            name="name",
            plugin_type="webhook",
            rate_limit_config={"rules": [{"limit": 1, "match": "match", "time_unit": "s"}]},
            retry={},
            status="active",
            webhook_config={"endpoints": {}},
        )
        assert_matches_type(PluginCreateResponse, plugin, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Arcade) -> None:
        response = client.plugins.with_raw_response.create(
            name="name",
            plugin_type="webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert_matches_type(PluginCreateResponse, plugin, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Arcade) -> None:
        with client.plugins.with_streaming_response.create(
            name="name",
            plugin_type="webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert_matches_type(PluginCreateResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Arcade) -> None:
        plugin = client.plugins.retrieve(
            "plugin_id",
        )
        assert_matches_type(PluginRetrieveResponse, plugin, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Arcade) -> None:
        response = client.plugins.with_raw_response.retrieve(
            "plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert_matches_type(PluginRetrieveResponse, plugin, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Arcade) -> None:
        with client.plugins.with_streaming_response.retrieve(
            "plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert_matches_type(PluginRetrieveResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plugin_id` but received ''"):
            client.plugins.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Arcade) -> None:
        plugin = client.plugins.update(
            "plugin_id",
        )
        assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Arcade) -> None:
        plugin = client.plugins.update(
            "plugin_id",
            description="description",
            name="name",
            rate_limit_config={},
            retry={},
            status="inactive",
            webhook_config={},
        )
        assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Arcade) -> None:
        response = client.plugins.with_raw_response.update(
            "plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Arcade) -> None:
        with client.plugins.with_streaming_response.update(
            "plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plugin_id` but received ''"):
            client.plugins.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        plugin = client.plugins.delete(
            "plugin_id",
        )
        assert plugin is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.plugins.with_raw_response.delete(
            "plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = response.parse()
        assert plugin is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.plugins.with_streaming_response.delete(
            "plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = response.parse()
            assert plugin is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plugin_id` but received ''"):
            client.plugins.with_raw_response.delete(
                "",
            )


class TestAsyncPlugins:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.list()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.list(
            limit=1,
            offset=1,
            binding_type="binding_type",
        )
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.plugins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert_matches_type(PluginListResponse, plugin, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.plugins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert_matches_type(PluginListResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.create(
            name="name",
            plugin_type="webhook",
        )
        assert_matches_type(PluginCreateResponse, plugin, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.create(
            description="description",
            name="name",
            plugin_type="webhook",
            rate_limit_config={"rules": [{"limit": 1, "match": "match", "time_unit": "s"}]},
            retry={},
            status="active",
            webhook_config={"endpoints": {}},
        )
        assert_matches_type(PluginCreateResponse, plugin, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArcade) -> None:
        response = await async_client.plugins.with_raw_response.create(
            name="name",
            plugin_type="webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert_matches_type(PluginCreateResponse, plugin, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArcade) -> None:
        async with async_client.plugins.with_streaming_response.create(
            name="name",
            plugin_type="webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert_matches_type(PluginCreateResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.retrieve(
            "plugin_id",
        )
        assert_matches_type(PluginRetrieveResponse, plugin, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArcade) -> None:
        response = await async_client.plugins.with_raw_response.retrieve(
            "plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert_matches_type(PluginRetrieveResponse, plugin, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArcade) -> None:
        async with async_client.plugins.with_streaming_response.retrieve(
            "plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert_matches_type(PluginRetrieveResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plugin_id` but received ''"):
            await async_client.plugins.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.update(
            "plugin_id",
        )
        assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.update(
            "plugin_id",
            description="description",
            name="name",
            rate_limit_config={},
            retry={},
            status="inactive",
            webhook_config={},
        )
        assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArcade) -> None:
        response = await async_client.plugins.with_raw_response.update(
            "plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArcade) -> None:
        async with async_client.plugins.with_streaming_response.update(
            "plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert_matches_type(PluginUpdateResponse, plugin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plugin_id` but received ''"):
            await async_client.plugins.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        plugin = await async_client.plugins.delete(
            "plugin_id",
        )
        assert plugin is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.plugins.with_raw_response.delete(
            "plugin_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plugin = await response.parse()
        assert plugin is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.plugins.with_streaming_response.delete(
            "plugin_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plugin = await response.parse()
            assert plugin is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plugin_id` but received ''"):
            await async_client.plugins.with_raw_response.delete(
                "",
            )
