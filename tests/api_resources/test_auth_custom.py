from typing import List, Union, Optional
from unittest.mock import Mock, AsyncMock

import pytest

from arcadepy._types import NOT_GIVEN, NotGiven
from arcadepy._client import Arcade, AsyncArcade
from arcadepy.resources.auth import AuthResource, AsyncAuthResource
from arcadepy.types.shared.authorization_response import AuthorizationResponse


@pytest.mark.parametrize(
    "scopes, expected_scopes",
    [
        (["scope1"], "scope1"),
        (["scope1", "scope2"], "scope1 scope2"),
        (None, NOT_GIVEN),
    ],
)
def test_wait_for_completion_calls_status_from_auth_response(
    scopes: Optional[List[str]], expected_scopes: Union[str, NotGiven]
) -> None:
    client = Arcade(api_key="test")
    auth = AuthResource(client)
    auth.status = Mock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response_or_id = AuthorizationResponse(status="pending", authorization_id="auth_id123", scopes=scopes)

    auth.wait_for_completion(auth_response_or_id)

    auth.status.assert_called_with(
        authorization_id="auth_id123",
        scopes=expected_scopes,
        wait=45,
    )


def test_wait_for_completion_calls_status_with_auth_id() -> None:
    client = Arcade(api_key="test")
    auth = AuthResource(client)
    auth.status = Mock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response_or_id = "auth_id123"
    scopes = ["scope1", "scope2"]

    auth.wait_for_completion(auth_response_or_id, scopes)

    auth.status.assert_called_with(
        authorization_id="auth_id123",
        scopes="scope1 scope2",
        wait=45,
    )


@pytest.mark.asyncio
async def test_async_wait_for_completion_calls_status_from_auth_response() -> None:
    client = AsyncArcade(api_key="test")
    auth = AsyncAuthResource(client)
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response_or_id = AuthorizationResponse(
        status="pending", authorization_id="auth_id123", scopes=["scope1", "scope2"]
    )

    await auth.wait_for_completion(auth_response_or_id)

    auth.status.assert_called_with(
        authorization_id="auth_id123",
        scopes="scope1 scope2",
        wait=45,
    )


@pytest.mark.asyncio
async def test_async_wait_for_completion_calls_status_with_auth_id() -> None:
    client = AsyncArcade(api_key="test")
    auth = AsyncAuthResource(client)
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))  # type: ignore

    auth_response_or_id = "auth_id"
    scopes = ["scope1", "scope2"]

    await auth.wait_for_completion(auth_response_or_id, scopes)

    auth.status.assert_called_with(
        authorization_id="auth_id",
        scopes="scope1 scope2",
        wait=45,
    )
