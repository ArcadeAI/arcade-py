# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types.admin import (
    AuthProviderResponse,
    AuthProviderListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthProviders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.create(
            id="id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.create(
            id="id",
            description="description",
            oauth2={
                "client_id": "client_id",
                "authorize_request": {
                    "endpoint": "endpoint",
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "client_secret": "client_secret",
                "pkce": {
                    "code_challenge_method": "code_challenge_method",
                    "enabled": True,
                },
                "refresh_request": {
                    "endpoint": "endpoint",
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "scope_delimiter": ",",
                "token_introspection_request": {
                    "endpoint": "endpoint",
                    "triggers": {
                        "on_token_grant": True,
                        "on_token_refresh": True,
                    },
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "token_request": {
                    "endpoint": "endpoint",
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "user_info_request": {
                    "endpoint": "endpoint",
                    "triggers": {
                        "on_token_grant": True,
                        "on_token_refresh": True,
                    },
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
            },
            provider_id="provider_id",
            status="status",
            type="type",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Arcade) -> None:
        response = client.admin.auth_providers.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Arcade) -> None:
        with client.admin.auth_providers.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.list()
        assert_matches_type(AuthProviderListResponse, auth_provider, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.admin.auth_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = response.parse()
        assert_matches_type(AuthProviderListResponse, auth_provider, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.admin.auth_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = response.parse()
            assert_matches_type(AuthProviderListResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.delete(
            "id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.admin.auth_providers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.admin.auth_providers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.admin.auth_providers.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.get(
            "id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Arcade) -> None:
        response = client.admin.auth_providers.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Arcade) -> None:
        with client.admin.auth_providers.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.admin.auth_providers.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_patch(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.patch(
            path_id="id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_method_patch_with_all_params(self, client: Arcade) -> None:
        auth_provider = client.admin.auth_providers.patch(
            path_id="id",
            body_id="id",
            description="description",
            oauth2={
                "authorize_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "client_id": "client_id",
                "client_secret": "client_secret",
                "pkce": {
                    "code_challenge_method": "code_challenge_method",
                    "enabled": True,
                },
                "refresh_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "scope_delimiter": ",",
                "token_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "user_info_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                    "triggers": {
                        "on_token_grant": True,
                        "on_token_refresh": True,
                    },
                },
            },
            provider_id="provider_id",
            status="status",
            type="type",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_raw_response_patch(self, client: Arcade) -> None:
        response = client.admin.auth_providers.with_raw_response.patch(
            path_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    def test_streaming_response_patch(self, client: Arcade) -> None:
        with client.admin.auth_providers.with_streaming_response.patch(
            path_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_patch(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.admin.auth_providers.with_raw_response.patch(
                path_id="",
            )


class TestAsyncAuthProviders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.create(
            id="id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.create(
            id="id",
            description="description",
            oauth2={
                "client_id": "client_id",
                "authorize_request": {
                    "endpoint": "endpoint",
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "client_secret": "client_secret",
                "pkce": {
                    "code_challenge_method": "code_challenge_method",
                    "enabled": True,
                },
                "refresh_request": {
                    "endpoint": "endpoint",
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "scope_delimiter": ",",
                "token_introspection_request": {
                    "endpoint": "endpoint",
                    "triggers": {
                        "on_token_grant": True,
                        "on_token_refresh": True,
                    },
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "token_request": {
                    "endpoint": "endpoint",
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "user_info_request": {
                    "endpoint": "endpoint",
                    "triggers": {
                        "on_token_grant": True,
                        "on_token_refresh": True,
                    },
                    "auth_method": "auth_method",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
            },
            provider_id="provider_id",
            status="status",
            type="type",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.auth_providers.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = await response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.auth_providers.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = await response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.list()
        assert_matches_type(AuthProviderListResponse, auth_provider, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.auth_providers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = await response.parse()
        assert_matches_type(AuthProviderListResponse, auth_provider, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.auth_providers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = await response.parse()
            assert_matches_type(AuthProviderListResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.delete(
            "id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.auth_providers.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = await response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.auth_providers.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = await response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.admin.auth_providers.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.get(
            "id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.auth_providers.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = await response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.auth_providers.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = await response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.admin.auth_providers.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_patch(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.patch(
            path_id="id",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_method_patch_with_all_params(self, async_client: AsyncArcade) -> None:
        auth_provider = await async_client.admin.auth_providers.patch(
            path_id="id",
            body_id="id",
            description="description",
            oauth2={
                "authorize_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "client_id": "client_id",
                "client_secret": "client_secret",
                "pkce": {
                    "code_challenge_method": "code_challenge_method",
                    "enabled": True,
                },
                "refresh_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "scope_delimiter": ",",
                "token_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                },
                "user_info_request": {
                    "auth_method": "auth_method",
                    "endpoint": "endpoint",
                    "method": "method",
                    "params": {"foo": "string"},
                    "request_content_type": "application/x-www-form-urlencoded",
                    "response_content_type": "application/x-www-form-urlencoded",
                    "response_map": {"foo": "string"},
                    "triggers": {
                        "on_token_grant": True,
                        "on_token_refresh": True,
                    },
                },
            },
            provider_id="provider_id",
            status="status",
            type="type",
        )
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_raw_response_patch(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.auth_providers.with_raw_response.patch(
            path_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_provider = await response.parse()
        assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

    @parametrize
    async def test_streaming_response_patch(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.auth_providers.with_streaming_response.patch(
            path_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_provider = await response.parse()
            assert_matches_type(AuthProviderResponse, auth_provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_patch(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.admin.auth_providers.with_raw_response.patch(
                path_id="",
            )
