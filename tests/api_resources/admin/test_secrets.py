# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from arcadepy import Arcade, AsyncArcade
from tests.utils import assert_matches_type
from arcadepy.types.admin import SecretListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSecrets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Arcade) -> None:
        secret = client.admin.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Arcade) -> None:
        response = client.admin.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Arcade) -> None:
        with client.admin.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Arcade) -> None:
        secret = client.admin.secrets.delete(
            "secret_id",
        )
        assert secret is None

    @parametrize
    def test_raw_response_delete(self, client: Arcade) -> None:
        response = client.admin.secrets.with_raw_response.delete(
            "secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = response.parse()
        assert secret is None

    @parametrize
    def test_streaming_response_delete(self, client: Arcade) -> None:
        with client.admin.secrets.with_streaming_response.delete(
            "secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Arcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            client.admin.secrets.with_raw_response.delete(
                "",
            )


class TestAsyncSecrets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncArcade) -> None:
        secret = await async_client.admin.secrets.list()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.secrets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert_matches_type(SecretListResponse, secret, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.secrets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert_matches_type(SecretListResponse, secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncArcade) -> None:
        secret = await async_client.admin.secrets.delete(
            "secret_id",
        )
        assert secret is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncArcade) -> None:
        response = await async_client.admin.secrets.with_raw_response.delete(
            "secret_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        secret = await response.parse()
        assert secret is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncArcade) -> None:
        async with async_client.admin.secrets.with_streaming_response.delete(
            "secret_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            secret = await response.parse()
            assert secret is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncArcade) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `secret_id` but received ''"):
            await async_client.admin.secrets.with_raw_response.delete(
                "",
            )
