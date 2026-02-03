# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.pagination import SyncOffsetPage, AsyncOffsetPage
from arcadepy.types.admin import UserConnectionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserConnections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        user_connection = client.admin.user_connections.list()
        assert_matches_type(SyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Arcade) -> None:
        user_connection = client.admin.user_connections.list(
            limit=0,
            offset=0,
            provider={"id": "id"},
            user={"id": "id"},
        )
        assert_matches_type(SyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.admin.user_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_connection = response.parse()
        assert_matches_type(SyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.admin.user_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_connection = response.parse()
            assert_matches_type(SyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        user_connection = client.admin.user_connections.delete(
            "id",
        )
        assert user_connection is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.admin.user_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_connection = response.parse()
        assert user_connection is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.admin.user_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_connection = response.parse()
            assert user_connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.admin.user_connections.with_raw_response.delete(
                "",
            )


class TestAsyncUserConnections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        user_connection = await async_client.admin.user_connections.list()
        assert_matches_type(AsyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncArcade) -> None:
        user_connection = await async_client.admin.user_connections.list(
            limit=0,
            offset=0,
            provider={"id": "id"},
            user={"id": "id"},
        )
        assert_matches_type(AsyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.user_connections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_connection = await response.parse()
        assert_matches_type(AsyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.user_connections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_connection = await response.parse()
            assert_matches_type(AsyncOffsetPage[UserConnectionResponse], user_connection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        user_connection = await async_client.admin.user_connections.delete(
            "id",
        )
        assert user_connection is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.user_connections.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_connection = await response.parse()
        assert user_connection is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.user_connections.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_connection = await response.parse()
            assert user_connection is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.admin.user_connections.with_raw_response.delete(
                "",
            )
