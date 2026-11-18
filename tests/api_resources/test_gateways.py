# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types import (
    GatewayListResponse,
    GatewayCreateResponse,
    GatewayUpdateResponse,
    GatewayReplaceResponse,
    GatewayRetrieveResponse,
    GatewaySlugInfoResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        gateway = client.gateways.list(
            "org_id",
            "project_id",
        )
        assert_matches_type(GatewayListResponse, gateway, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        gateway = client.gateways.list(
            "org_id",
            "project_id",
            limit=1,
            offset=1,
        )
        assert_matches_type(GatewayListResponse, gateway, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.list(
            "org_id",
            "project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayListResponse, gateway, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.list(
            "org_id",
            "project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewayListResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.list(
                "",
                "project_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.list(
                "org_id",
                "",
            )

    @parametrize
    def test_method_create(self, client: Arcade) -> None:
        gateway = client.gateways.create(
            "org_id",
            "project_id",
            name="name",
        )
        assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Arcade) -> None:
        gateway = client.gateways.create(
            "org_id",
            "project_id",
            allowed_passthrough_headers=["allowed_passthrough_headers"],
            auth_type="arcade",
            consent_skip_client_ids=["consent_skip_client_ids"],
            description="description",
            instructions="instructions",
            name="name",
            slug="slug",
            status="status",
            tool_filter={},
            user_source_id="user_source_id",
        )
        assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.create(
            "org_id",
            "project_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.create(
            "org_id",
            "project_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.create(
                "",
                "project_id",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.create(
                "org_id",
                "",
                name="name",
            )

    @parametrize
    def test_method_slug_info(self, client: Arcade) -> None:
        gateway = client.gateways.slug_info(
            "org_id",
            "project_id",
            slug="slug",
        )
        assert_matches_type(GatewaySlugInfoResponse, gateway, path=["response"])

    @parametrize
    def test_raw_response_slug_info(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.slug_info(
            "org_id",
            "project_id",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewaySlugInfoResponse, gateway, path=["response"])

    @parametrize
    def test_streaming_response_slug_info(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.slug_info(
            "org_id",
            "project_id",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewaySlugInfoResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_slug_info(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.slug_info(
                "",
                "project_id",
                slug="slug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.slug_info(
                "org_id",
                "",
                slug="slug",
            )

    @parametrize
    def test_method_retrieve(self, client: Arcade) -> None:
        gateway = client.gateways.retrieve(
            "org_id",
            "project_id",
            "gateway_id",
        )
        assert_matches_type(GatewayRetrieveResponse, gateway, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.retrieve(
            "org_id",
            "project_id",
            "gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayRetrieveResponse, gateway, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.retrieve(
            "org_id",
            "project_id",
            "gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewayRetrieveResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.retrieve(
                "",
                "project_id",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.retrieve(
                "org_id",
                "",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.gateways.with_raw_response.retrieve(
                "org_id",
                "project_id",
                "",
            )

    @parametrize
    def test_method_replace(self, client: Arcade) -> None:
        gateway = client.gateways.replace(
            "org_id",
            "project_id",
            "gateway_id",
            id="id",
            name="name",
        )
        assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

    @parametrize
    def test_method_replace_with_all_params(self, client: Arcade) -> None:
        gateway = client.gateways.replace(
            "org_id",
            "project_id",
            "gateway_id",
            allowed_passthrough_headers=["allowed_passthrough_headers"],
            auth_type="arcade",
            consent_skip_client_ids=["consent_skip_client_ids"],
            description="description",
            id="id",
            instructions="instructions",
            name="name",
            slug="slug",
            status="status",
            tool_filter={},
            user_source_id="user_source_id",
        )
        assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

    @parametrize
    def test_raw_response_replace(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.replace(
            "org_id",
            "project_id",
            "gateway_id",
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

    @parametrize
    def test_streaming_response_replace(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.replace(
            "org_id",
            "project_id",
            "gateway_id",
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.replace(
                "",
                "project_id",
                "gateway_id",
                id="id",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.replace(
                "org_id",
                "",
                "gateway_id",
                id="id",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.gateways.with_raw_response.replace(
                "org_id",
                "project_id",
                "",
                id="id",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Arcade) -> None:
        gateway = client.gateways.update(
            "org_id",
            "project_id",
            "gateway_id",
        )
        assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Arcade) -> None:
        gateway = client.gateways.update(
            "org_id",
            "project_id",
            "gateway_id",
            allowed_passthrough_headers=["allowed_passthrough_headers"],
            auth_type="arcade",
            consent_skip_client_ids=["consent_skip_client_ids"],
            description="description",
            instructions="instructions",
            name="name",
            slug="slug",
            status="status",
            tool_filter={},
            user_source_id="user_source_id",
        )
        assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.update(
            "org_id",
            "project_id",
            "gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.update(
            "org_id",
            "project_id",
            "gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.update(
                "",
                "project_id",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.update(
                "org_id",
                "",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.gateways.with_raw_response.update(
                "org_id",
                "project_id",
                "",
            )

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        gateway = client.gateways.delete(
            "org_id",
            "project_id",
            "gateway_id",
        )
        assert gateway is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.gateways.with_raw_response.delete(
            "org_id",
            "project_id",
            "gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = response.parse()
        assert gateway is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.gateways.with_streaming_response.delete(
            "org_id",
            "project_id",
            "gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = response.parse()
            assert gateway is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.gateways.with_raw_response.delete(
                "",
                "project_id",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            client.gateways.with_raw_response.delete(
                "org_id",
                "",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            client.gateways.with_raw_response.delete(
                "org_id",
                "project_id",
                "",
            )


class TestAsyncGateways:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.list(
            "org_id",
            "project_id",
        )
        assert_matches_type(GatewayListResponse, gateway, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.list(
            "org_id",
            "project_id",
            limit=1,
            offset=1,
        )
        assert_matches_type(GatewayListResponse, gateway, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.list(
            "org_id",
            "project_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayListResponse, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.list(
            "org_id",
            "project_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewayListResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.list(
                "",
                "project_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.list(
                "org_id",
                "",
            )

    @parametrize
    async def test_method_create(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.create(
            "org_id",
            "project_id",
            name="name",
        )
        assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.create(
            "org_id",
            "project_id",
            allowed_passthrough_headers=["allowed_passthrough_headers"],
            auth_type="arcade",
            consent_skip_client_ids=["consent_skip_client_ids"],
            description="description",
            instructions="instructions",
            name="name",
            slug="slug",
            status="status",
            tool_filter={},
            user_source_id="user_source_id",
        )
        assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.create(
            "org_id",
            "project_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.create(
            "org_id",
            "project_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewayCreateResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.create(
                "",
                "project_id",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.create(
                "org_id",
                "",
                name="name",
            )

    @parametrize
    async def test_method_slug_info(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.slug_info(
            "org_id",
            "project_id",
            slug="slug",
        )
        assert_matches_type(GatewaySlugInfoResponse, gateway, path=["response"])

    @parametrize
    async def test_raw_response_slug_info(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.slug_info(
            "org_id",
            "project_id",
            slug="slug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewaySlugInfoResponse, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_slug_info(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.slug_info(
            "org_id",
            "project_id",
            slug="slug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewaySlugInfoResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_slug_info(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.slug_info(
                "",
                "project_id",
                slug="slug",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.slug_info(
                "org_id",
                "",
                slug="slug",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.retrieve(
            "org_id",
            "project_id",
            "gateway_id",
        )
        assert_matches_type(GatewayRetrieveResponse, gateway, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.retrieve(
            "org_id",
            "project_id",
            "gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayRetrieveResponse, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.retrieve(
            "org_id",
            "project_id",
            "gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewayRetrieveResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.retrieve(
                "",
                "project_id",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.retrieve(
                "org_id",
                "",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.gateways.with_raw_response.retrieve(
                "org_id",
                "project_id",
                "",
            )

    @parametrize
    async def test_method_replace(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.replace(
            "org_id",
            "project_id",
            "gateway_id",
            id="id",
            name="name",
        )
        assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.replace(
            "org_id",
            "project_id",
            "gateway_id",
            allowed_passthrough_headers=["allowed_passthrough_headers"],
            auth_type="arcade",
            consent_skip_client_ids=["consent_skip_client_ids"],
            description="description",
            id="id",
            instructions="instructions",
            name="name",
            slug="slug",
            status="status",
            tool_filter={},
            user_source_id="user_source_id",
        )
        assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.replace(
            "org_id",
            "project_id",
            "gateway_id",
            id="id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.replace(
            "org_id",
            "project_id",
            "gateway_id",
            id="id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewayReplaceResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.replace(
                "",
                "project_id",
                "gateway_id",
                id="id",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.replace(
                "org_id",
                "",
                "gateway_id",
                id="id",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.gateways.with_raw_response.replace(
                "org_id",
                "project_id",
                "",
                id="id",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.update(
            "org_id",
            "project_id",
            "gateway_id",
        )
        assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.update(
            "org_id",
            "project_id",
            "gateway_id",
            allowed_passthrough_headers=["allowed_passthrough_headers"],
            auth_type="arcade",
            consent_skip_client_ids=["consent_skip_client_ids"],
            description="description",
            instructions="instructions",
            name="name",
            slug="slug",
            status="status",
            tool_filter={},
            user_source_id="user_source_id",
        )
        assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.update(
            "org_id",
            "project_id",
            "gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.update(
            "org_id",
            "project_id",
            "gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert_matches_type(GatewayUpdateResponse, gateway, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.update(
                "",
                "project_id",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.update(
                "org_id",
                "",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.gateways.with_raw_response.update(
                "org_id",
                "project_id",
                "",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        gateway = await async_client.gateways.delete(
            "org_id",
            "project_id",
            "gateway_id",
        )
        assert gateway is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.gateways.with_raw_response.delete(
            "org_id",
            "project_id",
            "gateway_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gateway = await response.parse()
        assert gateway is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.gateways.with_streaming_response.delete(
            "org_id",
            "project_id",
            "gateway_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gateway = await response.parse()
            assert gateway is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.gateways.with_raw_response.delete(
                "",
                "project_id",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `project_id` but received ''"):
            await async_client.gateways.with_raw_response.delete(
                "org_id",
                "",
                "gateway_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `gateway_id` but received ''"):
            await async_client.gateways.with_raw_response.delete(
                "org_id",
                "project_id",
                "",
            )
