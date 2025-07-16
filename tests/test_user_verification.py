# Tests for user verification functionality

from __future__ import annotations

import httpx
import pytest
from respx import MockRouter

import arcadepy
from arcadepy import Arcade, AsyncArcade
from arcadepy.types import UserVerificationConfirmResponse


class TestUserVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_confirm_default_url(self, client: Arcade, respx_mock: MockRouter) -> None:
        # Mock the response and capture the request
        mocked = respx_mock.post("https://cloud.arcade.dev/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "auth_id": "ac_2zKml...",
                    "next_uri": "https://example.com/callback",
                },
            )
        )

        response = client.user_verification.confirm(
            flow_id="flow_123",
            user_id="user_456",
        )

        assert isinstance(response, UserVerificationConfirmResponse)
        assert response.auth_id == "ac_2zKml..."
        assert response.next_uri == "https://example.com/callback"

        # Verify the request was made with correct headers
        assert mocked.called
        request = mocked.calls.last.request
        # Verify the Authorization header has Bearer prefix
        assert request.headers["authorization"] == f"Bearer {client.api_key}"

    @parametrize
    def test_confirm_custom_url(self, client: Arcade, respx_mock: MockRouter) -> None:
        # Mock the response
        respx_mock.post("https://self-hosted.example.com/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "auth_id": "ac_custom...",
                    "next_uri": "https://custom.example.com/callback",
                },
            )
        )

        response = client.user_verification.confirm(
            flow_id="flow_789",
            user_id="user_012",
            base_url="https://self-hosted.example.com",
        )

        assert isinstance(response, UserVerificationConfirmResponse)
        assert response.auth_id == "ac_custom..."
        assert response.next_uri == "https://custom.example.com/callback"

    @parametrize
    def test_confirm_trailing_slash(self, client: Arcade, respx_mock: MockRouter) -> None:
        # Mock the response
        respx_mock.post("https://trailing-slash.example.com/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "auth_id": "ac_slash...",
                    "next_uri": "https://example.com",
                },
            )
        )

        response = client.user_verification.confirm(
            flow_id="flow_abc",
            user_id="user_def",
            base_url="https://trailing-slash.example.com/",
        )

        assert isinstance(response, UserVerificationConfirmResponse)
        assert response.auth_id == "ac_slash..."
        assert response.next_uri == "https://example.com"

    @parametrize
    def test_confirm_error_response(self, client: Arcade, respx_mock: MockRouter) -> None:
        # Mock an error response
        respx_mock.post("https://cloud.arcade.dev/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                400,
                json={
                    "code": 400,
                    "msg": "An error occurred during verification",
                },
            )
        )

        with pytest.raises(arcadepy.BadRequestError):
            client.user_verification.confirm(
                flow_id="invalid_flow",
                user_id="invalid_user",
            )


class TestAsyncUserVerification:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_confirm_default_url(self, async_client: AsyncArcade, respx_mock: MockRouter) -> None:
        # Mock the response
        respx_mock.post("https://cloud.arcade.dev/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "auth_id": "ac_2zKml...",
                    "next_uri": "https://example.com/callback",
                },
            )
        )

        response = await async_client.user_verification.confirm(
            flow_id="flow_123",
            user_id="user_456",
        )

        assert isinstance(response, UserVerificationConfirmResponse)
        assert response.auth_id == "ac_2zKml..."
        assert response.next_uri == "https://example.com/callback"

    @parametrize
    async def test_confirm_custom_url(self, async_client: AsyncArcade, respx_mock: MockRouter) -> None:
        # Mock the response
        respx_mock.post("https://self-hosted.example.com/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "auth_id": "ac_custom...",
                    "next_uri": "https://custom.example.com/callback",
                },
            )
        )

        response = await async_client.user_verification.confirm(
            flow_id="flow_789",
            user_id="user_012",
            base_url="https://self-hosted.example.com",
        )

        assert isinstance(response, UserVerificationConfirmResponse)
        assert response.auth_id == "ac_custom..."
        assert response.next_uri == "https://custom.example.com/callback"

    @parametrize
    async def test_confirm_trailing_slash(self, async_client: AsyncArcade, respx_mock: MockRouter) -> None:
        # Mock the response
        respx_mock.post("https://trailing-slash.example.com/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                200,
                json={
                    "auth_id": "ac_slash...",
                    "next_uri": "https://example.com",
                },
            )
        )

        response = await async_client.user_verification.confirm(
            flow_id="flow_abc",
            user_id="user_def",
            base_url="https://trailing-slash.example.com/",
        )

        assert isinstance(response, UserVerificationConfirmResponse)
        assert response.auth_id == "ac_slash..."
        assert response.next_uri == "https://example.com"

    @parametrize
    async def test_confirm_error_response(self, async_client: AsyncArcade, respx_mock: MockRouter) -> None:
        # Mock an error response
        respx_mock.post("https://cloud.arcade.dev/api/v1/oauth/confirm_user").mock(
            return_value=httpx.Response(
                400,
                json={
                    "code": 400,
                    "msg": "An error occurred during verification",
                },
            )
        )

        with pytest.raises(arcadepy.BadRequestError):
            await async_client.user_verification.confirm(
                flow_id="invalid_flow",
                user_id="invalid_user",
            )
