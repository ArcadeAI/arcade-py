# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from arcade_engine import ArcadeEngine, AsyncArcadeEngine
from arcade_engine.types.shared import AuthorizationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthorization:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_authorize(self, client: ArcadeEngine) -> None:
        authorization = client.authorization.authorize(
            auth_requirement={"provider": "provider"},
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    def test_method_authorize_with_all_params(self, client: ArcadeEngine) -> None:
        authorization = client.authorization.authorize(
            auth_requirement={
                "provider": "provider",
                "oauth2": {
                    "authority": "authority",
                    "scopes": ["string", "string", "string"],
                },
            },
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    def test_raw_response_authorize(self, client: ArcadeEngine) -> None:
        response = client.authorization.with_raw_response.authorize(
            auth_requirement={"provider": "provider"},
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = response.parse()
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    def test_streaming_response_authorize(self, client: ArcadeEngine) -> None:
        with client.authorization.with_streaming_response.authorize(
            auth_requirement={"provider": "provider"},
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = response.parse()
            assert_matches_type(AuthorizationResponse, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: ArcadeEngine) -> None:
        authorization = client.authorization.status(
            authorization_id="authorizationID",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: ArcadeEngine) -> None:
        authorization = client.authorization.status(
            authorization_id="authorizationID",
            scopes="scopes",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: ArcadeEngine) -> None:
        response = client.authorization.with_raw_response.status(
            authorization_id="authorizationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = response.parse()
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: ArcadeEngine) -> None:
        with client.authorization.with_streaming_response.status(
            authorization_id="authorizationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = response.parse()
            assert_matches_type(AuthorizationResponse, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthorization:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_authorize(self, async_client: AsyncArcadeEngine) -> None:
        authorization = await async_client.authorization.authorize(
            auth_requirement={"provider": "provider"},
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    async def test_method_authorize_with_all_params(self, async_client: AsyncArcadeEngine) -> None:
        authorization = await async_client.authorization.authorize(
            auth_requirement={
                "provider": "provider",
                "oauth2": {
                    "authority": "authority",
                    "scopes": ["string", "string", "string"],
                },
            },
            user_id="user_id",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncArcadeEngine) -> None:
        response = await async_client.authorization.with_raw_response.authorize(
            auth_requirement={"provider": "provider"},
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = await response.parse()
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncArcadeEngine) -> None:
        async with async_client.authorization.with_streaming_response.authorize(
            auth_requirement={"provider": "provider"},
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = await response.parse()
            assert_matches_type(AuthorizationResponse, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncArcadeEngine) -> None:
        authorization = await async_client.authorization.status(
            authorization_id="authorizationID",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncArcadeEngine) -> None:
        authorization = await async_client.authorization.status(
            authorization_id="authorizationID",
            scopes="scopes",
        )
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncArcadeEngine) -> None:
        response = await async_client.authorization.with_raw_response.status(
            authorization_id="authorizationID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authorization = await response.parse()
        assert_matches_type(AuthorizationResponse, authorization, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncArcadeEngine) -> None:
        async with async_client.authorization.with_streaming_response.status(
            authorization_id="authorizationID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authorization = await response.parse()
            assert_matches_type(AuthorizationResponse, authorization, path=["response"])

        assert cast(Any, response.is_closed) is True
